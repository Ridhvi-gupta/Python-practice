'''

factorial(0) = 1   
factorail(1) = 1
factorail(2) = 2 x 1
factorail(3) = 3 x 2 x 1
factorail(4) = 4 x 3 x 2 x 1
factorail(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n x n-1 x......3 x 2 x 1
factorial(n) = n * factorial(n-1)   # recursive case

'''

def factorial(n):
    if(n==1 or n == 0):    # base condition which does't call the function any further          
        return 1
    return n * factorial(n-1)   # function calling itself

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")