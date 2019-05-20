from preprocess.parser import get_data_as_lists
from gensim.corpora import Dictionary
from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
import numpy as np


def get_train_vocabularies(train_data):
    x = train_data[0]
    y = train_data[0]

    # Create vocabulary of words
    code_vocab = Dictionary(x)
    code_vocab.filter_extremes(no_below=5)

    comment_vocab = Dictionary(y)
    comment_vocab.filter_extremes(no_below=5, keep_tokens=["bos", "eos", "pad", "ood"])

    print(len(code_vocab.token2id))
    print(len(comment_vocab.token2id))
    return code_vocab, comment_vocab


def get_train_input(max_seq_length_code=100, max_seq_length_comment=50):
    data_train = get_data_as_lists()[0]
    x = data_train[0]
    y = data_train[1]
    y = ["BOS " + sequence + "  EOS" for sequence in y]

    tokenized_x = [text_to_word_sequence(sequence) for sequence in x]
    tokenized_y = [text_to_word_sequence(sequence) for sequence in y]

    zipped_tokenized = list(zip(tokenized_x, tokenized_y))
    filtered_data = [(x, y) for x, y in zipped_tokenized if (len(x) <= max_seq_length_code and len(y) <= max_seq_length_comment)]

    filtered_x, filtered_y = zip(*filtered_data)

    padded_x = [sequence + ['pad'] * (max_seq_length_code - len(sequence)) for sequence in filtered_x]
    padded_y = [sequence + ['pad'] * (max_seq_length_comment - len(sequence)) for sequence in filtered_y]

    code_vocab, comment_vocab = get_train_vocabularies((padded_x, padded_y))

    encoded_x = [code_vocab.doc2idx(sequence) for sequence in padded_x]
    encoded_y = [comment_vocab.doc2idx(sequence) for sequence in padded_y]

    decoder_target_data = np.zeros((len(data_train[0][1]), max_seq_length_comment-1, len(comment_vocab)+1), dtype='float32')
    comment_ix_map = comment_vocab.token2id

    for i, sentence in enumerate(padded_y):
        for t, word in enumerate(sentence):
            if t > 0:
                word_ix = comment_ix_map[word] if (word in comment_ix_map) else len(comment_vocab)
                decoder_target_data[i, t-1, word_ix] = 1


    print()






get_train_input()
