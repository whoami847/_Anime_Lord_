from pyrogram import Client, filters
from pyrogram.types import Message
from modules.decorators import admin_only

@Client.on_message(filters.command("cmd") & filters.private)
@admin_only
async def admin_cmds(client, message: Message):
    await message.reply_text(
        "**Admin Panel**\n\n"
        "/status - Bot status and user count\n"
        "/broadcast - Send message to all users\n"
        "/restart - Restart the bot\n"
        "/forcesub - Manage Force Sub settings\n"
        "/users - View or edit user settings"
    )

@Client.on_message(filters.command("restart") & filters.private)
@admin_only
async def restart_bot(client, message: Message):
    await message.reply_text("♻️ Restarting...")
    import os, sys
    os.execl(sys.executable, sys.executable, *sys.argv)
