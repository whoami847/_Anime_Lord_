from pyrogram import Client, filters
from pyrogram.types import Message
from modules.database import set_auto_delete, get_auto_delete
from plugins.force_sub import check_force_sub
from asyncio import sleep

@Client.on_message(filters.command("auto_del") & filters.private)
async def auto_delete_config(client, message: Message):
    if not await check_force_sub(client, message):
        return

    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        return await message.reply_text("**Usage:** `/auto_del <seconds>`")

    seconds = int(args[1])
    user_id = message.from_user.id

    await set_auto_delete(user_id, seconds)
    await message.reply_text(f"**Auto delete set to {seconds} seconds.**")

@Client.on_message(filters.private & filters.document)
async def auto_delete_handler(client, message: Message):
    user_id = message.from_user.id
    delay = await get_auto_delete(user_id)

    if delay:
        await sleep(delay)
        try:
            await message.delete()
        except:
            pass
