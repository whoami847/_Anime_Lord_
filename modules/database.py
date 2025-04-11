from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import datetime

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client["file_share_bot"]

# Collections
users_col = db["users"]
files_col = db["files"]
settings_col = db["settings"]
batches_col = db["batches"]
broadcast_col = db["broadcast"]
force_sub_col = db["force_sub"]  # Collection for force subscription

# Force Subscription Functions

async def get_fsub_channels():
    """Fetch all force subscription channels from the database."""
    data = await force_sub_col.find().to_list(length=None)
    return [item["chat_id"] for item in data]  # Return a list of chat_ids

async def add_fsub_channel(chat_id):
    """Add a new channel to the force subscription list."""
    exists = await force_sub_col.find_one({"chat_id": chat_id})
    if not exists:
        await force_sub_col.insert_one({"chat_id": chat_id})

async def remove_fsub_channel(chat_id):
    """Remove a channel from the force subscription list."""
    await force_sub_col.delete_one({"chat_id": chat_id})

async def is_user_joined(client, user_id, channel_id):
    """Check if the user has joined the given channel."""
    try:
        member = await client.get_chat_member(channel_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

# Save File Data
async def save_file_data(file_id, user_id, file_name):
    """Save the file's data into the database."""
    await files_col.insert_one({
        "file_id": file_id,
        "user_id": user_id,
        "file_name": file_name,
        "timestamp": datetime.datetime.utcnow()
    })
