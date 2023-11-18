from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram import F
from loader import dp
from core.keyboards.inline.inline import (fridge_inline_keyboard, category_inline_keyboard, phone_inline_keyboard,
                                          conditioner_inline_keyboard, tv_inline_keyboard)


@dp.callback_query(F.data == 'phone')
async def phone_list(call: CallbackQuery, bot: Bot):
    await call.message.edit_text("Телефоны", reply_markup=phone_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'tv')
async def tv_list(call: CallbackQuery, bot: Bot):
    await call.message.edit_text("Телевизоры", reply_markup=tv_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'conditioner')
async def conditioner_list(call: CallbackQuery, bot: Bot):
    await call.message.edit_text("Кондиционеры", reply_markup=conditioner_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'fridge')
async def fridge_list(call: CallbackQuery, bot: Bot):
    await call.message.edit_text("Холодильники", reply_markup=fridge_inline_keyboard())
    await call.answer()


@dp.callback_query(F.data == 'back_category')
async def back_category(call: CallbackQuery, bot: Bot):
    await call.message.edit_text('Категории товаров', reply_markup=category_inline_keyboard())
    await call.answer()