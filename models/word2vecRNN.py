from preprocess.word2vec import convert_to_keras_embeddings
from preprocess.parser import get_data_as_lists
from keras import Sequential
from keras.layers import SimpleRNN, Dense, Flatten, Input
from keras.optimizers import Adam
from keras.preprocessing.text import text_to_word_sequence, one_hot
from keras.callbacks import TensorBoard
from keras.utils import to_categorical
import numpy as np
from gensim.corpora import Dictionary


model = Sequential()

x = get_data_as_lists()[0][0]
y = get_data_as_lists()[0][1]
y = ["BOS " + sentence + " EOS" for sentence in y]

x_test = get_data_as_lists()[1][0]
y_test = get_data_as_lists()[1][1]
y_test = ["BOS " + sentence + " EOS" for sentence in y_test]

# Create vocabulary of words
all_code_words = set()
for eng in lines.eng:
    for word in eng.split():
        if word not in all_eng_words:
            all_eng_words.add(word)

all_french_words = set()
for fr in lines.fr:
    for word in fr.split():
        if word not in all_french_words:
            all_french_words.add(word)
