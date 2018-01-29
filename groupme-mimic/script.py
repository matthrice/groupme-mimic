from settings import BOT, GLOBALS
from train import train
from lib.markov.generate import generate
from bot import write_message, destroy_bot
import pickle
import time
import os


CURR_PATH = os.path.abspath(os.curdir)
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')
MODEL_PATH = os.path.join(CURR_PATH, 'models/markovmodel.pickle')
HISTORY_PATH = os.path.join(CURR_PATH, 'resources')


def run_bot():

	pickle_in = open(ARGS_PATH, 'rb')
	bot_info = pickle.load(pickle_in)


	while(1):

		train(GLOBALS['token'],
			 bot_info['chat_id'],
			 bot_info['user_id'],
			 BOT['user_name'],
			 HISTORY_PATH,
			 MODEL_PATH,
			 GLOBALS['msg_count'],
			 GLOBALS['msg_limit']
			 )


		message = generate(MODEL_PATH)
		print(message)

		write_message(bot_info['bot_id'], message)

		time.sleep(5)


run_bot()

