# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:49:59 2019

@author: Moras
"""

import re
import os
import numpy as np
import pandas as pd
import jeiba
import datetime as dt

def str2date(Date):
  year = int(Date[0:4])
  month = int(Date[5:7])
  day = int(Date[8:])
  return dt.datetime(year, month, day)

def date2str(time):
    y = str(time.year)
    m = int(time.month)
    d = int(time.day)
    if(m < 10):
        m = '0'+str(m)
    if(d < 10):
        d = '0'+str(d)
    return('{}-{}-{}'.format(y, m ,d))
    #%%
def segtext(text, stopset):
  tmp = []
  words = jeiba.cut(text, 1, 1)
  for word in words:
    if((word not in stopset) and word != ''):
        tmp.append(word)
  return tmp
#%%
News = []
with open("TBMC_news (8).txt", 'r', encoding  = 'utf-8' ) as file:
    for line in file:
        News.append(line.strip('\n'))



NewsCluster = []
tmp = []
for line in News:
    if(line == ''):
        NewsCluster.append(tmp)
        tmp = []
    else:
        tmp.append(line)


news = []
for line in NewsCluster:
    tmp = [line[2][8:], str2date(re.sub('/', '-', line[6][6:]).strip(' ')), line[0][11:] ]
    news.append(tmp)

newspd = pd.DataFrame(news, columns = ['title', 'date', 'database'])

num = []
seg= []
#change = []
for i in range(len(newspd)):
    num.append([])
    seg.append([])
#    change.append([])
    
newspd['stockno'] = pd.Series(num)
newspd['seg'] = pd.Series(seg)
#newspd['chg'] = pd.Series(change)

for i in range(len(newspd)):
    if('台泥' in newspd['title'][i]):
        newspd['stockno'][i].append('1101')
    if('亞泥' in newspd['title'][i]):
        newspd['stockno'][i].append('1102')
    if('嘉泥' in newspd['title'][i]):
        newspd['stockno'][i].append('1103')
    if('環泥' in newspd['title'][i]):
        newspd['stockno'][i].append('1104')
    if('水泥' in newspd['title'][i]):
        newspd['stockno'][i].append('666')
        
#%%
from datetime import timedelta
from Reporter import reporter

m1 = reporter(1101)
collect = m1.news

stopSet = set()
with open("StopWords.txt", "r", encoding = "utf-8") as Sfile:
    for word in Sfile:
        stopSet.add(word.strip('\n'))    



for i in range(len(newspd)):
  if(newspd['stockno'][i] != []):
    tmp = segtext(newspd['title'][i], stopSet)
    newspd['seg'][i] = [tmp, date2str(newspd['date'][i])]
  

for i in range(len(newspd)):
  if(newspd['stockno'][i] != []):
    date = str2date(newspd['seg'][i][1])
    
    while(1):
      try:
        sdate = date2str(date)
        collect[sdate].append(newspd['seg'][i][0])
        break
      except:
        date += timedelta(1)




        
        
