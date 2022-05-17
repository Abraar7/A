""" 4.py: Question 4 """

__author__ = "Abraar Masud Nafiz"
__email__ = "abraar.codes@protonmail.com"
__copyright__ = "MIT License, (c) 2022 Abraar7"
__status__ = "Finished"


def is_valid(n: int) -> bool:
    """
    Checks whether a 16-digit number represents a valid credit card number.
    Arguments:
        n: a 16-digit positive integer
    Returns:
        True or False
    """
    checksum = 0
    digits = [int(d) for d in str(n)]
    odds, evens = digits[-1::-2], digits[-2::-2]
    checksum += sum(odds)
    for d in evens:
        checksum += sum([int(d) for d in str(d * 2)])
    result = checksum % 10 == 0
    print(f"For card {card}, checksum is {checksum}")
    return result


if __name__ == "__main__":

    cards = [4111111111111111, 4111111111111178, 4532015112830366, 6011514433546201, 6771549495586802]

    for card in cards:
        if is_valid(card):
            print(f"Number {card} is Valid")
        else:
            print(f"Number {card} is Invalid")
