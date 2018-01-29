"""
generate.py

Generate messages from saved markov model
"""

from lib.markov.chain import load_model, generate_sentence


def generate(MODEL_PATH):
    """
    Generate messages

    Params:
        @MODEL_PATH - path where model is located
    Return:
        Setence based of markov chain
    """
    markov_model = load_model(MODEL_PATH)
    sentence = ''
    while len(sentence.split()) < 5: # desired length greater than 5
        sentence = generate_sentence(markov_model)
    return sentence
