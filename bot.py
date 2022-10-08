from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from sqlighter import *

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if check_user(message.chat.id):
        if check_admin(message.chat.id):
            await message.reply_document(get_file(), caption='Последняя версия Casva для Android')
        else:
            await message.reply_document(get_file(), caption='Последняя версия Casva для Android')
    else:
        create_user(message.chat.id)
        await message.reply_document(get_file(), caption='Последняя версия Casva для Android')


@dp.message_handler(content_types=['document'])
async def getting_file(message: types.Message):
    if check_admin(message.chat.id):
        create_file(message.document.file_id)
        await message.reply('Файл сохранен, начинаю отправлять последнюю версию всем пользователям')
        for user in get_user_list():
            await bot.send_document(user, message.document.file_id, caption='Новая версия Casva!')
        await message.reply('Готово!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
