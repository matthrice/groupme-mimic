from chain import load_model, generate_sentence

markov_model = {}
load_model(markov_model, 'markov_model.pickle')
sentence = generate_sentence(markov_model)

print(sentence)