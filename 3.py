""" 3.py: Question 3 """

__author__ = "Abraar Masud Nafiz"
__email__ = "abraar.codes@protonmail.com"
__copyright__ = "MIT License, (c) 2022 Abraar7"
__status__ = "Finished"


def myfunc(n: int) -> int:
    """
    Implements a recursive function defined in the question.
    Arguments:
        n: a positive integer
    Returns:
        1 for the base case, otherwise 1 + myfunc(n - 1)
    """
    return 1 if n == 1 else 1 + myfunc(n - 1)


if __name__ == '__main__':
    print(f"The result of f(5) is {myfunc(5)}")
