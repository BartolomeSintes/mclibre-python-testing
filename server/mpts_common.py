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


def add_test(input, random, output, comma):
    print("    {")
    print('       "input" : [', end="")
    if len(input) == 1:
        if strType(input[0]) != "str":
            print(input[0], end="")
        else:
            print(f'"{input[0]}"', end="")
    elif len(input) > 1:
        for i in range(len(input) - 1):
            if strType(input[i]) != "str":
                print(input[i], end="")
            else:
                print(f'"{input[i]}"', end="")
            print(", ", end="")
        if strType(input[-1]) != "str":
            print(input[-1], end="")
        else:
            print(f'"{input[-1]}"', end="")
    print("],")
    print('       "random" : [', end="")
    if len(random) == 1:
        if strType(random[0]) != "str":
            print(random[0], end="")
        else:
            print(f'"{random[0]}"', end="")
    elif len(random) > 1:
        for i in range(len(random) - 1):
            if strType(random[i]) != "str":
                print(random[i], end="")
            else:
                print(f'"{random[i]}"', end="")
            print(", ", end="")
        if strType(random[-1]) != "str":
            print(random[-1], end="")
        else:
            print(f'"{random[-1]}"', end="")
    print("],")
    print('       "output" : [', end="")
    for i in range(len(output) - 1):
        print(f'"{output[i]}", ', end="")
    print(f'"{output[-1]}"', end="")
    print("]")
    if comma:
        print("    },")
    else:
        print("    }")


def generate_prime(nth):
    if nth == 1:
        return(2)
    elif nth == 2:
        return(3)
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
        return(primes[-1])
