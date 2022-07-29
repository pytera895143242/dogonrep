from aiogram import executor
from misc import dp
import handlers
import asyncio
from handlers.getlink import get_links

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(get_links())
    executor.start_polling(dp, skip_updates=True)