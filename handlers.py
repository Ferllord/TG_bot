from main import bot, dp
import requests
from aiogram.types import Message,CallbackQuery
from config import admin_id
import os
from coice import coice

url_kat = 'https://loremflickr.com/320/240'
url_dog = 'https://loremflickr.com/320/240/dog'
path = 'C:\\Users\\alshe\\Desktop\\to_send.jpg'

def save_phot(url):
    p = requests.get(url, allow_redirects=True)
    with open(path, 'wb') as file:
        file.write(p.content)


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')

@dp.message_handler()
async def echo(message: Message):
    text = f'{message.text}'
    if text != 'Собачка' and text != 'Котик' and text != '/start':
        await message.answer(text='Напишите /start для начала использования')
    else:
        if text == '/start':
            await message.answer(text='Начнем!',reply_markup=coice)
        else:
            if text == 'Собачка' :
                url = url_dog
            elif text == 'Котик':
                url = url_kat
            save_phot(url)
            with open(path,'rb') as file:
                await message.answer_photo(photo=file,reply_markup=coice)
                os.remove(path)



# @dp.callback_query_handler(text = 'kat')
# async def kat_call(callback : CallbackQuery):
#     save_phot(url_kat)
#     with open(path,'rb') as file:
#         await callback.message.answer_photo(file)
#         os.remove(path)
#         await callback.answer()
#
#
# @dp.callback_query_handler(text = 'dog')
# async def kat_call(callback : CallbackQuery):
#     save_phot(url_dog)
#     with open(path,'rb') as file:
#         await callback.message.answer_photo(file)
#         os.remove(path)
#         await callback.answer()