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


def add_test(input, output, comma):
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
    print('       "output" : [', end="")
    for i in range(len(output) - 1):
        print(f'"{output[i]}", ', end="")
    print(f'"{output[-1]}"', end="")
    print("]")
    if comma:
        print("    },")
    else:
        print("    }")

