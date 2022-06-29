import re

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
