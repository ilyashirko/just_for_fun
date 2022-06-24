# Write a function that takes a non-negative integer
# and displays the number of ones in its binary representation

from math import log2


def count_ones(number: int) -> int:
    degree = int(log2(number))
    two2power = 2 ** degree
    if two2power == number:
        return 1
    else:
        return 1 + count_ones(number - two2power)
