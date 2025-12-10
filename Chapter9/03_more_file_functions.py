f = open("file.txt")

# lines = f.readlines() # Reads all lines into a list
# print(lines, type(lines))

# line1 = f.readline()  # Reads a single line from the file
# print(line1, type(line1))
# line2 = f.readline()  
# print(line2, type(line2))
# line3 = f.readline()  
# print(line3, type(line3))
# line4 = f.readline()  
# print(line4, type(line4))
# line5 = f.readline()  # no more lines to read, so no output
# # print(line5, type(line5))
# print(line5 =="") # True, empty string

##  This can be done with the help of a loop, as above code is very cumbersome process, line will keep on printing until there are no more lines to read  
line = f.readline()
while(line != ""):  # while line is not empty
    print(line)
    line = f.readline()

f.close()