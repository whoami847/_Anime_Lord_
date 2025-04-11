import os

# MongoDB Connection URL
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Bot Token and API Keys
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", 123456))
API_HASH = os.getenv("API_HASH", "")

# Owner/Admin ID
ADMINS = os.getenv("ADMINS", "").split(",")  # Comma separated list of admin IDs

# Force Subscription Channels
FORCE_SUB_CHANNELS = os.getenv("FORCE_SUB_CHANNELS", "").split(",")

# Storage Channel for files
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", -1001234567890))

# Optional: Port for fake HTTP server on Koyeb
PORT = int(os.getenv("PORT", 8080))
