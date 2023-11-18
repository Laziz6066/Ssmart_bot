from aiogram.utils.keyboard import InlineKeyboardBuilder


def category_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='Холодильники', callback_data="fridge")
    keyword_builder.button(text='Телефоны', callback_data="phone")
    keyword_builder.button(text='Телевизоры', callback_data="tv")
    keyword_builder.button(text='Кондиционеры', callback_data="conditioner")
    keyword_builder.button(text='И так далее... нужен список категорий', callback_data='qwe')

    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def fridge_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="fridge_tcl")
    keyword_builder.button(text='Roison', callback_data="fridge_roison")
    keyword_builder.button(text='Samsung', callback_data="fridge_samsung")
    keyword_builder.button(text='Beko', callback_data="fridge_beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def phone_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="phone_tcl")
    keyword_builder.button(text='Xiaomi', callback_data="phone_xiaomi")
    keyword_builder.button(text='Samsung', callback_data="phone_samsung")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def tv_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="tv_tcl")
    keyword_builder.button(text='Roison', callback_data="tv_roison")
    keyword_builder.button(text='Samsung', callback_data="tv_samsung")
    keyword_builder.button(text='Wellstar', callback_data="tv_wellstar")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def conditioner_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="conditioner_tcl")
    keyword_builder.button(text='Roison', callback_data="conditioner_roison")
    keyword_builder.button(text='AUX', callback_data="conditioner_aux")
    keyword_builder.button(text='Immer', callback_data="conditioner_immer")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()