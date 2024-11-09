from itertools import count

with open('D:/ItStep/Piton/files/origin.txt') as file:
    content = file.read()

new_text = []
word_count = 0

for word in content.split():
    if len(word) > 6:
        word_count += 1
        new_text.append(f"{word_count}: {word}")

with open('D:/ItStep/Piton/files/overwrite.txt', 'w') as output_file:
    output_file.write("\n".join(new_text))