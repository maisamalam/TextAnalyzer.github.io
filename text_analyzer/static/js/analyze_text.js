document.getElementById('analyze-button').addEventListener('click', function(e) {
    e.preventDefault();

    const text = document.getElementById('text-input').value;

    fetch('http://localhost:5000/analyze_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: text,
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sentence_complexity').innerText = "Sentence Complexity: " + data.sentence_complexity;
        document.getElementById('vocabulary_richness').innerText = "Vocabulary Richness: " + data.vocabulary_richness;
        document.getElementById('spelling_mistakes').innerText = "Spelling Mistakes: " + data.spelling_mistakes.join(', ');
        document.getElementById('grammatical_errors').innerText = "Grammatical Errors: " + data.grammatical_errors;
        document.getElementById('3-grams').innerText = "3-grams: " + JSON.stringify(data['3-grams']);
        document.getElementById('stylistic_patterns').innerText = "Stylistic Patterns: " + JSON.stringify(data.stylistic_patterns);
        document.getElementById('semantic_coherence').innerText = "Semantic Coherence: " + JSON.stringify(data.semantic_coherence);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

