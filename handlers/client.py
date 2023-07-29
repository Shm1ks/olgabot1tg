# -*- coding: utf-8 -*-
from aiogram import  types, Dispatcher, asyncio
from aiogram.dispatcher import FSMContext
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from filters import IsPrivate
from create_bot import dp
from aiogram.types import ContentType, Message, InputFile
from inlinekeyboard import start, start2, money, posmoney, gooda, vaprosorzapis
from data import admin_id


async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, "👋 Привет, я Бот Леоновой Ольги.\n\n"
												 "Расскажу тебе о профессии лешмейкер в интересном формате.\n\n"
												 "Просто читай и жми на кнопки.",
												 reply_markup=start
												 )
	
async def prestart(call: types.CallbackQuery):
	await call.message.answer('Выбери работу по душе и тебя никогда не придётся работать!!!\n\n\n'
							  '🏅И я с гордостью сейчас говорю, что я наращиваю реснички.\n'
							  'Потому что я научилась это делать хорошо и тебя научу.\n'
							  'ЛЕШМЕЙКЕР - это мастер по наращиванию ресниц. Одна из самых высокооплачиваемых профессий 2022 года.\n\n\n'
							  'И ещё 6 лет назад я этого не знала и конечно не понимала.\n'
							  'Ресницы делают взгляд моложе, придают уверенность и могут менять внешность девушки.\n'
							  'С помощью ресниц можно стать милой, дерзкой, весёлой или грустной.\n',
							  reply_markup=start2
							)
	
async def gaid(call: types.CallbackQuery):
	gaid = 'https://telegra.ph/Rukovodstvo-05-17-4'
	await call.answer('Сейчас я вам отправлю гайд. Обязательно к прочтению!!!',
					  show_alert=True
							)
	await asyncio.sleep(2)
	await call.message.answer(f"[В этом гайде я расскажу что такое наращивание ресниц, " \
                   f"какое оно бывает, стоимость по России, " \
                   f"сколько держатся наращённые реснички и многое другое.\n" \
                   f"Пожалуйста, прочтите гайд здесь]({gaid}).", parse_mode=types.ParseMode.MARKDOWN
					  )
	await asyncio.sleep(80)
	await call.message.answer('Как думаешь? Сколько мастера зарабатывают?',
			   				  reply_markup=money)
	
	

async def moneyreply(call: types.CallbackQuery):
	await call.message.answer('👍 Правильно и такие деньги то же.\n'
							  'Всё зависит от амбиций и желания мастера.\n\n\n'
							  'Но самое главное на мой взгляд, это то, что нет начальников.\n\n\n'
							  'Которые указывают👈, что и как делать. Когда отдыхать, а когда работать.\n\n\n' 
							  'Тебя никто не штрафует и не увольняет. Не следит и не подсматривает за тобой в камеру.\n\n\n'
							  'А так же, что это творческая профессия,'
							  'где раскрывается талант мастера и его индивидуальность.',
							  reply_markup=posmoney
							)
	
async def truereply(call: types.CallbackQuery):
	await call.message.answer('Согласна. Но ты не узнаешь, пока не попробуешь.')
	await asyncio.sleep(3)
	await call.message.answer('Я, Леонова Ольга.\n\n\n'
							  'Эксперт по скоростному наращиванию ресниц и продвижению мастеров. Учу наращивать ресницы офлайн и онлайн. Наращиваю в среднем за 1:10, рекорд скорости 34 минуты 🔥\n\n\n'
							  'Если вы хотите попробовать, но боитесь и не знаете получится у вас или нет, то приглашаю на БЕСПЛАТНЫЙ пробный часовой урок по наращиванию ресниц.\n\n\n'
							  'На этой неделе осталось 1 место на бесплатный урок, где я дам пошаговый план как начать и расскажу: как и сколько можно зарабатывать в ваших обстоятельствах. Вы сами сможете попробовать себя в качестве мастера, когда прямо, во время урока будете приклеивать свои первые реснички на манекен.',
							  reply_markup=gooda
							)
	
async def goodteach(call: types.CallbackQuery):
	await call.message.answer('А дальше, если только захотите, то запишитесь ко мне на обучение. Стоимость 15000 рублей вместо 20000, для тех, кто был на моём бесплатном уроке.\n'
			   
							  'Кстати, на обучение беру не всех. Честно. Если у вас не будет получаться, я вам об этом скажу. И тогда не будет смысла учиться.'
							  )
	await asyncio.sleep(10)
	await call.message.answer('Ну что, остались ещё вопросы? Уверенна что да.\n'
							  'Тогда просто напиши мне по Вотсап и задай их.',
							  reply_markup=vaprosorzapis
							)
	



def register_handlers_client(dp : Dispatcher):
	##dp.register_message_handler(send_photo_phile_id, content_types=ContentType.PHOTO)
	dp.register_callback_query_handler(prestart, text='Prestart')
	dp.register_callback_query_handler(gaid, text='gaid')
	dp.register_callback_query_handler(moneyreply, text='True')
	dp.register_callback_query_handler(truereply, text='posmoney')
	dp.register_callback_query_handler(goodteach, text='gooda')
	dp.register_message_handler(command_start, IsPrivate(), commands=['start'])
