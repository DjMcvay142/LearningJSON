with open("myfile.txt", "w") as file:
    file.write(" Name: Dan McVay \n Course: Computing and Information Science Foundation")

with open("myfile.txt", "r") as file:
    print(file.read())

with open("myfile.txt", "a") as file:
    file.write("\n This is an appended line")

with open("myfile.txt", "r") as file:
    print(file.read())