from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import config


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
	await bot.set_webhook(config.URL_APP)

async def on_shutdown(dp):
	await bot.delete_webhook()

@dp.message_handler()
async def echo_send(types : types.Message):
	if message.text == 'Привет':
		await message.answer('И тебе тоже')







keyboard = InlineKeyboardMarkup()
urlkb = InlineKeyboardButton(text='Ссылка', url='https://t.me/taker_play')
keyboard.add(urlkb)

@dp.message_handler(commands=['start'])
async def url_command(message : types.Message):
	await message.answer('Вот:', reply_markup=urlkb)

executor.start_webhook(
	dispatcher = dp,
	webhook_path = '',
	on_startup=on_startup,
	on_shutdown=on_shutdown,
	skip_updates=True,
	host="0.0.0.0",
	port=int(os.environ.get('PORT', 5000)))


		