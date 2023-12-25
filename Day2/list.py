# List
my_list = ["a", 2, 'true']
print(my_list[1])
my_list[0] = 'b'
print(my_list[0])

my_list.append(44)
print(my_list)

print(my_list[2])

my_list.pop(0)
print(my_list)

my_list.insert(1,6)
print(my_list)

print(len(my_list))

for tem in my_list:
    print(tem)

print("------")

for i in range(len(my_list)):
    print(my_list[i])
