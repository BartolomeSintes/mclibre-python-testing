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


def add_test(comma, *args):
    print("    {")
    for i in args:
        # print()
        # print(i)
        # print()
        print(f'       "{i[0]}" : [', end="")
        if len(i[1]) == 1:
            if strType(i[1][0]) != "str":
                print(i[1][0], end="")
            else:
                print(f'"{i[1][0]}"', end="")
        elif len(i[1]) > 1:
            for j in range(len(i[1]) - 1):
                if strType(i[1][j]) != "str":
                    print(i[1][j], end="")
                else:
                    print(f'"{i[1][j]}"', end="")
                print(", ", end="")
            if strType(i[1][-1]) != "str":
                print(i[1][-1], end="")
            else:
                print(f'"{i[1][-1]}"', end="")
        print("],")
    if comma:
        print("    },")
    else:
        print("    }")


numero_1 = random.randrange(0, 20)
numero_2 = random.randrange(0, 20)
resultado = (numero_1 + numero_2) / 2
add_test(
    NOT_LAST_TEST,
    ["input", [numero_1, numero_2]],
    [
        "ouput",
        [
            "CÁLCULO DE LA MEDIA DE DOS NÚMEROS",
            "Escriba un número: ",
            "Escriba otro número: ",
            f"La media aritmética de {str(float(numero_1))} y {str(float(numero_2))} es {str(resultado)}",
        ],
    ],
)

