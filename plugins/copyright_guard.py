from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import sleep
from datetime import datetime, timedelta

FORWARD_WINDOW = 20 * 60  # ২০ মিনিট

forward_times = {}

@Client.on_message(filters.private & filters.document)
async def copyright_guard_handler(client, message: Message):
    user_id = message.from_user.id
    msg_id = message.id
    forward_times[msg_id] = datetime.utcnow()

    await sleep(FORWARD_WINDOW)
    time_passed = datetime.utcnow() - forward_times.get(msg_id, datetime.utcnow())
    
    if time_passed >= timedelta(seconds=FORWARD_WINDOW):
        try:
            await message.delete()
        except:
            pass
        finally:
            forward_times.pop(msg_id, None)
