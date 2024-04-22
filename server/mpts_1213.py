import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):

    if exercise_id == 1213_11:
        # Exercise 121311 BEGINNING
        # /examenes/12-13/examen-130129.html

        # Valor negativo
        p = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [p]],
            [
                "output",
                [
                    "CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES",
                    "Escriba la cantidad de peniques: ",
                    "Por favor, escriba un número positivo.",
                ],
            ],
        )

        # Valores positivos o nulos
        r = random.randrange(0, 5)
        co = random.randrange(0, 2)
        ch = random.randrange(0, 20)
        l = random.randrange(0, 100)

        p = l * 20 * 12 + ch * 12 + co * 5 + r

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [p]],
            [
                "output",
                [
                    "CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES",
                    "Escriba la cantidad de peniques: ",
                    f"{p} peniques son {l} libras, {ch} chelines, {co} coronas y {r} peniques.",
                ],
            ],
        )

        # Algún valor nulo
        r = random.randrange(0, 5)
        co = random.randrange(0, 2)
        ch = random.randrange(0, 20)
        l = random.randrange(0, 100)
        x = random.choice(["r", "co", "ch", "l"])
        if x == "r":
            r = 0
        elif x == "co":
            co = 0
        elif x == "ch":
            ch = 0
        else:
            l = 0

        p = l * 20 * 12 + ch * 12 + co * 5 + r

        mpts_common.add_test(
            LAST_TEST,
            ["input", [p]],
            [
                "output",
                [
                    "CONVERTIDOR A LIBRAS, CHELINES, CORONAS Y PENIQUES",
                    "Escriba la cantidad de peniques: ",
                    f"{p} peniques son {l} libras, {ch} chelines, {co} coronas y {r} peniques.",
                ],
            ],
        )

        # Exercise 121311 END

    elif exercise_id == 1213_12:
        # Exercise 121312 BEGINNING
        # /examenes/12-13/examen-130129.html

        # 0, 0, 0
        a = 0
        b = 0
        c = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} forman una sucesión aritmética de diferencia 0 y una sucesión geométrica de razón cualquiera.",
                ],
            ],
        )

        # 0, 0, x
        a = 0
        b = 0
        c = random.randrange(-1000, 1000)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} no forman ni una sucesión aritmética ni geométrica.",
                ],
            ],
        )

        # x, 0, 0
        a = random.randrange(-1000, 1000)
        b = 0
        c = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} forman una sucesión geométrica de razón 0.",
                ],
            ],
        )

        # x, x, x
        a = random.randrange(-1000, 1000)
        b = a
        c = a

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} forman una sucesión aritmética de diferencia 0 y una sucesión geométrica de razón 1.",
                ],
            ],
        )

        # x , x + c,  x + c + c
        a = random.randrange(-1000, 1000)
        b = random.randrange(-1000, 1000)
        c = b + b - a

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} forman una sucesión aritmética de diferencia {b - a}.",
                ],
            ],
        )

        # x,  x * c,  x * c * c
        tmp = random.randrange(-1000, 1000)
        a = random.randrange(-1000, 1000)
        b = a * tmp
        c = b * tmp

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} forman una sucesión geométrica de razón {float(tmp)}.",
                ],
            ],
        )

        # x, y, x + y
        # sale aritmetica si y = 2 * x
        # sale geometrica si y = x * (1 ± sqrt 5) / 2
        tmp = random.randrange(3, 1000)
        a = random.randrange(-1000, 1000)
        b = a * tmp
        c = a + b

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} no forman ni una sucesión aritmética ni geométrica.",
                ],
            ],
        )

        # x, y, x + y
        # sale aritmetica si y = 2 * x
        # sale geometrica si y = x * (1 ± sqrt 5) / 2
        tmp = random.randrange(-1000, -2)
        a = random.randrange(-1000, 1000)
        b = a * tmp
        c = a + b

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "SUCESIONES",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{a} {b} {c} no forman ni una sucesión aritmética ni geométrica.",
                ],
            ],
        )

        # Exercise 121312 END

    elif exercise_id == 1213_13:
        # Exercise 121313 BEGINNING
        # /examenes/12-13/examen-130129.html

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

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["output", ["¿Cuántos valores va a introducir? ", "¡Imposible!",],],
        )

        # Sin valores crecientes
        n = random.randrange(2, 20)
        v = [n]
        for _ in range(n):
            v += [v[-1] - random.randrange(0, 10)]
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba el primer número: ",
        ]
        for i in range(2, n + 1):
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += ["Ha escrito 0 valores mayores que el anterior"]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # 1 valor creciente
        n = random.randrange(2, 20)
        m = 1
        f = random.randrange(-100, 100)
        vd = []
        for _ in range(n - m - 1):
            vd += [-random.randrange(0, 10)]
        for _ in range(m):
            vd += [random.randrange(1, 10)]
        random.shuffle(vd)
        v = [n, f]
        for i in vd:
            v += [v[-1] + i]
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba el primer número: ",
        ]
        for i in range(2, n + 1):
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += ["Ha escrito 1 valor mayor que el anterior"]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # algunos valores crecientes
        n = random.randrange(3, 20)
        m = random.randrange(2, n)
        f = random.randrange(-100, 100)
        vd = []
        for _ in range(n - m - 1):
            vd += [-random.randrange(0, 10)]
        for _ in range(m):
            vd += [random.randrange(1, 10)]
        random.shuffle(vd)
        v = [n, f]
        for i in vd:
            v += [v[-1] + i]
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba el primer número: ",
        ]
        for i in range(2, n + 1):
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += [f"Ha escrito {m} valores mayores que el anterior"]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # todos bajan
        n = random.randrange(2, 20)
        m = n - 1
        f = random.randrange(-100, 100)
        vd = []
        for _ in range(n - m - 1):
            vd += [-random.randrange(0, 10)]
        for _ in range(m):
            vd += [random.randrange(1, 10)]
        random.shuffle(vd)
        v = [n, f]
        for i in vd:
            v += [v[-1] + i]
        tmp_output = [
            "¿Cuántos valores va a introducir? ",
            "Escriba el primer número: ",
        ]
        for i in range(2, n + 1):
            tmp_output += [f"Escriba el número {i}: "]
        tmp_output += [f"Ha escrito {m} valores mayores que el anterior"]

        mpts_common.add_test(
            LAST_TEST, ["input", v], ["output", tmp_output],
        )

        # Exercise 121313 END
