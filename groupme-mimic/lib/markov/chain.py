import pickle
import random

def add_word(key1, key2, markov_model):
    """
    add a word to markov model

    Params:
        @key1 - primary word
        @key2 - secondary word
    """
    if key1 in markov_model:
        if key2 in markov_model[key1]:
            markov_model[key1][key2] += 1
        else:
            markov_model[key1][key2] = 1
    else:
        markov_model[key1] = { key2: 1 }

def build_markov(text_data, markov_model):
    """
    Build model using markov chains

    Params:
        @text_data - full set of text to be parsed
        @markov_model - dictionary for building markov model

    """
    for line in text_data:
        line = line.lower().split()
        if line == '':
            continue
        for i, word in enumerate(line):
            if i == len(line) - 1:
                add_word('END', word, markov_model)
            else:
                if i == 0:
                    add_word('START', word, markov_model)
                add_word(word, line[i + 1], markov_model)


def save_model(markov_model, filename):
    """
    Save model as 'markov_model.pickle'

    Params:
        @markov_model - dicitonary of markov model
        @filename - filename for saving model
    """
    pickle_out = open(filename, 'wb+')
    pickle.dump(markov_model, pickle_out)
    pickle_out.close()

def load_model(filename):
    """
    Load model from specified filename

    Params:
        @filename - filename where model is saved

    Return:
        markov_model in dictionary form
    """

    pickle_in = open(filename, 'rb')
    markov_model = pickle.load(pickle_in)

    return markov_model

def build_choice_set(markov_model, word):
    """
    Build array for random next choice

    Params:
        @markov_model - dictionary of markov_model
    """
    words = []
    for key, value in markov_model[word].items():
        for i in range(value):
            words.append(key)
    return words

def generate_sentence(markov_model):
    """
    Use markov chain to generate sentences

    Params:
        @markov_model - dictionary of markov_model
    """

    generated = []
    while True:
        if not generated:
            words = build_choice_set(markov_model, 'START')
        elif generated[-1] in markov_model['END']:
            if generated[-1] in markov_model: # if it also has words which follow it
                freq_end = markov_model['END'][generated[-1]]
                freq_middle = 0
                for key in markov_model[generated[-1]]:
                    freq_middle += markov_model[generated[-1]][key]

                odds = freq_middle / (freq_end + freq_middle)
                if random.random() < odds: # case middle wins
                    words = build_choice_set(markov_model, generated[-1])
                else:
                    break
            else:
                break
        else:
            words = build_choice_set(markov_model, generated[-1])
        generated.append(random.choice(words))

    if not (generated[-1][-1] == '!'
            or generated[-1][-1] == '?'
            or generated[-1][-1] == '.'):
        generated[-1] += '.'

    return ' '.join(generated)
