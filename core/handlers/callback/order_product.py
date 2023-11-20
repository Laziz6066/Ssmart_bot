from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from core.utils.state_form import OrderForm
from loader import dp
from aiogram import F
from aiogram import Bot
from core.keyboards.reply.basic import get_reply_admin_edit_keyboard, get_reply_contact_keyboard
from core.database.order import create_order
from core.settings import settings


@dp.callback_query(F.data.startswith('order_'))
async def order_name(call: CallbackQuery, state: FSMContext):
    await call.answer(f'{call.from_user.first_name}, Введите ФИО.')
    await state.set_state(OrderForm.GET_NAME)


@dp.message(OrderForm.GET_NAME)
async def get_name(message: Message, state: FSMContext):
    await message.answer('Введите свой номер телефона.', reply_markup=get_reply_contact_keyboard())
    await state.update_data(name=message.text)
    await state.set_state(OrderForm.GET_PHONE)


@dp.message(OrderForm.GET_PHONE)
async def get_phone(message: Message, state: FSMContext, bot: Bot):
    await message.answer("Данные записаны", reply_markup=get_reply_admin_edit_keyboard())
    context_data = await state.get_data()
    name = context_data.get('name')
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    product_name = context_data.get('product_name')
    product_price = context_data.get('product_price')

    await create_order(name, phone, product_name, product_price)

    admin_message = (
        f'New registration:\r\n'
        f'Name: {name}\r\n'
        f'Phone: {phone}\r\n'
        f'Product: {product_name}\r\n'
        f'Price: {product_price}'
    )

    # Use the bot.send_message method to send the notification
    await bot.send_message(chat_id=settings.bots.admin_id, text=admin_message)

    await message.answer(f'Данные записаны\r\n{name}\r\n{phone}\r\nВыбранный товар: {product_name}\r\n'
                         f'Цена: {product_price}')
    await state.clear()