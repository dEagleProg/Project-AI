from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Чатиться')],
    [KeyboardButton(text = 'Сгенерировать картинку')]

],                  resize_keyboard=True,
                    input_field_placeholder='Выберите действие')

cancel = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='❌ Отмена')]],
                             resize_keyboard=True,
                             input_field_placeholder='Выберите действие')