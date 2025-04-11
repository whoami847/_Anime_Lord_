from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from keep_alive import keep_alive
from plugins import basic_commands, force_sub, file_share, batch_save, broadcast
from modules import admin_panel, auto_delete, user_settings, logger

app = Client("AnimeLordBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load plugins
app.add_handler(MessageHandler(basic_commands.start_command, filters.command("start")))
app.add_handler(MessageHandler(basic_commands.help_command, filters.command("help")))
app.add_handler(MessageHandler(basic_commands.status_command, filters.command("status")))

app.add_handler(MessageHandler(force_sub.manage_fsub, filters.command("forcesub")))
app.add_handler(MessageHandler(force_sub.list_fsub_channels, filters.command("req_fsub")))

app.add_handler(MessageHandler(file_share.handle_file, filters.document | filters.video | filters.audio))
app.add_handler(MessageHandler(batch_save.handle_batch, filters.caption))
app.add_handler(MessageHandler(broadcast.broadcast_message, filters.command("broadcast") & filters.user(ADMINS)))

app.add_handler(MessageHandler(admin_panel.admin_cmds, filters.command("cmd") & filters.user(ADMINS)))
app.add_handler(MessageHandler(admin_panel.restart_bot, filters.command("restart") & filters.user(ADMINS)))

app.add_handler(MessageHandler(auto_delete.auto_delete_config, filters.command("auto_del")))
app.add_handler(MessageHandler(user_settings.user_settings_handler, filters.command("users")))

# Start the server to keep bot alive
keep_alive()

# Run the bot
app.run()
