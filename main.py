import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file('shakespeare.txt','https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# All characters be lowercase for less choices the AI can do
# The grammar is not good but becomes beteer performance
text = open(filepath, 'rb').read().decode('utf-8').lower()  

# # testing purposes
# text = text[300000:800000] 

characters = sorted(set(text))

char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))


SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_chars = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_chars.append(text[i + SEQ_LENGTH])

x = np.zeros(len(sentences), SEQ_LENGTH, len(characters), dtype = bool)
y = np.zeros(len(sentences), len(characters), dtype = bool)

for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i,t, char_to_index[character]] = 1
    y[i, char_to_index[next_chars[i]]] = 1



