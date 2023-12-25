from random import randint
from flask import Flask



app = Flask(__name__)
# Question 1-2
num1 = 1
num2 = 0
try:
    a = num1 / num2
except ZeroDivisionError as a:
    print(a)
    print("you are dividing by zero")

#Question3
 # yes
 # finally is use in exception blocks most time as the last thing in that block

#Question 4
 # All exception

#Question5
# The problem with using the word exception and not specific with the type of exception is that:
# 1 It is bad practice
# 2 You don't know the type of exception you are trying to handle

#Question 6
#except IOError
# This type of exception deals with mostly input and output conditions
#IOError exception is raised when an input or output operation is taking place, there can be many reasons for this.


#except ZeroDivisionError
# This exception happen when you divide by zero like in question 1

#Question7

list_of_student = open('C:\\Users\\markw\\PycharmProjects\\Devops2510\\Day3\\word.txt','w')
list_of_student.close()

#Question8
list_of_student = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/word.txt','w')
list_of_student.write("Mark")
list_of_student.close()

#Question9
list_of_student = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/word.txt','r')
st = list_of_student.read()
print(st)
list_of_student.close()

#Q uestion10
coding = 'utf8'
list_of_student = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/hebrew.txt','w',encoding=coding,errors='ignore')
st = list_of_student.write('שם')
print(st)
list_of_student.close()

# #Question11
# # accessed via <HOST>:<PORT>/get_random
# @app.route("content")
# def random():
#     return open('words.txt').read(),200
#
# # using default
# @app.route('/register')
# def hello_user():
#     open('words.txt','w').write('hello')
#     return 'success', 201 # status code
#
# app.run(host='127.0.0.1', debug=True, port=3000)


from PIL import Image
# creating a image object (main image)
im1 = Image.open(r"C:\Users\markw\Pictures\Screenpresso\2023-04-01_09h13_45.png")


im1 = im1.save("2023-04-01_09h13_45.png")
