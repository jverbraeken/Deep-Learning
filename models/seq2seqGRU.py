embedding_size = 50
import tensorflow as tf
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.layers import Input, GRU, Dense, BatchNormalization
from keras.models import Model
from keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_accuracy

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, filter_and_pad, encode_sequences


def sparse_cross_entropy(y_true, y_pred):
    """
    Calculate the cross-entropy loss between y_true and y_pred.

    y_true is a 2-rank tensor with the desired output.
    The shape is [batch_size, sequence_length] and it
    contains sequences of integer-tokens.

    y_pred is the decoder's output which is a 3-rank tensor
    with shape [batch_size, sequence_length, num_words]
    so that for each sequence in the batch there is a one-hot
    encoded array of length num_words.
    """

    # Calculate the loss. This outputs a
    # 2-rank tensor of shape [batch_size, sequence_length]
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y_true, logits=y_pred)

    # Keras may reduce this across the first axis (the batch)
    # but the semantics are unclear, so to be sure we use
    # the loss across the entire 2-rank tensor, we reduce it
    # to a single scalar with the mean function.
    loss_mean = tf.reduce_mean(loss)

    return loss_mean



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
encoder = GRU(50, return_state=True)
encoder_outputs, state_h = encoder(en_x)

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
# Comment word embeddings
final_dex = comment_embedding(decoder_inputs)

# decoder lstm
decoder_lstm = GRU(50, return_sequences=True, return_state=True)
decoder_outputs,_ = decoder_lstm(final_dex, initial_state=state_h)

batch_norm = BatchNormalization()(decoder_outputs)

decoder_dense = Dense(len(comment_vocab) + 1, activation='softmax')
decoder_outputs = decoder_dense(batch_norm)

# While training, model takes eng and french words and outputs #translated french word
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
# rmsprop is preferred for nlp tasks

optimizer = Adam(lr=0.1, beta_2=0.98, decay=1e-4)

decoder_target = tf.placeholder(dtype='int32', shape=(None, None))

model.compile(optimizer=optimizer, loss=sparse_cross_entropy, metrics=[sparse_categorical_accuracy],
              target_tensors=decoder_target)

path_checkpoint = 'checkpoints/seq2seqGRU.keras'
callback_checkpoint = ModelCheckpoint(filepath=path_checkpoint,
                                      monitor='val_loss',
                                      verbose=1,
                                      save_weights_only=True,
                                      save_best_only=True)

callback_tensorboard = TensorBoard(log_dir='logs/',
                                   histogram_freq=0,
                                   write_graph=False,
                                   update_freq=20000)

model.fit([encoded_x, encoded_y], decoder_target_data, batch_size=256, epochs=100, validation_split=0.1,
          callbacks=[callback_checkpoint, callback_tensorboard])
model.save('weights/seq2seqGRU.h5')
