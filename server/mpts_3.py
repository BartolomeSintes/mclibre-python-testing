import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 31:
        # Exercise 31 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios//ej-if-else-1.html

        # par, impar
        par = 2 * random.randrange(-20, 20)
        impar = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [par, impar]],
            [
                "output",
                [
                    "PAR E IMPAR (1)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "¡Gracias por su colaboración!",
                ],
            ],
        )

        # par, par
        par_1 = 2 * random.randrange(-20, 20)
        par_2 = 2 * random.randrange(-20, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [par_1, par_2]],
            [
                "output",
                [
                    "PAR E IMPAR (1)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "Uno o más de los valores que ha escrito no son correctos.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # par, par
        impar_1 = 2 * random.randrange(-20, 20) + 1
        impar_2 = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [impar_1, impar_2]],
            [
                "output",
                [
                    "PAR E IMPAR (1)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "Uno o más de los valores que ha escrito no son correctos.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # par, par
        par = 2 * random.randrange(-20, 20)
        impar = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            LAST_TEST,
            ["input", [impar, par]],
            [
                "output",
                [
                    "PAR E IMPAR (1)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "Uno o más de los valores que ha escrito no son correctos.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # Exercise 31 END

    elif exercise_id == 32:
        # Exercise 32 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios//ej-if-else-1.html

        # par, impar
        par = 2 * random.randrange(-20, 20)
        impar = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [par, impar]],
            [
                "output",
                [
                    "PAR E IMPAR (2)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "¡Gracias por su colaboración!",
                ],
            ],
        )

        # impar
        impar = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [impar]],
            [
                "output",
                [
                    "PAR E IMPAR (2)",
                    "Escriba un número par: ",
                    "No ha escrito un número par.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # par, par
        par_1 = 2 * random.randrange(-20, 20)
        par_2 = 2 * random.randrange(-20, 20)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [par_1, par_2]],
            [
                "output",
                [
                    "PAR E IMPAR (2)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "No ha escrito un número impar.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # Exercise 32 END

    elif exercise_id == 33:
        # Exercise 33 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios//ej-if-else-1.html

        # par, impar
        par = 2 * random.randrange(-20, 20)
        impar = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [par, impar]],
            [
                "output",
                [
                    "PAR E IMPAR (3)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "¡Gracias por su colaboración!",
                ],
            ],
        )

        # impar, impar
        impar_1 = 2 * random.randrange(-20, 20) + 1
        impar_2 = 2 * random.randrange(-20, 20) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [impar_1, impar_2]],
            [
                "output",
                [
                    "PAR E IMPAR (3)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "No ha escrito un número par.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # impar, par
        impar = 2 * random.randrange(-20, 20) + 1
        par = 2 * random.randrange(-20, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [impar, par]],
            [
                "output",
                [
                    "PAR E IMPAR (3)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "No ha escrito un número par.",
                    "No ha escrito un número impar.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # par, par
        par_1 = 2 * random.randrange(-20, 20)
        par_2 = 2 * random.randrange(-20, 20)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [par_1, par_2]],
            [
                "output",
                [
                    "PAR E IMPAR (3)",
                    "Escriba un número par: ",
                    "Escriba un número impar: ",
                    "No ha escrito un número impar.",
                    "Ejecute de nuevo el programa para volver a intentarlo.",
                ],
            ],
        )

        # Exercise 33 END

