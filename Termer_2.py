!pip install scikit-learn matplotlib gensim numpy

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import gensim.downloader as api

word_vectors = api.load('glove-wiki-gigaword-100')

sports_words = ['football', 'soccer', 'tennis', 'basketball', 'cricket', 'goal', 'player', 'team', 'coach', 'score']
sports_vectors = np.array([word_vectors[word] for word in sports_words])

pca = PCA(n_components=2)
sports_2d = pca.fit_transform(sports_vectors)
plt.figure(figsize=(8,6))
for i, word in enumerate(sports_words):
  plt.scatter(sports_2d[i,0], sports_2d[i,1])
  plt.annotate(word, (sports_2d[i,0], sports_2d[i,1]))
plt.title("PCA Visualization of Sports Words")
plt.show()

result=word_vectors.most_similar("man",topn=5 )
for word, similarity in result:
 print(f"{word}: {similarity:.4f}")
