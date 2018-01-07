import sys
from chain import build_markov, save_model
import os

filenames = []
text_data = []
markov_model = {}

"""Get command line file arguments"""
try:
    filenames = sys.argv[1:]
except:
    print("There must be at least one text")
    sys.exit(2)

"""Open file and build markov"""
markov_model = {}
for filename in filenames:
    with open(filename, 'r') as f:
        formatted_text = f.read().replace('\n', '').split('.')
        build_markov(formatted_text, markov_model)

save_model(markov_model, 'models/markov_model.pickle')