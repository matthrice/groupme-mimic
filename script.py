from settings import BOT, GLOBALS
from train import train
from lib.markov.generate import generate
from bot import register_bot, write_message
import pickle

ARGS_PATH = 'models/persistent_args.pickle'



def run_bot(args_file, retrain=False, reregister=False, repickle=False):
	
	persistent_args = {
		'chat_id': '',
		'user_id': '',
		'bot_id': ''
	}

	if (retrain):

		persistent_args['chat_id'], persistent_args['user_id'] = train(GLOBALS['token'],
			 BOT['group_name'],
			 BOT['user_name'],
			 GLOBALS['path'],
			 GLOBALS['msg_count'],
			 GLOBALS['msg_limit']
			 )

	if (reregister):

		persistent_args['bot_id'] = register_bot(GLOBALS['token'],
		     BOT['group_name'],
		     BOT['user_name'],
		     BOT['bot_name'],
		     BOT['avatar_url']
			 )

	if (repickle):
		pickle_out = open(args_file, 'wb+')
		pickle.dump(persistent_args, pickle_out)
		pickle_out.close()


	pickle_in = open(args_file, 'rb')
	args2 = pickle.load(pickle_in)

	message = generate()

	write_message(args2['bot_id'], message)

run_bot(ARGS_PATH, True, True, True)

