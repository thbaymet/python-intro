def my_function():
    """
    This is a simple python function, with no argument.
    It prints "Hello World"
    :return: NoneType Nothing returned
    """
    print("Hello World")


my_function()  # Make a call to that function

my_function2 = my_function

my_function2()


def who_knows(who="World"):
    """
    This function simply prints out the given parameter value
    :param who: the value to print
    :return: Nothing returned
    """
    print("Hello {}".format(who.capitalize()))


who_knows()
who_knows("patrick")
