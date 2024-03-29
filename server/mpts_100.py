import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 1001:
        # Exercise 1001 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # Comprueba salida
        mpts_common.add_test(LAST_TEST, ["output", ["¡Hola, mundo!"]])
        # Exercise 1001 END

    elif exercise_id == 1002:
        # Exercise 1002 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # Comprueba salida
        mpts_common.add_test(
            LAST_TEST, ["output", ["SALUDANDO", "¡Hola, mundo!", "¡Adiós, amigo!"]]
        )

        # Exercise 1002 END

    elif exercise_id == 1003:
        # Exercise 1003 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # número pequeño
        numero = random.randrange(0, 10)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero]],
            [
                "output",
                [
                    "ESCRIBA NÚMERO",
                    "Escriba un número entero: ",
                    f"Ha escrito el número {numero}.",
                ],
            ],
        )

        # número negativo
        numero = random.randrange(-100, 0)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [numero]],
            [
                "output",
                [
                    "ESCRIBA NÚMERO",
                    "Escriba un número entero: ",
                    f"Ha escrito el número {numero}.",
                ],
            ],
        )

        # Exercise 1003 END

    elif exercise_id == 1004:
        # Exercise 1004 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        a = random.randrange(0, 100) / 10
        b = random.randrange(0, 100) / 10
        c = a + b

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "SUMA NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{a} + {b} = {c}",
                ],
            ],
        )

        # Exercise 1004 END

    elif exercise_id == 1005:
        # Exercise 1005 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # números crecientes
        a = random.randrange(0, 1000)
        b = random.randrange(10 * a, 20000) / 10

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "NÚMEROS CRECIENTES",
                    "Escriba un número: ",
                    "Escriba otro número más grande: ",
                    "Gracias por su colaboración.",
                ],
            ],
        )

        # números decrecientes
        a = random.randrange(100, 1000) / 10
        b = random.randrange(0, round(a) - 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "NÚMEROS CRECIENTES",
                    "Escriba un número: ",
                    "Escriba otro número más grande: ",
                    "¡Le he pedido un número más grande!",
                ],
            ],
        )

        # números iguales
        a = random.randrange(0, 1000)
        b = a

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "NÚMEROS CRECIENTES",
                    "Escriba un número: ",
                    "Escriba otro número más grande: ",
                    "¡Le he pedido un número más grande!",
                ],
            ],
        )
        # Exercise 1005 END

    elif exercise_id == 1006:
        # Exercise 1006 BEGINNING

        # número pequeño
        a = random.randrange(1, 7)

        mpts_common.add_test(
            LAST_TEST,
            ["random", [a]],
            ["output", ["TIRADA DE DADO", f"Ha salido un {a}."]],
        )

        # Exercise 1006 END

    elif exercise_id == 1007:
        # Exercise 1007 BEGINNING

        # Negros
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["choice", ["Negros"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido Negros."]],
        )

        # Rojos
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["choice", ["Rojos"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido Rojos."]],
        )

        # J
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["choice", ["J"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido J."]],
        )

        # Q
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["choice", ["Q"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido Q."]],
        )

        # K
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["choice", ["K"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido K."]],
        )

        # As
        mpts_common.add_test(
            LAST_TEST,
            ["choice", ["As"]],
            ["output", ["TIRADA DE DADO DE PÓKER", "Ha salido As."]],
        )

        # Exercise 1006 END

    elif exercise_id == 1008:
        # Exercise 1007 BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # letra fija
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", ["a"]],
            [
                "output",
                ["ESCRIBA LETRA", "Escriba una letra: ", "Ha escrito la letra a."],
            ],
        )

        # letra
        letra = random.choice(["a", "b", "c", "d"])

        mpts_common.add_test(
            LAST_TEST,
            ["input", [letra]],
            [
                "output",
                [
                    "ESCRIBA LETRA",
                    "Escriba una letra: ",
                    f"Ha escrito la letra {letra}.",
                ],
            ],
        )

        # Exercise 1007 END

    elif exercise_id == 1009:
        # Exercise 10078BEGINNING
        # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html

        # 2 segundos
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", ["", ""]],
            ["time", [1.0, 3.0]],
            [
                "output",
                [
                    "CRONÓMETRO",
                    "Pulse Intro para empezar a contar el tiempo: ",
                    "Pulse Intro para terminar de contar el tiempo: ",
                    "Han pasado 2.0 s.",
                ],
            ],
        )

        # segundos
        a = random.randrange(10, 1000)
        b = random.randrange(a + 100, 2000)
        mpts_common.add_test(
            LAST_TEST,
            ["input", ["", ""]],
            ["time", [a / 10, b / 10]],
            [
                "output",
                [
                    "CRONÓMETRO",
                    "Pulse Intro para empezar a contar el tiempo: ",
                    "Pulse Intro para terminar de contar el tiempo: ",
                    f"Han pasado {round((b-a)/10, 1)} s.",
                ],
            ],
        )

        # Exercise 1009 END
