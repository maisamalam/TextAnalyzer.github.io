from flask import Flask, request, jsonify, render_template
import nltk
from nltk import FreqDist
from nltk.util import ngrams
from textblob import TextBlob, Word
from collections import Counter
from flask_cors import CORS
import re
import numpy as np


# Install nltk data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

app = Flask(__name__)
CORS(app)

port = 8080

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
    mistakes = [word for word in words if Word(word).spellcheck()[0][0] != word and word.isalpha()]
    return mistakes

def grammatical_errors(text):
    blob = TextBlob(text)
    grammar_mistakes = len(blob.correct().raw_sentences) - len(blob.raw_sentences)
    return grammar_mistakes

def ngram_analysis(text, n):
    words = nltk.word_tokenize(text)
    n_grams = ngrams(words, n)
    freq = FreqDist(n_grams)
    filtered_freq = [(gram, count) for gram, count in freq.items() if all(word.isalpha() for word in gram)]
    return filtered_freq

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
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/analyze_text', methods=['POST'])
def analyze_text_endpoint():
    data = request.get_json()
    text = data.get('text', '')

    processed_text = text_preprocessing(text)
    analysis = {
        'sentence_complexity': sentence_complexity(text),
        'vocabulary_richness': vocabulary_richness(processed_text),
        'spelling_mistakes': spelling_mistakes(processed_text),
        'grammatical_errors': grammatical_errors(text),
        '3-grams': ngram_analysis(processed_text, 3),
        'stylistic_patterns': stylistic_patterns(processed_text),
        'semantic_coherence': semantic_coherence(text),
    }
    return jsonify(analysis)

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0', port=8080, debug=True)