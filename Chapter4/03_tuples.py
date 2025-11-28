a = (1, 2, 5, 6)
print(type(a))  
a = (1)
print(type(a))
a1 = (1,)  # Tuple with single element
print(type(a1))
b = ()
print(type(b))
a = (1,45,342,3424,False, "Rohan", "Shivam")
# a[0] = 4532  # This will raise an error since tuples are immutable
print(a)
print(type(a))

c = (1)
print(type(c)) # Not a tuple, just an integer
d = (1,)
print(type(d)) # This is a tuple
e = (1,45,342,3424,False, "Rohan", "Shivam")
print(type(e))
