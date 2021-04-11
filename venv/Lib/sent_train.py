from konlpy.tag import Okt
import konlpy
import json
import os
import nltk
import numpy as np
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from keras.models import load_model

def read_data(filename):
    with open(filename, 'rt', encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

train_data = read_data('./ratings_train.txt')
test_data = read_data('./ratings_test.txt')

okt = Okt()

def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json','rt',encoding='UTF8') as f:
        train_docs = json.load(f)
    with open('test_docs.json','rt',encoding='UTF8') as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
    with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs for t in d[0]]

text = nltk.Text(tokens, name='NMSC')

selected_words = [f[0] for f in text.vocab().most_common(10000)]
with open('./selected_words.json','w',encoding="utf-8") as make_file:
    json.dump(selected_words,make_file, ensure_ascii=False, indent="\t")
    print("selected_words is saved")

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]

x_train = np.asarray(train_x).astype('float16')
x_test = np.asarray(test_x).astype('float16')

y_train = np.asarray(train_y).astype('float16')
y_test = np.asarray(test_y).astype('float16')

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
             loss=losses.binary_crossentropy,
             metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=10, batch_size=512)

model_json = model.to_json()
with open('./model.json', "w") as json_file :
    json_file.write(model_json)

model.save('./model.h5')
print("Saved model to disk")