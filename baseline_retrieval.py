import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("1. Loading your training subset (D_10k)...")
# Load your generated parquet file
train_df = pd.read_parquet("train_en_kn_10k_seed_42.parquet")

# Example test sentences (In your full pipeline, load FLORES-200 devtest here)
test_sentences = [
    "What is your name?",
    "Where is the nearest railway station?",
    "The weather is very pleasant today."
]

print("2. Fitting TF-IDF Vectorizer on English training sentences...")
vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2))
train_tfidf = vectorizer.fit_transform(train_df['en'])

print("3. Retrieving translations for test sentences...")
test_tfidf = vectorizer.transform(test_sentences)

# Compute cosine similarity between test sentences and training pool
similarities = cosine_similarity(test_tfidf, train_tfidf)

for i, test_sent in enumerate(test_sentences):
    # Find the index of the highest similarity score
    best_match_idx = similarities[i].argmax()
    retrieved_en = train_df.loc[best_match_idx, 'en']
    retrieved_kn = train_df.loc[best_match_idx, 'kn']
    score = similarities[i][best_match_idx]
    
    print(f"\n--- Test Sentence {i+1} ---")
    print(f"Input (Test): {test_sent}")
    print(f"Best Matched Train Source: {retrieved_en} (Similarity: {score:.2f})")
    print(f"Retrieved Output (Kannada): {retrieved_kn}")