import gensim
from gensim.utils import simple_preprocess

from preprocess.parser import get_data_as_lists


def read_data(input_strings):
    for line in input_strings:
        yield simple_preprocess(line)


def create_embeddings(input_strings):
    documents = list(read_data(input_strings))

    model = gensim.models.Word2Vec(
        documents,
        size=3000,
        window=2,
        min_count=1,
        workers=10)
    model.train(documents, total_examples=len(documents), epochs=10)
    return model.wv


code_data = get_data_as_lists()[0][0]
create_embeddings(code_data)
