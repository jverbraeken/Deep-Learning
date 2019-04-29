from tensorflow import keras

model = keras.Sequential()

gru_params = {"units": 10, "activation": 'tanh', "recurrent_activation": 'hard_sigmoid', "use_bias": True,
              "kernel_initializer": 'glorot_uniform', "recurrent_initializer": 'orthogonal',
              "bias_initializer": 'zeros', "kernel_regularizer": None, "recurrent_regularizer": None,
              "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None,
              "recurrent_constraint": None, "bias_constraint": None, "dropout": 0.0, "recurrent_dropout": 0.0,
              "implementation": 1, "return_sequences": False, "return_state": False, "go_backwards": False,
              "stateful": False, "unroll": False, "reset_after": False
              }
dense_parameters = {"units": 10, "activation": None, "use_bias": True, "kernel_initializer": 'glorot_uniform',
                    "bias_initializer": 'zeros', "kernel_regularizer": None, "bias_regularizer": None,
                    "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}

adam_params = {"lr": 0.001, "beta_1": 0.9, "beta_2": 0.999, "epsilon": None, "decay": 0.0, "amsgrad": False}

model.add(keras.layers.GRU(**gru_params))
model.add(keras.layers.Dense(**dense_parameters))

adam = keras.optimizers.Adam(**adam_params)
model.compile(loss='mean_squared_error', optimizer=adam) 