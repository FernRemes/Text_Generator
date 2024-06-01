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


# Create a list of sentences and a list of the next character for each sentence
sentences = []
next_chars = []

# Loop through the text the create the sequences of characters and the corresponding next character
for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_chars.append(text[i + SEQ_LENGTH])


# Initialize numpy arrays for input (x) and output (y) with the appropriate dimensions
x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype = np.float32)
y = np.zeros((len(sentences), len(characters)), dtype = np.float32)

# Populate the numpy arrays with one-hot encoded data
for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i,t, char_to_index[character]] = 1
    y[i, char_to_index[next_chars[i]]] = 1

# Build the Nueral Network model
model = Sequential()
model.add(LSTM(128, input_shape = (SEQ_LENGTH, len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = RMSprop(learning_rate = 0.01))

# Train the model with the training data
# Use a batch size of 256 and train for 4 epochs
model.fit(x,y, batch_size = 256, epochs = 4)

# Save the model to a file
# Only need to train the model once
model.save('textgenerator.model.keras')
