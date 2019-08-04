from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize
from Reporter import reporter
import json

with open('News.json', 'r') as file:
  collect = json.load(file)

summary = []
for i, j in collect.items():
  for item in j:
    summary.append(item)

corpus = [TaggedDocument(item, [i]) for i, item in enumerate(summary)]

max_epochs = 100
vec_size = 250
alpha = 0.025

modeltext = Doc2Vec(size=vec_size,
                alpha=alpha, 
                min_alpha=0.0025,
                min_count= 30,
                dbow_words = 1,
                window = 5,
                negative = 20
                )
  
modeltext.build_vocab(corpus)

for epoch in range(max_epochs):
    if(epoch%20 == 0):
      print('iteration {0}'.format(epoch))
    modeltext.train(corpus,
                total_examples=modeltext.corpus_count,
                epochs=modeltext.iter)
    modeltext.alpha -= 0.002
    modeltext.min_alpha = modeltext.alpha
    
model_name = "new_d2v_c30_w5_n20_d1_s250.model"
modeltext.save(model_name)
print("{} Model Saved".format(model_name))

# d2v2_w5_c30_150_d1_n20 "lr", "LinearSVR" all greater than 50%