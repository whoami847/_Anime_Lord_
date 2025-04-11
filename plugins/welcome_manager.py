from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.database import get_welcome_buttons
from modules.decorators import is_forcesub_passed

@Client.on_message(filters.command("start") & filters.private)
@is_forcesub_passed
async def welcome_user(client, message: Message):
    user = message.from_user
    buttons = await get_welcome_buttons()

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=buttons.get("help", "Help"), callback_data="help"),
         InlineKeyboardButton(text=buttons.get("about", "About"), callback_data="about")]
    ])

    await message.reply_photo(
        photo="https://telegra.ph/file/312b439aa91d9262d7df6.jpg",
        caption=f"ʜᴇʟʟᴏ {user.mention}!\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ!",
        reply_markup=keyboard
    )
