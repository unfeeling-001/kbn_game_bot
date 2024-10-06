import asyncio

from aiogram import Bot, Dispatcher

from handlers import handler
from callbacks import callbacks

TOKEN = 'YOU_API'


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        handler.rt,
        callbacks.rt
    )

    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled!')
