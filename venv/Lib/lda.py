import re
import pandas as pd
from konlpy.tag import Kkma
from collections import Counter
import random
kkma = Kkma()

def get_noun(msg_txt): #전처리과정(토큰화)
    nouns = list()
    pattern = re.compile("[ㄱ-ㅎㅏ-ㅣ]+")
    msg_txt = re.sub(pattern, "", msg_txt).strip()
    nounsEx = ""
    if len(msg_txt) > 0:
        pos = kkma.pos(msg_txt)
        for keyword, type in pos:
            if (type == "NNG" or type == "NNP") and (keyword not in ["은", "는", "이", "가", "로", "기", "고", "라", "씨"]):
                if not nounsEx:
                    nounsEx = keyword
                else:
                    nounsEx = nounsEx + " " + keyword
            if (type != "NNG" and type != "NNP"):
                if nounsEx:
                    nouns.append(nounsEx)
                nounsEx = ""
    return nouns

def TextFileRead(textList,categori): #빈 리스트를 넣어 텍스트를 읽어서 저장하는 함수
    if categori=="all":
        for i in range(180):  # 텍스트를 읽어들여 textList에 저장
            tmp_text = ''
            with open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/" + categori + f"/news{i + 1}.txt", encoding="utf-8") as f:
                tmp_text = f.read()
                textList.append(tmp_text)
    else:
        for i in range(120):  # 텍스트를 읽어들여 textList에 저장
            tmp_text = ''
            with open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/" + categori + f"/news{i + 1}.txt", encoding="utf-8") as f:
                tmp_text = f.read()
                textList.append(tmp_text)
    return textList

def isNotBlank(myString):  # 텍스트가 비었는지 확인하는 함수
    return bool(myString and myString.strip())

def get_documents(textList,categori): #전처리 과정을 마친 리스트를 documents로 반환하는 함수
    nounList = list()  # 전처리 과정을 끝낸 텍스트들을 저장할 list인 nounList 선언
    documents = list()  # LDA 과정을 수행할 list인 documents 선언

    TextFileRead(textList,categori)

    for i in range(len(textList)):  # textList에 있는 텍스트를 전처리 과정을 거쳐서 nounList에 저장
        tmp_noun = get_noun(textList[i])
        nounList.append(tmp_noun)

    for i in range(len(textList)):  # nounList에 있는 전처리된 텍스트를 documents에 저장
        tmp_val = nounList[i]
        documents.append(tmp_val)

    return documents

def TPM(textList,categori):


    documents = get_documents(textList,categori)

    # 여기부터 토픽모델링(LDA) 과정
    def p_topic_given_document(topic, d, alpha=0.1):
        return ((document_topic_counts[d][topic] + alpha) /
                (document_lengths[d] + K * alpha))

    def p_word_given_topic(word, topic, beta=0.1):
        return ((topic_word_counts[topic][word] + beta) /
                (topic_counts[topic] + V * beta))

    def topic_weight(d, word, k):
        return p_word_given_topic(word, k) * p_topic_given_document(k, d)

    def choose_new_topic(d, word):
        return sample_from([topic_weight(d, word, k) for k in range(K)])

    def sample_from(weights):
        total = sum(weights)
        rnd = total * random.random()
        for i, w in enumerate(weights):
            rnd -= w
            if rnd <= 0:
                return i

    random.seed(0)
    K = 10  # 토픽의 개수는 10개로 설정
    document_topics = [[random.randrange(K) for word in documents]
                       for document in documents]
    document_topic_counts = [Counter() for _ in documents]
    topic_word_counts = [Counter() for _ in range(K)]
    topic_counts = [0 for _ in range(K)]
    document_lengths = [len(document) for document in documents]
    distinct_words = set(word for document in documents for word in document)
    V = len(distinct_words)
    D = len(documents)

    for d in range(D):
        for word, topic in zip(documents[d], document_topics[d]):
            document_topic_counts[d][topic] += 1
            topic_word_counts[topic][word] += 1
            topic_counts[topic] += 1

    for iter in range(1000):
        for d in range(D):
            for i, (word, topic) in enumerate(zip(documents[d],
                                                  document_topics[d])):
                document_topic_counts[d][topic] -= 1
                topic_word_counts[topic][word] -= 1
                topic_counts[topic] -= 1
                document_lengths[d] -= 1
                new_topic = choose_new_topic(d, word)
                document_topics[d][i] = new_topic
                document_topic_counts[d][new_topic] += 1
                topic_word_counts[new_topic][word] += 1
                topic_counts[new_topic] += 1
                document_lengths[d] += 1

    topic_list = list()  # 토픽들에 해당되는 기사 list를 저장할 list인 topic_list 선언

    for i in range(10):  # 토픽별 리스트 생성 및 리스트를 topic_list에 넣음
        tmp_list = list()
        topic_list.append(tmp_list)


    for i in range(len(textList)):  # 문서의 개수만큼 반복
        mostTopic = document_topic_counts[i].most_common(1)  # 텍스트가 갖는 단어 중 가장 많은 토픽의 단어
        tmp_text2 = textList[i]  # text를 임시 저장한 변수
        if (isNotBlank(textList[i]) == True):  # 텍스트가 비어있지 않으면
            for n in range(10):  # 설정한 토픽의 개수인 10회 반복
                if (mostTopic[0][0] == n):  # n번토픽의 단어를 가장 많이 함유하고 있으면
                    topic_list[n].append(tmp_text2)  # topic_list[n]번에 해당 기사 저장

    # 여기서부터 정렬하는 코드
    topic_list_sorted = sorted(topic_list, key=len, reverse=True)  # 정렬된 토픽리스트
    fiveTopicIndex = list()  # 가장 많은 기사를 갖는 토픽을 분류하기 위해 5개의 index값을 가질 변수 선언

    for i in range(5):  # fiveTopicIndex에 상위 다섯 개 토픽의 인덱스 저장
        for j in range(10):
            if (j not in fiveTopicIndex) and (len(topic_list_sorted[i]) == len(topic_list[j])):
                fiveTopicIndex.append(j)

    #토픽의 제목을 설정하는 코드
    for i in range(5):
        tn3 = []
        tmp_tpn = topic_word_counts[fiveTopicIndex[i]].most_common(3)
        for j in range(3):
            tn3.append(tmp_tpn[j][0])
        tpl = tn3[0]+ ", " +tn3[1]+ ", " +tn3[2]
        f = open("C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/result/" + categori + "/" + categori +f"_result{i+1}_name.txt", "w", encoding="UTF8")
        f.write(tpl)
        f.close()



    SelectedTopic = list()  # 다섯개의 선정된 토픽을 넣을 list
    for i in range(5):  # 다섯개의 토픽을 넣는 과정
        SelectedTopic.append(topic_list[fiveTopicIndex[i]])

    TopicWord = list()  # 토픽에 해당되는 단어를 넣을 list
    for i in range(5):  # 토픽에 해당되는 단어를 list에 추가
        TopicWord.append(list(topic_word_counts[fiveTopicIndex[i]].elements()))

    SelectedTopicNews = list()  # 최종 선정된 다섯개의 토픽, 5개의 뉴스 (2차원배열)
    for i in range(5):
        news = list()
        SelectedTopicNews.append(news)

    for i in range(5):  # 토픽이 다섯개라 본 과정을 5번 반복
        TopicWordCnt = []  # 토픽 단어 count 변수 초기화
        for j in range(len(SelectedTopic[i])):  # 각 토픽에 해당되는 기사 수만큼
            TopicWordCnt.append(0)  # 단어 count 초기값 0으로 초기화

        for j in range(len(SelectedTopic[i])):  # 각 토픽에 해당되는 기사 수만큼
            for k in range(len(TopicWord[i])):  # 토픽에 해당하는 단어의 개수만큼 반복
                if TopicWord[i][k] in SelectedTopic[i][j]:  # 토픽의 단어가 기사에 있으면
                    TopicWordCnt[j] = TopicWordCnt[j] + 1  # count+1

        # 여기서부터 정렬하는 코드

        TopicWordCntSorted = sorted(TopicWordCnt, reverse=True)  # 토픽카운트 변수 정렬

        NewsIndex = list()  # 기사의 인덱스를 갖는 list 선언
        # print("기사의 인덱스 찾기")
        for j in range(5):  # 선정할 기사 개수인 5번 반복
            if TopicWordCntSorted[j] in TopicWordCnt:  # 정렬된 기사 개수가 정렬하지않은 단어카운트 변수에 있으면
                NewsIndex.append(TopicWordCnt.index(TopicWordCntSorted[j]))  # NewsIndex에 index 추가
                TopicWordCnt[TopicWordCnt.index(TopicWordCntSorted[j])] = 0  # 중복되지 않게 추가된 index의 값은 0으로 초기화
            else:
                print("NOT FOUNDED")  # 오류 발생시

        # 최종 선정된 다섯개의 뉴스 기사 출력
        for j in range(5):
            SelectedTopicNews[i].append(SelectedTopic[i][NewsIndex[j]])
    return SelectedTopicNews