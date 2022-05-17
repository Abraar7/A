""" 2.py: Question 2 """

__author__ = "Abraar Masud Nafiz"
__email__ = "abraar.codes@protonmail.com"
__copyright__ = "MIT License, (c) 2022 Abraar7"
__status__ = "Finished"


def dotProduct(x: list, y: list) -> float:
    """
    Calculates the Dot product of two vectors, which is the sum of the products of corresponding components.
    Arguments:
        x: vector (list)
        y: vector (list)
        (Vector is a single one-dimension array of lists)
    Returns:
        The Dot Product of the vectors.
    """
    return sum([i * j for (i, j) in zip(x, y)])


if __name__ == '__main__':
    list1 = [5, -3, 9]
    list2 = [1, 2, 6]
    print(dotProduct(list1, list2))
