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
    keyword_builder.button(text='тут', callback_data="tcl")
    keyword_builder.button(text='будут', callback_data="roison")
    keyword_builder.button(text='название', callback_data="samsung")
    keyword_builder.button(text='брендов', callback_data="beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def phone_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='тут', callback_data="tcl")
    keyword_builder.button(text='будут', callback_data="roison")
    keyword_builder.button(text='название', callback_data="samsung")
    keyword_builder.button(text='брендов', callback_data="beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def tv_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='тут', callback_data="tcl")
    keyword_builder.button(text='будут', callback_data="roison")
    keyword_builder.button(text='название', callback_data="samsung")
    keyword_builder.button(text='брендов', callback_data="beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def conditioner_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='тут', callback_data="tcl")
    keyword_builder.button(text='будут', callback_data="roison")
    keyword_builder.button(text='название', callback_data="samsung")
    keyword_builder.button(text='брендов', callback_data="beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()