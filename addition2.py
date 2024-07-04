import random

with open('32732 2.txt', 'r') as file:
    text_data = file.read()

words = text_data.split()

dictionary = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in dictionary:
        dictionary[current_word] = []

    dictionary[current_word].append(next_word)

generated_text = []
current_word = random.choice(list(dictionary.keys()))
generated_text.append(current_word)

for _ in range(199):
    current_word = random.choice(dictionary[current_word])
    generated_text.append(current_word)

generated_text = ' '.join(generated_text)
print(generated_text)