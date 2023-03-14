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

    elif exercise_id == 2021_22:
        # Exercise 202122 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210526.html

        # Si M es el grande, m el pequeño y c el intermedio, hay 13 combinaciones posibles:
        # Mmc, Mcm, mMc, mcM, cMm, cmM, Mmm, mMm, mmM, mMM, MmM, MMm, MMM
        # Así que he hecho ocho pruebas, repartiendo las combinaciones entre los dos jugadores
        # y repitiendo el caso MMM. En tres gana Cubitus, en tres gana Humerus y en dos empatan.

        # C: Mmc, H: mmM, gana Cubitus
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = random.randrange(1, Cp)  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [CM, Cm, Cc, Hm, Hm, HM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {CM} {Cm} {Cc} => {Cp} puntos",
                    f"Tirada de Humerus: {Hm} {Hm} {HM} => {Hp} puntos",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # C: Mcm, H: mMM, gana Humerus
        Cp = random.randrange(2, 5)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = random.randrange(1 + Cp, 6)  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [CM, Cc, Cm, Hm, HM, HM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {CM} {Cc} {Cm} => {Cp} puntos",
                    f"Tirada de Humerus: {Hm} {HM} {HM} => {Hp} puntos",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # C: mMc, H: MmM, empate
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = Cp  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [Cm, CM, Cc, HM, Hm, HM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {Cm} {CM} {Cc} => {Cp} puntos",
                    f"Tirada de Humerus: {HM} {Hm} {HM} => {Hp} puntos",
                    "Han empatado.",
                ],
            ],
        )

        # C: mcM, H: MMm, gana Humerus La forma de calcular los valores es como el primero pero intercambio los valores para que gane Humerus
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = random.randrange(1, Cp)  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [HM, HM, Hm, Cm, Cc, CM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {HM} {HM} {Hm} => {Hp} puntos",
                    f"Tirada de Humerus: {Cm} {Cc} {CM} => {Cp} puntos",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # C: cMm, H: Mmm, gana Cubitus La forma de calcular los valores es como el segundo pero intercambio los valores para que gane Cubitus
        Cp = random.randrange(2, 5)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = random.randrange(1 + Cp, 6)  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            [
                "random",
                [
                    HM,
                    Hm,
                    Hm,
                    Cc,
                    CM,
                    Cm,
                ],
            ],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {HM} {Hm} {Hm} => {Hp} puntos",
                    f"Tirada de Humerus: {Cc} {CM} {Cm} => {Cp} puntos",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # C: cmM, H: mMm, empate La forma de calcular los valores es como el tercero pero intercambio los valores
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        Hp = Cp  # Puntos de Humerus
        HM = random.randrange(1 + Hp, 7)
        Hm = HM - Hp
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [Hm, HM, Hm, Cc, Cm, CM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {Hm} {HM} {Hm} => {Hp} puntos",
                    f"Tirada de Humerus: {Cc} {Cm} {CM} => {Cp} puntos",
                    "Han empatado.",
                ],
            ],
        )

        # C: mcM, H: MMM, gana Cubitus La forma de calcular los valores de Cubitus es como el primero
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        HM = random.randrange(1, 7)  # Puntos de Humerus
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [Cm, Cc, CM, HM, HM, HM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {Cm} {Cc} {CM} => {Cp} puntos",
                    f"Tirada de Humerus: {HM} {HM} {HM} => 0 puntos",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # C: mcM, H: MMM, gana Cubitus La forma de calcular los valores de Cubitus es como el anterior pero intercambio los valores
        Cp = random.randrange(2, 6)  # Puntos de Cubitus
        CM = random.randrange(1 + Cp, 7)
        Cm = CM - Cp
        Cc = random.randrange(1 + Cm, CM)

        HM = random.randrange(1, 7)  # Puntos de Humerus
        mpts_common.add_test(
            LAST_TEST,
            ["random", [HM, HM, HM, Cm, Cc, CM]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Tirada de Cubitus: {HM} {HM} {HM} => 0 puntos",
                    f"Tirada de Humerus: {Cm} {Cc} {CM} => {Cp} puntos",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # Exercise 202122 END

    elif exercise_id == 2021_23:
        # Exercise 202123 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210526.html

        # Si M es el grande, m el pequeño y c el intermedio, hay 13 combinaciones posibles:
        # Mmc, Mcm, mMc, mcM, cMm, cmM, Mmm, mMm, mmM, mMM, MmM, MMm, MMM
        # Así que he hecho ocho pruebas, repartiendo las combinaciones entre los dos jugadores
        # y repitiendo el caso MMM. En tres gana Cubitus, en tres gana Humerus y en dos empatan.

        # Número de partidas incorrecto
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "¿Cuántos turnos va a tener la partida? ",
                    "",
                    "¡La partida debe tener al menos un turno!",
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
                    "JUEGO DE DADOS (2)",
                    "¿Cuántos turnos va a tener la partida? ",
                    "",
                    "¡La partida debe tener al menos un turno!",
                ],
            ],
        )

        # 1 turno Gana Cubitus
        n = 1
        c = [
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
        ]
        d = random.randrange(1, 7)
        while not d in c:
            d = random.randrange(1, 7)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", c + [d]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "¿Cuántos turnos va a tener la partida? ",
                    "",
                    "Turno 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
                    f"  Tirada de Humerus: {d}",
                    "  Punto para Cubitus",
                    "",
                    "Ha ganado Cubitus (1 a 0).",
                ],
            ],
        )

        # 1 turno Gana Humerus
        n = 1
        c = [
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
        ]
        d = random.randrange(1, 7)
        while d in c:
            d = random.randrange(1, 7)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", c + [d]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "¿Cuántos turnos va a tener la partida? ",
                    "",
                    "Turno 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
                    f"  Tirada de Humerus: {d}",
                    "  Punto para Humerus",
                    "",
                    "Ha ganado Humerus (1 a 0).",
                ],
            ],
        )

        # 2 turnos Gana Cubitus
        n = 2
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        for i in range(n):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while not (d in c):
                d = random.randrange(1, 7)
            tmp_random += c + [d]
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
                f"  Tirada de Humerus: {d}",
                "  Punto para Cubitus",
                "",
            ]
        tmp_output += ["Ha ganado Cubitus (2 a 0)."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # 2 turnos Gana Humerus
        n = 2
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        for i in range(n):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while d in c:
                d = random.randrange(1, 7)
            tmp_random += c + [d]
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
                f"  Tirada de Humerus: {d}",
                "  Punto para Humerus",
                "",
            ]
        tmp_output += ["Ha ganado Humerus (2 a 0)."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # 2 turnos Empatan
        n = 2
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        c = [
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
        ]
        d = random.randrange(1, 7)
        while not d in c:
            d = random.randrange(1, 7)
        tmp_random += c + [d]
        tmp_output += [
            "Turno 1",
            f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
            f"  Tirada de Humerus: {d}",
            "  Punto para Cubitus",
            "",
        ]
        c = [
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
            random.randrange(1, 7),
        ]
        d = random.randrange(1, 7)
        while d in c:
            d = random.randrange(1, 7)
        tmp_random += c + [d]
        tmp_output += [
            "Turno 2",
            f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]}",
            f"  Tirada de Humerus: {d}",
            "  Punto para Humerus",
            "",
        ]
        tmp_output += ["Han empatado (a 1)."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # n turnos Gana Cubitus
        n1 = random.randrange(2, 5)
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        for i in range(n1):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while not d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Cubitus"]]
        n2 = random.randrange(1, n1)
        for i in range(n2):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Humerus"]]
        random.shuffle(tmp_random)
        tmp_random_2 = []
        for i in range(len(tmp_random)):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_random[i][0]} {tmp_random[i][1]} {tmp_random[i][2]} {tmp_random[i][3]}",
                f"  Tirada de Humerus: {tmp_random[i][4]}",
                f"  Punto para {tmp_random[i][5]}",
                "",
            ]
            tmp_random_2 += [tmp_random[i][0], tmp_random[i][1], tmp_random[i][2], tmp_random[i][3], tmp_random[i][4]]
        tmp_output += [f"Ha ganado Cubitus ({n1} a {n2})."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n1 + n2]],
            ["random", tmp_random_2],
            ["output", tmp_output],
        )

        # n turnos Gana Humerus
        n1 = random.randrange(2, 5)
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        for i in range(n1):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Humerus"]]
        n2 = random.randrange(1, n1)
        for i in range(n2):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while not d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Cubitus"]]
        random.shuffle(tmp_random)
        tmp_random_2 = []
        for i in range(len(tmp_random)):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_random[i][0]} {tmp_random[i][1]} {tmp_random[i][2]} {tmp_random[i][3]}",
                f"  Tirada de Humerus: {tmp_random[i][4]}",
                f"  Punto para {tmp_random[i][5]}",
                "",
            ]
            tmp_random_2 += [tmp_random[i][0], tmp_random[i][1], tmp_random[i][2], tmp_random[i][3], tmp_random[i][4]]
        tmp_output += [f"Ha ganado Humerus ({n1} a {n2})."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n1 + n2]],
            ["random", tmp_random_2],
            ["output", tmp_output],
        )

        # n turnos Empatan
        n1 = random.randrange(2, 5)
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (2)",
            "¿Cuántos turnos va a tener la partida? ",
            "",
        ]
        for i in range(n1):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Humerus"]]
        n2 = n1
        for i in range(n2):
            c = [
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
                random.randrange(1, 7),
            ]
            d = random.randrange(1, 7)
            while not d in c:
                d = random.randrange(1, 7)
            tmp_random += [c + [d] + ["Cubitus"]]
        random.shuffle(tmp_random)
        tmp_random_2 = []
        for i in range(len(tmp_random)):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_random[i][0]} {tmp_random[i][1]} {tmp_random[i][2]} {tmp_random[i][3]}",
                f"  Tirada de Humerus: {tmp_random[i][4]}",
                f"  Punto para {tmp_random[i][5]}",
                "",
            ]
            tmp_random_2 += [tmp_random[i][0], tmp_random[i][1], tmp_random[i][2], tmp_random[i][3], tmp_random[i][4]]
        tmp_output += [f"Han empatado (a {n1})."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [n1 + n2]],
            ["random", tmp_random_2],
            ["output", tmp_output],
        )

        # Exercise 202123 END
