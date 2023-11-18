from loader import dp
from aiogram import F
from aiogram.types import Message
from core.bot_text.text import button_development


@dp.message(F.text == 'Удалить товар')
async def get_product_form(message: Message):
    await message.answer(text=button_development)


@dp.message(F.text == 'Сделать рассылку')
async def get_product_form(message: Message):
    await message.answer(text=button_development)


@dp.message(F.text == 'Изменить товар')
async def get_product_form(message: Message):
    await message.answer(text=button_development)