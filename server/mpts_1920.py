import mpts_common
import datetime
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 192011:
        # Exercise 192011 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/19-20/examen-200221.html

        # Valor negativo
        d = -random.randrange(100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    "Por favor, no escriba números negativos.",
                ],
            ],
        )

        # Cero días
        d = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    "0 días son 0 baktún, 0 katún, 0 tun, 0 uinal y 0 kin.",
                ],
            ],
        )

        # sólo kin
        ki = random.randrange(1, 20)
        d = ki
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    f"{d} días son 0 baktún, 0 katún, 0 tun, 0 uinal y {ki} kin.",
                ],
            ],
        )

        # kin, iumal
        ki = random.randrange(20)
        ui = random.randrange(1, 18)
        d = ki + ui * 20
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    f"{d} días son 0 baktún, 0 katún, 0 tun, {ui} uinal y {ki} kin.",
                ],
            ],
        )

        # kin, iumal, tun
        ki = random.randrange(20)
        ui = random.randrange(18)
        tu = random.randrange(1, 20)
        d = ki + ui * 20 + tu * 18 * 20
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    f"{d} días son 0 baktún, 0 katún, {tu} tun, {ui} uinal y {ki} kin.",
                ],
            ],
        )

        # kin, iumal, tun, katun
        ki = random.randrange(20)
        ui = random.randrange(18)
        tu = random.randrange(20)
        ka = random.randrange(1, 20)
        d = ki + ui * 20 + tu * 18 * 20 + ka * 20 * 18 * 20
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    f"{d} días son 0 baktún, {ka} katún, {tu} tun, {ui} uinal y {ki} kin.",
                ],
            ],
        )

        # kin, iumal, tun, katun, baktun
        ki = random.randrange(20)
        ui = random.randrange(18)
        tu = random.randrange(20)
        ka = random.randrange(20)
        ba = random.randrange(1, 10)
        d = ki + ui * 20 + tu * 18 * 20 + ka * 20 * 18 * 20 + ba * 20 * 20 * 18 * 20
        mpts_common.add_test(
            LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "CUENTA LARGA MAYA",
                    "Escriba una cantidad de días: ",
                    f"{d} días son {ba} baktún, {ka} katún, {tu} tun, {ui} uinal y {ki} kin.",
                ],
            ],
        )

        # Exercise 192011 END

    elif exercise_id == 192012:
        # Exercise 192012 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/19-20/examen-200221.html

        # a < 0
        a = -random.randrange(100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    "¡No ha escrito un número entero positivo!",
                ],
            ],
        )

        # a == 0
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    "¡No ha escrito un número entero positivo!",
                ],
            ],
        )

        # b == a
        a = random.randrange(1, 100)
        b = a

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"¡El múltiplo debe ser mayor que {a}!",
                ],
            ],
        )

        # b < a
        a = random.randrange(1, 100)
        b = a - random.randrange(1, a + 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"¡El múltiplo debe ser mayor que {a}!",
                ],
            ],
        )

        # b no múltiplo de a
        a = random.randrange(1, 100)
        b = a * random.randrange(2, 10) + random.randrange(1, a - 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"¡{b} no es múltiplo de {a}!",
                ],
            ],
        )

        # c == a
        a = random.randrange(1, 100)
        b = a * random.randrange(2, 10)
        c = a

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"Escriba un divisor de {b} distinto de {a}: ",
                    f"¡Le he pedido un número distinto de {a}!",
                ],
            ],
        )

        # c > b
        a = random.randrange(1, 100)
        b = a * random.randrange(2, 10)
        c = b + random.randrange(1, 100)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"Escriba un divisor de {b} distinto de {a}: ",
                    f"¡El divisor debe ser menor que {b}!",
                ],
            ],
        )

        # c no divisor de b
        a = random.randrange(1, 100)
        b = a * random.randrange(3, 10)
        c = b - random.randrange(1, a + 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"Escriba un divisor de {b} distinto de {a}: ",
                    f"¡{c} no es divisor de {b}!",
                ],
            ],
        )

        # a, b, c válidos
        a = random.randrange(1, 100)
        b = a * 2 * random.randrange(3, 10)
        c = b // 2

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "PIDE NÚMEROS",
                    "Escriba un número entero positivo: ",
                    f"Escriba un múltiplo de {a}: ",
                    f"Escriba un divisor de {b} distinto de {a}: ",
                    f"¡Gracias por su colaboración!",
                ],
            ],
        )

        # Exercise 192012 END

    elif exercise_id == 192013:
        # Exercise 192013 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/19-20/examen-200221.html

        # H < 0
        h = -random.randrange(1, 100)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 501) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Matiz incorrecto. Inténtelo de nuevo.",
                ],
            ],
        )

        # H > 360
        h = random.randrange(361, 1000)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 501) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Matiz incorrecto. Inténtelo de nuevo.",
                ],
            ],
        )

        # S < 0
        h = random.randrange(0, 361)
        s = -random.randrange(0, 10001) / 10000
        l = random.randrange(0, 501) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Saturación incorrecta. Inténtelo de nuevo.",
                ],
            ],
        )

        # S > 1
        h = random.randrange(0, 361)
        s = 1 + random.randrange(1, 10001) / 10000
        l = random.randrange(0, 501) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Saturación incorrecta. Inténtelo de nuevo.",
                ],
            ],
        )

        # L > 0
        h = random.randrange(0, 361)
        s = random.randrange(0, 501) / 10000
        l = -random.randrange(0, 10001) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Luminosidad incorrecta. Inténtelo de nuevo.",
                ],
            ],
        )

        # L > 1
        h = random.randrange(0, 361)
        s = random.randrange(0, 501) / 10000
        l = 1 + random.randrange(1, 10001) / 10000
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "Luminosidad incorrecta. Inténtelo de nuevo.",
                ],
            ],
        )

        # L = 0
        h = random.randrange(0, 361)
        s = random.randrange(0, 10001) / 10000
        l = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "El color es R = 0, G = 0, B = 0",
                ],
            ],
        )

        # L = 1
        h = random.randrange(0, 361)
        s = random.randrange(0, 10001) / 10000
        l = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    "El color es R = 255, G = 255, B = 255",
                ],
            ],
        )

        # 0 < H <= 60, L < 0.5
        h = random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 0 < H <= 60, L > 0.5
        h = random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 60 < H <= 120, L < 0.5
        h = 60 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 60 < H <= 120, L > 0.5
        h = 60 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 120 < H <= 180, L < 0.5
        h = 120 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 120 < H <= 180, L > 0.5
        h = 120 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 180 < H <= 240, L < 0.5
        h = 180 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 180 < H <= 240, L > 0.5
        h = 180 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 240 < H <= 300, L < 0.5
        h = 240 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 240 < H <= 300, L > 0.5
        h = 240 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 300 < H <= 360, L < 0.5
        h = 300 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # 300 < H <= 360, L > 0.5
        h = 300 + random.randrange(0, 61)
        s = random.randrange(0, 10001) / 10000
        l = 0.5 + random.randrange(0, 5000) / 10000
        r, g, b = mpts_common.hsl_2_rgb(h, s, l)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [h, s, l]],
            [
                "output",
                [
                    "CONVERTIDOR HSL a RGB",
                    "Introduzca las componentes HSL:",
                    "Matiz (entero de 0 a 360) H = ",
                    "Saturación (decimal de 0 a 1) S = ",
                    "Luminosidad (decimal de 0 a 1) L = ",
                    f"El color es R = {r}, G = {g}, B = {b}",
                ],
            ],
        )

        # Exercise 192013 END #

    elif exercise_id == 192014:
        # Exercise 192014 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/19-20/examen-200221.html

        # Coincide un dado AB / AC
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, a, c]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {a} y {c}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado AB / CA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, c, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {c} y {a}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado BA / AC
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [b, a, a, c]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {b} y {a}.",
                    f"Beatriz ha sacado {a} y {c}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado BA / CA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [b, a, c, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {b} y {a}.",
                    f"Beatriz ha sacado {c} y {a}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado AA / AB
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, a, a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {a}.",
                    f"Beatriz ha sacado {a} y {b}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado AA / BA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, a, b, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {a}.",
                    f"Beatriz ha sacado {b} y {a}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado AA / BA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, a, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {a} y {a}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # Coincide un dado AA / BA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [b, a, a, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {b} y {a}.",
                    f"Beatriz ha sacado {a} y {a}.",
                    "Ha ganado Beatriz.",
                ],
            ],
        )

        # No coincide ningún dado: AB / CD
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        dados.remove(c)
        d = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, c, d]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {c} y {d}.",
                    "Ha ganado Alejandro.",
                ],
            ],
        )

        # No coincide ningún dado: AA / BC
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, a, b, c]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {a}.",
                    f"Beatriz ha sacado {b} y {c}.",
                    "Ha ganado Alejandro.",
                ],
            ],
        )

        # No coincide ningún dado: AB / CC
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        dados.remove(b)
        c = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, c, c]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {c} y {c}.",
                    "Ha ganado Alejandro.",
                ],
            ],
        )

        # No coincide ningún dado: AA / BB
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, a, b, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {a}.",
                    f"Beatriz ha sacado {b} y {b}.",
                    "Ha ganado Alejandro.",
                ],
            ],
        )

        # Coinciden dos dados: AB / AB
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {a} y {b}.",
                    "Han empatado.",
                ],
            ],
        )

        # Coinciden dos dados: AB / BA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        dados.remove(a)
        b = random.choice(dados)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b, b, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {b}.",
                    f"Beatriz ha sacado {b} y {a}.",
                    "Han empatado.",
                ],
            ],
        )

        # Coinciden dos dados: AA / AA
        dados = [1, 2, 3, 4, 5, 6]
        a = random.choice(dados)
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a, a, a, a]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    f"Alejandro ha sacado {a} y {a}.",
                    f"Beatriz ha sacado {a} y {a}.",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 192014 END
