from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from app.generators import gpt_text, gpt_image, gpt_vision
from app.database.requests import set_user, get_user, calculate

from decimal import Decimal
import uuid
import os

import app.keyboards as kb
from app.states import Chat, Image

user = Router()

@user.message(F.text == '❌ Отмена')
@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await message.answer('На старт!', reply_markup=kb.main)
    await state.clear()

@user.message(F.text == 'Чатиться')
async def cmd_chat(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Chat.text)
        await message.answer('Введите Ваш запрос', reply_markup=kb.cancel)
    else:
        await message.answer('У Вас недостаточно средств')

@user.message(Chat.text, ~F.photo)
async def text_chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Chat.wait)
        response = await gpt_text(message.text, 'gpt-4o')
        await calculate(message.from_user.id, response['usage'], 'gpt-4o', user)
        await message.answer(response['response'], parse_mode='Markdown')
        await state.set_state(Chat.text)
    else:
        await message.answer('У Вас недостаточно средств')

@user.message(Chat.text, F.photo)
async def photo_chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Chat.wait)
        
        # Получение фото
        file = await message.bot.get_file(message.photo[-1].file_id)
        file_path = file.file_path
        file_name = f"{uuid.uuid4()}.jpeg"
        
        # Скачивание файла
        await message.bot.download_file(file_path, file_name)
        
        # Текстовый запрос (если caption пустой, то используем стандартный запрос)
        req = message.caption if message.caption else "Опишите, что изображено на этом фото."
        
        # Запрос в GPT Vision
        try:
            response = await gpt_vision(req, 'gpt-4o', file_name)
            await calculate(message.from_user.id, response['usage'], 'gpt-4o', user)
            await message.answer(response['response'], parse_mode='Markdown')
        except Exception as e:
            await message.answer(f"Произошла ошибка при обработке изображения: {e}")
        
        # Очистка состояния и удаление временного файла
        await state.set_state(Chat.text)
        os.remove(file_name)
    else:
        await message.answer('У Вас недостаточно средств')

@user.message(Image.wait)
@user.message(Chat.wait)
async def wait_wait(message: Message):
    await message.answer('Подождите, пожалуйста, сообщение генерируется...')

###### Генерация картинок ######

@user.message(F.text == 'Сгенерировать картинку')
async def cmd_generate_image(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Image.text)
        await message.answer('Введите Ваш запрос', reply_markup=kb.cancel)
    else:
        await message.answer('У Вас недостаточно средств')

@user.message(Image.text)
async def image_generation_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Image.wait)
        response = await gpt_image(message.text, 'dall-e-3')
        await calculate(message.from_user.id, response['usage'], 'dall-e-3', user)
        print(response)
        try:
            await message.answer_photo(photo=response['response'])
        except Exception as e:
            print(e)
            await message.answer(response['response'], parse_mode='Markdown')
        await state.set_state(Image.text)
    else:
        await message.answer('У Вас недостаточно средств')
