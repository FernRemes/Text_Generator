* install tensor
* install keras
* if tenosr installation outputs an error: ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\Username\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages\\tensorflow\\include\\external\\com_github_grpc_grpc\\src\\core\\ext\\filters\\client_channel\\lb_policy\\grpclb\\client_load_reporting_filter.h'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths

Suggestion: 
    go to your computer's "Registry Editor"
    ( Optional ) make a backup of current Registry
    Go to this directory: "\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem"
    You will find a file named LongPathsEnabled
    Click it and change value data to 1
    Press Okay
    Restart Computer

You should now have no problem with long file packets



Shakespeare File:
https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt


Decoding file:

filepath = tf.keras.utils.get_file('shakespeare.txt','https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# All characters be lowercase for less choices the AI can do
# The grammar is not good but becomes beteer performance
text = open(filepath, 'rb').read().decode('utf-8').lower()  

Sort the characters from the text file:

characters = sorted(set(text))

char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))


