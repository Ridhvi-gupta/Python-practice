# To open any file in append mode, st is written to the end of the file

st = "Hey Harry you are amazing"

f = open("myfile.txt", "a")

f.write(st)

f.close()

# Output
# Hey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazing