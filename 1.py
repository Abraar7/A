""" 1.py: Question 1 """

__author__ = "Abraar Masud Nafiz"
__email__ = "abraar.codes@protonmail.com"
__copyright__ = "MIT License, (c) 2022 Abraar7"
__status__ = "Finished"


def countBits(n: int) -> int:
    """
    Counts number of bits set to 1 in binary representation of a positive integer.
    Arguments:
        n: a positive integer
    Returns:
        Returns the count of bits set to 1 in a positive integer
    """
    numStr = str(bin(n))
    return numStr.count('1')


def countBits2(n: int) -> int:
    """
    Counts number of bits set to 1 in binary representation of a positive integer.
    Arguments:
        n: a positive integer
    Returns:
        Returns the count of bits set to 1 in a positive integer
    """
    numStr = str(bin(n))
    return sum(map(lambda x: 1 if '1' in x else 0, numStr))


if __name__ == '__main__':

    nums = [11, 12, 13, 14, 15, 16]

    for num in nums:
        print(f"The Binary of {num} has {countBits(num)} bits set to 1")
        print(f"The Binary of {num} has {countBits2(num)} bits set to 1")
