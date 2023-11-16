from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from loader import dp
from aiogram import F
from core.keyboards.reply import get_reply_keyboard, get_reply_admin_keyboard, get_reply_admin_edit_keyboard
from core.keyboards.inline import category_inline_keyboard
from core.settings import settings


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}\nНужен текст "
                         f"приветственного сообщения для клиентов и описание бота что он делает\n"
                         f"{hbold('Нет жестких правил или конструкций можно написать что угодно я лишь привёл пример')}",
                         reply_markup=get_reply_keyboard())
    if message.from_user.id == settings.bots.admin_id:
        await message.answer("Добро пожаловать Вы администратор", reply_markup=get_reply_admin_keyboard())


@dp.message(F.text == 'Условия рассрочки')
async def installment_terms(message: Message):
    await message.answer(f'Тут нужно написать условия рассрочки\nМожно текстом\nМожно картинкой\n'
                         f'{hbold("Нет жестких правил или конструкций можно написать что угодно я лишь привёл пример")}')


@dp.message(F.text == 'Акции и скидки')
async def promotions_discounts(message: Message):
    await message.answer(f'Тут можно будет посмотреть список акций и скидок на товары\nМожно текстом\nМожно картинкой\n'
                         f'{hbold("Нет жестких правил или конструкций можно написать что угодно я лишь привёл пример")}')


@dp.message(F.text == 'Наши контакты')
async def contacts(message: Message):
    await message.answer('Тут нужно вставить контактные данные\nНомер телефона\nusername в телеграм\n'
                         f'{hbold("Нет жестких правил или конструкций можно написать что угодно я лишь привёл пример")}')


@dp.message(F.text == 'Товары')
async def products_list(message: Message):
    await message.answer('Категории товаров', reply_markup=category_inline_keyboard())


@dp.message(F.text == 'Админ-панель')
async def admin_panel(message: Message):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer('Вы вошли в админ панель', reply_markup=get_reply_admin_edit_keyboard())
    else:
        await message.answer('У вас нет прав доступа\r\nЧтобы получть доступ к админ панели свяжитесь по этому'
                             ' номеру\r\n+998886396066')