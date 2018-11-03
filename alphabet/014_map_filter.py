# An inline function
def square(number): return number ** 2


# Map with a an inline function
print(list(map(square, [1, 2, 3, 4])))

# Map with a simple map function
print(list(map(lambda number: number ** 2, [1, 2, 3, 4])))

# Lambda function with parameter name not specified
print(list(map(lambda _: _ ** 2, [1, 2, 3, 4])))


def is_even(number): return number % 2 == 0


# Filter list with an inline function
print(list(filter(is_even, [1, 2, 3, 4, 5])))

# Filter list with a lambda function
print(list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5])))

# Lambda function parameter name place holder '_'
print(list(filter(lambda _: _ % 2 == 0, [1, 2, 3, 4, 5])))







