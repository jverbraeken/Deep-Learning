from preprocess.word2vec import convert_to_keras_embeddings
from preprocess.parser import get_data_as_lists
from keras import Sequential
from keras.layers import SimpleRNN, Dense
from keras.optimizers import Adam
from keras.preprocessing.text import text_to_word_sequence, one_hot



model = Sequential()

x = get_data_as_lists()[0][0]
y = get_data_as_lists()[0][1]

x_test = get_data_as_lists()[1][0]
y_test = get_data_as_lists()[1][1]

simple_rnn_params = {"units": 10, "activation": 'tanh', "use_bias": True, "kernel_initializer": 'glorot_uniform',
                     "recurrent_initializer": 'orthogonal', "bias_initializer": 'zeros', "kernel_regularizer": None,
                     "recurrent_regularizer": None, "bias_regularizer": None, "activity_regularizer": None,
                     "kernel_constraint": None, "recurrent_constraint": None, "bias_constraint": None, "dropout": 0.0,
                     "recurrent_dropout": 0.0, "return_sequences": True, "return_state": False, "go_backwards": False,
                     "stateful": False, "unroll": False
                     }

dense_parameters = {"units": 50000, "activation": None, "use_bias": True, "kernel_initializer": 'glorot_uniform',
                    "bias_initializer": 'zeros', "kernel_regularizer": None, "bias_regularizer": None,
                    "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}

adam_params = {"lr": 0.001, "beta_1": 0.9, "beta_2": 0.999, "epsilon": None, "decay": 0.0, "amsgrad": False}

train_params = {"epochs": 1, "batch_size": 8}

model.add(convert_to_keras_embeddings(x))
model.add(SimpleRNN(**simple_rnn_params))
model.add(Dense(**dense_parameters))

adam = Adam(**adam_params)
model.compile(loss='mean_squared_error', optimizer=adam)

tokenized_x = [text_to_word_sequence(sequence) for sequence in x]
tokenized_y = [one_hot(sequence, 50000) for sequence in y]

model.fit(tokenized_x, tokenized_y, **train_params)

score = model.evaluate(x_test, y_test, batch_size=32)
print(score)
