import mpts_common
import datetime
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):

    if exercise_id == 111221:
        # Exercise 111221 BEGINNING
        # /examenes/11-12/examen-120601-2.html

        # Valor negativo
        a = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["¿Cuántos valores va a introducir? ", "¡Imposible!",],],
        )

        # Cero
        a = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["¿Cuántos valores va a introducir? ", "¡Imposible!",],],
        )

        # 1
        a = 1
        b = random.randrange(-100, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "¿Cuántos valores va a introducir? ",
                    "Escriba un número: ",
                    "Gracias por su colaboración",
                ],
            ],
        )

        # Ningún número igual
        n = random.randrange(1, 11)
        todos = list(range(-100, 100))
        num = random.sample(todos, n)
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(n - 1):
            tmp_output += [f"Escriba un número distinto de {num[i]}: "]
        num = [n] + num
        tmp_output += ["Gracias por su colaboración"]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Un número igual que el anterior
        n = random.randrange(2, 11)
        iguales = 1
        todos = list(range(-100, 100))
        num = random.sample(todos, n)
        igu = random.sample(range(1, n), iguales)
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(n):
            if i in igu:
                num[i] = num[i - 1]
                tmp_output[2*i+2:2*i+2] = [f"¡{num[i]} no es distinto de {num[i]}!"]
                if i != n-1:
                    tmp_output += [f"Escriba un número distinto de {num[i]}: "]
            elif i != n-1:
                tmp_output += [f"Escriba un número distinto de {num[i]}: "]
        num = [n] + num
        tmp_output += ["Gracias por su colaboración"]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # varios números iguales que el anterior
        n = random.randrange(4, 11)
        iguales = random.randrange(2, n-1)
        todos = list(range(-100, 100))
        num = random.sample(todos, n)
        igu = random.sample(range(1, n), iguales)
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(n):
            if i in igu:
                num[i] = num[i - 1]
                tmp_output[2*i+2:2*i+2] = [f"¡{num[i]} no es distinto de {num[i]}!"]
                if i != n-1:
                    tmp_output += [f"Escriba un número distinto de {num[i]}: "]
            elif i != n-1:
                tmp_output += [f"Escriba un número distinto de {num[i]}: "]
        num = [n] + num
        tmp_output += ["Gracias por su colaboración"]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # todos menos 1
        n = random.randrange(4, 11)
        iguales = n-2
        todos = list(range(-100, 100))
        num = random.sample(todos, n)
        igu = random.sample(range(1, n), iguales)
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(n):
            if i in igu:
                num[i] = num[i - 1]
                tmp_output[2*i+2:2*i+2] = [f"¡{num[i]} no es distinto de {num[i]}!"]
                if i != n-1:
                    tmp_output += [f"Escriba un número distinto de {num[i]}: "]
            elif i != n-1:
                tmp_output += [f"Escriba un número distinto de {num[i]}: "]
        num = [n] + num
        tmp_output += ["Gracias por su colaboración"]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # todos
        n = random.randrange(4, 11)
        iguales = n-1
        todos = list(range(-100, 100))
        num = random.sample(todos, n)
        igu = random.sample(range(1, n), iguales)
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(n):
            if i in igu:
                num[i] = num[i - 1]
                tmp_output[2*i+2:2*i+2] = [f"¡{num[i]} no es distinto de {num[i]}!"]
                if i != n-1:
                    tmp_output += [f"Escriba un número distinto de {num[i]}: "]
            elif i != n-1:
                tmp_output += [f"Escriba un número distinto de {num[i]}: "]
        num = [n] + num
        tmp_output += ["Gracias por su colaboración"]
        mpts_common.add_test(
            LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Exercise 111221 END

    elif exercise_id == 111231:
        # Exercise 111231 BEGINNING
        # /examenes/11-12/examen-120607.html

        # Valor negativo
        w = random.randrange(1, 11)
        h = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    "Por favor, escriba valores mayores que cero.",
                ],
            ],
        )

        # Valor negativo
        w = -random.randrange(1, 11)
        h = random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    "Por favor, escriba valores mayores que cero.",
                ],
            ],
        )

        # Valor cero
        w = 0
        h = random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    "Por favor, escriba valores mayores que cero.",
                ],
            ],
        )

        # Valor cero
        w = random.randrange(1, 11)
        h = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    "Por favor, escriba valores mayores que cero.",
                ],
            ],
        )

        # Valores positivos enteros
        w = random.randrange(1, 10000)
        h = random.randrange(1, 10000)
        s = round(float(w * h), 1)
        p = round(float(2 * w + 2 * h), 1)
        d = round(float((w * w + h * h) ** 0.5), 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    f"La superficie del rectángulo es {s}",
                    f"El perímetro del rectángulo es {p}",
                    f"La diagonal del rectángulo mide {d}",
                ],
            ],
        )

        # Valores positivos decimales
        w = random.randrange(1, 10000) / 100
        h = random.randrange(1, 10000) / 100
        s = round(w * h, 1)
        p = round(2 * w + 2 * h, 1)
        d = round((w * w + h * h) ** 0.5, 1)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [w, h]],
            [
                "output",
                [
                    "CÁLCULO DE DATOS DE UN RECTÁNGULO",
                    "Escriba la anchura del rectángulo: ",
                    "Escriba la altura del rectángulo: ",
                    f"La superficie del rectángulo es {s}",
                    f"El perímetro del rectángulo es {p}",
                    f"La diagonal del rectángulo mide {d}",
                ],
            ],
        )

        # Exercise 111211 END
