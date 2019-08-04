# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:20:17 2019

@author: Moras
"""
from sklearn.metrics import precision_score as precision
from sklearn.metrics import accuracy_score as accuracy
from sklearn.metrics import recall_score as recall

def get_label_predict(label, predict):
  v = []
  k = []
  y = []
  for i, j in label.items():
    y.append(j)
  for i, j in predict.items():
    v.append(j[0])
    k.append(j[1])
  return y, v, k


def output_result(l , y):
  print("Accuracy:  {}".format(accuracy(l, y)))
  print("Precision: {}".format(precision(l, y)))
  print("Recall:    {}".format(recall(l, y)))
  print("-----------------------------------------------")
  return accuracy(l, y),precision(l, y),recall(l, y)


def score(label, y):
  l, v, k = get_label_predict(label, y)
  print("-----vote result-----")
  output_result(l, v)
  print("-----kmeans result-----")
  output_result(l, k)
  return None