sentence = "Дано предложение. Напечатать все его различные слова."
word_list = sentence.split()

unique_words = set(word_list)

for word in unique_words:
    print(word)