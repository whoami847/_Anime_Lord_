from pyrogram.types import Message
from pyrogram import Client, filters
from config import ADMINS
from functools import wraps

def admin_only(func):
    @wraps(func)
    async def wrapper(client: Client, message: Message):
        if str(message.from_user.id) not in ADMINS:
            return await message.reply_text("🚫 You are not authorized to use this command.")
        return await func(client, message)
    return wrapper
