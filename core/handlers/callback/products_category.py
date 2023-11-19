from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram import F
from loader import dp
from core.keyboards.inline.inline import (fridge_inline_keyboard, category_inline_keyboard_ru, phone_inline_keyboard,
                                          conditioner_inline_keyboard, tv_inline_keyboard, category_inline_keyboard_uz)
from core.database.language import get_language
from core.bot_text import text
from core.settings import settings


@dp.callback_query(F.data == 'phone')
async def phone_list(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
        await call.message.edit_text("Телефоны", reply_markup=phone_inline_keyboard())
    else:
        await call.message.edit_text("Telefonlar", reply_markup=phone_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'tv')
async def tv_list(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
        await call.message.edit_text("Телевизоры", reply_markup=tv_inline_keyboard())
    else:
        await call.message.edit_text("Televizorlar", reply_markup=tv_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'conditioner')
async def conditioner_list(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
        await call.message.edit_text("Кондиционеры", reply_markup=conditioner_inline_keyboard())
    else:
        await call.message.edit_text("Konditsionerlar", reply_markup=conditioner_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'fridge')
async def fridge_list(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
        await call.message.edit_text("Холодильники", reply_markup=fridge_inline_keyboard())
    else:
        await call.message.edit_text("Xolodilniklar", reply_markup=fridge_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'back_category')
async def back_category(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    lang = await get_language(user_id)
    if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
        await call.message.edit_text(text=text.products_list_ru, reply_markup=category_inline_keyboard_ru())
        await call.answer()
    else:
        await call.message.edit_text(text=text.products_list_uz, reply_markup=category_inline_keyboard_uz())
        await call.answer()