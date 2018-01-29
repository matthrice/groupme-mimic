"""Main file to tie markov chaining and groupme scraping together"""
import os
from lib.markov.model import model_markov
from lib.scrape.groupme import scrape_history, get_groupme_info
from settings import GLOBALS, BOT

def train(token, group_name, user_name, path, msg_count, msg_limit):
	chat_id, user_id = get_groupme_info(token, group_name, user_name)
	filename = user_name.replace(" ", "")
	scrape_history(token, chat_id, user_id, filename, path, msg_count, msg_limit)
	model_markov(path, filename)
	return chat_id, user_id
