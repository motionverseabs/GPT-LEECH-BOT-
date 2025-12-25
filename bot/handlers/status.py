from pyrogram import Client, filters
from pyrogram.types import Message
from bot.utils.queue import active_downloads

@Client.on_message(filters.command("status"))
async def status_handler(client: Client, message: Message):
    await message.reply_text(
        f"📊 **Bot Status**\n\n"
        f"Active downloads: {active_downloads}"
    )
