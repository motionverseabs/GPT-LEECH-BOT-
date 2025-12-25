import os
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.utils.downloader import download_file
from bot.utils.queue import active_downloads
from bot.config import MAX_GLOBAL_DOWNLOADS
from bot.utils.logger import get_logger

log = get_logger("mirror")

@Client.on_message(filters.command("mirror"))
async def mirror_handler(client: Client, message: Message):
    global active_downloads

    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: /mirror <direct_url>")

    if active_downloads >= MAX_GLOBAL_DOWNLOADS:
        return await message.reply_text("⏳ Server busy. Please wait.")

    url = message.command[1]
    filename = url.split("/")[-1] or "file.bin"

    active_downloads += 1
    status = await message.reply_text("⬇️ Downloading...")

    try:
        path = await download_file(url, filename)
        await status.edit_text("📤 Uploading...")
        await message.reply_document(path)
        os.remove(path)
    except Exception as e:
        await status.edit_text(f"❌ Error: {e}")
    finally:
        active_downloads -= 1
