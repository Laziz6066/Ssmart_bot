from aiogram.utils.keyboard import InlineKeyboardBuilder


def category_inline_keyboard_ru():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='Холодильники', callback_data="fridge")
    keyword_builder.button(text='Телефоны', callback_data="phone")
    keyword_builder.button(text='Телевизоры', callback_data="tv")
    keyword_builder.button(text='Кондиционеры', callback_data="conditioner")
    keyword_builder.button(text='И так далее... нужен список категорий', callback_data='qwe')
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def category_inline_keyboard_uz():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='Xolodilniklar', callback_data="fridge")
    keyword_builder.button(text='Telefonlar', callback_data="phone")
    keyword_builder.button(text='Televizorlar', callback_data="tv")
    keyword_builder.button(text='Konditsionerlar', callback_data="conditioner")
    keyword_builder.button(text='И так далее... нужен список категорий', callback_data='qwe')
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def fridge_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="fridge_TCL")
    keyword_builder.button(text='Roison', callback_data="fridge_Roison")
    keyword_builder.button(text='Samsung', callback_data="fridge_Samsung")
    keyword_builder.button(text='Beko', callback_data="fridge_Beko")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def phone_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="phone_TCL")
    keyword_builder.button(text='Xiaomi', callback_data="phone_Xiaomi")
    keyword_builder.button(text='Samsung', callback_data="phone_Samsung")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def tv_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="tv_TCL")
    keyword_builder.button(text='Roison', callback_data="tv_Roison")
    keyword_builder.button(text='Samsung', callback_data="tv_Samsung")
    keyword_builder.button(text='Wellstar', callback_data="tv_Wellstar")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def conditioner_inline_keyboard():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='TCL', callback_data="conditioner_TCL")
    keyword_builder.button(text='Roison', callback_data="conditioner_Roison")
    keyword_builder.button(text='AUX', callback_data="conditioner_AUX")
    keyword_builder.button(text='Immer', callback_data="conditioner_Immer")
    keyword_builder.button(text='Нужен список брендов', callback_data='qwe')
    keyword_builder.button(text='Назад', callback_data="back_category")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def submit_application_ru():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text='Оставить заявку на оформление', callback_data="order_item")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()


def submit_application_uz():
    keyword_builder = InlineKeyboardBuilder()
    keyword_builder.button(text="Rasmiylashtirish uchun so'rovnoma qoldirish", callback_data="order_item")
    keyword_builder.adjust(1)
    return keyword_builder.as_markup()