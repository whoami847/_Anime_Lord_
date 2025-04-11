from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["file_share_bot"]

users_col = db["users"]
files_col = db["files"]
settings_col = db["settings"]
batches_col = db["batches"]
broadcast_col = db["broadcast"]
