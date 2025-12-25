import os

# ===== REQUIRED =====
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# ===== LIMITS =====
MAX_FILE_SIZE_GB = 2
MAX_GLOBAL_DOWNLOADS = 3
MAX_USER_DOWNLOADS = 3
QUEUE_LIMIT = 5

# ===== VALIDATION =====
if not BOT_TOKEN or not API_ID or not API_HASH or not OWNER_ID:
    raise RuntimeError("Missing required ENV variables (BOT_TOKEN / API_ID / API_HASH / OWNER_ID)")
