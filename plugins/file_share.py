from pyrogram import Client, filters
from pyrogram.types import Message
from modules.database import save_file_data
from modules.utils import generate_share_link
from plugins.force_sub import check_force_sub

STORAGE_CHANNEL_ID = -1001234567890  # তোমার স্টোরেজ চ্যানেলের ID এখানে বসাও

@Client.on_message(filters.private & filters.document | filters.video | filters.audio)
async def handle_file(client, message: Message):
    if not await check_force_sub(client, message):
        return

    sent = await message.forward(chat_id=STORAGE_CHANNEL_ID)
    file_id = str(sent.id)
    user_id = message.from_user.id
    file_name = message.document.file_name if message.document else "Unnamed"
    
    await save_file_data(file_id, user_id, file_name)
    share_link = generate_share_link(file_id)
    
    await message.reply_text(
        f"**Your File is Saved!**\n\n"
        f"**Name:** `{file_name}`\n"
        f"**Link:** {share_link}"
  )
