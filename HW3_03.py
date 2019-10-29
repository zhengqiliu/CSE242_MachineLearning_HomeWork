#coding=utf-8
import os
import re
import string
import collections
import nltk
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from math import log

txt = ""
for filename in os.listdir("enron1\ham"):
    try:
        f = open("enron1\\ham\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass

for filename in os.listdir("enron2\ham"):
    try:
        f = open("enron2\\ham\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass

for filename in os.listdir("enron3\ham"):
    try:
        f = open("enron3\\ham\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass
for filename in os.listdir("enron4\ham"):
    try:
        f = open("enron4\\ham\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass
for filename in os.listdir("enron5\ham"):
    try:
        f = open("enron5\\ham\\" + filename,"r", encoding='utf-8')
        txt += f.read()
    except:
        pass

txt = txt.lower()
txt = re.sub(r'\d+', '', txt)
txt = txt.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words("english"))
corpus = txt.split()

cnt = collections.Counter(corpus)
for key in list(cnt.keys()):
    if key in stop_words:
        del cnt[key]

txt = ""
for filename in os.listdir("enron1\spam"):
    try:
        f = open("enron1\\spam\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass

for filename in os.listdir("enron2\spam"):
    try:
        f = open("enron2\\spam\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass

for filename in os.listdir("enron3\spam"):
    try:
        f = open("enron3\\spam\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass
for filename in os.listdir("enron4\spam"):
    try:
        f = open("enron4\\spam\\" + filename,"r",encoding='utf-8')
        txt += f.read()
    except:
        pass
for filename in os.listdir("enron5\spam"):
    try:
        f = open("enron5\\spam\\" + filename,"r", encoding='utf-8')
        txt += f.read()
    except:
        pass

txt = txt.lower()
txt = re.sub(r'\d+', '', txt)
txt = txt.translate(str.maketrans('', '', string.punctuation))

stop_words = set(stopwords.words("english"))
corpus = txt.split()

cntS = collections.Counter(corpus)
for key in list(cntS.keys()):
    if key in stop_words:
        del cntS[key]

cnt_ham = 15045
cnt_spam = 12671
ham_word_number = spam_word_number = 0
for v in cnt.values():
    ham_word_number += v
for v in cntS.values():
    spam_word_number += v

def cnt_ham_prob(corpus):
    res = log((cnt_ham)/(cnt_ham + cnt_spam))
    for w in corpus:
        if w in stop_words:
            continue
        if w not in cnt:
            res += log(1/ham_word_number)
        else:
            res += log(cnt[w]/ham_word_number)

    return res

def cnt_spam_prob(corpus):
    res = log((cnt_spam) / (cnt_ham + cnt_spam))
    for w in corpus:
        if w in stop_words:
            continue
        if w not in cntS:
            res += log(1 / spam_word_number)
        else:
            res += log(cntS[w] / spam_word_number)

    return res

denominator = 0
numerator = 0
for filename in os.listdir("enron6\ham"):
    try:
        f = open("enron6\\ham\\" + filename,"r",encoding='utf-8')
        txt = f.read()
        denominator += 1
        txt = txt.lower()
        txt = re.sub(r'\d+', '', txt)
        txt = txt.translate(str.maketrans('', '', string.punctuation))

        stop_words = set(stopwords.words("english"))
        corpus = txt.split()

        if cnt_ham_prob(corpus) > cnt_spam_prob(corpus):
            numerator += 1
    except:
        pass

for filename in os.listdir("enron6\spam"):
    try:
        f = open("enron6\\spam\\" + filename,"r",encoding='utf-8')
        txt = f.read()
        denominator += 1
        txt = txt.lower()
        txt = re.sub(r'\d+', '', txt)
        txt = txt.translate(str.maketrans('', '', string.punctuation))

        stop_words = set(stopwords.words("english"))
        corpus = txt.split()

        if cnt_ham_prob(corpus) < cnt_spam_prob(corpus):
            numerator += 1
    except:
        pass

print(numerator/denominator)

'''
0.068
0.9793351302785265
'''