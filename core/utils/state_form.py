from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME = State()
    GET_DESCRIPTION = State()
    GET_PHOTO = State()
    GET_PRICE = State()
    GET_CATEGORY = State()
    GET_BRAND = State()
