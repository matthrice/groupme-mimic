import sys
from chain import build_markov, save_model

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
try:
    for filename in filenames:
        print(filename)
        with open(filename, 'r') as f:
            build_markov(f, markov_model)
except:
    print("Could not open file")
    sys.exit(2)

save_model(markov_model, 'models/markov_model.pickle')