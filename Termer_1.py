!pip install gensim
from gensim.downloader import load

word_vectors = load('glove-wiki-gigaword-100') 

result = word_vectors.most_similar(positive=['kitten', 'dog'], negative=['cat'], topn=1)
print("Result of 'kitten - cat + dog':", result[0][0])
