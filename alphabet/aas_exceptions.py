def get_sum(a, b):
    try:
        result = a + b
    except:
        print("Impossible to get addition of '{}' and '{}'".format(a, b))
    else:
        print("Successfully done the addition of {} and {}".format(a, b))
        return result


print('get_sum: ', get_sum(10, 20))
print('get_sum: ', get_sum(10, "hello"))


def open_and_write():
    try:
        f = open('simplefile.txt', 'r')
        f.write('Some simple line to write')
    except TypeError:
        print('Got TypeError exception, verify your code')
    except OSError:
        print('Got OSError exception, something goes wrong here !')
    except:
        print('Got another exception not handled :(')
    finally:
        print('With an exception or not, the job is done. ')


open_and_write()


def ask_for_integer():
    while True:
        try:
            result = int(input('Please enter an integer number: '))
        except:
            print("Sorry something goes wrong. Try again")
            continue
        else:
            print("Thank you.")
            break
        finally:
            print("One try/except/else/finally block execution has just finished")


# ask_for_integer()

