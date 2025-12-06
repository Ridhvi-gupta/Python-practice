## Program to find average of 3 numbers
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))

# average = (a + b + c)/3
# print(average)

# # To do same thing for different set of numbers
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))

# average = (a + b + c)/3
# print(average)

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)
    return "average"

## To print the function 5 times
# avg() # To call/run the function or Function call
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()

a = avg()
print(a)