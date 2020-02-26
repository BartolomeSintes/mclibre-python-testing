def strType(var):
    try:
        if int(var) == float(var):
            return "int"
    except:
        try:
            float(var)
            return "float"
        except:
            return "str"


def add_test(comma, *args):
    print("    {")
    for i in range(len(args)):
        # print()
        # print(i)
        # print()
        print(f'       "{args[i][0]}" : [', end="")
        if len(args[i][1]) == 1:
            if strType(args[i][1][0]) != "str":
                print(args[i][1][0], end="")
            else:
                print(f'"{args[i][1][0]}"', end="")
        elif len(args[i][1]) > 1:
            for j in range(len(args[i][1]) - 1):
                if strType(args[i][1][j]) != "str":
                    print(args[i][1][j], end="")
                else:
                    print(f'"{args[i][1][j]}"', end="")
                print(", ", end="")
            if strType(args[i][1][-1]) != "str":
                print(args[i][1][-1], end="")
            else:
                print(f'"{args[i][1][-1]}"', end="")
        if i == len(args) - 1:
            print("]")
        else:
            print("],")
    if comma:
        print("    },")
    else:
        print("    }")


def generate_prime(nth):
    if nth == 1:
        return 2
    elif nth == 2:
        return 3
    else:
        primes = [2, 3]
        while len(primes) < nth:
            is_prime = False
            n = primes[-1] + 2
            while is_prime == False:
                is_prime = True
                for i in primes:
                    if n % i == 0:
                        is_prime = False
                if is_prime == False:
                    n += 2
            primes += [n]
        return primes[-1]


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def generate_date():
    import datetime
    import random

    year = random.randrange(1583, 2100)
    month = random.randrange(1, 13)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randrange(1, 32)
    elif month in [4, 6, 9, 11]:
        day = random.randrange(1, 31)
    elif leap_year(year):
        day = random.randrange(1, 30)
    else:
        day = random.randrange(1, 29)
    return (year, month, day)


def hsl_2_rgb(h, s, l):
    import math

    # does not check 0 <= h <= 360, 0 <= s <= 1, 0 <= l <= 1
    c = (1 - abs(2 * l - 1)) * s
    h2 = h / 60
    x = c * (1 - abs(h2 % 2 - 1))
    h3 = math.ceil(h2)

    if h3 == 1:
        r, g, b = c, x, 0
    elif h3 == 2:
        r, g, b = x, c, 0
    elif h3 == 3:
        r, g, b = 0, c, x
    elif h3 == 4:
        r, g, b = 0, x, c
    elif h3 == 5:
        r, g, b = x, 0, c
    elif h3 == 6:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0

    m = l - c / 2

    r = round(255 * (r + m))
    g = round(255 * (g + m))
    b = round(255 * (b + m))

    return r, g, b

