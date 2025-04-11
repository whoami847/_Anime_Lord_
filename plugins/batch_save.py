from pyrogram import Client, filters
from pyrogram.types import Message
from modules.database import save_batch_files
from modules.utils import generate_batch_link
from plugins.force_sub import check_force_sub

@Client.on_message(filters.private & filters.caption & filters.text)
async def handle_batch(client, message: Message):
    if not await check_force_sub(client, message):
        return

    # ধরে নিচ্ছি ইউজার একাধিক ফাইল আইডি পাঠাচ্ছে caption আকারে
    file_ids = message.text.split()
    user_id = message.from_user.id

    combo_id = await save_batch_files(user_id, file_ids)
    combo_link = generate_batch_link(combo_id)

    await message.reply_text(
        f"**Batch Saved Successfully!**\n\n"
        f"**Combo Link:** {combo_link}"
  )
