import pickle
import os
import json

from bot import register_bot

settings = json.load(open('settings.json'))

CURR_PATH = os.path.abspath(os.curdir)
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')

bot_info = register_bot(settings['token'],
             settings['group_name'],
             settings['user_name'],
             settings['bot_name'],
             settings['avatar_url']
             )

pickle_out = open(ARGS_PATH, 'wb+')
pickle.dump(bot_info, pickle_out)
pickle_out.close()
