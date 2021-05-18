#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('-------- Importing libraries and datasets --------')
import pandas as pd
import numpy as np
import re
import nltk
import spacy
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
nlp = spacy.load("en_core_web_md", disable=['parser', 'ner'])

df = pd.read_csv('train.csv',header=None, names=['polarity','tweet_id','date','query','username','tweet'])
df['polarity'] = df['polarity'].replace(4,1)
df.drop_duplicates('tweet_id', keep=False, inplace=True, ignore_index=True)
df = df.loc[:,['tweet','polarity']]

print('-------- Cleaning the data --------')

def data_cleaning(desired_column):
    def username_removal(tweet):
        compiled = re.compile(r'@[A-Za-z0-9_]+')
        cleaned = re.sub(compiled,'',tweet)
        return cleaned

    def website_removal(tweet):
        compiled_1 = re.compile(r'http\S+')
        cleaned = re.sub(compiled_1,'',tweet)

        compiled_2 = re.compile(r'\S+.com')
        cleaned = re.sub(compiled_2,'',cleaned)
        return cleaned

    def repeated_chars_removal(tweet):
        compiled = re.compile(r'(.)\1+')
        cleaned = re.sub(compiled, r'\1\1', tweet)
        return cleaned

    def start_with_symbol_removal(tweet):
        compiled = re.compile(r"[^a-zA-Z0-9!?' ][a-zA-Z0-9]+")
        cleaned = re.sub(compiled, '', tweet)
        return cleaned

    def repeated_comma_dot_removal(tweet):
        compiled = re.compile(r'[.]+')
        cleaned = re.sub(compiled, r'.', tweet)

        compiled = re.compile(r'[,]+')
        cleaned = re.sub(compiled, r',', cleaned)
        return cleaned

    def extra_whitespaces_removal(tweet):
        compiled = re.compile(r'\s{2,}')
        cleaned = re.sub(compiled, ' ',tweet)
        return cleaned.strip()

    desired_column = desired_column.apply(username_removal)
    desired_column = desired_column.apply(website_removal)
    desired_column = desired_column.apply(repeated_chars_removal)
    desired_column = desired_column.apply(start_with_symbol_removal)

    desired_column = desired_column.str.replace("[^a-zA-Z0-9!?.,' ]",'', regex=True)

    desired_column = desired_column.apply(repeated_comma_dot_removal)
    desired_column = desired_column.apply(extra_whitespaces_removal)
    return desired_column

df['tweet'] = data_cleaning(df['tweet'])

blanks = []
for idx, tweet in enumerate(df['tweet']):
    if type(tweet) == str:
        if (tweet.isspace()) or (len(tweet.split()) == 0):
            blanks.append(idx)
    elif type(tweet) == float:
        blanks.append(idx)

df.drop(df.index[blanks],inplace=True)

print('-------- Exporting to CSV file --------')
df.to_csv('train_preprocessed.csv',index=False)

print('-------- Implementing VADER lexicon --------')
df['compound'] = df['tweet'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x)['compound'])
df = df.loc[:,['compound','tweet','polarity']]

print('-------- Exporting to CSV file --------')
df.to_csv('train_sid.csv',index=False)

print('-------- Applying normalization --------')
df["tweet"] = df['tweet'].apply(lambda x: ' '.join([token.lemma_.lower() if token.lemma_ != '-PRON-' else token.lower_ for token in nlp(x)]))

print('-------- A bit more cleaning --------')
df['tweet'] = df['tweet'].str.replace("[^a-zA-Z]",' ', regex=True)
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([tweet for tweet in x.split() if len(tweet) > 1]))
df['tweet'] = df['tweet'].apply(extra_whitespaces_removal)

blanks = []
for idx, tweet in enumerate(df['tweet']):
    if type(tweet) == str:
        if (tweet.isspace()) or (len(tweet.split()) == 0):
            blanks.append(idx)
    elif type(tweet) == float:
        blanks.append(idx)

df.drop(df.index[blanks],inplace=True)

print('-------- Exporting to CSV file --------')
df.to_csv('train_lemma.csv',index=False)

