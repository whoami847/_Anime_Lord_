from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_command(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ]]
    )
    await message.reply_text(
        f"ʜᴇʟʟᴏ {message.from_user.mention},\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ғɪʟᴇ ꜱʜᴀʀɪɴɢ ʙᴏᴛ!",
        reply_markup=keyboard
    )

@Client.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        "**ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ:**\n\n"
        "/genlink - sᴀᴠᴇ ᴀɴᴅ ɢᴇᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n"
        "/batch - ɢᴇɴᴇʀᴀᴛᴇ ᴄᴏᴍʙᴏ ʟɪɴᴋ ꜰʀᴏᴍ ᴍᴜʟᴛɪᴘʟᴇ ꜰɪʟᴇs\n"
        "/status - sʜᴏᴡ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ ᴀɴᴅ ᴜsᴇʀ ᴄᴏᴜɴᴛ\n"
    )

@Client.on_message(filters.command("status"))
async def status_command(client, message: Message):
    # Placeholder response
    await message.reply_text("ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ ꜰɪɴᴇ.\nᴜᴘᴛɪᴍᴇ: 00:00:00\nᴜsᴇʀs: 1234")
