# File

#This will read the content on file
my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r')
content = my_file.read()
print(content)

#This will read and write to the file
my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','r+')
my_file.write("just another day")
print(content)

#This append the file by adding the text  to the end
my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','a')
my_file.write(" this append the file by adding to the end")
print(content)

#This will delete the content in the file and add the new one
my_file = open('C:/Users/markw/PycharmProjects/Devops2510/Day3/name','w')
my_file.write("Hello ")
my_file.close()
