from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply_text(
        "**📘 Commands**\n\n"
        "/start – Start bot\n"
        "/help – Show help\n"
        "/mirror – Direct link download\n"
        "/ytdl – YouTube download\n"
        "/torrent – Torrent / Magnet\n"
        "/leech – Telegram file leech\n"
        "/status – Active downloads\n"
        "/cancel – Cancel task\n"
        "/ping – Bot alive\n\n"
        "**Admin**\n"
        "/stats\n"
        "/restart\n"
        "/ban /unban\n"
        "/speedtest"
    )
