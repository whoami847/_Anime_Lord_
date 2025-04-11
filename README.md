# Anime Lord Bot

Anime Lord is a Telegram bot for file sharing, with support for Force Subscription, Batch Save, and more! 

## Features

- **File Sharing:** Upload and generate shareable links for files.
- **Force Subscription:** Force users to join specific channels before using the bot.
- **Batch Save:** Save multiple files and generate a single combo link.
- **Admin Panel:** Admins can manage force sub channels, broadcast messages, and restart the bot.
- **Auto Delete:** Set time-based auto-deletion for files or messages.

## Requirements

- Python 3.7+
- MongoDB for database storage
- A Telegram Bot Token from BotFather

## Setup

1. Clone this repository.
2. Install the required libraries using:
    ```
    pip install -r requirements.txt
    ```
3. Set up your `.env` file with the required variables (see below).
4. Run the bot using:
    ```
    python main.py
    ```

## Environment Variables

- `MONGO_URI`: MongoDB connection URI.
- `BOT_TOKEN`: Your Telegram Bot Token.
- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API hash.
- `ADMINS`: Comma-separated list of admin user IDs.
- `FORCE_SUB_CHANNELS`: Channels for force subscription.
- `STORAGE_CHANNEL`: Telegram channel ID for file storage.

## License

This project is licensed under the MIT License.
