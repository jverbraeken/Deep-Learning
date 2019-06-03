from keras.models import load_model
import tensorflow as tf
from keras.models import Model, Input
import numpy as np

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, encode_sequences, tokenize_string

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

model = load_model('weights/seq2seqLSTM.h5', custom_objects={'sparse_cross_entropy': sparse_cross_entropy}, compile=False)
print()

encoder_inputs = Input(shape=(None,))

enc_x = model.get_layer('embedding_1')(encoder_inputs)
encoder_outputs, state_h, state_c = model.get_layer('lstm_1')(enc_x)
encoder_states = [state_h, state_c]
encoder_model = Model(encoder_inputs, encoder_states)

decoder_state_input_h = Input(shape=(50,))
decoder_state_input_c = Input(shape=(50,))

decoder_inputs = Input(shape=(None,))

enc_y = model.get_layer('embedding_2')(decoder_inputs)

decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_outputs, state_h, state_c = model.get_layer('lstm_2')(
    enc_y, initial_state=decoder_states_inputs)
decoder_states = [state_h, state_c]
decoder_outputs = model.get_layer('dense_1')(decoder_outputs)

decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states)


def decode_sequence(input_seq, comment_vocab):
    # Encode the input as state vectors.
    states_value = encoder_model.predict(input_seq)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0] = comment_vocab.token2id['bos']

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value)

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = comment_vocab.id2token(sampled_token_index)
        decoded_sentence += sampled_char

        # Exit condition: either hit max length
        # or find stop character.
        if (sampled_char == 'eos' or
           len(decoded_sentence) > 50):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update states
        states_value = [h, c]

    return decoded_sentence


if __name__ == '__main__':
    data = get_data_as_lists()
    data_train = data[0]
    data_validation = data[1]
    code_embedding, comment_embedding, code_vocab, comment_vocab = get_embedding_layers(data_train=data_train,
                                                                                        max_seq_length_code=50,
                                                                                        max_seq_length_comment=50)

    padded_x = [sequence + ['pad'] * (50 - len(sequence)) for sequence in tokenize_string(data_validation[0])]
    padded_y = [sequence + ['pad'] * (50 - len(sequence)) for sequence in tokenize_string(data_validation[1])]

    encoded_x = np.array([code_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in padded_x])
    encoded_y = np.array([comment_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in padded_y])

    print(decode_sequence(encoded_x[0], comment_vocab))