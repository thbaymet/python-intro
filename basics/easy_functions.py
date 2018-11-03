def occurrence_is_odd(number, array):
    """
    Find if occurrence of the "number" in the "array" is odd or not
    :param number: an integer in the array
    :param array: integer items
    :return: True if the occurrence of the number in array is odd, False else
    """
    count = 0
    for item in array:
        if item == number:
            count += 1
    return count % 2 != 0


def sum_of_odds(array):
    """
    Find the sum of the numbers which's occurrences are odd number
    https://www.geeksforgeeks.org/sum-of-all-odd-frequency-elements-in-an-array/
    :param array: list of integer numbers
    :return: Sum of the numbers which's occurrences are odd.
    """
    sum_of = 0
    for item in array:
        if occurrence_is_odd(item, array):
            sum_of += item
    return sum_of


print("sum_of_odds: ", sum_of_odds([1, 2, 2, 4, 5, 5]))


def sum_of_odds_v2(array):
    """
    Find the sum of the numbers which's occurrences are odd number
    https://www.geeksforgeeks.org/sum-of-all-odd-frequency-elements-in-an-array/
    :param array: list of integer numbers
    :return: Sum of the numbers which's occurrences are odd.
    """
    my_dict = {0: 0}
    for item in array:
        my_dict[item] = 0

    for item in array:
        my_dict[item] += 1

    sum_of = 0
    for key, value in my_dict.items():
        if not (value % 2 == 0):
            sum_of += key

    return sum_of


print("sum_of_odds_v2: ", sum_of_odds_v2([1, 2, 2, 4, 5, 5]))


# Print sum of only even numbers from given array
print("sum_of_evens: ", sum([_ for _ in [1, 2, 2, 4, 5, 5] if _ % 2 == 0]))


def is_typed_name(name, typed_name):
    """
    Defines whether "typed_name" is typed name of the "name"
    https://www.geeksforgeeks.org/check-if-a-string-is-the-typed-name-of-the-given-name/
    :param name: string, a name
    :param typed_name: a typed name of the name
    :return: True if type_named is typed name of the "name", False else
    """
    correct_index = 0
    name_length = len(name)
    for index, letter in enumerate(typed_name):
        if index > 0 and (letter != typed_name[index - 1] or letter not in 'aeiou'):
            correct_index += 1
        if name_length <= correct_index or name[correct_index] != letter:
            return False
    return True


print("is_typed_name: ", is_typed_name("alex", "aaaleex"))  # Must return True
print("is_typed_name: ", is_typed_name("alex", "aaallex"))  # Must return False


def is_prime_number(number):
    """
    Defines whether number is a prime number or not:
    Prime numbers are 2, 3, 5, 7
    :param number: an integer
    :return: True if the "number" is a prime number, False else
    """
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return False


def sort_only_composite_numbers(array):
    """
    Sort only composite numbers in the "array", prime numbers stay in the same place.
    :param array: array of integers
    :return: array on which only composite numbers are sorted
    """
    composites = sorted([n for n in array if not is_prime_number(n)])
    i = 0
    for index, number in enumerate(array):
        if is_prime_number(number):
            array[index] = number
        else:
            array[index] = composites[i]
            i += 1
    return array


print("sort_only_composite_numbers: ", sort_only_composite_numbers([23, 10, 7, 6, 6]))


def lesser_of_two_evens(former, latter):
    """
    Returns the lesser of "former" and "latter" if both of them are even numbers.
    Returns the greater of them if one or both numbers are odd numbers.
    :param former: an integer number
    :param latter: an integer number
    :return: lesser of former and latter if both of them are even numbers, else greater of them
    """
    return min(former, latter) if former % 2 == 0 and latter % 2 == 0 else max(former, latter)


print("lesser_of_two_evens: ", lesser_of_two_evens(2, 4))
print("lesser_of_two_evens: ", lesser_of_two_evens(2, 5))


def first_fourth_capitalized(word):
    """
    Capitalize only first and fourth letters of a word
    :param word: a string, one or multiple words
    :return: 'word' with first and fourth letters capitalized
    """
    old = ''
    for index, letter in enumerate(word):
        old += str(letter).capitalize() if index in [0, 3] else letter
    return old


print("first_fourth_capitalized: ", first_fourth_capitalized('macdonald'))


def mirrored_phrase(phrase):
    """
    Mirror a phrase by reversing the order of the words in it
    :param phrase: string like a phrase or sequence of words
    :return: a string with words in reversed order
    """
    words = phrase.split()
    words.reverse()
    return " ".join(words)


print("mirrored_phrase: ", mirrored_phrase("I am ready"))


def within_10_of(number):
    return True if abs(number - 100) <= 10 or abs(number - 200) <= 10 else False


print("within_10_of: ", within_10_of(90))  # True
print("within_10_of: ", within_10_of(150))  # False


def count_pattern_occurrence(pattern, string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(pattern):
            count += 1
    return count


print("count_patter_occurrence: ", count_pattern_occurrence('hah', 'hahahah'))  # 3


def paper_doll(string):
    """
    Given a string, this function returns it by multiplying 3 its every character
    :param string: a string
    :return: string on which every character is multiplied by 3
    """
    result = ''
    for letter in string:
        result += letter * 3
    return result


print("paper_doll: ", paper_doll("Hello"))

