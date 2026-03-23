"""
    This the module docstring
"""

print("Hello world")


def fizz_buzz(i):
    """
    This is the function doctstring
    """
    if i % 15 == 0:
        return "fizz_buzz"
    if i % 3 == 0:
        return "fizz"
    if i % 5 == 0:
        return "buzz"
    return i
