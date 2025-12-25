from pyrogram import Client, filters
from pyrogram.types import Message
from bot.keyboards import start_keyboard
from bot.utils.logger import get_logger

log = get_logger("start")

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    log.info(f"/start by {message.from_user.id}")
    await message.reply_text(
        "👋 **Welcome to Advanced Public Leech Bot**\n\n"
        "Use buttons below or type /help\n\n"
        "⚠️ Public limits apply.",
        reply_markup=start_keyboard()
    )
