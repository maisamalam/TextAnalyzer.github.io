import nltk
from nltk import FreqDist
from nltk.util import ngrams
from textblob import TextBlob, Word
from collections import Counter
import re
import numpy as np

# Install nltk data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def text_preprocessing(text):
    # Convert to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def sentence_complexity(text):
    sentences = nltk.sent_tokenize(text)
    avg_sentence_length = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences) / len(sentences)
    return avg_sentence_length

def vocabulary_richness(text):
    words = nltk.word_tokenize(text)
    word_freq = FreqDist(words)
    return len(word_freq) / len(words)

def spelling_mistakes(text):
    words = nltk.word_tokenize(text)
    mistakes = [word for word in words if Word(word).spellcheck()[0][0] != word]
    return mistakes

def grammatical_errors(text):
    blob = TextBlob(text)
    grammar_mistakes = len(blob.correct().raw_sentences) - len(blob.raw_sentences)
    return grammar_mistakes

def ngram_analysis(text, n):
    words = nltk.word_tokenize(text)
    n_grams = ngrams(words, n)
    freq = FreqDist(n_grams)
    return freq.most_common()

def stylistic_patterns(text):
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    tag_counts = Counter(tag for word, tag in pos_tags)
    return tag_counts

def semantic_coherence(text):
    sentences = nltk.sent_tokenize(text)
    polarity_scores = [TextBlob(sentence).sentiment.polarity for sentence in sentences]
    subjectivity_scores = [TextBlob(sentence).sentiment.subjectivity for sentence in sentences]
    polarity_std_dev = np.std(polarity_scores)
    subjectivity_std_dev = np.std(subjectivity_scores)
    return polarity_std_dev, subjectivity_std_dev

text = ""

processed_text = text_preprocessing(text)
print("Sentence complexity:", sentence_complexity(text))
print("Vocabulary richness:", vocabulary_richness(processed_text))
print("Spelling mistakes:", spelling_mistakes(processed_text))
print("Grammatical errors:", grammatical_errors(text))
print("3-grams:", ngram_analysis(processed_text, 3))
print("Stylistic patterns:", stylistic_patterns(processed_text))
print("Semantic coherence (polarity, subjectivity):", semantic_coherence(text))

