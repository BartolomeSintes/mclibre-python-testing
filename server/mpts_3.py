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
    if exercise_id == 32:
        # Exercise 32 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-mas-1.html

        # dia == 0
        dia = 0
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # dia < 0
        dia = - random.randrange(1, 29)
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # dia >= 32
        dia = random.randrange(32, 50)
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # mes == 0
        dia = random.randrange(1, 29)
        mes = 0
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # mes < 0
        dia = random.randrange(1, 29)
        mes = - random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # mes >= 13
        dia = random.randrange(1, 29)
        mes = random.randrange(13, 20)
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 31 de mes con 31 días
        dia = 31
        mes = random.choice([1, 3, 5, 7, 8, 10, 12])
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 31 de mes con menos de 31 días
        dia = 31
        mes = random.choice([2, 4, 6, 9, 11])
        anyo = random.randrange(1583, 5000)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 29 febrero múltiplo de 400
        dia = 29
        mes = 2
        anyo = random.randrange(1600, 5000, 400)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 29 febrero múltiplo de 100 (no de 400)
        dia = 29
        mes = 2
        anyo = 1600 + 400 * random.randrange(0, 11) + 100 * random.randrange(1, 4)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 29 febrero múltiplo de 4 (no de 100)
        dia = 29
        mes = 2
        anyo = 1600 + 100 * random.randrange(0, 5) + 4 * random.randrange(1, 25)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} existe",
            ],
            NOT_LAST_TEST,
        )

        # dia 29 febrero no múltiplo de 4
        dia = 29
        mes = 2
        anyo = 1584 + 4 * random.randrange(0, 150) + random.randrange(1, 4)
        add_test(
            [dia, mes, anyo],
            [
                "COMPROBACIÓN DE FECHA",
                "Escriba el número de día: ",
                "Escriba el número de mes: ",
                "Escriba el número de año: ",
                f"El día {dia} del mes {mes} del año {anyo} no existe",
            ],
            LAST_TEST,
        )

        # Exercise 32 END

    if exercise_id == 33:
        # Exercise 33 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-mas-1.html

        # dia == 0
        opcion = "c"
        add_test(
            [opcion],
            [
                "GALONES Y PINTAS",
                "",
                "Este programa permite:",
                "a. Convertir litros en galones y pintas.",
                "b. Convertir galones y pintas en litros",
                "Elija una opción: ",
                "Debe escribir a o b.",
                "Programa terminado",
            ],
            LAST_TEST,
        )

        # Exercise 33 END
