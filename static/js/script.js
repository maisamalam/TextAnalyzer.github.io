document.getElementById('analyze-button').addEventListener('click', function() {
    var text = document.getElementById('text-area').value;
    
    fetch('/analyze_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: text}),
    })
    .then(response => response.json())
    .then(data => {
        var resultsElement = document.getElementById('results');
        resultsElement.innerHTML = '';

        for (var key in data) {
            var value = data[key];

            var resultElement = document.createElement('p');
            resultElement.textContent = key + ': ' + value;

            resultsElement.appendChild(resultElement);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
