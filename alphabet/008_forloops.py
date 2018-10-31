# For loops in Python

# Loop string characters
for a_character in "My string":
    print(a_character)


# Loop integer list
for an_integer in [1, 2, 4, 5, 9]:
    print(an_integer)


# Loop a complex type of list
for _ in ["one", 2, "three", 4, 'four', ['x', 'y', 'z']]:
    print(_)


# Loop a tuple
the_tuple = (4, 'you', True, 'for', 'me', False)
for item in the_tuple:
    print(item)


tuple_list = [('one', 1), ('two', 2), ('three', 3)]
for (word, number) in tuple_list:
    print(f"'{number}' is called as '{word}'")


for item in [3, 4, 5]:
    pass
    if item > 3:
        print("Hello")


for letter in "here is":
    if letter == 'e':
        continue  # Will jump to the top
    elif letter == 'r':
        break
    print(letter)


print("That's it")
