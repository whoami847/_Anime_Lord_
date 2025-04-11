from pyrogram import Client, filters
from pyrogram.types import Message
from modules.database import get_all_users
from modules.decorators import is_admin
from pyrogram.errors import PeerIdInvalid, UserIsBlocked, InputUserDeactivated

@Client.on_message(filters.command("broadcast") & filters.private)
@is_admin
async def broadcast_message(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ.")

    users = await get_all_users()
    sent, failed = 0, 0

    for user_id in users:
        try:
            await message.reply_to_message.copy(chat_id=user_id)
            sent += 1
        except (PeerIdInvalid, UserIsBlocked, InputUserDeactivated):
            failed += 1
        except Exception:
            failed += 1

    await message.reply(f"✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ\n\nᴛᴏᴛᴀʟ: {len(users)}\n✅: {sent}\n❌: {failed}")
