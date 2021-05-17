import logging
from aiogram import Bot, Dispatcher, executor, types
from app import get_page
from datetime import datetime
from pyppeteer.errors import NetworkError
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config['DEFAULT']['API_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        byte_img = await get_page(message.text)
        await bot.send_document(message.chat.id, (f'{datetime.now()}.png', byte_img))
    except NetworkError:
        await message.reply("Page not found")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
