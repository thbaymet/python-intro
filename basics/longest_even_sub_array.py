# Exercise taken from
# https://www.geeksforgeeks.org/length-of-the-longest-subarray-with-only-even-elements/

"""Given an array arr[].
    The task is to find the length of the longest sub-array of arr[]
    such that it contains only even elements."""


def max_even_sub_array(an_array):
    """Given an array arr[].
    Return the max length of the sub-arrays
    of an_array composed only even numbers contiguous """
    ans = 0
    current_count = 0
    for i in an_array:
        if i % 2 == 0:
            current_count += 1
        else:
            ans = max(ans, current_count)
            current_count = 0
    return ans


array = [9, 8, 5, 4, 4, 4, 2, 4, 1]
max_len = max_even_sub_array(array)
print(array)
print(max_len)
