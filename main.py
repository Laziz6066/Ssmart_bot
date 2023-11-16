import asyncio
from aiogram import Bot
from aiogram.enums import ParseMode
import logging
from core.handlers.basic import command_start_handler
from core.settings import settings
from loader import dp
from core.utils.commands import set_commands
from core.handlers.products_callback import fridge_list, back_category, phone_list, conditioner_list, tv_list
from aiogram import F


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


dp.startup.register(start_bot)
dp.shutdown.register(stop_bot)
dp.message.register(command_start_handler)
dp.callback_query.register(fridge_list, F.text == 'fridge')
dp.callback_query.register(back_category, F.text == 'back_category')
dp.callback_query.register(phone_list, F.text == 'phone')
dp.callback_query.register(conditioner_list, F.text == 'conditioner')
dp.callback_query.register(tv_list, F.text == 'tv')


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())