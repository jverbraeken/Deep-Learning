embedding_size = 50
import numpy as np
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.layers import Input, LSTM, Dense, BatchNormalization
from keras.losses import sparse_categorical_crossentropy
from keras.models import Model
from keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_accuracy

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, filter_and_pad, encode_sequences

# define max code length and comments length
MAX_CODE_LENGTH = 50
MAX_COMMENT_LENGTH = 50

# get data and pad
data_train = get_data_as_lists()[0]
padded_x, padded_y = filter_and_pad(data_train, MAX_CODE_LENGTH, MAX_COMMENT_LENGTH)

# compute embeddings and vocabulary
code_embedding, comment_embedding, code_vocab, comment_vocab = get_embedding_layers(data_train=data_train,
                                                                                    max_seq_length_code=MAX_CODE_LENGTH,
                                                                                    max_seq_length_comment=MAX_COMMENT_LENGTH,
                                                                                    embeddings_location_comment=None,
                                                                                    documents=padded_y,
                                                                                    )
# encode sequences
encoded_x, encoded_y, decoder_target_data = encode_sequences(code_vocab, comment_vocab, padded_x, padded_y,
                                                             MAX_COMMENT_LENGTH)

# reshape target to required dimensions
decoder_target_data = np.reshape(decoder_target_data, (decoder_target_data.shape[0], decoder_target_data.shape[1], -1))

# create encoder model
encoder_inputs = Input(shape=(None,))
en_x = code_embedding(encoder_inputs)
encoder = LSTM(50, return_state=True)
_, state_h, state_c = encoder(en_x)
# We discard `encoder_outputs` and only keep the states.
encoder_states = [state_h, state_c]

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
# Comment word embeddings
dec_x = comment_embedding(decoder_inputs)
# decoder lstm
decoder_lstm = LSTM(50, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(dec_x, initial_state=encoder_states)

# add batchnorm
batch_norm = BatchNormalization()(decoder_outputs)
decoder_outputs = Dense(len(comment_vocab) + 1, activation='softmax')(batch_norm)

# While training, model takes code and comment sequences and outputs generated comment
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# define optimizer and compile
optimizer = Adam(lr=0.1, beta_2=0.98, decay=1e-4)
model.compile(optimizer=optimizer, loss=sparse_categorical_crossentropy, metrics=[sparse_categorical_accuracy])

# define callbacks (add tensorboard and model checkpoints)
path_checkpoint = 'checkpoints/seq2seqLSTM.keras'
callback_checkpoint = ModelCheckpoint(filepath=path_checkpoint,
                                      monitor='val_loss',
                                      verbose=1,
                                      save_weights_only=True,
                                      save_best_only=True)

callback_tensorboard = TensorBoard(log_dir='logs/lstm',
                                   histogram_freq=0,
                                   write_graph=False,
                                   update_freq=20000)

# train model
model.fit([encoded_x, encoded_y], decoder_target_data, batch_size=256, epochs=100, validation_split=0.1,
          callbacks=[callback_checkpoint, callback_tensorboard])

# save final model weights
model.save('weights/seq2seqLSTM.h5')
