import re
import os
import random

# Milestones
# 1. Ask for the project name and author
# 2. Ask for Project date
# 3. Develop skeleton structure
# 4. Make use of TODO list
# Finish this project
# Better to make the milestones small than too large,
# Milestones: “reduce the number of things you have to think about at any one time”.
# https://robertheaton.com/ppab7-auto-project-builder/

# ^ signals start of string, $ signals end of it in the "re" documentation

# .ljust(40) was conflicting with my validation

# Validates user input and length


i = 0
while True:
    projectName = input("What is the title of your project? ")
    state = bool(projectName.isidentifier())

    if not state:
        i += 1
        if i == 3:
            print("I give up")
            exit()
        else:
            print("Invalid input, please try again")
            continue
    elif len(projectName) < 1 or len(projectName) > 40:
        print("Please enter a name between 1-40 characters")
        continue
    else:
        break

# Validates user input length
while True:
    projectAuthor = input("Who is the author of this project? ")
    if len(projectAuthor) < 1 or len(projectAuthor) > 40:
        print("Please enter a name between 1-40 characters")
        continue
    else:
        break

print("## PROJECT DETAILS ##")
print("Project name: " + projectName)
print("Author: " + projectAuthor)

# Code that didn't work
# direct = "C:\\Users\\User\\PycharmProjects\\"
# input_new = input("Enter a new Project folder name: ")
# new_path = os.path.join(direct, input_new)
# os.mkdir(new_path, mode=0o666)
# print("Directory '% s' is built!" % new_path)

while True:

    direct = "C:\\Users\\User\\PycharmProjects\\"
    input_new = input("Enter a new Project folder name: ")
    new_path = os.path.join(direct, input_new)
    # Code that didn't work
    # os.mkdir(new_path, mode=0o666)
    # print("Directory '% s' is built!" % new_path)
    #
    if os.path.exists(new_path):
        input_new = input("Directory already exists. Enter a new Project folder name: ")
        new_path = os.path.join(direct, input_new)
        if os.path.exists(new_path):
            print("Directory already exists")
        else:
            os.mkdir(new_path, mode=0o666)
            print("Directory '% s' created at " % new_path)
            break
    else:
        os.mkdir(new_path, mode=0o666)
        print("Directory '% s' created at " % new_path)
        break

with open(new_path + "/README.md", "+w") as text:
    text.write(f"# {projectName} \n\n ## Description\n\nTODO \n\n ## How to install the project \n\nTODO\n\n ## How "
               f"to run the project \n\nTODO\n\n ## Author\n\n{projectAuthor}")

print("File '% s' created at " % new_path)