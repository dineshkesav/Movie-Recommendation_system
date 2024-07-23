# -*- coding: utf-8 -*-
"""movie-recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-_Dlq4ybx2sbZS8sdOHbDo73y_YBN6y_

**MOVIE RECOMMENDATION SYSTEM**

The goal of a movie recommendation system is to help users find movies based on their interest. It looks at the movies they've watched and rated, then suggests new ones you might enjoy based on your tastes. By doing this, it makes choosing a movie easier and more fun, just like a friend giving you a great recommendation.

**IMPORT LIBRARIES**
"""

import numpy as np
import pandas as pd

"""**IMPORT DATASET**"""

df=pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.columns

df.shape

"""**FEATURES**"""

df_features= df[['Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')

df_features

df_features.shape

x = df_features['Movie_Genre']+' '+df_features['Movie_Keywords']+' '+df_features['Movie_Tagline']+' '+df_features['Movie_Cast']+' '+df_features['Movie_Director']

x.shape

"""**Feature Text Conversion to Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tf=TfidfVectorizer()

x=tf.fit_transform(x)

x.shape

print(x)

"""**Use Cosine Similarity for similarity score**"""

from sklearn.metrics.pairwise import cosine_similarity

score=cosine_similarity(x)

score.shape

score

"""**Find Movies with closest spelling**"""

fav_mov=input('Enter a movie name    :    ')

mov_list=df['Movie_Title'].tolist()

import difflib as dl

rec_mov=dl.get_close_matches(fav_mov,mov_list)
print(rec_mov)

index=df[df.Movie_Title==rec_mov[0]]['Movie_ID'].values[0]
print(index)

"""List of similar movies"""

rec_score=list(enumerate(score[index]))
print(rec_score)

len(rec_score)

"""**Recommended Movies by getting favourite movie name**"""

sim_mov=sorted(rec_score,key=lambda x:x[1],reverse=True)
print(sim_mov)

"""Printing top 30 movies"""

print('Top 30 Recommended Movies are :\n\n')
i=1
for j in sim_mov:
  k=j[0]
  title=df[df.index==k]['Movie_Title'].values[0]
  if(i<31):
    print(i,'  :  ',title)
    i+=1

"""**Top 10 Recommended Movies**"""

moviename=input('Enter a movie name   :    ')
all_mov=df['Movie_Title'].tolist()
cls_mt=dl.get_close_matches(moviename,all_mov)
close_match=cls_mt[0]
ind_mov=df[df.Movie_Title==close_match]['Movie_ID'].values[0]
rec_score=list(enumerate(score[ind_mov]))
sim_mov=sorted(rec_score,key=lambda x:x[1],reverse=True)
print('Top 10 suggested Movies :\n\n')
i=1
for j in sim_mov:
  k=j[0]
  title=df[df.index==k]['Movie_Title'].values[0]
  if(i<11):
    print(i,'  :  ',title)
    i+=1