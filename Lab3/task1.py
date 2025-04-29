import re

text = "Apples! and bananas? are delicious."
print("Заданий текст:", text)

cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print("1. Виправлений текст:", cleaned_text)

char = 'o'
words_with_char = re.findall(r'\b\w*' + char + r'\w*\b', text, re.IGNORECASE)
print("2. Знайдені слова з заданою буквою:", words_with_char)

n = 6
words_n_length = re.findall(r'\b\w{' + str(n) + r'}\b', text)
print("3. Знайдені слова з заданою довжиною:", words_n_length)

matching_words = re.findall(r'\b[aAbB]\w*s\b', text, re.IGNORECASE)
print("4. Слова, які починаються 'a' чи 'b' і закінчуються 's':", matching_words)
