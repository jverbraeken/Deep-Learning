from preprocess.parser import get_data_as_lists
from gensim.utils import simple_preprocess
import gensim

def _tokenize_data(input_strings):
    for line in input_strings:
        yield simple_preprocess(line)



def _create_embeddings(input_strings):
    documents = list(_tokenize_data(input_strings))

    model = gensim.models.Word2Vec(
        documents,
        size=150,
        window=10,
        min_count=1,
        workers=10)
    model.train(documents, total_examples=len(documents), epochs=10)
    return model.wv



def create_code_embedding(save=True):
    code_data = get_data_as_lists()[0][0]
    embedding = _create_embeddings(code_data)
    if(save):
        embedding.save("embeddings/train_code.model")
    return embedding


def create_comment_embedding(save=True):
    comment_data = get_data_as_lists()[0][1]
    embedding = _create_embeddings(comment_data)
    if(save):
        embedding.save("embeddings/train_comment.model")
    return embedding


def convert_to_keras_embeddings(corpus, wv=None, load_from_file=""):
    if(len(load_from_file)>0):
        wv = gensim.models.KeyedVectors.load(load_from_file, mmap='r')
    elif(wv is None):
        wv = _create_embeddings(corpus)
        print("created embedding for corpus")

    return wv.get_keras_embedding(False)
