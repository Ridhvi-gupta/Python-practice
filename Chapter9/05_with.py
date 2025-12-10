f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statment like this (means the output will be the same):
with open("file.txt") as f:
    print(f.read())

# You don't need to explicitly close the file when using with statement.