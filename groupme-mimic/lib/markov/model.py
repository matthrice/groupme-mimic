import sys
from lib.markov.chain import build_markov, save_model
import os

MODEL_PATH = 'groupme-mimic/models/markovmodel.pickle'

def model_markov(path, filename):
    markov_model = {}

    """Open file and build markov"""
    full_path = os.path.join(path, '{}chathistory.txt'.format(filename))
    with open(full_path, 'r') as f:
        formatted_text = f.read().replace('\n', '').split('.')
        build_markov(formatted_text, markov_model)

    save_model(markov_model, MODEL_PATH)
