from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.types import Message, FSInputFile
from loader import dp
from aiogram import F
from core.keyboards.reply.basic import get_reply_start_keyboard, get_reply_admin_keyboard, get_reply_admin_edit_keyboard
from core.keyboards.inline.inline import category_inline_keyboard
from core.settings import settings
from aiogram import Bot
from core.bot_text import text


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:

    photo = FSInputFile(path='D:/PycharmProjects/Ssmart_bot/photo-1.jpg')
    if message.from_user.id == settings.bots.admin_id:
        await bot.send_photo(message.chat.id, photo, caption=f"Вы являетесь АДМИНИСТРАТОРОМ!!!\r\n{text.start_text}",
                             reply_markup=get_reply_admin_keyboard())
    else:
        await bot.send_photo(message.chat.id, photo, caption=text.start_text,
                             reply_markup=get_reply_start_keyboard())


@dp.message(F.text == 'Условия рассрочки')
async def installment_terms(message: Message):
    await message.answer(text=text.installment_terms)


@dp.message(F.text == 'Акции и скидки')
async def promotions_discounts(message: Message):
    await message.answer(text=text.promotions_discounts)


@dp.message(F.text == 'Наши контакты')
async def contacts(message: Message):
    await message.answer(text=text.contacts)


@dp.message(F.text == 'Товары')
async def products_list(message: Message):
    await message.answer(text=text.products_list, reply_markup=category_inline_keyboard())


@dp.message(F.text == 'Админ-панель')
async def admin_panel(message: Message):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer(text=text.admin_panel, reply_markup=get_reply_admin_edit_keyboard())
    else:
        await message.answer(text=text.admin_permission)


@dp.message(F.text == 'Главное меню')
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=get_reply_admin_keyboard())


# @dp.message()
# async def any_message(message: Message):
#     await message.answer('В боте нет такой команды')