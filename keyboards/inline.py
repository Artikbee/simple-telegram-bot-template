from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MeetingCD(CallbackData, prefix='meetings'):
    meeting_id: int


def get_keyboard_command_start():
    buttons = [
        [
            InlineKeyboardButton(
                text='Привет',
                url='www.google.com',

            )
        ],
        [
            InlineKeyboardButton(
                text='Привет',
                callback_data='ttt',
            )
        ],

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_keyboard_get_info_meetings(meetings):
    builder = InlineKeyboardBuilder()
    for i in meetings:
        builder.add(
            InlineKeyboardButton(
                text=f'{i.date}, {i.time}',
                callback_data=MeetingCD(
                    meeting_id=i.id
                ).pack()
            )
        )

    builder.add(
        InlineKeyboardButton(
            text='Вернуться к основному меню',
            callback_data='go_back'
        )
    )
    keyboard = builder.adjust(1, 1).as_markup()
    return keyboard
