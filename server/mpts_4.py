import random

NOT_LAST_TEST = True
LAST_TEST = False


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


def exercise(exercise_id):
    if exercise_id == 50:
        # Exercise 50 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-mas-1.html

        # Empate
        a = random.randrange(1, 7)
        b = a
        add_test(
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # gana Alberto
        a = random.randrange(2, 7)
        b = a - random.randrange(1, a)
        add_test(
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Ha ganado Alberto.",
            ],
            NOT_LAST_TEST,
        )

        # gana Bárbara
        a = random.randrange(1, 6)
        b = random.randrange(a + 1, 7)
        add_test(
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Ha ganado Bárbara.",
            ],
            LAST_TEST,
        )

        # Exercise 33 END
