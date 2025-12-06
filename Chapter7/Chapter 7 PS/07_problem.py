'''
For n = 3
  *    # 2 spaces
 ***   # 1 space
*****  # no space


For n = 5
    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")