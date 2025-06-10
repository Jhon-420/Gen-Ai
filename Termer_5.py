word_embeddings = {
"adventure": ["journey", "exploration", "quest"],
"robot": ["machine", "automation", "mechanism"],
"forest": ["woods", "jungle", "wilderness"],
"ocean": ["sea", "waves", "depths"],
"magic": ["spell", "wizardry", "enchantment"]
}

def get_similar_words(seed_word):
    if seed_word in word_embeddings:
        return word_embeddings[seed_word]
    else:
        return ["No similar words found"]

def create_paragraph(seed_word):
    similar_words = get_similar_words(seed_word)
    if "No similar words found" in similar_words:
        return f"Sorry, I couldn't find similar words for '{seed_word}'."

    paragraph = (
        f"Once upon a time, there was a great {seed_word}. It was full of {', '.join(similar_words[:-1])}, and {similar_words[-1]}. Everyone who experienced this {seed_word} always remembered it as a remarkable tale."
    )
    return paragraph

seed_word = "adventure" 

story = create_paragraph(seed_word)
print("Generated Paragraph:")
print(story)