# 1. Creating your first test case
# There is an implementation for get_divisible_by_five function in the cell below.
# Your task is to create a test case for this function to verify that it works
# correctly.

def get_divisible_by_five(numbers):
    """Returns a list of numbers which are divisible by five in the list got as an argument"""
    result = []
    for num in numbers:
        if not num % 5:
            result.append(num)

    return result


def test_get_divisible_by_five():
    assert (get_divisible_by_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                   14, 15, 16, 17, 18, 19, 20]) == [5, 10, 15,
                                                                    20])
