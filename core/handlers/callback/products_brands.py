from core.database.products import db_start, get_products
from aiogram.types import CallbackQuery
from aiogram import F
from loader import dp
from core.keyboards.inline.inline import submit_application_ru, submit_application_uz
from core.database.language import get_language
from core.settings import settings
from aiogram.fsm.context import FSMContext


@dp.callback_query(F.data.startswith('fridge_'))
async def fridge_category(call: CallbackQuery, state: FSMContext):
    db, cur = await db_start()
    products = await get_products(cur)
    brand_f = call.data.split('_')[1]
    print(brand_f)
    if products:
        for product in products:
            user_id, name, description, photo, price, category, brand = product
            if category == "fridge" and brand == brand_f:
                user_id = call.from_user.id
                lang = await get_language(user_id)
                if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=f"{name}\r\n{description}\r\n"
                                                                                          f"{price}",
                                              reply_markup=submit_application_ru())
                else:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=f"{name}\r\n{description}\r\n"
                                                                                          f"{price}",
                                              reply_markup=submit_application_uz())
                await state.update_data(product_name=name)
                await state.update_data(product_price=price)
    await call.answer()


@dp.callback_query(F.data.startswith('phone_'))
async def fridge_category(call: CallbackQuery, state: FSMContext):
    db, cur = await db_start()
    products = await get_products(cur)
    brand_f = call.data.split('_')[1]
    print(brand_f)
    if products:
        for product in products:
            user_id, name, description, photo, price, category, brand = product
            if category == "phone" and brand == brand_f:
                user_id = call.from_user.id
                lang = await get_language(user_id)
                if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_ru())

                else:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_uz())
                await state.update_data(product_name=name)
                await state.update_data(product_price=price)
    await call.answer()


@dp.callback_query(F.data.startswith('tv_'))
async def fridge_category(call: CallbackQuery, state: FSMContext):
    db, cur = await db_start()
    products = await get_products(cur)
    brand_f = call.data.split('_')[1]
    print(brand_f)
    if products:
        for product in products:
            user_id, name, description, photo, price, category, brand = product
            if category == "tv" and brand == brand_f:
                user_id = call.from_user.id
                lang = await get_language(user_id)
                if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_ru())
                else:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_uz())
                await state.update_data(product_name=name)
                await state.update_data(product_price=price)
    await call.answer()


@dp.callback_query(F.data.startswith('conditioner_'))
async def fridge_category(call: CallbackQuery, state: FSMContext):
    db, cur = await db_start()
    products = await get_products(cur)
    brand_f = call.data.split('_')[1]
    print(brand_f)
    if products:
        for product in products:
            user_id, name, description, photo, price, category, brand = product
            if category == "conditioner" and brand == brand_f:
                user_id = call.from_user.id
                lang = await get_language(user_id)
                if lang == '🇷🇺 Русский' or call.from_user.id == settings.bots.admin_id:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_ru())
                else:
                    await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                              caption=f"{name}\r\n{description}\r\n"
                                                      f"{price}",
                                              reply_markup=submit_application_uz())
                await state.update_data(product_name=name)
                await state.update_data(product_price=price)
    await call.answer()