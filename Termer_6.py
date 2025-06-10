# !pip install transformers
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

sentences = [
    "I love using this product! It makes my life so much easier.",
    "The service was terrible, and I'm very disappointed.",
    "It's an average experience, nothing special but not bad either."]

for sentence in sentences:
    result = sentiment_analyzer(sentence)[0]
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {result['label']} (Score: {result['score']:.2f})\n")