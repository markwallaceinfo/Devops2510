# A

#num=Noneark = 34
age_kevin = 21
age_mark = 10
if age_mark > age_kevin:
    print("BIG")
else:
    print("small")

# b
for x in range(5):
    print(x)

# c
season = 2
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("no season")

# D
10

# E
you_age = 23
last_name = "John"
currency = 3.5
flew = True
door_number = 23

print(you_age)
print(last_name)
print(currency)
print(flew)
print(door_number)
print(currency + you_age)

# f
number = input("Enter your phone number")
print("phone number is " + number)


# g
def print_hello():
    print("hello")


def add_two_number(a, b):
    add = a + b
    print(add)


print(add_two_number(2, 3))


# h

def student(name):
    print(name)


def number(num):
    result = int(num) / 2
    print(result)


print(student("alex"))

print(number(10))



# Question I
def addition(num1, num2):
    sum = num1 + num2
    return sum


def name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


print(addition(25, 30))
print(name("Jame", "Grade"))

#Question J

list_of_numbers = [5, 6, 7]
for i in list_of_numbers:
    print(i)
print(type(list_of_numbers))

#Question K
#
items = list(input())
def sum_list():
    sum_numbers = 0
    for x in range(len(items)):
        sum_numbers = 0 + items[x]
    print(sum_numbers)

print(sum_list())

print(sum_list())

#Question L
student_grades = {"mark":75,"john":97,"kevin":78}
for x in student_grades.keys():
    print(x)

#CHALLENGES:

#Question O-1
student_grades = int(input("Please enter grades: "))


#questio O-2
def enter_grade_sum(student_grades):
    sum = +student_grades
enter_grade_sum()

#QUESTION P
input = ('h','e','l','l','o')
def tupl_str(input):
    str = ''
    for a in input:
        str = str + a
    return str
print(tupl_str(input))