from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import text_14_5
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.row(button)
kb.insert(button2)
kb.row(button3)
kb.insert(button4)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_inline = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_inline2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.row(button_inline)
kb_inline.insert(button_inline2)

kb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f'{text_14_5.product1}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{text_14_5.product2}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{text_14_5.product3}', callback_data='product_buying')],
        [InlineKeyboardButton(text=f'{text_14_5.product4}', callback_data='product_buying')]
    ], resize_keyboad=True
)