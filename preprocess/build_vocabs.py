import numpy as np
from gensim.corpora import Dictionary
from gensim.models import Word2Vec, KeyedVectors
from keras.layers import Embedding
from keras.preprocessing.text import text_to_word_sequence

from preprocess.parser import get_data_as_lists


def get_train_vocabularies(train_data):
    x = train_data[0]
    y = train_data[1]

    # Create vocabulary of words
    code_vocab = Dictionary(x)
    code_vocab.filter_extremes(no_below=5, keep_tokens=['pad'])

    comment_vocab = Dictionary(y)
    comment_vocab.filter_extremes(no_below=5, keep_tokens=["bos", "eos", "pad", "ood"])
    return code_vocab, comment_vocab


def tokenize_string(string_sequences):
    return [text_to_word_sequence(sequence) for sequence in string_sequences]


def get_word_embedding(documents, embedding_size=100, window_size=10, epochs=10):
    model = Word2Vec(
        documents,
        size=embedding_size,
        window=window_size,
        min_count=5,
        workers=10)
    model.train(documents, total_examples=len(documents), epochs=epochs)
    return model.wv


def get_embedding_weights(vocab, word_embedding_location=None, **kwargs):
    if (word_embedding_location is not None):
        word_embedding = KeyedVectors.load(word_embedding_location, mmap='r')
    else:
        word_embedding = get_word_embedding(**kwargs)
    token_id_map = vocab.token2id

    weights = np.zeros((len(vocab) + 1, word_embedding.vector_size))

    for token, id in token_id_map.items():
        if token in word_embedding:
            weights[id + 1] = word_embedding.get_vector(token)
    return weights


def filter_and_pad(data, max_seq_length_code=100, max_seq_length_comment=50):
    x = data[0]
    y = data[1]
    y = ["BOS " + sequence + "  EOS" for sequence in y]

    tokenized_x = tokenize_string(x)
    tokenized_y = tokenize_string(y)

    zipped_tokenized = list(zip(tokenized_x, tokenized_y))
    filtered_data = [(x, y) for x, y in zipped_tokenized if
                     (len(x) <= max_seq_length_code and len(y) <= max_seq_length_comment)]

    filtered_x, filtered_y = zip(*filtered_data)

    padded_x = [sequence + ['pad'] * (max_seq_length_code - len(sequence)) for sequence in filtered_x]
    padded_y = [sequence + ['pad'] * (max_seq_length_comment - len(sequence)) for sequence in filtered_y]
    return padded_x, padded_y


def encode_sequences(code_vocab, comment_vocab, data_x, data_y, max_seq_length_comment):
    encoded_x = np.array([code_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in data_x])
    encoded_y = np.array([comment_vocab.doc2idx(sequence, unknown_word_index=0) for sequence in data_y])

    decoder_target_data = np.zeros((len(encoded_y), max_seq_length_comment), dtype=np.int32)
    comment_ix_map = comment_vocab.token2id

    for i, sentence in enumerate(data_y):
        for t, word in enumerate(sentence):
            if t > 0:
                word_ix = comment_ix_map[word] if (word in comment_ix_map) else len(comment_vocab)
                decoder_target_data[i, t - 1] = word_ix

    return encoded_x, encoded_y, decoder_target_data


def get_train_input(max_seq_length_code=100, max_seq_length_comment=50):
    data_train = get_data_as_lists()[0]
    padded_x, padded_y = filter_and_pad(data_train, max_seq_length_code, max_seq_length_comment)

    code_vocab, comment_vocab = get_train_vocabularies((padded_x, padded_y))

    encoded_x, encoded_y, decoder_target_data = encode_sequences(code_vocab, comment_vocab, padded_x, padded_y,
                                                                 max_seq_length_comment)

    return encoded_x, encoded_y, decoder_target_data


def get_embedding_layers(data_train, max_seq_length_code=100, max_seq_length_comment=50,
                         embeddings_location_code="embeddings/code.model",
                         embeddings_location_comment="embeddings/comment.model"):

    code_vocab, comment_vocab = get_train_vocabularies(
        filter_and_pad(data_train, max_seq_length_code, max_seq_length_comment))
    weights_code = get_embedding_weights(vocab=code_vocab, word_embedding_location=embeddings_location_code)
    weights_comment = get_embedding_weights(vocab=comment_vocab, word_embedding_location=embeddings_location_comment)
    embedding_layer_code = Embedding(weights_code.shape[0],
                                     weights_code.shape[1],
                                     weights=[weights_code],
                                     input_length=max_seq_length_code,
                                     trainable=False,
                                     mask_zero=True)

    embedding_layer_comment = Embedding(weights_comment.shape[0],
                                        weights_comment.shape[1],
                                        weights=[weights_comment],
                                        input_length=max_seq_length_comment,
                                        trainable=False,
                                        mask_zero=True)

    return embedding_layer_code, embedding_layer_comment, code_vocab, comment_vocab


if __name__ == '__main__':
    data_train = get_data_as_lists()[0]
    padded_x, padded_y = filter_and_pad(data_train, 100, 50)
    weights_code = get_word_embedding(padded_x, embedding_size=100, window_size=10, epochs=10)
    weights_comment = get_word_embedding(padded_y, embedding_size=100, window_size=10, epochs=10)
    weights_code.save("embeddings/code.model")
    weights_comment.save("embeddings/comment.model")
