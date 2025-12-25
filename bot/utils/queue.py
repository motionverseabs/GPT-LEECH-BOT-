import asyncio

download_queue = asyncio.Queue()
active_downloads = 0
