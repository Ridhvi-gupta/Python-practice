import numpy as np
# Working with multidimensional arrays using numpy

# Forming a 3-letter word using string concatenation
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])  

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]  # Accessing elements and concatenating to form the word
print(word)  # Output: ASS

