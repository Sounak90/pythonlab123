from string import punctuation

def word_frequency(text):
    text = text.lower()
    cleaned_text = " "
    for ch in text:
        if ch not in punctuation:
            cleaned_text += ch
    words = cleaned_text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word,0) + 1
    return freq
print(word_frequency("Hello! hello world!"))