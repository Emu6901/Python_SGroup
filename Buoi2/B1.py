import re


def inputNameAndAge():
    name = ""
    age = -1
    while (age < 0 or age > 150) or re.search("\d", name) :
        name = input('Enter a name: ')
        age = int(input('Enter an age: '))
    print("Name: {} \nAge: {}\n".format(name.strip(), age))


inputNameAndAge()



