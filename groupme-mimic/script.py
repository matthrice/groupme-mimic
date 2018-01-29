"""
script.py

Script to run GroupMe bot
"""

from train import train
from lib.markov.generate import generate
from bot import write_message
import pickle
import time
import json
import os

"""Absolute paths for models and resources"""
CURR_PATH = os.path.abspath(os.curdir)
ARGS_PATH = os.path.join(CURR_PATH, 'models/bot_info.pickle')
MODEL_PATH = os.path.join(CURR_PATH, 'models/markovmodel.pickle')
HISTORY_PATH = os.path.join(CURR_PATH, 'resources')

"""Constants for API querying"""
SECONDS_IN_DAY = 86400
MSG_COUNT = 10000
MSG_LIMIT = 100

"""User defined settings"""
settings = json.load(open('settings.json'))

def run_bot():
	"""
	Script to run bot

	- Runs on user defined intervals
	- Trains the bot on each iteration to keep up with new messages
	- Generates a message and writes it to chat every iteration
	"""


	"""Retrieve persistent bot info"""
	pickle_in = open(ARGS_PATH, 'rb')
	bot_info = pickle.load(pickle_in)

	"""Bot loop"""
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

