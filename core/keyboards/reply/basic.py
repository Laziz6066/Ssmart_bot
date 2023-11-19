from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_start_keyboard_ru():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Условия рассрочки')
    keyboard_builder.button(text='Акции и скидки')
    keyboard_builder.button(text='Товары')
    keyboard_builder.button(text='Наши контакты')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def get_reply_start_keyboard_uz():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Rassrochka shartlari')
    keyboard_builder.button(text='Aksiya va skidkalar')
    keyboard_builder.button(text='Tovarlar')
    keyboard_builder.button(text='Bizning kontaktlarimiz')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def get_reply_admin_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Условия рассрочки')
    keyboard_builder.button(text='Акции и скидки')
    keyboard_builder.button(text='Товары')
    keyboard_builder.button(text='Наши контакты')
    keyboard_builder.button(text='Админ-панель')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def get_reply_admin_edit_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Добавить товар')
    keyboard_builder.button(text='Удалить товар')
    keyboard_builder.button(text='Изменить товар')
    keyboard_builder.button(text='Сделать рассылку')
    keyboard_builder.button(text='Главное меню')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def language_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='🇷🇺 Русский')
    keyboard_builder.button(text="🇺🇿 O'zbekcha")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def get_reply_contact_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Отправить свой номер', request_contact=True)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)