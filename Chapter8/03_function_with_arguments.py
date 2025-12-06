# Two arguments are passed here
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return  # If no value is specified, it returns None by default
    # return "done"
    # return 7
    # return "ok"

# goodDay("Harry", "Thank you") # Function call
# goodDay("Rohan", "Thank you")
# goodDay("Divya", "Thanks")
a = goodDay("Harry", "Thank you")
print(a)  # This will print 'None' since the function does not return anything ( if we do not write not return)
