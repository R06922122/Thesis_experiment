# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:49:59 2019

@author: Moras
"""


from Reporter import reporter
from gensim.models.doc2vec import Doc2Vec
from sklearn.preprocessing import StandardScaler
import datetime


def str2date(Date):
  year = int(Date[0:4])
  month = int(Date[5:7])
  day = int(Date[8:])
  return datetime.datetime(year, month, day)

def date2str(time):
    y = str(time.year)
    m = int(time.month)
    d = int(time.day)
    if(m < 10):
        m = '0'+str(m)
    if(d < 10):
        d = '0'+str(d)
    return('{}-{}-{}'.format(y, m ,d))

def feature_label(stockno, num, textmodel):
  textmodel = Doc2Vec.load(textmodel)
  
  fakenews = reporter(stockno)
  tmpnews = fakenews.news
  label = fakenews.L
  
  news = {}
  for i, j in tmpnews.items():
    if(j != []):
      news[i] = j
  
  timeline  = list(news.keys())
  timeline.reverse()
  deadline = str2date(timeline[num-1])
  
  x_train = []
  y_train = []
  x_test = {}
  y_test = {}
  history = []
  
  for date, fnews in news.items():
      if(str2date(date) >= deadline):
        continue
      else:
        for newfake in fnews:
          if(newfake in history):
            continue
          history.append(newfake)
          x_train.append(textmodel.infer_vector(newfake))
          if(label[date] > 0):
            y_train.append(1)
          else:
            y_train.append(-1)
  
  for i, j in news.items():
    if(str2date(i) >= deadline):
      x_test[i] = []
      if(label[i] > 0):
        y_test[i] = 1
      else:
        y_test[i] = -1
      
  for i, j in news.items():
    if(str2date(i) >= deadline):
      for new in j:
        x_test[i].append(textmodel.infer_vector(new))
  
  
  return [x_train, y_train, x_test, y_test]
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  