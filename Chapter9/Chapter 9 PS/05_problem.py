words = ["Donkey", "bad", "clean"]

with open("file.txt", "r") as file:
    content = file.read()

for word in words:
    content = content.replace(word, "#" * len(word))  # We will use content instead of contentNew here, to update the same variable

with open("file.txt", "w") as file:
    file.write(content)