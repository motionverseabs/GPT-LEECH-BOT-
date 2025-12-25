from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ping"))
async def ping_handler(client: Client, message: Message):
    await message.reply_text("🏓 Pong! Bot is alive.")
