def greatest(a, b, c):
    if(a>c and a>b):
        return a
    elif(b>c and b>a):
        return b   
    elif(c>a and c>b):
        return c

a = 1
b = 2
c = 3

print(greatest(a, b, c))
