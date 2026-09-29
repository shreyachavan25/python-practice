""" Read data from the file """

""" READ THE ENTIRE FILE AT ONCE """

with open("notes.txt", "r") as file:
    contents = file.read()
print(contents)
print(" ")


""" READ THE FILE AS A LIST OF LINES """

with open("notes.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())
print(" ")


""" READ ONE LINE AT A TIME """

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
print(" ")