# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:51:54 2019

@author: User
"""

from datetime import date
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
import json

#%% Repoter 2006/06/17 ~ 2019/03/07
    
class reporter():
    
    def __init__(self, StockNo): 
        self.stockno = StockNo
        self.L = self.get_label(self.stockno)
        self.news = self.all_news(self.stockno)

    def all_news(self, stockno):
        news = {}
        with open('News.json'.format(stockno), 'r') as f:
            news = json.loads(f.read())
        return news
    
    def model(self, model):
        return (Doc2Vec.load(model))
    
    def get_label(self, stockno):
        num = stockno - 1101
        label = {}
        with open('all_label.json', 'r', encoding = 'utf-8') as file:
          tmp = json.load(file)
        for i, j in tmp.items():
          label[i] = j[num]
        return label
        
        
        
        
        
#%%
#def clean(report):w
    
        
        
        