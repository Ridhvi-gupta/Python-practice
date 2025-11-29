d = {} # Empty dictionary
print(type(d))
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
}

# print(marks)  # prints the entire dictionary
# print(type(marks))  # prints the type of the dictionary
print(marks, type(marks))  # prints the dictionary and its type

# print(marks[0])  # This will raise a KeyError since dictionaries do not support indexing
print(marks["Harry"])  # prints the value associated with the key "Harry"


# marks1 = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23,
#     0: "Harry"
# }
# print(marks1)  