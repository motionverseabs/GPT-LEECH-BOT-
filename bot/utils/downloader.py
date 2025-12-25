import aiohttp
import os
from bot.config import MAX_FILE_SIZE_GB
from bot.utils.logger import get_logger

log = get_logger("downloader")

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def download_file(url: str, filename: str):
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            size = int(resp.headers.get("Content-Length", 0))
            if size > MAX_FILE_SIZE_GB * 1024 * 1024 * 1024:
                raise ValueError("File too large")

            with open(filepath, "wb") as f:
                async for chunk in resp.content.iter_chunked(1024 * 1024):
                    f.write(chunk)

    return filepath
