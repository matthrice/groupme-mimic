import pickle
import os
import json

from bot import register_bot

CURR_PATH = os.path.abspath(os.curdir)
SETTINGS_PATH = os.path.join(CURR_PATH, 'settings.json')
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')

try:
    settings = json.load(open(SETTINGS_PATH))
except ValueError:
    print("Could not load settings.json")
    exit(1)

settings = json.load(open(SETTINGS_PATH))

bot_info = register_bot(settings['token'],
             settings['group_name'],
             settings['user_name'],
             settings['bot_name'],
             settings['avatar_url']
             )

pickle_out = open(ARGS_PATH, 'wb+')
pickle.dump(bot_info, pickle_out)
pickle_out.close()
