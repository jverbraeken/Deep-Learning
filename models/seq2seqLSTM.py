embedding_size = 50
 from keras.layers import Input, LSTM, Dense, Dropout, BatchNormalization
from keras.losses import sparse_categorical_crossentropy
from keras.models import Model
from keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_accuracy

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, filter_and_pad, encode_sequences

MAX_CODE_LENGTH = 50
MAX_COMMENT_LENGTH = 50

data_train = get_data_as_lists()[0]
code_embedding, comment_embedding, code_vocab, comment_vocab = get_embedding_layers(data_train=data_train,
                                                                                    max_seq_length_code=MAX_CODE_LENGTH,
                                                                                    max_seq_length_comment=MAX_COMMENT_LENGTH)

padded_x, padded_y = filter_and_pad(data_train, MAX_CODE_LENGTH, MAX_COMMENT_LENGTH)
encoded_x, encoded_y, decoder_target_data = encode_sequences(code_vocab, comment_vocab, padded_x, padded_y,
                                                             MAX_COMMENT_LENGTH)

encoder_inputs = Input(shape=(None,))
# Code words embedding
en_x = code_embedding(encoder_inputs)

# Encoder lstm
encoder = LSTM(10, return_state=True, activation='tanh')
encoder_outputs, state_h, state_c = encoder(en_x)
# We discard `encoder_outputs` and only keep the states.
encoder_states = [state_h, state_c]

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
# Comment word embeddings
final_dex = comment_embedding(decoder_inputs)
# decoder lstm
decoder_lstm = LSTM(10, return_sequences=True, return_state=True, activation='tanh')
decoder_outputs, _, _ = decoder_lstm(final_dex, initial_state=encoder_states)

batch_norm = BatchNormalization()(decoder_outputs)
dropout = Dropout(0.2)(batch_norm)

decoder_dense = Dense(len(comment_vocab), activation='softmax')
decoder_outputs = decoder_dense(dropout)
# While training, model takes eng and french words and outputs #translated french word
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
# rmsprop is preferred for nlp tasks

optimizer = Adam(epsilon=0.0001, clipnorm=1.0)

model.compile(optimizer=optimizer, loss=sparse_categorical_crossentropy, metrics=[sparse_categorical_accuracy])
model.fit([encoded_x, encoded_y], decoder_target_data, batch_size=256, epochs=100)
model.save('weights/seq2seqLSTM.h5')
