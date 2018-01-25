"""Main file to tie markov chaining and groupme scraping together"""
import os
from lib.markov.model import model_markov
from lib.markov.generate import generate
from lib.scrape.groupme import scrape_history, get_groupme_info
from settings import GLOBALS

def create_bot(token, group_name, user_name, path, msg_count, msg_limit, rescrape=True, retrain=True):
	chat_id, user_id = get_groupme_info(token, group_name, user_name)
	filename = user_name.replace(" ", "")
	if rescrape:
		scrape_history(token, chat_id, user_id, filename, path, msg_count, msg_limit)
	if retrain:
		model_markov(path, filename)
	generate()

create_bot(GLOBALS['token'],
		   GLOBALS['group_name'],
		   GLOBALS['user_name'],
		   GLOBALS['path'],
		   GLOBALS['msg_count'],
		   GLOBALS['msg_limit'],
		   True, True)