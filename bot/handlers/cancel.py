from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("cancel"))
async def cancel_handler(client: Client, message: Message):
    await message.reply_text("❌ Cancel not supported in v1 (coming soon).")
