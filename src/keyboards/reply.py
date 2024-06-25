from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose_type_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Привет"),
        ],
        [
            KeyboardButton(text="Привет"),
        ],
    ]
)
