import sys
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from database.session import async_session_local
from keyboards.set_menu import set_main_menu
from middlewares.database import DataBaseSession
import logging

from config import load_config
from handlers.user import user_router


async def main() -> None:
    config = load_config()

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=config.tg_bot.TOKEN)

    dp.include_routers(
        user_router,
    )
    await set_main_menu(bot)

    dp.update.middleware(DataBaseSession(session_pool=async_session_local))

    dp.workflow_data.update(
        {
            "bot": bot,
        }
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
