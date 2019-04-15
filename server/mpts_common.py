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
