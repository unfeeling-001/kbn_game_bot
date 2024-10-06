from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder




go = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Давай!", callback_data="go")
        ]
    ]
)

play_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Камень"),
            KeyboardButton(text="Ножницы"),
            KeyboardButton(text="Бумага")
        ]
    ],resize_keyboard=True
)