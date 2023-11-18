from core.database.products import db_start, get_products
from aiogram.types import CallbackQuery
from aiogram import F, Bot
from loader import dp


@dp.callback_query(F.data == 'fridge_tcl')
async def fridge_category(call: CallbackQuery):
    db, cur = await db_start()
    products = await get_products(cur)
    if products:
        for product in products:
            user_id, name, description, photo, price, category, brand = product
            if category == "fridge" and brand == 'TCL':
                await call.bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=f"{name}\r\n{description}\r\n"
                                                                                      f"{price}\r\n{category}\r\n{brand}")
    await call.answer()

