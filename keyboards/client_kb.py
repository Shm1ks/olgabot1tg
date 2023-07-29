from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



kb_client = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Профиль'),
            KeyboardButton(text='Бобер')
        ],
        [
            KeyboardButton(text='Человек')
        ]
    ],
    resize_keyboard=True
    )

