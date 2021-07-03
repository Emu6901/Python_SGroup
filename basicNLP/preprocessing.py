import json
import math

import numpy as np
import pandas as pd

specialchars = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
                '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '']
file_path = 'dataset/csv/khoa_hoc.csv'
VOCAB = dict()
NUM_SENTENCE = 0
SENTENCES_LISTS = []


def preprocessing_df(df):
    preprocess_data = []
    for row in df:
        preprocess_data.append(preprocessing_row(row))
    return preprocess_data


def preprocessing_row(text):
    global NUM_SENTENCE
    data = []
    text = str(text).split('\n')
    data += [para.replace('\r', '').split(' ') for para in text]
    # print(data)
    # print(len(data))
    NUM_SENTENCE += len(data)
    for sen in data:
        # print(sen)
        preprocessing_sen(sen)


def preprocessing_sen(text):
    global VOCAB
    global SENTENCES_LISTS
    text = str(text).strip().lower()
    for c in specialchars:
        if c in text:
            text = text.replace(c, '')
    if text != '':
        SENTENCES_LISTS.append(text)
        list_words = text.split(' ')
        # print(text)
        for word in list_words:
            if word != '':
                if word in VOCAB:
                    VOCAB[word] += 1
                else:
                    VOCAB[word] = 1
    # exit(0)


def termfreq(document, word):
    N = len(document)
    occurance = len([token for token in document if token == word])
    return occurance / N


def inverse_doc_freq(word):
    try:
        word_occurance = VOCAB[word] + 1
    except:
        word_occurance = 1
    return np.log(NUM_SENTENCE / word_occurance)


def tf_idf(sentence):
    tf_idf_vec = []
    for word in sentence:
        tf = termfreq(sentence, word)
        idf = inverse_doc_freq(word)

        value = tf * idf
        tf_idf_vec.append(value)
    return tf_idf_vec


if __name__ == "__main__":
    print(specialchars)
    df = pd.read_csv(file_path)
    data = df.values[:, 1]
    data = preprocessing_df(data)
    # VOCAB.pop('')
    # print(VOCAB)
    with open('data.json', 'w') as fp:
        json.dump(VOCAB, fp, sort_keys=True, indent=4)

    vectors = []
    for sent in SENTENCES_LISTS:
        vec = tf_idf(sent)
        vectors.append(vec)

    size = 0
    for i in vectors:
        size+=1
        print(size, len(i), i)
        break
    df = pd.DataFrame(vectors)
    df.to_csv('tf_idf.csv')