def print_all(*args):
    """
    Prints all given parameters' value with a "=>" separator.
    :param args: tuple of elements to print
    :return: Nothing returned
    """
    print("VALUES: ", *args, sep=' => ', end=". It is done.")


print_all("one", "two", "three")
print()


def which_fruit(**kwargs):
    if 'fruit' in kwargs:
        print('My favourite fruit is {}'.format(kwargs['fruit']))
    else:
        print("I don't like any fruit.")


which_fruit(fruit='apple')


def both_args_and_kwargs(*args, **kwargs):
    for item in args:
        print(item)
    for item in kwargs:
        print(item)


both_args_and_kwargs(45, 'Hello', name='John')


def my_func(word):
    """
    This function, given a word/name, return a string representation with even
    letters in uppercase and odd letters in lowercase.
    :param word: a string word
    :return: a string with even letters in uppercase and odd letters in lowercase.
    """
    res_string = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            res_string += letter.upper()
        else:
            res_string += letter.lower()
    return res_string


print(my_func("Patrick"))

