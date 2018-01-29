from settings import BOT, GLOBALS
from train import train
from lib.markov.generate import generate
from bot import register_bot, write_message, destroy_bot
import pickle

ARGS_PATH = 'groupme-mimic/models/bot_id.pickle'



def run_bot(retrain=False, reregister=False):

	chat_id = ''
	user_id = ''
	bot_id = ''

	if (retrain):

		chat_id, user_id = train(GLOBALS['token'],
			 BOT['group_name'],
			 BOT['user_name'],
			 GLOBALS['path'],
			 GLOBALS['msg_count'],
			 GLOBALS['msg_limit']
			 )

	if (reregister):

		bot_id = register_bot(GLOBALS['token'],
		     BOT['group_name'],
		     BOT['user_name'],
		     BOT['bot_name'],
		     BOT['avatar_url']
			 )

		pickle_out = open(ARGS_PATH, 'wb+')
		pickle.dump(bot_id, pickle_out)
		pickle_out.close()

	pickle_in = open(ARGS_PATH, 'rb')
	bot_id = pickle.load(pickle_in)

	message = generate()

	write_message(bot_id, message)


run_bot(retrain=True, reregister=True)

