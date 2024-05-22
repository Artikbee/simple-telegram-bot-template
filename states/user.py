from aiogram.fsm.state import StatesGroup, State


class UserFSM(StatesGroup):
    SOME_STATE = State()
