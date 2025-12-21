# Creating class
class Employee:
    # name = "Harry"  If name is not given in class attributes
    language = "Py" # This is a class attribute
    salary = 1200000

# Creating object of class, harry is a object of class Employee
# harry is first object of class Employee
harry = Employee() # Employee() is a memory allocation statement
harry.name = "Harry" # This is an object attribute
# Accessing class attributes using object
# print(harry.name)
print(harry.name, harry.language, harry.salary)

# Creating another object of class Employee
rohan = Employee()
rohan.name = "Rohan Roro Robinson" # Dynamically adding attribute to object
print(rohan.name, rohan.salary, rohan.language)

# Here, name is an instance attribute and language, salary are class attributes as they directly belong to class
# Oject attributes are also known as instance attributes