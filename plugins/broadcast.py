from pyrogram import Client, filters
from pyrogram.types import Message
from utils.fonts import smallcaps
from modules.database import get_all_users
import asyncio
import os

ADMINS = [int(os.environ.get("OWNER_ID", 0))]

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast_message(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text(smallcaps("Reply to a message to broadcast."))

    users = await get_all_users()
    total = len(users)
    success = 0
    fail = 0

    for user_id in users:
        try:
            await message.reply_to_message.copy(chat_id=user_id)
            success += 1
        except:
            fail += 1
        await asyncio.sleep(0.3)

    await message.reply_text(
        smallcaps(f"Broadcast Finished.\nSuccess: {success}\nFailed: {fail}\nTotal: {total}")
    )
