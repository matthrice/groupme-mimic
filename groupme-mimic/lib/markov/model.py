import sys
from lib.markov.chain import build_markov, save_model
import os

def model_markov(history_path, model_path, filename):
    markov_model = {}

    """Open file and build markov"""
    full_path = os.path.join(history_path, '{}chathistory.txt'.format(filename))
    with open(full_path, 'r') as f:
        formatted_text = f.read().replace('\n', '').split('.')
        build_markov(formatted_text, markov_model)

    save_model(markov_model, model_path)
