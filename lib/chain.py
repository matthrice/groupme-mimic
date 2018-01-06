import pickle
import random

def build_markov(text_data, markov_model):
    """Build model using markov chains"""

    for text in text_data:
        while text:
            line = text.readline()
            if line == "":
                break
            print(line)
            line = line.lower().split()
            for i, word in enumerate(line):
                if i == len(line) - 1:
                    markov_model['END'] = markov_model.get('END', []) + [word]
                else:
                    if i == 0:
                        markov_model['START'] = markov_model.get('START', []) + [word]
                    markov_model[word] = markov_model.get(word, []) + [line[i + 1]]

def save_model(markov_model, filename):
    """Save model as 'markov_model.pickle' """

    pickle_out = open(filename, 'wb')
    pickle.dump(markov_model, pickle_out)
    pickle_out.close()

def load_model(markov_model, filename):
    """Load model from specified filename"""

    pickle_in = open(filename, 'rb')
    markov_model = pickle.load(pickle_in)


def generate_sentence(markov_model):
    """Use markov chain to generate sentences"""

    generated = []
    while True:
        if not generated:
            words = markov_model['START']
        elif generated[-1] in markov_model['END']:
            break
        else:
            words = markov_model[generated[-1]]
        generated.append(random.choice(words))
    
    return generated.join(" ")
