from konlpy.tag import Okt
import konlpy
import json
import os
import nltk
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from keras.models import load_model
from keras.models import model_from_json

def read_file(cat,topic_num,len):
    file_list = list()
    for i in range(len):
        tmp_text = ''
        with open('C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/result/' + cat + '/' + cat + '_result' + topic_num + '_' + f"{i+1}.txt", encoding = "utf-8") as f:
            tmp_text = f.read()
            file_list.append(tmp_text)
    return file_list

def predict(string):

    if os.path.isfile('C:/Users/sam/PycharmProjects/sam2/venv/Lib/selected_words.json'):
        with open('C:/Users/sam/PycharmProjects/sam2/venv/Lib/selected_words.json','rt',encoding='UTF8') as f:
            selected_words = json.load(f)

    def tokenize(doc):
        return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

    def term_frequency(doc):
        return [doc.count(word) for word in selected_words]

    okt = Okt()

    json_file = open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)

    loaded_model.load_weights("C:/Users/sam/PycharmProjects/sam2/venv/Lib/model.h5")

    loaded_model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                 loss=losses.binary_crossentropy,
                 metrics=[metrics.binary_accuracy])


    #긍정 1 중립 2 부정 0
    def predict_pos_neg(string):
        token = tokenize(string)
        tf = term_frequency(token)
        data = np.expand_dims(np.asarray(tf).astype('float16'), axis=0)
        score = float(loaded_model.predict(data))
        if(score >= 0.75):
            print("긍정")
            return 1
        elif(score >=0.4) :
            print("중립")
            return 2
        else:
            print("부정")
            return 0

    result = predict_pos_neg(text)

    return result

def cat_predict(string):
    cat_result = list()

    if os.path.isfile('C:/Users/sam/PycharmProjects/sam2/venv/Lib/selected_words.json'):
        with open('C:/Users/sam/PycharmProjects/sam2/venv/Lib/selected_words.json','rt',encoding='UTF8') as f:
            selected_words = json.load(f)

    def tokenize(doc):
        return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

    def term_frequency(doc):
        return [doc.count(word) for word in selected_words]

    okt = Okt()

    json_file = open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)

    loaded_model.load_weights("C:/Users/sam/PycharmProjects/sam2/venv/Lib/model.h5")

    loaded_model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                 loss=losses.binary_crossentropy,
                 metrics=[metrics.binary_accuracy])


    #긍정 1 중립 2 부정 0
    def cat_predict_pos_neg(string):
        token = tokenize(string)
        tf = term_frequency(token)
        data = np.expand_dims(np.asarray(tf).astype('float16'), axis=0)
        score = float(loaded_model.predict(data))
        if(score >= 0.7):
            return 1
        elif(score >=0.1) :
            return 2
        else:
            return 0

    for i in range(len(string)):
        result = cat_predict_pos_neg(string[i])
        if(result == 1):
            cat_result.append(1)
        elif(result == 2):
            cat_result.append(2)
        else:
            cat_result.append(0)

    return cat_result
