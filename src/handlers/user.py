from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.keyboards import get_keyboard_command_start
from src.lexicon import LEXICON_MESSAGES_RU

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_MESSAGES_RU['start'],
        reply_markup=get_keyboard_command_start()
    )
