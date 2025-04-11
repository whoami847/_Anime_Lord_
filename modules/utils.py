import string

def generate_share_link(file_id: str) -> str:
    return f"https://t.me/YourBotUsername?start={file_id}"

def generate_batch_link(batch_id: str) -> str:
    return f"https://t.me/YourBotUsername?start=batch_{batch_id}"

def smallcaps(text: str) -> str:
    normal = string.ascii_letters
    small_caps = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘʟᴛᴜᴠᴡxʏᴢ" * 2
    return text.translate(str.maketrans(normal, small_caps))
