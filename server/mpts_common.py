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
