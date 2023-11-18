from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_state_brand_fridge_keyboard():
    keyword_builder = ReplyKeyboardBuilder()
    keyword_builder.button(text='TCL')
    keyword_builder.button(text='Roison')
    keyword_builder.button(text='Samsung')
    keyword_builder.button(text='Beko')
    keyword_builder.button(text='Нужен список брендов')
    keyword_builder.adjust(2, 2)
    return keyword_builder.as_markup()


def get_state_brand_phone_keyboard():
    keyword_builder = ReplyKeyboardBuilder()
    keyword_builder.button(text='TCL')
    keyword_builder.button(text='Xiaomi')
    keyword_builder.button(text='Samsung')
    keyword_builder.button(text='Нужен список брендов')
    keyword_builder.adjust(2, 2)
    return keyword_builder.as_markup()


def get_state_brand_tv_keyboard():
    keyword_builder = ReplyKeyboardBuilder()
    keyword_builder.button(text='TCL')
    keyword_builder.button(text='Roison')
    keyword_builder.button(text='Samsung')
    keyword_builder.button(text='Wellstar')
    keyword_builder.button(text='Нужен список брендов')
    keyword_builder.adjust(2, 2)
    return keyword_builder.as_markup()


def get_state_brand_conditioner_keyboard():
    keyword_builder = ReplyKeyboardBuilder()
    keyword_builder.button(text='TCL')
    keyword_builder.button(text='Roison')
    keyword_builder.button(text='Immer')
    keyword_builder.button(text='AUX')
    keyword_builder.button(text='Нужен список брендов')
    keyword_builder.adjust(2, 2)
    return keyword_builder.as_markup()