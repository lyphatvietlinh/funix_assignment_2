# TASK 1

filename = input("Enter a filename: ")

try:
    file_object = open(filename)
    print("File founded!")
except IOError:
    print("Could not find your file!")

# TASK 2
#This is some changes