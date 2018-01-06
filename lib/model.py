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

"""Open files"""
try:
    for filename in filenames:
        temp_file = open(filename, 'r')
        text_data.append(temp_file)
except:
    print("Could not open file")
    sys.exit(2)

markov_model = {}
build_markov(text_data, markov_model)
save_model(markov_model, 'markov_model.pickle')