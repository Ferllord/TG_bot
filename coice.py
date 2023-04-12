from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

coice = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton(text='Котик')
but2 = KeyboardButton(text='Собачка')
coice.add(but1,but2)