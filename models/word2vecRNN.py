from preprocess.word2vec import convert_to_keras_embeddings
from preprocess.parser import get_data_as_lists
from keras import Sequential
from keras.layers import SimpleRNN, Dense, Flatten, Input
from keras.optimizers import Adam
from keras.preprocessing.text import text_to_word_sequence, one_hot
from keras.callbacks import TensorBoard
from keras.utils import to_categorical
import numpy as np
from gensim.corpora import Dictionary


model = Sequential()

x = get_data_as_lists()[0][0]
y = get_data_as_lists()[0][1]

x_test = get_data_as_lists()[1][0]
y_test = get_data_as_lists()[1][1]

max_sequence_length = 1000

tensorboard_cb = TensorBoard(log_dir='./Graph', histogram_freq=0,  
          write_graph=True, write_images=True)
train_params = {"epochs": 1, "batch_size": 8, "callbacks": [tensorboard_cb]}

tokenized_y = [text_to_word_sequence(sequence) for sequence in y]
word_dic = Dictionary(documents=tokenized_y, prune_at=2000000)
word_dic.filter_extremes(no_below=10, no_above=0.5, keep_n=50000)
word_dic.compactify()

simple_rnn_params = {"units": 10, "activation": 'tanh', "use_bias": True, "kernel_initializer": 'glorot_uniform',
                     "recurrent_initializer": 'orthogonal', "bias_initializer": 'zeros', "kernel_regularizer": None,
                     "recurrent_regularizer": None, "bias_regularizer": None, "activity_regularizer": None,
                     "kernel_constraint": None, "recurrent_constraint": None, "bias_constraint": None, "dropout": 0.0,
                     "recurrent_dropout": 0.0, "return_sequences": True, "return_state": False, "go_backwards": False,
                     "stateful": False, "unroll": False
                     }

dense_parameters = {"units": len(word_dic)+1, "activation": None, "use_bias": True, "kernel_initializer": 'glorot_uniform',
                    "bias_initializer": 'zeros', "kernel_regularizer": None, "bias_regularizer": None,
                    "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}

adam_params = {"lr": 0.001, "beta_1": 0.9, "beta_2": 0.999, "epsilon": None, "decay": 0.0, "amsgrad": False}

print("encoding y to one-hots")
y_onehot = np.array([word_dic.doc2idx(sequence.lower().split(), unknown_word_index=0) for sequence in y])
print("encoding y to one-hots done")

tokenized_x = [text_to_word_sequence(sequence) for sequence in x]
zipped_xy = zip(tokenized_x, y_onehot)
tokenized_xy = [zipped for zipped in zipped_xy if len(zipped[0]) <= max_sequence_length]

unzipped_xy = list(zip(*tokenized_xy))
unzipped_x = list(unzipped_xy[0])
targets = list(unzipped_xy[1])

tokenized_x = np.array(unzipped_x)
print("tokenizing x done")

model.add(convert_to_keras_embeddings(x, load_from_file="embeddings/train_code.model", max_sequence_length=max_sequence_length))
model.add(SimpleRNN(**simple_rnn_params))
model.add(Flatten())
model.add(Dense(**dense_parameters))

adam = Adam(**adam_params)
model.compile(loss='sparse_categorical_crossentropy', optimizer=adam)

print("model compiled")

model.fit(tokenized_x, np.array(targets), **train_params)
print("model fitted")
#
#
#
# score = model.evaluate(x_test, y_test, batch_size=32)
# print(score)
