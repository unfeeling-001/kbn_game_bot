from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards import main_kb as kb

rt = Router()

class CheckPassword(StatesGroup):
    peek = State()

@rt.message(Command('start'))
async def start(message: Message):
    
    await message.answer(f'Привет, {message.from_user.last_name} \nДавай сыграем в КНБ?', reply_markup=kb.go)

