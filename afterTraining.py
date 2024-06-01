import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

# Download the dataset
filepath = tf.keras.utils.get_file('shakespeare.txt','https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# Read the text data and convert it to lowercase 
# the grammar may be incorrect but the AI will handle better with less choices 
text = open(filepath, 'rb').read().decode('utf-8').lower()  

# Use a subset of the text for testing purposes
# if your computer can support large datasets than comment out
text = text[300000:800000] 

# Create a sorted list of unique characters in the dataset
characters = sorted(set(text))

# Create dictionaries to map each characters to their index and vice versa
char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))

# Define the length of each sequence and the step size for creating sequences
SEQ_LENGTH = 40
STEP_SIZE = 3


model = tf.keras.models.load_model('textgenerator.model.keras')

def sample(preds, temprature = 1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temprature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def generate_text(length, temperature):
    start = random.randint(0, len(text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = text[start : start + SEQ_LENGTH]
    generated += sentence
    for _ in range(length) :
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, character in enumerate(sentence) :
            x[0, t, char_to_index[character]] = 1

        predictions = model.predict(x, verbose = 0)[0]
        next_index = sample(predictions, temperature)
        next_char = index_to_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

    return generated

print('---------0.2---------')
print(generate_text(300, 0.2))
print('---------0.1---------')
print(generate_text(300, 0.1))
print('---------0.3---------')
print(generate_text(300, 0.3))
print('---------0.5---------')
print(generate_text(300, 0.5))
print('---------0.6---------')
print(generate_text(300, 0.6))
print('---------0.8---------')
print(generate_text(300, 0.8))
print('---------1.0---------')
print(generate_text(300, 1.0))