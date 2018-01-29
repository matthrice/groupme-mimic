import pickle
import os

from bot import register_bot
from settings import GLOBALS, BOT

CURR_PATH = os.path.abspath(os.curdir)
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')

bot_info = register_bot(GLOBALS['token'],
             BOT['group_name'],
             BOT['user_name'],
             BOT['bot_name'],
             BOT['avatar_url']
             )

print(bot_info)

pickle_out = open(ARGS_PATH, 'wb+')
pickle.dump(bot_info, pickle_out)
pickle_out.close()
