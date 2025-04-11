from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("users") & filters.private)
async def user_settings_handler(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔔 Notifications", callback_data="toggle_notifications")],
            [InlineKeyboardButton("⬅️ Back", callback_data="go_back")]
        ]
    )
    await message.reply_text(
        "⚙️ *Your Settings Panel*\n\nSelect your preferences below:",
        reply_markup=keyboard
    )
