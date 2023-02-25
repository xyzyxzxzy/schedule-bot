import logging

from vkwave.bots import SimpleLongPollBot

from config import TOKEN, GROUP_ID
from handlers import router

logging.basicConfig(level="DEBUG")

bot = SimpleLongPollBot(TOKEN, group_id=GROUP_ID)
bot.dispatcher.add_router(router)

bot.run_forever()