import datetime
import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 2021_11:
        # Exercise 202111 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210519.html

        caracteres = "abcdefghijklmnñopqrstuvwxyz1234567890"
        u_d = ["m", "km"]
        u_t = ["s", "h"]

        # Unidad de distancia no m/km
        ud = "m"
        while ud in u_d:
            ud = ""
            for _ in range(random.randrange(1, 3)):
                ud += caracteres[random.randrange(len(caracteres))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [ud]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "La unidad de distancia que ha indicado no es m o km.",
                ],
            ],
        )

        # Unidad de tiempo no s/h
        ud = u_d[random.randrange(2)]
        d = random.randrange(500)
        ut = "s"
        while ut in u_t:
            ut = ""
            for _ in range(random.randrange(1, 3)):
                ut += caracteres[random.randrange(len(caracteres))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [ud, d, ut]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "Distancia recorrida: ",
                    "Unidad de tiempo (s o h): ",
                    "La unidad de tiempo que ha indicado no es s o h.",
                ],
            ],
        )

        # distancia m (entero) / tiempo s (entero)
        d = float(random.randrange(999))
        t = float(random.randrange(999))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", ["m", d, "s", t]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "Distancia recorrida: ",
                    "Unidad de tiempo (s o h): ",
                    "Tiempo empleado: ",
                    f"Si ha recorrido {d} m en {t} s su velocidad ha sido {round(d / t, 1)} m/s ({round(d / t * 3.6, 1)} km/h).",
                ],
            ],
        )

        # distancia m (entero) / tiempo h (decimal)
        d = float(random.randrange(99999))
        t = float(random.randrange(999) / 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", ["m", d, "h", t]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "Distancia recorrida: ",
                    "Unidad de tiempo (s o h): ",
                    "Tiempo empleado: ",
                    f"Si ha recorrido {d} m en {t} h su velocidad ha sido {round(d / t / 3600, 1)} m/s ({round(d / t / 1000, 1)} km/h).",
                ],
            ],
        )

        # distancia km (decimal) / tiempo s (entero)
        d = float(random.randrange(99999) / 1000)
        t = float(random.randrange(999))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", ["km", d, "s", t]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "Distancia recorrida: ",
                    "Unidad de tiempo (s o h): ",
                    "Tiempo empleado: ",
                    f"Si ha recorrido {d} km en {t} s su velocidad ha sido {round(d / t * 1000, 1)} m/s ({round(d / t * 3600 , 1)} km/h).",
                ],
            ],
        )

        # distancia km (decimal) / tiempo h (decimal)
        d = float(random.randrange(99999) / 1000)
        t = float(random.randrange(999) / 100)
        mpts_common.add_test(
            LAST_TEST,
            ["input", ["km", d, "h", t]],
            [
                "output",
                [
                    "VELOCIDAD",
                    "Unidad de distancia (m o km): ",
                    "Distancia recorrida: ",
                    "Unidad de tiempo (s o h): ",
                    "Tiempo empleado: ",
                    f"Si ha recorrido {d} km en {t} h su velocidad ha sido {round(d / t / 3.6, 1)} m/s ({round(d / t, 1)} km/h).",
                ],
            ],
        )

        # Exercise 202111 END

    elif exercise_id == 2021_12:
        # Exercise 202112 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210519.html

        # Número de partidas incorrecto
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántas veces se va a tirar el dado? ",
                    "",
                    "¡No se puede tirar menos de una vez el dado!",
                ],
            ],
        )

        # Número de partidas incorrecto
        n = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántas veces se va a tirar el dado? ",
                    "",
                    "¡No se puede tirar menos de una vez el dado!",
                ],
            ],
        )

        # Una partida, gana Cubitus
        n = 1
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        a = 2 * random.randrange(1, 4)
        tmp_output += [
            f"Tirada 1: {a}",
            f"Total: {a} => Punto para Cubitus",
            "Puntuación acumulada: Cubitus 1 - Humerus 0",
            "",
            "Ha ganado Cubitus.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", [a]], ["output", tmp_output]
        )

        # Una partida, gana Humerus
        n = 1
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        a = 1 + 2 * random.randrange(0, 3)
        tmp_output += [
            f"Tirada 1: {a}",
            f"Total: {a} => Punto para Humerus",
            "Puntuación acumulada: Cubitus 0 - Humerus 1",
            "",
            "Ha ganado Humerus.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", [a]], ["output", tmp_output]
        )

        # Dos partidas, gana Cubitus
        n = 2
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        a = 2 * random.randrange(1, 4)
        b = 2 * random.randrange(1, 4)
        tmp_output += [
            f"Tirada 1: {a}",
            f"Total: {a} => Punto para Cubitus",
            "Puntuación acumulada: Cubitus 1 - Humerus 0",
            "",
            f"Tirada 2: {b}",
            f"Total: {a + b} => Punto para Cubitus",
            "Puntuación acumulada: Cubitus 2 - Humerus 0",
            "",
            "Ha ganado Cubitus.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", [a, b]], ["output", tmp_output]
        )

        # Dos partidas, gana Humerus
        n = 2
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        a = 1 + 2 * random.randrange(0, 3)
        b = 2 * random.randrange(1, 4)
        tmp_output += [
            f"Tirada 1: {a}",
            f"Total: {a} => Punto para Humerus",
            "Puntuación acumulada: Cubitus 0 - Humerus 1",
            "",
            f"Tirada 2: {b}",
            f"Total: {a + b} => Punto para Humerus",
            "Puntuación acumulada: Cubitus 0 - Humerus 2",
            "",
            "Ha ganado Humerus.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", [a, b]], ["output", tmp_output]
        )

        # Dos partidas, empate
        n = 2
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        a = 1 + 2 * random.randrange(0, 3)
        b = 1 + 2 * random.randrange(1, 4)
        tmp_output += [
            f"Tirada 1: {a}",
            f"Total: {a} => Punto para Humerus",
            "Puntuación acumulada: Cubitus 0 - Humerus 1",
            "",
            f"Tirada 2: {b}",
            f"Total: {a + b} => Punto para Cubitus",
            "Puntuación acumulada: Cubitus 1 - Humerus 1",
            "",
            "Han empatado.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", [a, b]], ["output", tmp_output]
        )

        # Varias partidas
        n = random.randrange(4, 7)
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántas veces se va a tirar el dado? ",
            "",
        ]
        total = cubitus = humerus = 0
        dados = []
        for i in range(1, n + 1):
            d = random.randrange(1, 7)
            total += d
            dados += [d]
            if total % 2 == 0:
                cubitus += 1
                tmp_output += [
                    f"Tirada {i}: {d}",
                    f"Total: {total} => Punto para Cubitus",
                    f"Puntuación acumulada: Cubitus {cubitus} - Humerus {humerus}",
                    "",
                ]
            else:
                humerus += 1
                tmp_output += [
                    f"Tirada {i}: {d}",
                    f"Total: {total} => Punto para Humerus",
                    f"Puntuación acumulada: Cubitus {cubitus} - Humerus {humerus}",
                    "",
                ]
        if cubitus > humerus:
            tmp_output += ["Ha ganado Cubitus."]
        elif humerus > cubitus:
            tmp_output += ["Ha ganado Humerus."]
        else:
            tmp_output += ["Han empatado."]

        mpts_common.add_test(
            LAST_TEST, ["input", [n]], ["random", dados], ["output", tmp_output]
        )

        # Exercise 202112 END

    elif exercise_id == 2021_13:
        # Exercise 202113 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210519.html

        # Fallar a la primera
        a = random.randrange(1, 51)
        b = random.randrange(1, 51)
        while b == a:
            b = random.randrange(1, 51)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a]],
            ["input", [b]],
            [
                "output",
                [
                    "SUMAR Y GANAR",
                    "Vaya sumando todos los números que le iré diciendo.",
                    "Empezamos por 0.",
                    f"Más {a}: ",
                    "¿Ha entendido el juego?",
                ],
            ],
        )

        # Fallar a la segunda
        a = random.randrange(1, 51)
        b = random.randrange(1, 51)
        c = random.randrange(1, 51)
        while c == b:
            c = random.randrange(1, 51)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b]],
            ["input", [a, a + c]],
            [
                "output",
                [
                    "SUMAR Y GANAR",
                    "Vaya sumando todos los números que le iré diciendo.",
                    "Empezamos por 0.",
                    f"Más {a}: ",
                    f"Más {b}: ",
                    "¡Repase las sumas antes de jugar!",
                ],
            ],
        )

        # Fallar a la tercera
        n = 3
        tmp_random = [random.randrange(1, 51)]
        tmp_input = [tmp_random[0]]
        tmp_output = [
            "SUMAR Y GANAR",
            "Vaya sumando todos los números que le iré diciendo.",
            "Empezamos por 0.",
            f"Más {tmp_random[0]}: ",
        ]
        for i in range(1, n - 1):
            tmp_random += [random.randrange(1, 51)]
            tmp_input += [tmp_input[i - 1] + tmp_random[i]]
            tmp_output += [f"Más {tmp_random[i]}: "]
        a = random.randrange(1, 51)
        b = random.randrange(1, 51)
        while b == a:
            b = random.randrange(1, 51)
        tmp_random += [a]
        tmp_input += [tmp_input[n - 2] + b]
        tmp_output += [f"Más {tmp_random[-1]}: "]
        tmp_output += [f"¡Ha acertado {n-1} veces seguidas!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", tmp_random],
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Fallar a la cuarta
        n = 4
        tmp_random = [random.randrange(1, 51)]
        tmp_input = [tmp_random[0]]
        tmp_output = [
            "SUMAR Y GANAR",
            "Vaya sumando todos los números que le iré diciendo.",
            "Empezamos por 0.",
            f"Más {tmp_random[0]}: ",
        ]
        for i in range(1, n - 1):
            tmp_random += [random.randrange(1, 51)]
            tmp_input += [tmp_input[i - 1] + tmp_random[i]]
            tmp_output += [f"Más {tmp_random[i]}: "]
        a = random.randrange(1, 51)
        b = random.randrange(1, 51)
        while b == a:
            b = random.randrange(1, 51)
        tmp_random += [a]
        tmp_input += [tmp_input[n - 2] + b]
        tmp_output += [f"Más {tmp_random[-1]}: "]
        tmp_output += [f"¡Ha acertado {n-1} veces seguidas!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", tmp_random],
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Fallar después de n
        n = random.randrange(5, 8)
        tmp_random = [random.randrange(1, 51)]
        tmp_input = [tmp_random[0]]
        tmp_output = [
            "SUMAR Y GANAR",
            "Vaya sumando todos los números que le iré diciendo.",
            "Empezamos por 0.",
            f"Más {tmp_random[0]}: ",
        ]
        for i in range(1, n - 1):
            tmp_random += [random.randrange(1, 51)]
            tmp_input += [tmp_input[i - 1] + tmp_random[i]]
            tmp_output += [f"Más {tmp_random[i]}: "]
        a = random.randrange(1, 51)
        b = random.randrange(1, 51)
        while b == a:
            b = random.randrange(1, 51)
        tmp_random += [a]
        tmp_input += [tmp_input[n - 2] + b]
        tmp_output += [f"Más {tmp_random[-1]}: "]
        tmp_output += [f"¡Ha acertado {n-1} veces seguidas!"]
        mpts_common.add_test(
            LAST_TEST,
            ["random", tmp_random],
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 202113 END
