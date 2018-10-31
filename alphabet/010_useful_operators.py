# Useful operators in Python

for item in range(3, 0, -1):
    print(item)


my_list = list(range(10))

print(my_list)


my_string = "oneOrTwo"

for item in enumerate(my_string):
    print(item)


for index, value in enumerate(my_string):
    print(index, ' => ', value)


list1 = range(2)
list2 = ['a', 'b', 'c', 'd']

for item in zip(list1, list2):
    print(item)


my_list = list(zip(list1, list2))
print(my_list)


cond = 'x' in ['y', 'x']

print(42 in [4, 43, 45])
print('a' in 'my name is ')
print('my_key1' in {'my_key1': 'my_value'})

# Must be at the top of the file !!!
from random import shuffle, randint

my_list = list(range(10))
print(my_list)
shuffle(my_list)
print(my_list)

for i in range(5):
    print(randint(10, 100))


result = input("Enter a number: ")
print('You entered {}'.format(result))
