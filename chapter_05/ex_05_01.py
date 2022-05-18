# 05.01 | 176 | Create and test a function; then reads your __doc__ and checks its type

def factorial(n):
    """Returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# print(factorial(5))
# print(factorial.__doc__)
# print(type(factorial.__doc__))
