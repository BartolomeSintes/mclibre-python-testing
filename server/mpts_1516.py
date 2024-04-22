import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):

    if exercise_id == 1516_11:
        # Exercise 151611 BEGINNING
        # /examenes/15-16/examen-160525.html

        # dígito entidad negativo
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        d[random.randrange(0, 4)] = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    "Lo siento. No ha escrito correctamente los dígitos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # dígito entidad > 9
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        d[random.randrange(0, 4)] = random.randrange(10, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    "Lo siento. No ha escrito correctamente los dígitos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # dígito oficina negativo
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        d[random.randrange(4, 8)] = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    "Lo siento. No ha escrito correctamente los dígitos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # dígito oficina > 9
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        d[random.randrange(4, 8)] = random.randrange(10, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    "Lo siento. No ha escrito correctamente los dígitos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # dígitos válidos (1/2)
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        c = (
            11
            - (
                d[0] * 4
                + d[1] * 8
                + d[2] * 5
                + d[3] * 10
                + d[4] * 9
                + d[5] * 7
                + d[6] * 3
                + d[7] * 6
            )
            % 11
        )
        if c == 10:
            c = 1
        elif c == 11:
            c = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    f"El dígito de control es {c}.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # dígitos válidos (2/2)
        d = []
        for _ in range(8):
            d += [random.randrange(0, 10)]
        c = (
            11
            - (
                d[0] * 4
                + d[1] * 8
                + d[2] * 5
                + d[3] * 10
                + d[4] * 9
                + d[5] * 7
                + d[6] * 3
                + d[7] * 6
            )
            % 11
        )
        if c == 10:
            c = 1
        elif c == 11:
            c = 0

        mpts_common.add_test(
            LAST_TEST,
            ["input", d],
            [
                "output",
                [
                    "DIGITO DE CONTROL CUENTA CORRIENTE",
                    "",
                    "Escriba el primer dígito de la entidad:  ",
                    "Escriba el segundo dígito de la entidad: ",
                    "Escriba el tercer dígito de la entidad:  ",
                    "Escriba el cuarto dígito de la entidad:  ",
                    "",
                    "Escriba el primer dígito de la oficina:  ",
                    "Escriba el segundo dígito de la oficina: ",
                    "Escriba el tercer dígito de la oficina:  ",
                    "Escriba el cuarto dígito de la oficina:  ",
                    "",
                    f"El dígito de control es {c}.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Exercise 151611 END

    elif exercise_id == 1516_12:
        # Exercise 151612 BEGINNING
        # /examenes/15-16/examen-160525.html

        # Valor negativo
        n = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "SUMADOR DE PARES E IMPARES",
                    "",
                    "¿Cuántos números va a escribir? ",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Cero
        n = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "SUMADOR DE PARES E IMPARES",
                    "",
                    "¿Cuántos números va a escribir? ",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # solo pares
        np = random.randrange(3, 11)
        ni = 0
        tp = 0
        ti = 0
        num = []
        for _ in range(np):
            a = 2 * random.randrange(0, 100)
            num += [a]
            tp += a
        for _ in range(ni):
            a = 2 * random.randrange(0, 100) + 1
            num += [a]
            ti += a
        random.shuffle(num)
        tmp_output = [
            "SUMADOR DE PARES E IMPARES",
            "",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(np + ni):
            tmp_output += ["Escriba un número entero: "]
        num = [np + ni] + num

        tmp_output += [
            "",
            f"La suma de los números pares que ha escrito es {tp}",
            f"La suma de los números impares que ha escrito es {ti}",
            "",
            "Programa terminado",
        ]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # solo impares
        np = 0
        ni = random.randrange(3, 11)
        tp = 0
        ti = 0
        num = []
        for _ in range(np):
            a = 2 * random.randrange(0, 100)
            num += [a]
            tp += a
        for _ in range(ni):
            a = 2 * random.randrange(0, 100) + 1
            num += [a]
            ti += a
        random.shuffle(num)
        tmp_output = [
            "SUMADOR DE PARES E IMPARES",
            "",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(np + ni):
            tmp_output += ["Escriba un número entero: "]
        num = [np + ni] + num

        tmp_output += [
            "",
            f"La suma de los números pares que ha escrito es {tp}",
            f"La suma de los números impares que ha escrito es {ti}",
            "",
            "Programa terminado",
        ]

        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # pares e impares
        np = random.randrange(1, 11)
        ni = random.randrange(1, 11)
        tp = 0
        ti = 0
        num = []
        for _ in range(np):
            a = 2 * random.randrange(0, 100)
            num += [a]
            tp += a
        for _ in range(ni):
            a = 2 * random.randrange(0, 100) + 1
            num += [a]
            ti += a
        random.shuffle(num)
        tmp_output = [
            "SUMADOR DE PARES E IMPARES",
            "",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(np + ni):
            tmp_output += ["Escriba un número entero: "]
        num = [np + ni] + num

        tmp_output += [
            "",
            f"La suma de los números pares que ha escrito es {tp}",
            f"La suma de los números impares que ha escrito es {ti}",
            "",
            "Programa terminado",
        ]

        mpts_common.add_test(
            LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Exercise 151612 END

    elif exercise_id == 1516_21:
        # Exercise 151621 BEGINNING
        # /examenes/15-16/examen-160608.html

        # Punto sobre la circunferencia (1º cuadrante)
        cx = random.randrange(-100, 101)
        cy = random.randrange(-100, 101)
        r = random.randrange(10, 101)
        rx = random.randrange(0, r)
        ry = (r ** 2 - rx ** 2) ** 0.5
        x = cx + rx
        y = cy + ry

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cx / 10, cy / 10, r / 10, x / 10, y / 10]],
            [
                "output",
                [
                    "PUNTO Y CIRCUNFERENCIA",
                    "",
                    "Escriba la coordenada X del centro de la circunferencia: ",
                    "Escriba la coordenada Y del centro de la circunferencia: ",
                    "Escriba el radio de la circunferencia: ",
                    "",
                    "Escriba la coordenada X del punto: ",
                    "Escriba la coordenada Y del punto: ",
                    "",
                    "El punto está sobre la circunferencia.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Punto fuera de la circunferencia (2º cuadrante)
        cx = random.randrange(-100, 101)
        cy = random.randrange(-100, 101)
        r = random.randrange(10, 101)
        rx = random.randrange(0, r)
        ry = (r ** 2 - rx ** 2) ** 0.5
        x = cx - rx - random.randrange(1, 5)
        y = cy + ry + random.randrange(1, 5)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cx / 10, cy / 10, r / 10, x / 10, y / 10]],
            [
                "output",
                [
                    "PUNTO Y CIRCUNFERENCIA",
                    "",
                    "Escriba la coordenada X del centro de la circunferencia: ",
                    "Escriba la coordenada Y del centro de la circunferencia: ",
                    "Escriba el radio de la circunferencia: ",
                    "",
                    "Escriba la coordenada X del punto: ",
                    "Escriba la coordenada Y del punto: ",
                    "",
                    "El punto está fuera de la circunferencia.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Punto dentro de la circunferencia (3º cuadrante)
        cx = random.randrange(-100, 101)
        cy = random.randrange(-100, 101)
        r = random.randrange(10, 101)
        rx = random.randrange(0, r)
        ry = (r ** 2 - rx ** 2) ** 0.5
        x = cx - rx + random.randrange(1, 5)
        y = cy - ry + random.randrange(1, 5)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cx / 10, cy / 10, r / 10, x / 10, y / 10]],
            [
                "output",
                [
                    "PUNTO Y CIRCUNFERENCIA",
                    "",
                    "Escriba la coordenada X del centro de la circunferencia: ",
                    "Escriba la coordenada Y del centro de la circunferencia: ",
                    "Escriba el radio de la circunferencia: ",
                    "",
                    "Escriba la coordenada X del punto: ",
                    "Escriba la coordenada Y del punto: ",
                    "",
                    "El punto está dentro de la circunferencia.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Punto dentro/fuera/sobre la circunferencia (4º cuadrante)
        cx = random.randrange(-100, 101)
        cy = random.randrange(-100, 101)
        r = random.randrange(10, 101)
        rx = random.randrange(0, r)
        ry = (r ** 2 - rx ** 2) ** 0.5
        n = random.choice([1, 2, 3])
        if n == 1:
            x = cx + rx
            y = cy + ry
            t = "El punto está sobre la circunferencia."
        elif n == 2:
            x = cx - rx - random.randrange(1, 5)
            y = cy + ry + random.randrange(1, 5)
            t = "El punto está fuera de la circunferencia."
        else:
            x = cx - rx + random.randrange(1, 5)
            y = cy - ry + random.randrange(1, 5)
            t = "El punto está dentro de la circunferencia."

        mpts_common.add_test(
            LAST_TEST,
            ["input", [cx / 10, cy / 10, r / 10, x / 10, y / 10]],
            [
                "output",
                [
                    "PUNTO Y CIRCUNFERENCIA",
                    "",
                    "Escriba la coordenada X del centro de la circunferencia: ",
                    "Escriba la coordenada Y del centro de la circunferencia: ",
                    "Escriba el radio de la circunferencia: ",
                    "",
                    "Escriba la coordenada X del punto: ",
                    "Escriba la coordenada Y del punto: ",
                    "",
                    t,
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Exercise 151621 END

    elif exercise_id == 1516_22:
        # Exercise 151622 BEGINNING
        # /examenes/15-16/examen-160608.html

        # Valor negativo
        a = random.randrange(-100, 101)
        n = -random.randrange(1, 101)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, n]],
            [
                "output",
                [
                    "REPETICIONES",
                    "",
                    "Escriba un número entero: ",
                    "¿Cuántos números va a escribir? ",
                    "",
                    f"¡Valor incorrecto! No puede escribir {n} números.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Cero
        a = random.randrange(-100, 101)
        n = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, n]],
            [
                "output",
                [
                    "REPETICIONES",
                    "",
                    "Escriba un número entero: ",
                    "¿Cuántos números va a escribir? ",
                    "",
                    f"¡Valor incorrecto! No puede escribir {n} números.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Varios valores, más iguales que diferentes
        a = random.randrange(-100, 101)
        ni = random.randrange(2, 10)
        nd = random.randrange(1, ni)
        todos = list(range(-100, 100))
        todos.remove(a)
        num = random.sample(todos, nd)
        for _ in range(ni):
            num += [a]
        random.shuffle(num)
        num = [a, ni+nd] + num

        tmp_output = [
            "REPETICIONES",
            "",
            "Escriba un número entero: ",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(ni + nd):
            tmp_output += ["Escriba un número entero: "]
        tmp_output += [
            "",
            f"Ha escrito más veces el número {a} que el resto de números.",
            "",
            "Programa terminado",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Varios valores, más iguales que diferentes
        a = random.randrange(-100, 101)
        nd = random.randrange(2, 10)
        ni = random.randrange(1, nd)
        todos = list(range(-100, 100))
        todos.remove(a)
        num = random.sample(todos, nd)
        for _ in range(ni):
            num += [a]
        random.shuffle(num)
        num = [a, ni+nd] + num

        tmp_output = [
            "REPETICIONES",
            "",
            "Escriba un número entero: ",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(ni + nd):
            tmp_output += ["Escriba un número entero: "]
        tmp_output += [
            "",
            f"Ha escrito menos veces el número {a} que el resto de números.",
            "",
            "Programa terminado",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Varios valores, las mismas veeces iguales que diferentes
        a = random.randrange(-100, 101)
        nd = random.randrange(2, 10)
        ni = nd
        todos = list(range(-100, 100))
        todos.remove(a)
        num = random.sample(todos, nd)
        for _ in range(ni):
            num += [a]
        random.shuffle(num)
        num = [a, ni+nd] + num

        tmp_output = [
            "REPETICIONES",
            "",
            "Escriba un número entero: ",
            "¿Cuántos números va a escribir? ",
            "",
        ]
        for _ in range(ni + nd):
            tmp_output += ["Escriba un número entero: "]
        tmp_output += [
            "",
            f"Ha escrito tantas veces el número {a} como el resto de números.",
            "",
            "Programa terminado",
        ]
        mpts_common.add_test(
            LAST_TEST, ["input", num], ["output", tmp_output],
        )

        # Exercise 151622 END

    elif exercise_id == 1516_31:
        # Exercise 151631 BEGINNING
        # /examenes/15-16/examen-160628.html

        # Elección incorrecta
        opcion = "c"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Debe escribir a o b.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Litros incorrecto
        opcion = "a"
        l = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, l]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir litros en galones y pintas",
                    "Número de litros: ",
                    "No puede escribir valores negativos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Litros (entero) a galones y pintas
        opcion = "a"
        l = float(random.randrange(0, 11))
        g = int(l // (8 * 0.56826))
        p = round(l % (8 * 0.56826) / 0.56826, 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, l]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir litros en galones y pintas",
                    "Número de litros: ",
                    f"{l} litros son {g} galones y {p} pintas.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Litros (decimal) a galones y pintas
        opcion = "a"
        l = float(random.randrange(0, 1100)) / 100
        g = int(l // (8 * 0.56826))
        p = round(l % (8 * 0.56826) / 0.56826, 1)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, l]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir litros en galones y pintas",
                    "Número de litros: ",
                    f"{l} litros son {g} galones y {p} pintas.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Galones y pintas negativos
        opcion = "b"
        g = -random.randrange(1, 11)
        p = float(random.randrange(1, 11))

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, g, p]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir galones y pintas en litros",
                    "Número de galones: ",
                    "Número de pintas: ",
                    "No puede escribir valores negativos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Galones y pintas negativos
        opcion = "b"
        g = random.randrange(1, 11)
        p = float(-random.randrange(1, 11))

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, g, p]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir galones y pintas en litros",
                    "Número de galones: ",
                    "Número de pintas: ",
                    "No puede escribir valores negativos.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Galones y pintas (enteras) a litros
        opcion = "b"
        g = random.randrange(1, 11)
        p = float(random.randrange(1, 11))
        l = round(g * 8 * 0.56826 + p * 0.56826, 2)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [opcion, g, p]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir galones y pintas en litros",
                    "Número de galones: ",
                    "Número de pintas: ",
                    f"{g} galones y {p} pintas son {l} litros.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Galones y pintas (decimal) a litros
        opcion = "b"
        g = random.randrange(1, 11)
        p = random.randrange(1, 110) / 10
        l = round(g * 8 * 0.56826 + p * 0.56826, 2)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [opcion, g, p]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros.",
                    "",
                    "Elija una opción: ",
                    "",
                    "Convertir galones y pintas en litros",
                    "Número de galones: ",
                    "Número de pintas: ",
                    f"{g} galones y {p} pintas son {l} litros.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Exercise 151631 END
