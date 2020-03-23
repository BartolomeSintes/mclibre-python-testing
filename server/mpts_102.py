import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False

# Estas pruebas no son de ejercicios. Son ejemplos para probar programas incorrectos y ver
# que MPTC da mensajes coherentes.


def exercise(exercise_id):

    if exercise_id == 1021:
        # Pide un número entero, un número decimal y una palabra
        n = random.randrange(1, 100)
        d = random.randrange(1, 10000) / 100.0
        letras = "abcdefeghijklmnñopqrstuvwxyz "
        t = ""
        for _ in range(random.randrange(10, 30)):
            t += letras[random.randrange(len(letras))]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [n, d, t]],
            [
                "output",
                [
                    "MPTC 1021",
                    "Escriba un número entero: ",
                    "Escriba un número decimal: ",
                    "Escriba texto: ",
                    f"Ha escrito el número {n}",
                    f"Ha escrito el número {d}",
                    f"Ha escrito el texto {t}",
                ],
            ],
        )

        # Exercise 1021 END

    elif exercise_id == 1022:
        # Pide un número entero, un número decimal y una palabra
        n = random.randrange(1, 100)
        d = random.randrange(1, 10000) / 100.0
        letras = "abcdefeghijklmnñopqrstuvwxyz "
        t = ""
        for _ in range(random.randrange(10, 30)):
            t += letras[random.randrange(len(letras))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, d, t]],
            [
                "output",
                [
                    "MPTC 1021",
                    "Escriba un número entero: ",
                    "Escriba un número decimal: ",
                    "Escriba texto: ",
                    f"Ha escrito el número {n}",
                    f"Ha escrito el número {d}",
                    f"Ha escrito el texto {t}",
                ],
            ],
        )

        # Pide un número entero, un número decimal y una palabra
        n = random.randrange(1, 100)
        d = random.randrange(1, 10000) / 100.0
        letras = "abcdefeghijklmnñopqrstuvwxyz "
        t = ""
        for _ in range(random.randrange(10, 30)):
            t += letras[random.randrange(len(letras))]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [n, d, t]],
            [
                "output",
                [
                    "MPTC 1021",
                    "Escriba un número entero: ",
                    "Escriba un número decimal: ",
                    "Escriba texto: ",
                    f"Ha escrito el número {n}",
                    f"Ha escrito el número {d}",
                    f"Ha escrito el texto {t}",
                ],
            ],
        )

        # Exercise 1022 END

    elif exercise_id == 1023:
        # Pide un número entero, un número decimal y una palabra
        n = random.randrange(1, 100)
        d = random.randrange(1, 10000) / 100.0
        letras = "abcdefeghijklmnñopqrstuvwxyz "
        t = ""
        for _ in range(random.randrange(10, 30)):
            t += letras[random.randrange(len(letras))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, d, t]],
            [
                "output",
                [
                    "MPTC 1021",
                    "Escriba un número entero: ",
                    "Escriba un número decimal: ",
                    "Escriba texto: ",
                    f"Ha escrito el número {n}",
                    f"Ha escrito el número {d}",
                    f"Ha escrito el texto {t}",
                ],
            ],
        )

        # Pide un número entero, un número decimal y una palabra
        n = random.randrange(1, 100)
        d = random.randrange(1, 10000) / 100.0
        letras = "abcdefeghijklmnñopqrstuvwxyz "
        t = ""
        for _ in range(random.randrange(10, 30)):
            t += letras[random.randrange(len(letras))]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [n, d, t]],
            [
                "output",
                [
                    "MPTC 1021 VA A FALLAR",
                    "Escriba un número entero: ",
                    "Escriba un número decimal: ",
                    "Escriba texto: ",
                    f"Ha escrito el número {n}",
                    f"Ha escrito el número {d}",
                    f"Ha escrito el texto {t}",
                ],
            ],
        )

        # Exercise 1023 END
