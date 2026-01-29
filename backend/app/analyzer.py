import re
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s\.]", "", text)
    return text

def get_top_phrases(words, n):
    phrases = [
        " ".join(words[i:i+n])
        for i in range(len(words) - n + 1)
    ]
    return Counter(phrases).most_common(5)

def sentence_complexity(sentences):
    scores = {}
    for sentence in sentences:
        words = sentence.split()
        if not words:
            continue
        avg_len = sum(len(w) for w in words) / len(words)
        scores[sentence] = round((len(words) * 1.5) + avg_len, 2)
    return scores

def analyze_text(text):
    text = clean_text(text)
    words = text.split()
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    complexity = sentence_complexity(sentences)

    return {
        "top_2_word_phrases": get_top_phrases(words, 2),
        "top_3_word_phrases": get_top_phrases(words, 3),
        "reading_time_minutes": round(len(words) / 200, 2),
        "most_complex_sentence": max(complexity, key=complexity.get),
        "simplest_sentence": min(complexity, key=complexity.get),
        "sentence_complexity_scores": complexity,
        "all_sentences": sentences
    }
