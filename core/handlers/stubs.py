from loader import dp
from aiogram import F
from aiogram.types import Message
from core.bot_text.text import button_development
from core.settings import settings


@dp.message(F.text.in_(['Удалить товар', 'Сделать рассылку', 'Изменить товар']))
async def get_product_form(message: Message):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer(text=button_development)