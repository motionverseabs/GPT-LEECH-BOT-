from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.utils.logger import get_logger

log = get_logger("main")

app = Client(
    "advanced_leech_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

def main():
    log.info("Starting Advanced Leech Bot...")
    app.run()

if __name__ == "__main__":
    main()
