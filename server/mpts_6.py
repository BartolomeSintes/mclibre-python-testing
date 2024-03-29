import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 61:
        # Exercise 61 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Listas fijas
        mpts_common.add_test(
            LAST_TEST,
            [
                "output",
                [
                    "LISTAS FIJAS",
                    "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]",
                    "[4, 5, 6, 7, 8, 9, 10]",
                    "[-6, -5, -4, -3, -2, -1]",
                    "[-56, -55, -54, -53, -52, -51, -50]",
                    "[1, 3, 5, 7, 9, 11, 13, 15, 17]",
                    "[-6, -4, -2, 0, 2, 4, 6, 8, 10]",
                    "[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]",
                    "[10, 9, 8, 7, 6, 5, 4]",
                    "[-50, -51, -52, -53, -54, -55, -56]",
                    "[17, 15, 13, 11, 9, 7, 5, 3, 1]",
                    "[500, 400, 300, 200, 100, 0]",
                ],
            ],
        )

        # Exercise 61 END

    elif exercise_id == 62:
        # Exercise 62 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Número negativo
        a = -random.randrange(10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LISTAS A PARTIR DE VALOR",
                    "Escriba un número entero mayor que 0: ",
                    "¡Le he pedido un número entero mayor que 0!",
                ],
            ],
        )

        # 1
        a = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LISTAS A PARTIR DE VALOR",
                    "Escriba un número entero mayor que 0: ",
                    f"{list(range(a + 1))}",
                    f"{list(range(a, -1, -1))}",
                    f"{list(range(1, a))}",
                    f"{list(range(a - 1, 0, -1))}",
                    f"{list(range(a)) + list(range(a, -1, -1))}",
                ],
            ],
        )

        # > 1
        a = random.randrange(2, 11)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LISTAS A PARTIR DE VALOR",
                    "Escriba un número entero mayor que 0: ",
                    f"{list(range(a + 1))}",
                    f"{list(range(a, -1, -1))}",
                    f"{list(range(1, a))}",
                    f"{list(range(a - 1, 0, -1))}",
                    f"{list(range(a)) + list(range(a, -1, -1))}",
                ],
            ],
        )

        # Exercise 62 END

    elif exercise_id == 63:
        # Exercise 63 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Cero
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [0]],
            [
                "output",
                ["LISTAS DESDE CERO HASTA VALOR", "Escriba un número entero: ", "[0]"],
            ],
        )

        # Número positivo
        a = random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LISTAS DESDE CERO HASTA VALOR",
                    "Escriba un número entero: ",
                    f"{list(range(0, a + 1))}",
                ],
            ],
        )

        # Número negativo
        a = -random.randrange(1, 20)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LISTAS DESDE CERO HASTA VALOR",
                    "Escriba un número entero: ",
                    f"{list(range(0, a - 1, -1))}",
                ],
            ],
        )

        # Exercise 63 END

    elif exercise_id == 64:
        # Exercise 64 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Números iguales
        a = random.randrange(0, 20)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"¡Le he pedido un número mayor que {a}!",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos positivos
        a = random.randrange(10, 20)
        b = a - random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"¡Le he pedido un número mayor que {a}!",
                ],
            ],
        )

        # Segundo número menor que el primero, positivo y negativo
        a = random.randrange(1, 20)
        b = -random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"¡Le he pedido un número mayor que {a}!",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos negativos
        a = -random.randrange(0, 20)
        b = a - random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"¡Le he pedido un número mayor que {a}!",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos positivos
        a = random.randrange(0, 10)
        b = a + random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"{list(range(a, b + 1))}",
                    f"{list(range(b - 1, a - 1, -1))}",
                    f"{list(range(a + 1, b + 2))}",
                    f"{list(range(b - 1, a, -1))}",
                    f"{list(range(a, b)) + list(range(b, a - 1, -1))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, negativo y postivo
        a = -random.randrange(1, 10)
        b = a + random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"{list(range(a, b + 1))}",
                    f"{list(range(b - 1, a - 1, -1))}",
                    f"{list(range(a + 1, b + 2))}",
                    f"{list(range(b - 1, a, -1))}",
                    f"{list(range(a, b)) + list(range(b, a - 1, -1))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos negativos
        a = -random.randrange(11, 20)
        b = a + random.randrange(1, 10)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTAS ENTRE DOS NÚMEROS",
                    "Escriba un número entero: ",
                    f"Escriba un número entero mayor que {a}: ",
                    f"{list(range(a, b + 1))}",
                    f"{list(range(b - 1, a - 1, -1))}",
                    f"{list(range(a + 1, b + 2))}",
                    f"{list(range(b - 1, a, -1))}",
                    f"{list(range(a, b)) + list(range(b, a - 1, -1))}",
                ],
            ],
        )

        # Exercise 64 END

    elif exercise_id == 65:
        # Exercise 65 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Números iguales
        a = random.randrange(0, 20)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"[{a}]",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos positivos
        a = random.randrange(11, 20)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b - 1, -1))}",
                ],
            ],
        )

        # Segundo número menor que el primero, positivo y negativo
        a = random.randrange(1, 11)
        b = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b - 1, -1))}",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos negativos
        a = -random.randrange(1, 11)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b - 1, -1))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos positivos
        a = random.randrange(0, 11)
        b = a + random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b + 1))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, negativo y positivo
        a = -random.randrange(1, 11)
        b = random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b + 1))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos negativos
        a = -random.randrange(11, 21)
        b = a + random.randrange(1, 11)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE UN VALOR A OTRO",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b + 1))}",
                ],
            ],
        )

        # Exercise 65 END

    elif exercise_id == 66:
        # Exercise 66 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Números iguales
        a = random.randrange(0, 20)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    "[]",
                ],
            ],
        )

        # Uno de diferencia
        a = random.randrange(-20, 20)
        b = a + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    "[]",
                ],
            ],
        )

        # Uno de diferencia
        a = random.randrange(-20, 20)
        b = a - 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    "[]",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos positivos
        a = random.randrange(11, 20)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(b + 1, a))}",
                ],
            ],
        )

        # Segundo número menor que el primero, positivo y negativo
        a = random.randrange(1, 11)
        b = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(b + 1, a))}",
                ],
            ],
        )

        # Segundo número menor que el primero, ambos negativos
        a = -random.randrange(1, 11)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(b + 1, a))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos positivos
        a = random.randrange(0, 11)
        b = a + random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(a + 1, b))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, negativo y positivo
        a = -random.randrange(1, 11)
        b = random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(a + 1, b))}",
                ],
            ],
        )

        # Segundo número mayor que el primero, ambos negativos
        a = -random.randrange(11, 21)
        b = a + random.randrange(1, 11)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LISTA DE MENOR A MAYOR",
                    "Escriba un número entero: ",
                    "Escriba otro número entero: ",
                    f"{list(range(a + 1, b))}",
                ],
            ],
        )

        # Exercise 66 END

    elif exercise_id == 67:
        # Exercise 67 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Cantidad negativa
        a = random.randrange(0, 20)
        b = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "VALORES CONSECUTIVOS",
                    "Escriba el número entero inicial: ",
                    "Escriba cuántos valores quiere: ",
                    "¡La cantidad de valores no puede ser negativa!",
                ],
            ],
        )

        # Cantidad nula
        a = random.randrange(-20, 20)
        b = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "VALORES CONSECUTIVOS",
                    "Escriba el número entero inicial: ",
                    "Escriba cuántos valores quiere: ",
                    f"{list(range(a, a + b))}",
                ],
            ],
        )

        # Cantidad positiva (1)
        a = random.randrange(-20, 20)
        b = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "VALORES CONSECUTIVOS",
                    "Escriba el número entero inicial: ",
                    "Escriba cuántos valores quiere: ",
                    f"{list(range(a, a + b))}",
                ],
            ],
        )

        # Cantidad positiva, inicio negativo
        a = random.randrange(-20, 0)
        b = random.randrange(2, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "VALORES CONSECUTIVOS",
                    "Escriba el número entero inicial: ",
                    "Escriba cuántos valores quiere: ",
                    f"{list(range(a, a + b))}",
                ],
            ],
        )

        # Cantidad positiva, inicio positivo
        a = random.randrange(0, 21)
        b = random.randrange(2, 11)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "VALORES CONSECUTIVOS",
                    "Escriba el número entero inicial: ",
                    "Escriba cuántos valores quiere: ",
                    f"{list(range(a, a + b))}",
                ],
            ],
        )

        # Exercise 67 END

    elif exercise_id == 68:
        # Exercise 68 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Segundo menor que el primero (positivo)
        a = random.randrange(0, 21)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¡El número final debe ser mayor que el inicial!",
                ],
            ],
        )

        # Segundo menor que el primero (negativo)
        a = -random.randrange(1, 21)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¡El número final debe ser mayor que el inicial!",
                ],
            ],
        )

        # Iguales (pares)
        a = 2 * random.randrange(-20, 21)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{[a]}",
                ],
            ],
        )

        # Iguales (impares)
        a = 2 * random.randrange(-20, 21) + 1
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{[]}",
                ],
            ],
        )

        # par par
        a = 2 * random.randrange(-20, 21)
        b = a + 2 * random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b + 1, 2))}",
                ],
            ],
        )

        # par impar
        a = 2 * random.randrange(-20, 21)
        b = a + 2 * random.randrange(1, 11) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a, b + 1, 2))}",
                ],
            ],
        )

        # impar par
        a = 2 * random.randrange(-20, 21) + 1
        b = a + 2 * random.randrange(1, 11) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a + 1, b + 1, 2))}",
                ],
            ],
        )

        # impar impar
        a = 2 * random.randrange(-20, 21) + 1
        b = a + 2 * random.randrange(1, 11)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PARES ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    f"{list(range(a + 1, b + 1, 2))}",
                ],
            ],
        )

        # Exercise 68 END

    elif exercise_id == 69:
        # Exercise 69 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html

        # Segundo menor que el primero (positivo)
        a = random.randrange(0, 21)
        b = a - random.randrange(1, 21)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¡El número final debe ser mayor que el inicial!",
                ],
            ],
        )

        # Segundo menor que el primero (negativo)
        a = -random.randrange(1, 21)
        b = a - random.randrange(1, 21)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¡El número final debe ser mayor que el inicial!",
                ],
            ],
        )

        # Tercero nulo
        a = random.randrange(-20, 21)
        b = a + random.randrange(1, 21)
        c = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    "¡Los múltiplos deben ser de un número entero mayor que cero!",
                ],
            ],
        )

        # Tercero negativo
        a = random.randrange(-20, 21)
        b = a + random.randrange(1, 21)
        c = -random.randrange(1, 21)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    "¡Los múltiplos deben ser de un número entero mayor que cero!",
                ],
            ],
        )

        # Sin múltiplo
        c = random.randrange(20, 50)
        t = c * random.randrange(1, 3)
        a = t + random.randrange(1, c // 2)
        b = random.randrange(a, t + c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay 0 múltiplos de {c}:",
                    "[]",
                ],
            ],
        )

        # Con un múltiplo (no inicial)
        c = random.randrange(10, 20)
        t = c * random.randrange(1, 3)
        a = t + random.randrange(1, c)
        b = random.randrange(t + c, a + c)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay 1 múltiplos de {c}:",
                    f"{[t + c]}",
                ],
            ],
        )

        # Con un múltiplo (inicial)
        c = random.randrange(10, 20)
        t = c * random.randrange(1, 3)
        a = t
        b = random.randrange(a + 1, a + c)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay 1 múltiplos de {c}:",
                    f"{[a]}",
                ],
            ],
        )

        # Varios múltiplos (no inicial)
        c = random.randrange(10, 20)
        t = c * random.randrange(1, 3)
        a = t + random.randrange(1, c)
        n = random.randrange(2, 10)
        b = random.randrange(t + n * c, a + n * c)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay {n} múltiplos de {c}:",
                    f"{list(range(t + c, t + n * c + 1, c))}",
                ],
            ],
        )

        # Varios múltiplos (inicial)
        c = random.randrange(10, 20)
        t = c * random.randrange(1, 3)
        a = t
        n = random.randrange(2, 10)
        b = random.randrange(t + n * c - c, t + n * c)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay {n} múltiplos de {c}:",
                    f"{list(range(t, t + n * c, c))}",
                ],
            ],
        )

        # Varios múltiplos (inicial y final)
        c = random.randrange(10, 20)
        t = c * random.randrange(1, 3)
        a = t
        n = random.randrange(2, 10)
        b = t + (n - 1) * c

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÚLTIPLOS ENTRE VALORES",
                    "Escriba el número entero inicial: ",
                    "Escriba el número entero final: ",
                    "¿De qué número quiere los múltiplos?: ",
                    f"Entre {a} y {b} hay {n} múltiplos de {c}:",
                    f"{list(range(t, t + n * c, c))}",
                ],
            ],
        )

        # Exercise 69 END
