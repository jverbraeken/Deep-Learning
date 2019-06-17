import numpy as np
from keras.models import Model, Input
from keras.models import load_model

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, tokenize_string

# load model and print summary
model = load_model('weights/seq2seqLSTM.h5')
model.summary()

encoder_inputs = Input(shape=(50,))

# convert input to embeddings
enc_x = model.get_layer('embedding_1')(encoder_inputs)

# fetch encoder
encoder_outputs, state_h, state_c = model.get_layer('lstm_1')(enc_x)
encoder_states = [state_h, state_c]
encoder_model = Model(encoder_inputs, encoder_states)

# define decoder inputs
decoder_state_input_h = Input(shape=(50,))
decoder_state_input_c = Input(shape=(50,))
decoder_inputs = Input(shape=(50,))

# fetch decoder
enc_y = model.get_layer('embedding_2')(decoder_inputs)
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_outputs, state_h, state_c = model.get_layer('lstm_2')(enc_y, initial_state=decoder_states_inputs)
decoder_states = [state_h, state_c]
decoder_outputs = model.get_layer('batch_normalization_1')(decoder_outputs)
decoder_outputs = model.get_layer('dense_1')(decoder_outputs)

# define decoder
decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states)


# create a code comment for a given code snippet
def decode_sequence(input_seq, comment_vocab):
    # Encode the input as state vectors.
    states_value = encoder_model.predict(np.array(input_seq))

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 50))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0] = comment_vocab.token2id['bos']

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ''

    # create reverse index (ix -> words)
    ix_word_map = {v: k for k, v in comment_vocab.token2id.items()}
    ix_word_map[len(comment_vocab)] = 'UNK'

    # while generated comment length < 50 and generated token != EOS
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value)

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = ix_word_map[sampled_token_index]

        # Exit condition: either hit max length
        # or find stop character.
        if (sampled_char == 'eos' or
                len(decoded_sentence) > 50):
            stop_condition = True
        else:
            decoded_sentence += sampled_char + " "

        # Update the target sequence (of length 1).
        target_seq = np.zeros_like(target_seq)
        target_seq[0, 0] = sampled_token_index

        # Update states
        states_value = [h, c]

    return decoded_sentence

# create comments for code in validation set
if __name__ == '__main__':
    data = get_data_as_lists()
    data_train = data[0]
    data_validation = data[1]
    code_embedding, comment_embedding, code_vocab, comment_vocab = get_embedding_layers(data_train=data_train,
                                                                                        max_seq_length_code=50,
                                                                                        max_seq_length_comment=50)

    # filter and pad comments
    filtered_x = [sequence for sequence in tokenize_string(data_validation[0]) if len(sequence) <= 50]
    padded_x = [sequence + ['pad'] * (50 - len(sequence)) for sequence in filtered_x]
    encoded_x = np.array([code_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in padded_x])

    with open('generated_comments_lstm.txt', 'w') as file:
        for i in range(0, encoded_x.shape[0]):
            comment_i = decode_sequence([encoded_x[i]], comment_vocab)
            file.write("%s\n" % comment_i)
