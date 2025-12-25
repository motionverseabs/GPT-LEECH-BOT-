from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⬇️ Mirror", callback_data="mirror"),
                InlineKeyboardButton("🎬 YT-DL", callback_data="ytdl"),
            ],
            [
                InlineKeyboardButton("🧲 Torrent", callback_data="torrent"),
                InlineKeyboardButton("📥 Leech", callback_data="leech"),
            ],
            [
                InlineKeyboardButton("📊 Status", callback_data="status"),
                InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            ],
        ]
    )

def admin_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📈 Stats", callback_data="stats"),
                InlineKeyboardButton("⚡ Speedtest", callback_data="speedtest"),
            ],
            [
                InlineKeyboardButton("🚀 Restart", callback_data="restart"),
            ],
        ]
    )
