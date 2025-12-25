import os, sys
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.filters import admin_filter

@Client.on_message(filters.command("restart") & admin_filter)
async def restart_handler(client: Client, message: Message):
    await message.reply_text("🔄 Restarting bot...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

@Client.on_message(filters.command("stats") & admin_filter)
async def stats_handler(client: Client, message: Message):
    await message.reply_text("📈 Stats feature coming next phase.")

@Client.on_message(filters.command("speedtest") & admin_filter)
async def speedtest_handler(client: Client, message: Message):
    await message.reply_text("⚡ Speedtest coming next phase.")
