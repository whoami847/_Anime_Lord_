from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.database import get_fsub_channels, add_fsub_channel, remove_fsub_channel, is_user_joined

FORCE_JOIN_TEXT = "**You must join the following channel(s) to use this bot:**"

@Client.on_message(filters.private & filters.command("forcesub"))
async def manage_fsub(client, message: Message):
    if not message.from_user or not await client.is_sudo(message.from_user.id):
        return
    if len(message.command) < 2:
        return await message.reply_text("/forcesub add/remove <channel username>")
    
    action = message.command[1].lower()
    if action == "add" and len(message.command) == 3:
        channel = message.command[2]
        await add_fsub_channel(channel)
        await message.reply_text(f"➕ Added `{channel}` to force subscription list.")
    elif action == "remove" and len(message.command) == 3:
        channel = message.command[2]
        await remove_fsub_channel(channel)
        await message.reply_text(f"➖ Removed `{channel}` from force subscription list.")
    else:
        await message.reply_text("Usage:\n/forcesub add <channel>\n/forcesub remove <channel>")

@Client.on_message(filters.private & filters.command("req_fsub"))
async def list_fsub_channels(client, message: Message):
    if not message.from_user or not await client.is_sudo(message.from_user.id):
        return
    channels = await get_fsub_channels()
    if not channels:
        await message.reply_text("No channels set for force subscription.")
    else:
        msg = "**Current Force Subscription Channels:**\n\n"
        msg += "\n".join([f"- @{ch}" for ch in channels])
        await message.reply_text(msg)

async def check_force_sub(client: Client, message: Message):
    user_id = message.from_user.id
    channels = await get_fsub_channels()
    if not channels:
        return True
    btns = []
    for ch in channels:
        if not await is_user_joined(client, ch, user_id):
            btns.append([InlineKeyboardButton(text=f"Join @{ch}", url=f"https://t.me/{ch}")])
    if btns:
        btns.append([InlineKeyboardButton("✅ Joined", callback_data="check_fsub")])
        await message.reply_text(FORCE_JOIN_TEXT, reply_markup=InlineKeyboardMarkup(btns))
        return False
    return True
