
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
# print(f_to_c(f)) 
#  OR
# print(f"{f_to_c(f)} Degree C")

c = f_to_c(f)
print(f"{round(c, 2)} Degree C")



