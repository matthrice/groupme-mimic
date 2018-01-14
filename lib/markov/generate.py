from lib.markov.chain import load_model, generate_sentence

def generate_sentence(model_path):
    markov_model = load_model(model_path)
    sentence = generate_sentence(markov_model)

    print(sentence)