function detectLanguage() {
    var text = document.getElementById('inputText').value;
    var language = detectLang(text);
    document.getElementById('result').innerText = "Detected language: " + language;
}

function detectLang(text) {
    return window.langdetect.detect(text);
}
