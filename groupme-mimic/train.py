"""
train.py

Main file to tie markov chaining and groupme scraping together
"""
import os
from lib.markov.model import model_markov
from lib.scrape.groupme import scrape_history, get_groupme_info
import pickle



def train(token, chat_id, user_id, user_name, history_path, model_path, msg_count, msg_limit):
    """
    Train the markov model on a new set of messaging data

    Params
        @token - GroupMe API token
        @chat_id - GroupMe chat id
        @user_id - GroupMe user id for modeling
        @user_name - name for resources txt file
        @history_path - path for resources txt file
        @model_path - path for the markovmodel file
        @msg_count - number of messages to stretch back
        @msg_limit - number of messages to retrieve each iteration
                   - cannot exceed 100


    """
    filename = user_name.replace(" ", "")
    scrape_history(token, chat_id, user_id, filename, history_path, msg_count, msg_limit)
    model_markov(history_path, model_path, filename)

