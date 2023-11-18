from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.state_form import StepsForm
from loader import dp
from aiogram import F
from aiogram import Bot
from core.keyboards.reply.basic import get_reply_admin_edit_keyboard
from core.keyboards.reply.reply_product_category import get_state_category_keyboard
from core.keyboards.reply.reply_product_brand import (get_state_brand_tv_keyboard, get_state_brand_conditioner_keyboard,
                                                      get_state_brand_fridge_keyboard, get_state_brand_phone_keyboard)
from core.database.products import create_product


@dp.message(F.text == 'Добавить товар')
async def get_product_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем Добавлять товар. Введите название товара.')
    await state.set_state(StepsForm.GET_NAME)


@dp.message(StepsForm.GET_NAME)
async def get_product_name(message: Message, state: FSMContext):
    await message.answer('Введите описание товара.')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_DESCRIPTION)


@dp.message(StepsForm.GET_DESCRIPTION)
async def get_product_description(message: Message, state: FSMContext):
    await message.answer('Отправьте фото товара.')
    await state.update_data(description=message.text)
    await state.set_state(StepsForm.GET_PHOTO)


@dp.message(StepsForm.GET_PHOTO)
async def get_product_photo(message: Message, state: FSMContext):
    await message.answer("Выберите категорию товара", reply_markup=get_state_category_keyboard())
    await state.update_data(photo=message.photo[0].file_id)
    await state.set_state(StepsForm.GET_CATEGORY)


@dp.message(StepsForm.GET_CATEGORY)
async def get_product_category(message: Message, state: FSMContext):
    category = ''
    if message.text == 'Холодильники':
        category = 'fridge'
        await message.answer("Выберите Бренд товара", reply_markup=get_state_brand_fridge_keyboard())

    elif message.text == 'Телефоны':
        category = 'phone'
        await message.answer("Выберите Бренд товара", reply_markup=get_state_brand_phone_keyboard())

    elif message.text == 'Телевизоры':
        category = 'tv'
        await message.answer("Выберите Бренд товара", reply_markup=get_state_brand_tv_keyboard())

    elif message.text == 'Кондиционеры':
        category = 'conditioner'
        await message.answer("Выберите Бренд товара", reply_markup=get_state_brand_conditioner_keyboard())

    await state.update_data(category=category)
    await state.set_state(StepsForm.GET_BRAND)


@dp.message(StepsForm.GET_BRAND)
async def get_product_category(message: Message, state: FSMContext):
    await message.answer("Укажите цену товара", reply_markup=None)
    await state.update_data(brand=message.text)
    await state.set_state(StepsForm.GET_PRICE)


@dp.message(StepsForm.GET_PRICE)
async def get_product_price(message: Message, state: FSMContext, bot: Bot):
    await message.answer("Данные записаны", reply_markup=get_reply_admin_edit_keyboard())
    context_data = await state.get_data()
    name = context_data.get('name')
    description = context_data.get('description')
    photo = context_data.get('photo')
    category = context_data.get('category')
    brand = context_data.get('brand')
    price = message.text

    await create_product(name, description, photo, category, brand, price)

    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{name}\r\n{description}\r\n{price}\r\n'
                                                                       f'{category}\r\n{brand}')
    await state.clear()

