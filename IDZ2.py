word = "привет"  # ваше слово
new_word = ""

for i in range(0, len(word), 2):
    if i < len(word) - 1:
        new_word += word[i + 1] + word[i]
    else:
        new_word += word[i]

print(new_word)