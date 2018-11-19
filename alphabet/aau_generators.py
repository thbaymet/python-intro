def cube_ranges(n):
    """
    Returns a cube ranges generator which provides all values
    from 0 to n-1 power 3 (cube)
    :param n: an integer
    :return: from 0 to n-1 cube range generator
    """
    for x in range(n):
        yield x**3


print(cube_ranges(20))
print(list(cube_ranges(20)))


def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Print fibonacci series by using fibonacci generator
for i in fibonacci_gen(10):
    print(i, end=' ')
print()

