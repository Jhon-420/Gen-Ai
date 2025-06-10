word_embeddings = {
"ai": ["machine learning", "deep learning", "data science"],
"data": ["information", "dataset", "analytics"],
"science": ["research", "experiment", "technology"],
"learning": ["education", "training", "knowledge"],
"robot": ["automation", "machine", "mechanism"]
}

def find_similar_words(word):
    if word in word_embeddings:
        return word_embeddings[word]
    else:
        return []

def enrich_prompt(prompt):
    words = prompt.lower().split()
    enriched_words = []
    for word in words:
        similar_words = find_similar_words(word)
    if similar_words:
        enriched_words.append(f"{word} ({', '.join(similar_words)})")
    else:
        enriched_words.append(word)
        return " ".join(enriched_words)

original_prompt = "Explain AI and its applications in science."

enriched_prompt = enrich_prompt(original_prompt)

print("Original Prompt:")
print(original_prompt)
print("\nEnriched Prompt:")
print(enriched_prompt)