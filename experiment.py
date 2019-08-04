# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:33:09 2019

@author: Moras
"""
from Feature_Label import feature_label
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
from sklearn.linear_model import LogisticRegression as lr 
from sklearn.svm import NuSVC as ns
from sklearn.ensemble import AdaBoostClassifier as abc

#%%
def experiment(model, textmodel):
  
  trade_days = [30, 60]
  nos = [1101]
  all_predict = []
  all_labels = []
  
  
  for stockno in nos:
    for days in trade_days:
      data = feature_label(stockno, days, textmodel)

      feature= []
      for i, j in data[2].items():
        for vec in j:
          feature.append(vec)
      feature = np.array(feature)
      test_scaler = StandardScaler().fit(feature)

      x_train = np.array(data[0])
      y_train = np.array(data[1])

      train_scaler= StandardScaler().fit(x_train)
      x_train = train_scaler.transform(x_train)
      
      if(model == 'ns'):
        clf = ns(kernel = 'linear').fit(x_train, y_train)
      elif(model == 'abc'):
        clf = abc(learning_rate = 1, n_estimators = 100).fit(x_train, y_train)
      elif(model == 'lr'):
        clf = lr().fit(x_train, y_train)

      x_test = []
      pv = 0
      pk = 0
      y_test = {}
      predict = {}
      for i, j in data[2].items():
        tmp = 0
        if(j != []):
  #     ///////   vote   ///////
          for vec in j:
            tmp += clf.predict(test_scaler.transform(vec.reshape(1,-1)))
          if(tmp > 0):
            pv = 1
          else:
            pv = -1
  #     ///////   KMeans   ///////
          buf = []
          for vec in j:
            buf.append(vec)          
          center = KMeans(n_clusters = 1).fit(buf)
          result = test_scaler.transform(np.array(center.cluster_centers_[0]).reshape(1,-1))
          x_test.append(result)  
          if(clf.predict(result) > 0):
            pk = 1
          else:
            pk = -1
#          pk = clf.predict(result)

#          y_test.append(data[3][i])
          y_test[i] = data[3][i]
          predict[i] = [pv, pk]
      all_predict.append(predict)
      all_labels.append(y_test)
      print("StockNo: {}, {} trade days done".format(stockno, days))
  return all_labels, all_predict







'''
1101 lr 'new_d2v_c5_w5_n20_d1_s250.model'
     ns 'new_d2v_c20_w5_n20_d0_s150.model'
     abc'new_d2v_c30_w5_n20_d0_s180.model'
'''



'''
1102 lr 'new_d2v_c30_w5_n20_d0_s180.model'
     ns(SVC) 'new_d2v_c40_w5_n20_d0_s180.model'
     abc(100)    'new_d2v_c40_w5_n20_d1_s180.model'
'''

'''
1103 lr 'new_d2v_c20_w5_n20_d0_s180.model'
     ns 'new_d2v_c50_w5_n20_d1_s180.model'
     rfc 'new_d2v_c50_w5_n20_d1_s180.model'
     abc 'new_d2v_c60_w5_n20_d1_s180.model'

'''


'''
1104 lr 'new_d2v_c30_w4_n15_d1_s150.model'
     ns 'new_d2v_c40_w5_n20_d1_s180.model'
     rfc'new_d2v_c50_w5_n20_d1_s180.model'
     abc'new_d2v_c50_w5_n20_d0_s180.model'

'''



'''
ns(NuSVC poly) 'new_d2v_c40_w5_n20_d1_s180.model'  1101 1102 all good
               'new_d2v_c50_w5_n20_d1_s180.model'  1101 1102 better
               'new_d2v_c60_w5_n20_d1_s180.model'  not stable
'''

'''
abc           'new_d2v_c40_w5_n20_d0_s180.model'  1101 1102 all good

               
'''



# d2v_c15_w5_n20_s150.model lr good 2nd
# d2v_w5_c3_150.model lr good 1st
# d2v_w2_c15_150_d1_n20.model lr all bad
#  



