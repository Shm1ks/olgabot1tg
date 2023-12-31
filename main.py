from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin


async def on_startup(dp):
	from utils.notify_admins import on_startup_notify
	from utils.set_bot_commands import set_default_commands
	import filters
	filters.setup(dp)
	await on_startup_notify(dp)
	await set_default_commands(dp)

	print('Бот Запустился на сервер Telegram')


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)