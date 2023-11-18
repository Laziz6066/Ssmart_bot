from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_state_category_keyboard():
    keyword_builder = ReplyKeyboardBuilder()
    keyword_builder.button(text='Холодильники')
    keyword_builder.button(text='Телефоны')
    keyword_builder.button(text='Телевизоры')
    keyword_builder.button(text='Кондиционеры')
    keyword_builder.button(text='Нужен список категорий')
    keyword_builder.adjust(2, 2)
    return keyword_builder.as_markup()
