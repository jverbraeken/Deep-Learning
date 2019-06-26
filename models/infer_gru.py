import numpy as np
from keras.models import Model, Input
from keras.models import load_model

from preprocess.build_vocabs import get_embedding_layers, get_data_as_lists, tokenize_string

# load model from file
model = load_model('weights/seq2seqGRU.h5')

# print model description
model.summary()

# define input (sequence of size 50 with each element representing a word from the code)
encoder_inputs = Input(shape=(50,))

# get word embedding for each element
enc_x = model.get_layer('embedding_1')(encoder_inputs)

# fetch output and hidden state from model and define encoder model
encoder_outputs, state_h = model.get_layer('gru_1')(enc_x)
encoder_model = Model(encoder_inputs, state_h)

# define input (embedding of size 50 representing the hidden state from the encoder model)
decoder_state_input_h = Input(shape=(50,))

# define input (sequence of size 50 with each element representing a word from a comment)
decoder_inputs = Input(shape=(50,))

# get word embeddings for each element
enc_y = model.get_layer('embedding_2')(decoder_inputs)

# fetch output and hidden state from decoder model
decoder_outputs, state_h = model.get_layer('gru_2')(enc_y, initial_state=decoder_state_input_h)
decoder_outputs = model.get_layer('batch_normalization_1')(decoder_outputs)
decoder_outputs = model.get_layer('dense_1')(decoder_outputs)

# define decoder model
decoder_model = Model(
    [decoder_inputs] + decoder_state_input_h,
    [decoder_outputs] + state_h)


# method to create a comment from a code snippet
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

    # create reverse map (id-> word)
    ix_word_map = {v: k for k, v in comment_vocab.token2id.items()}
    ix_word_map[len(comment_vocab)] = 'UNK'

    # while comment size < 50 and created token != EOS
    while not stop_condition:
        # get state and output from decoder model based on state from encoder model
        output_tokens, h = decoder_model.predict([target_seq] + states_value)

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
        states_value = h

    return decoded_sentence

# Predict comments for the validation set
if __name__ == '__main__':
    data = get_data_as_lists()
    data_train = data[0]
    data_validation = data[1]

    # fetch embedding layers
    code_embedding, comment_embedding, code_vocab, comment_vocab = get_embedding_layers(data_train=data_train,
                                                                                        max_seq_length_code=50,
                                                                                        max_seq_length_comment=50)
    # filter code snippets on length
    filtered_x = [sequence for sequence in tokenize_string(data_validation[0]) if len(sequence) <= 50]

    # make all code snippets same size
    padded_x = [sequence + ['pad'] * (50 - len(sequence)) for sequence in filtered_x]

    # encode all code snippets as integers
    encoded_x = np.array([code_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in padded_x])

    # generate comment and write comments to file
    with open('generated_comments_gru.txt', 'w') as file:
        for i in range(0, encoded_x.shape[0]):
            comment_i = decode_sequence([encoded_x[i]], comment_vocab)
            file.write("%s\n" % comment_i)
