import asyncio
from aiogram import Bot
from aiogram.enums import ParseMode
import logging
from core.handlers.basic import command_start_handler
from core.settings import settings
from loader import dp
from core.utils.commands import set_commands
from core.handlers.callback.products_category import fridge_list, back_category, phone_list, conditioner_list, tv_list
from core.handlers.callback.products_brands import fridge_category
from aiogram import F
from core.database.products import db_start
from core.database.language import db_start_language
from core.handlers.products_add import (get_product_form, get_product_name, get_product_photo,
                                        get_product_price, get_product_description)
from core.handlers.basic import start_next_step_ru, start_next_step_uz
from core.handlers.callback.order_product import order_name
from core.database.order import db_start_order


async def start_bot(bot: Bot):
    await set_commands(bot)
    await db_start()
    await db_start_language()
    await db_start_order()
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


dp.startup.register(start_bot)
dp.shutdown.register(stop_bot)
dp.message.register(command_start_handler, F.text == 'start')
dp.message.register(start_next_step_ru, F.text == '🇷🇺 Русский')
dp.message.register(start_next_step_uz, F.text == "🇺🇿 O'zbekcha")

# dp.message.register(show_products, F.text == 'load')

dp.callback_query.register(fridge_list, F.text == 'fridge')
dp.callback_query.register(back_category, F.text == 'back_category')
dp.callback_query.register(phone_list, F.text == 'phone')
dp.callback_query.register(conditioner_list, F.text == 'conditioner')
dp.callback_query.register(tv_list, F.text == 'tv')
dp.callback_query.register(order_name, F.data.startswith('order_'))

dp.callback_query.register(fridge_category, F.text == 'fridge_tcl')

dp.message.register(get_product_form, F.text == 'Добавить товар')
dp.message.register(get_product_name)
dp.message.register(get_product_description)
dp.message.register(get_product_photo)
dp.message.register(get_product_price)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())