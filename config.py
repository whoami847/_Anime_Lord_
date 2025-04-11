import os

# MongoDB Connection URL
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Anime00:<db_password>@anime00.ltl8plf.mongodb.net/?retryWrites=true&w=majority&appName=Anime00")

# Bot Token and API Keys
BOT_TOKEN = os.getenv("BOT_TOKEN", "8018682528:AAEB0W9Ljb8Prfyi9qeVYX93OZzcGBuLEYA")
API_ID = int(os.getenv("API_ID", 28774737))
API_HASH = os.getenv("API_HASH", "851190ab85bb0b6dd547fff8e3c35b73")

# Owner/Admin ID
ADMINS = os.getenv("ADMINS", "7282066033").split(",")  # Comma separated list of admin IDs

# Force Subscription Channels
FORCE_SUB_CHANNELS = os.getenv("FORCE_SUB_CHANNELS", "-1002644513465").split(",")

# Storage Channel for files
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", -1002656647177))

# Optional: Port for fake HTTP server on Koyeb
PORT = int(os.getenv("PORT", 8080))
