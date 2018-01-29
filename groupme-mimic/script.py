from train import train
from lib.markov.generate import generate
from bot import write_message
import pickle
import time
import json
import os


CURR_PATH = os.path.abspath(os.curdir)
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')
MODEL_PATH = os.path.join(CURR_PATH, 'models/markovmodel.pickle')
HISTORY_PATH = os.path.join(CURR_PATH, 'resources')
SECONDS_IN_DAY = 86400
MSG_COUNT = 10000
MSG_LIMIT = 100

settings = json.load(open('settings.json'))

def run_bot():

	pickle_in = open(ARGS_PATH, 'rb')
	bot_info = pickle.load(pickle_in)


	while(1):

		train(settings['token'],
			 bot_info['chat_id'],
			 bot_info['user_id'],
			 settings['user_name'],
			 HISTORY_PATH,
			 MODEL_PATH,
			 MSG_COUNT,
			 MSG_LIMIT
			 )


		message = generate(MODEL_PATH)
		print(message)

		write_message(bot_info['bot_id'], message)

		time.sleep(SECONDS_IN_DAY / settings['frequency_per_day'])


run_bot()

