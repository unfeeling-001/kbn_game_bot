from aiogram import Router, F, types
from aiogram.types import CallbackQuery, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

import time
import random

from keyboards import main_kb as kb

class CheckPassword(StatesGroup):
    peek = State()

rt = Router()

knb = ['Камень', 'Ножницы', 'Бумага']
score = 0
bot_score = 0

@rt.callback_query(F.data == 'go')
async def show_profile(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    
    await callback.message.answer(f'Отлично !')
    time.sleep(1)
    
    await callback.message.answer(f'Камень !')
    time.sleep(0.5)
    
    await callback.message.answer(f'Ножницы !')
    time.sleep(0.5)
    
    await callback.message.answer(f'Бумага !', reply_markup=kb.play_btn)
    time.sleep(0.5)
    
    await state.set_state(CheckPassword.peek)


@rt.message(CheckPassword.peek)
async def a_panel_2(message: Message, state: FSMContext):
    global score, bot_score
    user_choice = message.text  # Выбор пользователя
    rand_p = random.choice(knb)  # Случайный выбор бота
    
    # Проверяем введенное пользователем значение и выводим результаты
    if user_choice == 'Камень' and rand_p == 'Камень':
        await message.answer(rand_p)
        await message.answer(f'Ничья ! \nСчет - {bot_score} : {score}')
        
    elif user_choice == 'Камень' and rand_p == 'Ножницы':
        score += 1
        await message.answer(rand_p)
        await message.answer(f'Вы победили ! \nСчет - {bot_score} : {score}')
        
    elif user_choice == 'Камень' and rand_p == 'Бумага':
        bot_score += 1
        await message.answer(rand_p)
        await message.answer(f'Ура, я победил ! \nСчет - {bot_score} : {score}')
        
    elif user_choice == 'Ножницы' and rand_p == 'Ножницы':
        await message.answer(rand_p)
        await message.answer(f'Ничья ! \nСчет - {bot_score} : {score}')
        
    elif user_choice == 'Ножницы' and rand_p == 'Бумага':
        score += 1
        await message.answer(rand_p)
        await message.answer(f'Вы победили ! \nСчет - {bot_score} : {score}')
        
    elif user_choice == 'Ножницы' and rand_p == 'Камень':
        bot_score += 1
        await message.answer(rand_p)
        await message.answer(f'Ура, я победил ! \nСчет - {bot_score} : {score}')
    
    elif user_choice == 'Бумага' and rand_p == 'Бумага':
        await message.answer(rand_p)
        await message.answer(f'Ничья ! \nСчет - {bot_score} : {score}')
    
    elif user_choice == 'Бумага' and rand_p == 'Камень':
        score += 1
        await message.answer(rand_p)
        await message.answer(f'Вы победили ! \nСчет - {bot_score} : {score}')
    
    elif user_choice == 'Бумага' and rand_p == 'Ножницы':
        bot_score += 1
        await message.answer(rand_p)
        await message.answer(f'Ура, я победил ! \nСчет - {bot_score} : {score}')

