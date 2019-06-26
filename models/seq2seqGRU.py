from keras.backend import sparse_categorical_crossentropy

embedding_size = 50
import tensorflow as tf
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.layers import Input, GRU, Dense, BatchNormalization
from keras.models import Model
from keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_accuracy
import numpy as np

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

# define input dimensionality
encoder_inputs = Input(shape=(None,))
# Code words embedding
en_x = code_embedding(encoder_inputs)

# Encoder GRU
encoder = GRU(50, return_state=True)
encoder_outputs, state_h = encoder(en_x)

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
# Comment word embeddings
final_dex = comment_embedding(decoder_inputs)

# decoder GRU
decoder_lstm = GRU(50, return_sequences=True, return_state=True)
decoder_outputs, _ = decoder_lstm(final_dex, initial_state=state_h)

 # add batchnorm
batch_norm = BatchNormalization()(decoder_outputs)
decoder_dense = Dense(len(comment_vocab) + 1, activation='softmax')
decoder_outputs = decoder_dense(batch_norm)

# While training, model takes code and comment sequences and outputs one-hot encoding of
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# define optimizer and compile
optimizer = Adam(lr=0.1, beta_2=0.98, decay=1e-4)
model.compile(optimizer=optimizer, loss=sparse_categorical_crossentropy, metrics=[sparse_categorical_accuracy])

# add callbacks
path_checkpoint = 'checkpoints/seq2seqGRU.keras'
callback_checkpoint = ModelCheckpoint(filepath=path_checkpoint,
                                      monitor='val_loss',
                                      verbose=1,
                                      save_weights_only=True,
                                      save_best_only=True)

callback_tensorboard = TensorBoard(log_dir='logs/gru',
                                   histogram_freq=0,
                                   write_graph=False,
                                   update_freq=20000)

# train model and save
model.fit([encoded_x, encoded_y], decoder_target_data, batch_size=256, epochs=100, validation_split=0.1,
          callbacks=[callback_checkpoint, callback_tensorboard])
model.save('weights/seq2seqGRU.h5')
