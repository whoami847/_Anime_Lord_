from functools import wraps
from pyrogram.types import Message
from config import ADMINS

# Admin Only Decorator
def admin_only(func):
    @wraps(func)
    async def wrapper(client, message: Message):
        if str(message.from_user.id) not in ADMINS:
            return await message.reply_text("🚫 You are not authorized to use this command.")
        return await func(client, message)
    return wrapper

# is_admin function (for broadcast command check)
def is_admin(user_id):
    """Check if the user is an admin."""
    return str(user_id) in ADMINS

# Other decorators if necessary can be added here
