class Employee:
    language = "Python" 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")


harry = Employee() 
harry.language = "Javascript" # This is an instance attribute
harry.getInfo() # calling getInfo using object
Employee.getInfo(harry) # calling getInfo using class name and passing object as argument
# Argument harry (object) will be acceopted by self parameter of getInfo method

harry.greet() # This will give error because greet function does not take self parameter
Employee.greet(harry) # This is the correct way to call greet method

# If we try to access class method using object, it will give error because class method does not take self parameter, so after using self parameter, both will be correct 