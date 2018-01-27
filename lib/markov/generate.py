from lib.markov.chain import load_model, generate_sentence

MODEL_PATH = 'models/markovmodel.pickle'

def generate():
    markov_model = load_model(MODEL_PATH)
    sentence = ''
    while len(sentence.split()) < 5: # desired length greater than 5
        sentence = generate_sentence(markov_model)
    return sentence