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
            [a],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                "Ha indicado una cantidad negativa.",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                "0 bytes son 0 GiB, 0 MiB, 0 KiB y 0 bytes.",
            ],
            NOT_LAST_TEST,
        )

        # Sólo bytes
        a = random.randrange(1, 1024)
        mpts_common.add_test(
            [a],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                f"{a} bytes son 0 GiB, 0 MiB, 0 KiB y {a} bytes.",
            ],
            NOT_LAST_TEST,
        )

        # Sólo kibibytes
        a = random.randrange(1, 1024)
        b = 1024 * a
        mpts_common.add_test(
            [b],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                f"{b} bytes son 0 GiB, 0 MiB, {a} KiB y 0 bytes.",
            ],
            NOT_LAST_TEST,
        )

        # Sólo mebibytes
        a = random.randrange(1, 1024)
        b = 1024 * 1024 * a
        mpts_common.add_test(
            [b],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                f"{b} bytes son 0 GiB, {a} MiB, 0 KiB y 0 bytes.",
            ],
            NOT_LAST_TEST,
        )

        # Sólo gibibytes
        a = random.randrange(1, 1024)
        b = 1024 * 1024 * 1024 * a
        mpts_common.add_test(
            [b],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                f"{b} bytes son {a} GiB, 0 MiB, 0 KiB y 0 bytes.",
            ],
            NOT_LAST_TEST,
        )

        # De todo
        a = random.randrange(1, 1024)
        b = random.randrange(1, 1024)
        c = random.randrange(1, 1024)
        d = random.randrange(1, 1024)
        e = 1024 * 1024 * 1024 * a + 1024 * 1024 * b + 1024 * c + d
        mpts_common.add_test(
            [e],
            [],
            [
                "MÚLTIPLOS BINARIOS",
                "Escriba un número de bytes: ",
                f"{e} bytes son {a} GiB, {b} MiB, {c} KiB y {d} bytes.",
            ],
            LAST_TEST,
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
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # r fuera de rango por arriba
        r = 256
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # r fuera de rango por arriba
        r = random.randrange(256, 300)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # g fuera de rango por abajo
        r = random.randrange(0, 256)
        g = -random.randrange(1, 10000)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # g fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(256, 300)
        b = random.randrange(0, 256)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # g fuera de rango por arriba
        r = random.randrange(0, 256)
        g = 256
        b = random.randrange(0, 256)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # b fuera de rango por abajo
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = -random.randrange(1, 10000)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # b fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = 256
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # b fuera de rango por arriba
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(256, 300)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "Por favor, escriba valores desde 0 hasta 255.",
            ],
            NOT_LAST_TEST,
        )

        # c = 0 r = g = b = 255
        r = 255
        g = r
        b = r
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                "El color es H = 0 S = 0.0 L = 1.0",
            ],
            NOT_LAST_TEST,
        )

        # c = 0 r = g = b != 255
        r = random.randrange(0, 255)
        g = r
        b = r
        l = round(r / 255, 3)
        mpts_common.add_test(
            [r, g, b],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = 0 S = 0.0 L = {l}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            NOT_LAST_TEST,
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
            [R, G, B],
            [],
            [
                "CONVERTIDOR RGB A HSL",
                "Introduzca las componentes RGB (valores entre 0 y 255)",
                "R = ",
                "G = ",
                "B = ",
                f"El color es H = {h} S = {round(s, 3)} L = {round(l, 3)}",
            ],
            LAST_TEST,
        )

        # Exercise 171812 END

    elif exercise_id == 171_813:
        # Exercise 171813 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/17-18/examen-180228.html

        # 0 - 0
        mpts_common.add_test(
            [],
            [0, 0],
            [
                "PARES Y NONES",
                "Pablo no saca ningún dedo.",
                "Noelia no saca ningún dedo.",
                "Total: 0.",
                "Ha ganado Pablo.",
            ],
            NOT_LAST_TEST,
        )

        # 0 - 1
        mpts_common.add_test(
            [],
            [0, 1],
            [
                "PARES Y NONES",
                "Pablo no saca ningún dedo.",
                "Noelia saca 1 dedo.",
                "Total: 1.",
                "Ha ganado Noelia.",
            ],
            NOT_LAST_TEST,
        )

        # 0 - par
        a = random.choice([2, 4])
        mpts_common.add_test(
            [],
            [0, a],
            [
                "PARES Y NONES",
                "Pablo no saca ningún dedo.",
                f"Noelia saca {a} dedos.",
                f"Total: {a}.",
                "Ha ganado Pablo.",
            ],
            NOT_LAST_TEST,
        )

        # 0 - impar
        a = random.choice([3, 5])
        mpts_common.add_test(
            [],
            [0, a],
            [
                "PARES Y NONES",
                "Pablo no saca ningún dedo.",
                f"Noelia saca {a} dedos.",
                f"Total: {a}.",
                "Ha ganado Noelia.",
            ],
            NOT_LAST_TEST,
        )

        # 1 - 1
        mpts_common.add_test(
            [],
            [1, 1],
            [
                "PARES Y NONES",
                "Pablo saca 1 dedo.",
                "Noelia saca 1 dedo.",
                "Total: 2.",
                "Ha ganado Pablo.",
            ],
            NOT_LAST_TEST,
        )

        # par - 1
        a = random.choice([2, 4])
        mpts_common.add_test(
            [],
            [a, 1],
            [
                "PARES Y NONES",
                f"Pablo saca {a} dedos.",
                "Noelia saca 1 dedo.",
                f"Total: {a + 1}.",
                "Ha ganado Noelia.",
            ],
            NOT_LAST_TEST,
        )

        # impar - 1
        a = random.choice([3, 5])
        mpts_common.add_test(
            [],
            [a, 1],
            [
                "PARES Y NONES",
                f"Pablo saca {a} dedos.",
                "Noelia saca 1 dedo.",
                f"Total: {a + 1}.",
                "Ha ganado Pablo.",
            ],
            NOT_LAST_TEST,
        )

        #  > 1 - > 1
        a = random.choice([2, 6])
        b = random.choice([2, 6])
        ganador = ["Pablo", "Noelia"]
        mpts_common.add_test(
            [],
            [a, b],
            [
                "PARES Y NONES",
                f"Pablo saca {a} dedos.",
                f"Noelia saca {b} dedos.",
                f"Total: {a + b}.",
                f"Ha ganado {ganador[(a+b)%2]}.",
            ],
            LAST_TEST,
        )

        # Exercise 171813 END
