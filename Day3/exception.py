#exception

try:
    my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r')
    my_file.write("Hello")
except:
    print("we have a problem")

print(123)



try:
    my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r')
    my_file.write("Hello")
except FileNotFoundError as e:
    print(e)
except UnicodeError:
    print("we have a problem")

print(123)

# Using finally block

try:
    my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r')
    my_file.write("Hello")
finally:
    print("you got my code")
print(123)



try:
    my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r')
    my_file.write("Hello")
except FileNotFoundError as e:
    print(e)
except UnicodeError:
    print("we have a problem")
finally:
    print("you crush my code")
print(123)


#using the with
with open('file_path','w') as file:
    file.write('hello world')


# u can use either
file = open('file_path','w')
try:
    file.write('hello world')
finally:
    file.close()