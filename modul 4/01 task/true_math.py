from math import inf


def divide(first, second):
    if second == 0:
        return inf
    res = first / second
    return res


print(divide(4, 0))
