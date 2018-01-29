"""Main file to tie markov chaining and groupme scraping together"""
import os
from lib.markov.model import model_markov
from lib.scrape.groupme import scrape_history, get_groupme_info
import pickle



def train(token, chat_id, user_id, user_name, history_path, model_path, msg_count, msg_limit):
	filename = user_name.replace(" ", "")
	scrape_history(token, chat_id, user_id, filename, history_path, msg_count, msg_limit)
	model_markov(history_path, model_path, filename)

