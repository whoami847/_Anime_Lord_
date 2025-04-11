from pyrogram import Client, filters
from pyrogram.types import Message

def to_small_caps(text: str) -> str:
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_caps = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ" * 2
    return text.translate(str.maketrans(normal, small_caps))

@Client.on_message(filters.text & filters.private, group=999)
async def style_all_messages(client, message: Message):
    if message.text.startswith("/"):
        return
    styled = to_small_caps(message.text)
    await message.reply_text(styled)
