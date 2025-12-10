word = "Donkey"

with open("file.txt", "r") as file:
    content = file.read()

contentNew = content.replace(word, "#####")

with open("file.txt", "w") as file:
    file.write(contentNew)