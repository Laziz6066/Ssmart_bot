from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.state_form import MailingForm
from loader import dp
from aiogram import F
from aiogram import Bot
from core.keyboards.reply.basic import get_reply_admin_edit_keyboard
from core.database.language import get_user_id, db_start_language
from core.settings import settings
from core.database.mailing import create_mailing


@dp.message(F.text == 'Сделать рассылку')
async def get_mailing_form(message: Message, state: FSMContext):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer(f'{message.from_user.first_name}, отправьте фото товара.')
        await state.set_state(MailingForm.GET_PHOTO)


@dp.message(MailingForm.GET_PHOTO)
async def get_mailing_photo(message: Message, state: FSMContext):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer("Введите текст.")
        await state.update_data(photo=message.photo[0].file_id)
        await state.set_state(MailingForm.GET_DESCRIPTION)


@dp.message(MailingForm.GET_DESCRIPTION)
async def get_mailing_description(message: Message, state: FSMContext, bot: Bot):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer("Данные записаны", reply_markup=get_reply_admin_edit_keyboard())
        context_data = await state.get_data()
        photo = context_data.get('photo')
        description = message.text

        await create_mailing(photo, description)
        db, cur = await db_start_language()
        mailings = await get_user_id(cur)
        for i in mailings:
            user_id, lang = i
            await bot.send_photo(chat_id=user_id, photo=photo, caption=f'{description}')
        await state.clear()