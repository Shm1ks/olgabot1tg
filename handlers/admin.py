from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import dp
from filters import IsPrivate

class FSMAdmin(StatesGroup):
    text = State()
    state = State()
    photo = State()



@dp.message_handler(IsPrivate(), text='/mailing')
async def cm_start(message : types.Message):
    await message.answer(f'Введите текст рассылки:')
    await FSMAdmin.text.set()

@dp.message_handler(IsPrivate(), state=FSMAdmin.text)
async def load_text(message : types.Message, state : FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                       [
                                            InlineKeyboardButton(text='Добавить Фотографии', callback_data='add_photo'),
                                            InlineKeyboardButton(text='Далее', callback_data='next')
                                       ]
                                       ])
    await state.update_data(text=answer)
    await FSMAdmin.state.set()

@dp.message_handler(text='add_photo', state=FSMAdmin.state)
async def add_photo(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Пришлите фото')
    await FSMAdmin.photo.set()

@dp.message_handler(text='add_photo', state=FSMAdmin.state)
async def add_photo(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Пришлите фото')
    await FSMAdmin.photo.set()

def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, commands=['Новости'])
	dp.register_message_handler(load_text, state=FSMAdmin.text)
	dp.register_message_handler(add_photo, content_types=['photo'], state=FSMAdmin.text)