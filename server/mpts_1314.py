import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):

    if exercise_id == 131422:
        # Exercise 131422 BEGINNING
        # /examenes/13-14/examen-140307.html

        # Número de valores negativo
        n = -random.randrange(1, 100)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["output", ["¿Cuántos valores va a introducir? ", "¡Imposible!",],],
        )

        # Cero valores
        n = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["output", ["¿Cuántos valores va a introducir? ", "¡Imposible!",],],
        )

        # Un valor
        n = 1
        v = random.randrange(1, 1000) / 10

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, v]],
            [
                "output",
                [
                    "¿Cuántos valores va a introducir? ",
                    "Escriba el número 1: ",
                    f"El producto de los números que ha escrito es {v}",
                    f"La media geométrica de los números que ha escrito es {v}",
                ],
            ],
        )

        # Varios valores, puede haber algún cero
        n = random.randrange(2, 20)
        v = [n]
        producto = 1
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
        ]
        for i in range(1, n + 1):
            valor = random.randrange(0, 100) / 10
            producto = producto * valor
            v += [valor]
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += [
            f"El producto de los números que ha escrito es {producto}",
            f"La media geométrica de los números que ha escrito es {round(producto**(1/n), 1)}",
        ]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # Varios valores, sin ceros
        n = random.randrange(2, 20)
        v = [n]
        producto = 1
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
        ]
        for i in range(1, n + 1):
            valor = random.randrange(1, 100) / 10
            producto = producto * valor
            v += [valor]
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += [
            f"El producto de los números que ha escrito es {producto}",
            f"La media geométrica de los números que ha escrito es {round(producto**(1/n), 1)}",
        ]

        mpts_common.add_test(
            LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # Exercise 131422 END
