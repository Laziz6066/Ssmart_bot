from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from loader import dp
from aiogram import F
from core.keyboards.reply.basic import (get_reply_start_keyboard_ru, get_reply_admin_keyboard,
                                        get_reply_admin_edit_keyboard, language_keyboard, get_reply_start_keyboard_uz)
from core.keyboards.inline.inline import category_inline_keyboard_ru, category_inline_keyboard_uz
from core.settings import settings
from aiogram import Bot
from core.bot_text import text
from core.database.language import create_language, get_language, db_start_language, get_user_id
from core.database.order import get_orders, db_start_order


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    photo = FSInputFile(path='D:/PycharmProjects/Ssmart_bot/photo-1.jpg')
    if message.from_user.id == settings.bots.admin_id:
        await bot.send_photo(message.chat.id, photo, caption=f"Вы являетесь АДМИНИСТРАТОРОМ!!!\r\n{text.start_text_ru}",
                             reply_markup=get_reply_admin_edit_keyboard())
    else:
        await bot.send_photo(message.chat.id, photo, caption=text.start_text_ru,
                             reply_markup=language_keyboard())


@dp.message(F.text == '🇷🇺 Русский')
async def start_next_step_ru(message: Message):
    await message.answer(text='Нажмите на нужную вам кнопку.', reply_markup=get_reply_start_keyboard_ru())
    lang = message.text
    user_id = message.from_user.id
    await create_language(user_id, lang)


@dp.message(F.text == "🇺🇿 O'zbekcha")
async def start_next_step_uz(message: Message):
    await message.answer(text="O'zingizga kerakli bo'lgan tugmani bosing.", reply_markup=get_reply_start_keyboard_uz())
    lang = message.text
    user_id = message.from_user.id
    await create_language(user_id, lang)


@dp.message(F.text.in_(['Условия рассрочки', 'Rassrochka shartlari']))
async def installment_terms(message: Message):
    user_id = message.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский':
        await message.answer(text=text.installment_terms_ru)
    else:
        await message.answer(text=text.installment_terms_uz)


@dp.message(F.text.in_(['Акции и скидки', 'Aksiya va skidkalar']))
async def promotions_discounts(message: Message):
    user_id = message.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский':
        await message.answer(text=text.promotions_discounts_ru)
    else:
        await message.answer(text=text.promotions_discounts_uz)


@dp.message(F.text.in_(['Наши контакты', 'Bizning kontaktlarimiz']))
async def contacts(message: Message):
    user_id = message.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский':
        await message.answer(text=text.contacts_ru)
    else:
        await message.answer(text=text.contacts_uz)


@dp.message(F.text.in_(['Товары', 'Tovarlar']))
async def products_list(message: Message):
    user_id = message.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or message.from_user.id == settings.bots.admin_id:
        await message.answer(text=text.products_list_ru, reply_markup=category_inline_keyboard_ru())
    else:
        await message.answer(text=text.products_list_uz, reply_markup=category_inline_keyboard_uz())


@dp.message(F.text == 'Админ-панель')
async def admin_panel(message: Message):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer(text=text.admin_panel, reply_markup=get_reply_admin_edit_keyboard())
    else:
        await message.answer(text=text.admin_permission)


@dp.message(F.text == 'Главное меню')
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=get_reply_admin_keyboard())


@dp.message(F.text == '/orders')
async def view_orders(message: Message):
    db, cur = await db_start_order()
    orders = await get_orders(cur)
    if orders:
        for order in orders:
            user_id, name, phone, product_name, product_price = order
            await message.answer(f'Имя: {name}\r\nНомер телефона: {phone}\r\nНазвание продукта: {product_name}\r\n'
                                 f'Цена продукта: {product_price}')