# Setup 
 - install tensorflow: ` pip install tensorflow `
 - install keras: ` pip install keras `
 ## Resources
 - tensorflow: [TensorFlow Installation](https://www.tensorflow.org/install) 
 - keras:[Keras Getting Started](https://keras.io/getting_started/)
 - Shakespeare File: ` https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt `
 - TBD:

## Troubleshooting
 - If the installation of TensorFlow produces an error message... ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\Username\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages\\tensorflow\\include\\external\\com_github_grpc_grpc\\src\\core\\ext\\filters\\client_channel\\lb_policy\\grpclb\\client_load_reporting_filter.h'

    ==HINT==: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at [Enable Long Paths](https://pip.pypa.io/warnings/enable-long-paths)

    ### Suggestion: 
     - [ ] Navigate to the "**Registry Editor**" on your computer.
     - [ ] **(Optional)** Create a backup of the current Registry for safety.
     - [ ] Access the following directory: "\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem"
     - [ ] Locate the file named "LongPathsEnabled".
     - [ ] Select the file and modify the value data to 1.
     - [ ] Click "Okay" to confirm the changes.
     - [ ] Restart your computer for the changes to take effect.
 - You should now have no problem with long file packets

# Understanding the Text Generator
 - For testing purposes, use a subset of the text to reduce processing time Here, we use a portion of the text from character 300,000 to 800,000: `text = text[300000:800000]`
 - **SEQ_LENGTH** determines how many characters are included in each input sequence. For example, if **SEQ_LENGTH** is 40, each input sequence will be 40 characters long: `SEQ_LENGTH = 40`
 - **STEP_SIZE** determines the interval between the start of each sequence. For example, if STEP_SIZE is 3, the sequences will start at positions 0, 3, 6, etc. This allows for overlapping sequences and increases the number of training examples.:`STEP_SIZE = 3`

 - Initialize numpy arrays for input (x) and output (y) with the appropriate dimensions 
 - x will have the shape (number of sequences, SEQ_LENGTH, number of unique characters)
 - y will have the shape (number of sequences, number of unique characters)
 *The dtype=np.float32 ensures the data is in the correct format for the model*
`x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.float32)`
`y = np.zeros((len(sentences), len(characters)), dtype=np.float32)`

 - Populate the numpy arrays with one-hot encoded data. Loop through each sequence and character to set the corresponding index in the array to 1: 
 ```
 for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i,t, char_to_index[character]] = 1
    y[i, char_to_index[next_chars[i]]] = 1

 ```
 ### Build The Model
 - The Sequential model allows us to build a neural network layer by layer
    `model = Sequential()`
 - Add an LSTM layer with 128 units. The input shape is (SEQ_LENGTH, len(characters)), where SEQ_LENGTH is the length of the sequence and len(characters) is the size of the character set.
    `model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))`
 - Add a Dense layer with len(characters) units to output a probability distribution over the character set
    `model.add(Dense(len(characters)))`
 - Add a softmax activation layer to convert the output to probabilities. The softmax activation function is commonly used for multi-class classification problems
    `model.add(Activation('softmax'))`
 - Compile the model with the categorical crossentropy loss function and RMSprop optimizer. The categorical crossentropy loss function is used for multi-class classification. The RMSprop optimizer is used with a learning rate of 0.01
    `model.compile(loss = 'categorical_crossentropy', optimizer = RMSprop(learning_rate = 0.01))`





