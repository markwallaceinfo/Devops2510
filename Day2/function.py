# Function ,methods

def do_something():
    a = 8
    b = 5
    c = 3
    print(a + b + c)


do_something()
print('----')

do_something()
print('-----')


# function types

def run():
    return "Hello"


my_word = run()
print(my_word)


def run1(name):
    print(name)


j_m = run1("john")
print(j_m)


def run2(name):
    return "Hello" + " " + name


print(run2("kevin"))


def age_name(age, name):
    return "is age and name of student :" + " " + age + " " + name


print(age_name(str(15), "James"))

def r():
    if 1>0:
        print(1)
        return

r()

