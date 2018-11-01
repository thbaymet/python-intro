def my_function():
    """
    This is a simple python function, without any argument
    :return: NoneType nothing return, just printed 'hello world'
    """
    print("Hello World")


my_function()  # Make a call to that function

my_function2 = my_function

my_function2()


def who_knows(who="World"):
    """
    This function simply prints out the given who value
    :param who: the value to print
    :return: nothing return, only printed
    """
    print("Hello {}".format(who.capitalize()))


who_knows()
who_knows("patrick")


def print_all(*args):
    """
    Prints all given parameters' value
    :param args: tuple of elements to print
    :return: Nothing returned, all are printed
    """
    print(args, sep=',', end=". I've correctly printed all given values.")


print_all("one", "two", "three")




