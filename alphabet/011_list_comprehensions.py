# List comprehensions in Python

my_list = [letter for letter in "Python"]

print(my_list)


my_list = [item for item in range(5)]
print(my_list)

# Pick square of items
my_list = [item**2 for item in range(5)]
print(my_list)

# No variable name
my_list = [_**3 for _ in range(7)]
print(my_list)

# Add if statement
my_list = [_**2 for _ in range(10) if _ % 2 == 0]
print(my_list)


celsius = [10, 20, 23, 43]
fahrenheit = [((9/5) * temp) for temp in celsius]
print(fahrenheit)


my_list = [_ if _ % 2 == 0 else 'ODD' for _ in range(10)]
print(my_list)


my_list = []

for x in range(5):
    for y in [2, 4, 19]:
        my_list.append(x * y)

print(my_list)

my_list = [x * y for x in range(5) for y in [2, 4, 19]]
print(my_list)

my_string = "Print the words which starts with the letter s"
for word in my_string.split(" "):
    if word.startswith("s"):
        print(word)

starts_with_s = [word for word in my_string.split(" ") if word.lower().startswith("s")]
print(starts_with_s)

even_numbers = [number for number in range(11) if number % 2 == 0]
print(even_numbers)
my_list = list(range(0, 11, 2))


divisible_by_three = [number for number in range(52) if number % 3 == 0]
print(divisible_by_three)

my_string = "Print every word in this sentence that has even number of letters"
even_length_words = [word for word in my_string.split(" ") if len(word) % 2 == 0]
print(even_length_words)


for number in range(100):
    if not number % 3 and not number % 5:  # % 15 is another solution
        print("BizzBuzz", number)
    elif not number % 3:
        print("Bizz", number)
    elif not number % 5:
        print("Buzz", number)
    else:
        print(number)


my_string = "Create a list of the first letters of every word in this string"
my_list = [word[0] for word in my_string.split(" ")]
print(my_list)

