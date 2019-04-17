import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 171_811:
        # Exercise 171811 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180228.html

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    "Ha indicado una cantidad negativa.",
                ],
            ],
        )

        # Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    "0 bytes son 0 GiB, 0 MiB, 0 KiB y 0 bytes.",
                ],
            ],
        )

        # Sólo bytes
        a = random.randrange(1, 1024)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{a} bytes son 0 GiB, 0 MiB, 0 KiB y {a} bytes.",
                ],
            ],
        )

        # Sólo kibibytes
        a = random.randrange(1, 1024)
        b = 1024 * a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [b]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{b} bytes son 0 GiB, 0 MiB, {a} KiB y 0 bytes.",
                ],
            ],
        )

        # Sólo mebibytes
        a = random.randrange(1, 1024)
        b = 1024 * 1024 * a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [b]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{b} bytes son 0 GiB, {a} MiB, 0 KiB y 0 bytes.",
                ],
            ],
        )

        # Sólo gibibytes
        a = random.randrange(1, 1024)
        b = 1024 * 1024 * 1024 * a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [b]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{b} bytes son {a} GiB, 0 MiB, 0 KiB y 0 bytes.",
                ],
            ],
        )

        # Dos de los cuatro, al azar
        v = [random.randrange(1, 1024), random.randrange(1, 1024), 0, 0]
        random.shuffle(v)
        e = 1024 * 1024 * 1024 * v[0] + 1024 * 1024 * v[1] + 1024 * v[2] + v[3]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [e]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{e} bytes son {v[0]} GiB, {v[1]} MiB, {v[2]} KiB y {v[3]} bytes.",
                ],
            ],
        )

        # Tres de los cuatro, al azar
        v = [
            random.randrange(1, 1024),
            random.randrange(1, 1024),
            random.randrange(1, 1024),
            0,
        ]
        random.shuffle(v)
        e = 1024 * 1024 * 1024 * v[0] + 1024 * 1024 * v[1] + 1024 * v[2] + v[3]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [e]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{e} bytes son {v[0]} GiB, {v[1]} MiB, {v[2]} KiB y {v[3]} bytes.",
                ],
            ],
        )

        # De todo
        a = random.randrange(1, 1024)
        b = random.randrange(1, 1024)
        c = random.randrange(1, 1024)
        d = random.randrange(1, 1024)
        e = 1024 * 1024 * 1024 * a + 1024 * 1024 * b + 1024 * c + d
        mpts_common.add_test(
            LAST_TEST,
            ["input", [e]],
            [
                "output",
                [
                    "MÚLTIPLOS BINARIOS",
                    "Escriba un número de bytes: ",
                    f"{e} bytes son {a} GiB, {b} MiB, {c} KiB y {d} bytes.",
                ],
            ],
        )

        # Exercise 171811 END

    elif exercise_id == 171_812:
        # Exercise 171812 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180228.html

        # r fuera de rango por abajo
        r = -random.randrange(1, 10000)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # r fuera de rango por arriba
        r = 256
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # r fuera de rango por arriba
        r = random.randrange(256, 300)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # g fuera de rango por abajo
        r = random.randrange(0, 256)
        g = -random.randrange(1, 10000)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # g fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(256, 300)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # g fuera de rango por arriba
        r = random.randrange(0, 256)
        g = 256
        b = random.randrange(0, 256)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # b fuera de rango por abajo
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = -random.randrange(1, 10000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # b fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = 256
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # b fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(256, 300)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "Por favor, escriba valores desde 0 hasta 255.",
                ],
            ],
        )

        # c = 0 r = g = b = 255
        r = 255
        g = r
        b = r
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    "El color es H = 0 S = 0.0 L = 1.0",
                ],
            ],
        )

        # c = 0 r = g = b != 255
        r = random.randrange(0, 255)
        g = r
        b = r
        l = round(r / 255, 3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [r, g, b]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = 0 S = 0.0 L = {l}",
                ],
            ],
        )

        # M = r, g = b
        R = random.randrange(1, 256)
        G = random.randrange(0, R)
        B = G
        r = R / 255
        g = G / 255
        b = B / 255
        h = 0
        l = (r + g) / 2
        s = (r - g) / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = r, g > b
        R = random.randrange(2, 255)
        G = random.randrange(1, R)
        B = random.randrange(0, G)
        r = R / 255
        g = G / 255
        b = B / 255
        c = r - b
        h = round((g - b) / c * 60) % 360
        l = (r + b) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = r, g < b
        R = random.randrange(2, 256)
        B = random.randrange(1, R)
        G = random.randrange(0, B)
        r = R / 255
        g = G / 255
        b = B / 255
        c = r - g
        h = round(((g - b) / c + 6) * 60) % 360
        l = (r + g) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = g, r = b
        G = random.randrange(1, 256)
        R = random.randrange(0, G)
        B = R
        r = R / 255
        g = G / 255
        b = B / 255
        h = 120
        l = (g + r) / 2
        s = (g - r) / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = g, b > r
        G = random.randrange(2, 256)
        B = random.randrange(1, G)
        R = random.randrange(0, B)
        r = R / 255
        g = G / 255
        b = B / 255
        c = g - r
        h = round(((b - r) / c + 2) * 60) % 360
        l = (g + r) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = g, b < r
        G = random.randrange(2, 256)
        R = random.randrange(1, G)
        B = random.randrange(0, R)
        r = R / 255
        g = G / 255
        b = B / 255
        c = g - b
        h = round(((b - r) / c + 8) * 60) % 360
        l = (g + b) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = b, r = g
        B = random.randrange(1, 256)
        R = random.randrange(0, B)
        G = R
        r = R / 255
        g = G / 255
        b = B / 255
        h = 240
        l = (b + r) / 2
        s = (b - r) / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = b, r > g
        B = random.randrange(2, 256)
        R = random.randrange(1, B)
        G = random.randrange(0, R)
        r = R / 255
        g = G / 255
        b = B / 255
        c = b - g
        h = round(((r - g) / c + 4) * 60) % 360
        l = (b + g) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # M = b, r < g
        B = random.randrange(2, 256)
        G = random.randrange(1, B)
        R = random.randrange(0, G)
        r = R / 255
        g = G / 255
        b = B / 255
        c = b - r
        h = round(((r - g) / c + 10) * 60) % 360
        l = (b + r) / 2
        s = c / (1 - abs(2 * l - 1))
        mpts_common.add_test(
            LAST_TEST,
            ["input", [R, G, B]],
            [
                "output",
                [
                    "CONVERTIDOR RGB A HSL",
                    "Introduzca las componentes RGB (valores entre 0 y 255)",
                    "R = ",
                    "G = ",
                    "B = ",
                    f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
                ],
            ],
        )

        # Exercise 171812 END

    elif exercise_id == 171_813:
        # Exercise 171813 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180228.html

        # 0 - 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [0, 0]],
            [
                "output",
                [
                    "PARES Y NONES",
                    "Pablo no saca ningún dedo.",
                    "Noelia no saca ningún dedo.",
                    "Total: 0.",
                    "Ha ganado Pablo.",
                ],
            ],
        )

        # 0 - 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [0, 1]],
            [
                "output",
                [
                    "PARES Y NONES",
                    "Pablo no saca ningún dedo.",
                    "Noelia saca 1 dedo.",
                    "Total: 1.",
                    "Ha ganado Noelia.",
                ],
            ],
        )

        # 0 - par
        a = random.choice([2, 4])
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [0, a]],
            [
                "output",
                [
                    "PARES Y NONES",
                    "Pablo no saca ningún dedo.",
                    f"Noelia saca {a} dedos.",
                    f"Total: {a}.",
                    "Ha ganado Pablo.",
                ],
            ],
        )

        # 0 - impar
        a = random.choice([3, 5])
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [0, a]],
            [
                "output",
                [
                    "PARES Y NONES",
                    "Pablo no saca ningún dedo.",
                    f"Noelia saca {a} dedos.",
                    f"Total: {a}.",
                    "Ha ganado Noelia.",
                ],
            ],
        )

        # 1 - 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [1, 1]],
            [
                "output",
                [
                    "PARES Y NONES",
                    "Pablo saca 1 dedo.",
                    "Noelia saca 1 dedo.",
                    "Total: 2.",
                    "Ha ganado Pablo.",
                ],
            ],
        )

        # par - 1
        a = random.choice([2, 4])
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, 1]],
            [
                "output",
                [
                    "PARES Y NONES",
                    f"Pablo saca {a} dedos.",
                    "Noelia saca 1 dedo.",
                    f"Total: {a + 1}.",
                    "Ha ganado Noelia.",
                ],
            ],
        )

        # impar - 1
        a = random.choice([3, 5])
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, 1]],
            [
                "output",
                [
                    "PARES Y NONES",
                    f"Pablo saca {a} dedos.",
                    "Noelia saca 1 dedo.",
                    f"Total: {a + 1}.",
                    "Ha ganado Pablo.",
                ],
            ],
        )

        #  > 1 - > 1
        a = random.choice([2, 6])
        b = random.choice([2, 6])
        ganador = ["Pablo", "Noelia"]
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "PARES Y NONES",
                    f"Pablo saca {a} dedos.",
                    f"Noelia saca {b} dedos.",
                    f"Total: {a + b}.",
                    f"Ha ganado {ganador[(a+b)%2]}.",
                ],
            ],
        )

        # Exercise 171813 END

    elif exercise_id == 171_821:
        # Exercise 171821 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180523.html#ejercicio-1

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    "Escriba una cantidad mayor que cero.",
                ],
            ],
        )

        # Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    "Escriba una cantidad mayor que cero.",
                ],
            ],
        )

        # Sólo ases
        a = random.randrange(1, 4)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {a} as(es).",
                ],
            ],
        )

        # Sólo sestercios
        b = random.randrange(1, 4)
        a = 4 * b

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {b} sestercio(s), ",
                ],
            ],
        )

        # Sólo denarios
        b = random.randrange(1, 25)
        a = 4 * 4 * b

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {b} denario(s), ",
                ],
            ],
        )
        # Sólo áureos
        b = random.randrange(1, 100)
        a = 25 * 4 * 4 * b

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {b} áureo(s), ",
                ],
            ],
        )

        # Dos de los cuatro, al azar
        v = [1, 1, 0, 0]
        random.shuffle(v)
        v = [
            v[0] * random.randrange(1, 100),
            v[1] * random.randrange(1, 25),
            v[2] * random.randrange(1, 4),
            v[3] * random.randrange(1, 4),
        ]
        a = 25 * 4 * 4 * v[0] + 4 * 4 * v[1] + 4 * v[2] + v[3]
        frase = ""
        if v[0]:
            frase += f"{v[0]} áureo(s), "
        if v[1]:
            frase += f"{v[1]} denario(s), "
        if v[2]:
            frase += f"{v[2]} sestercio(s), "
        if v[3]:
            frase += f"{v[3]} as(es)."

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {frase}",
                ],
            ],
        )

        # Tres de los cuatro, al azar
        v = [1, 1, 1, 0]
        random.shuffle(v)
        v = [
            v[0] * random.randrange(1, 100),
            v[1] * random.randrange(1, 25),
            v[2] * random.randrange(1, 4),
            v[3] * random.randrange(1, 4),
        ]
        a = 25 * 4 * 4 * v[0] + 4 * 4 * v[1] + 4 * v[2] + v[3]
        frase = ""
        if v[0]:
            frase += f"{v[0]} áureo(s), "
        if v[1]:
            frase += f"{v[1]} denario(s), "
        if v[2]:
            frase += f"{v[2]} sestercio(s), "
        if v[3]:
            frase += f"{v[3]} as(es)."

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {frase}",
                ],
            ],
        )

        # Los cuatro
        v = [
            random.randrange(1, 100),
            random.randrange(1, 25),
            random.randrange(1, 4),
            random.randrange(1, 4),
        ]
        a = 25 * 4 * 4 * v[0] + 4 * 4 * v[1] + 4 * v[2] + v[3]
        frase = ""
        if v[0]:
            frase += f"{v[0]} áureo(s), "
        if v[1]:
            frase += f"{v[1]} denario(s), "
        if v[2]:
            frase += f"{v[2]} sestercio(s), "
        if v[3]:
            frase += f"{v[3]} as(es)."

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONVERTIDOR DE ASES A ÁUREOS, DENARIOS Y SESTERCIOS",
                    "Escriba la cantidad de ases: ",
                    f"{a} ases son {frase}",
                ],
            ],
        )

        # Exercise 171821 END

    elif exercise_id == 171_822:
        # Exercise 171822 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180523.html

        # Gana Cubitus
        a = []
        b = []
        ta = tb = 0
        for _ in range(3):
            d = random.randrange(2, 6)
            a += [d]
            ta += d
            b += [d - 1]
            tb += d - 1
        a += [1, 6]
        b += [1, 6]
        random.shuffle(a)
        random.shuffle(b)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", a + b],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "",
                    f"Tirada de Cubitus: {a[0]} {a[1]} {a[2]} {a[3]} {a[4]} ",
                    f"Cubitus ha sacado {ta} puntos.",
                    "",
                    f"Tirada de Humerus: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]} ",
                    f"Humerus ha sacado {tb} puntos.",
                    "",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # Gana Humerus
        a = []
        b = []
        ta = tb = 0
        for _ in range(3):
            d = random.randrange(2, 6)
            a += [d]
            ta += d
            b += [d + 1]
            tb += d + 1
        a += [1, 6]
        b += [1, 6]
        random.shuffle(a)
        random.shuffle(b)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", a + b],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "",
                    f"Tirada de Cubitus: {a[0]} {a[1]} {a[2]} {a[3]} {a[4]} ",
                    f"Cubitus ha sacado {ta} puntos.",
                    "",
                    f"Tirada de Humerus: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]} ",
                    f"Humerus ha sacado {tb} puntos.",
                    "",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # Empatan
        a = []
        b = []
        ta = tb = 0
        for _ in range(3):
            d = random.randrange(2, 6)
            a += [d]
            ta += d
            b += [d]
            tb += d
        a += [1, 6]
        b += [1, 6]
        random.shuffle(a)
        random.shuffle(b)
        mpts_common.add_test(
            LAST_TEST,
            ["random", a + b],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "",
                    f"Tirada de Cubitus: {a[0]} {a[1]} {a[2]} {a[3]} {a[4]} ",
                    f"Cubitus ha sacado {ta} puntos.",
                    "",
                    f"Tirada de Humerus: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]} ",
                    f"Humerus ha sacado {tb} puntos.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 171822 END

    elif exercise_id == 171_823:
        # Exercise 171823 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180523.html

        # Jugadores negativos
        n = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "UNUS ET DUO",
                    "Escriba el número de jugadores: ",
                    "Escriba un número mayor que dos.",
                ],
            ],
        )

        # 0 jugadores
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "UNUS ET DUO",
                    "Escriba el número de jugadores: ",
                    "Escriba un número mayor que dos.",
                ],
            ],
        )

        # 1 jugador
        n = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "UNUS ET DUO",
                    "Escriba el número de jugadores: ",
                    "Escriba un número mayor que dos.",
                ],
            ],
        )

        # 2 jugadores
        n = 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "UNUS ET DUO",
                    "Escriba el número de jugadores: ",
                    "Escriba un número mayor que dos.",
                ],
            ],
        )

        # No acierta nadie
        n = random.randrange(3, 10)
        tmp_output = ["UNUS ET DUO", "Escriba el número de jugadores: "]
        tmp_random = []
        a = random.randrange(2, 7)
        tmp_random += [a]
        tmp_output += [f"El primer jugador ha sacado un {a}."]
        for i in range(2, n + 1):
            b = random.randrange(2, 7)
            c = random.randrange(2, 7)
            while b + c == a:
                b = random.randrange(2, 7)
                c = random.randrange(2, 7)
            tmp_random += [b, c]
            tmp_output += [""]
            tmp_output += [f"El jugador {i} ha sacado {b} y {c}."]
        tmp_output += [""]
        tmp_output += ["No ha ganado nadie."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Acierta uno
        n = random.randrange(3, 10)
        g = random.randrange(2, n + 1)
        tmp_output = ["UNUS ET DUO", "Escriba el número de jugadores: "]
        tmp_random = []
        a = random.randrange(2, 7)
        tmp_random += [a]
        tmp_output += [f"El primer jugador ha sacado un {a}."]
        for i in range(2, g):
            b = random.randrange(1, 7)
            c = random.randrange(1, 7)
            while b + c == a:
                b = random.randrange(1, 7)
                c = random.randrange(1, 7)
            tmp_random += [b, c]
            tmp_output += [""]
            tmp_output += [f"El jugador {i} ha sacado {b} y {c}."]
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        while b + c != a:
                b = random.randrange(1, 7)
                c = random.randrange(1, 7)
        tmp_random += [b, c]
        tmp_output += [""]
        tmp_output += [f"El jugador {g} ha sacado {b} y {c}."]
        tmp_output += [""]
        tmp_output += [f"El jugador {g} ha ganado."]

        mpts_common.add_test(
            LAST_TEST, ["input", [n]], ["random", tmp_random], ["output", tmp_output]
        )

        # Exercise 171823 END
