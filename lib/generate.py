from chain import load_model, generate_sentence

markov_model = {}
load_model(markov_model, 'models/markov_model.pickle')
sentence = generate_sentence(markov_model)

print(sentence)