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
            while not d in c:
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
        for i, tmp_r in enumerate(tmp_random):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_r[0]} {tmp_r[1]} {tmp_r[2]} {tmp_r[3]}",
                f"  Tirada de Humerus: {tmp_r[4]}",
                f"  Punto para {tmp_r[5]}",
                "",
            ]
            tmp_random_2 += [tmp_r[0], tmp_r[1], tmp_r[2], tmp_r[3], tmp_r[4]]
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
        for i, tmp_r in enumerate(tmp_random):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_r[0]} {tmp_r[1]} {tmp_r[2]} {tmp_r[3]}",
                f"  Tirada de Humerus: {tmp_r[4]}",
                f"  Punto para {tmp_r[5]}",
                "",
            ]
            tmp_random_2 += [tmp_r[0], tmp_r[1], tmp_r[2], tmp_r[3], tmp_r[4]]
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
        for i, tmp_r in enumerate(tmp_random):
            tmp_output += [
                f"Turno {i + 1}",
                f"  Tirada de Cubitus: {tmp_r[0]} {tmp_r[1]} {tmp_r[2]} {tmp_r[3]}",
                f"  Tirada de Humerus: {tmp_r[4]}",
                f"  Punto para {tmp_r[5]}",
                "",
            ]
            tmp_random_2 += [tmp_r[0], tmp_r[1], tmp_r[2], tmp_r[3], tmp_r[4]]
        tmp_output += [f"Han empatado (a {n1})."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [n1 + n2]],
            ["random", tmp_random_2],
            ["output", tmp_output],
        )

        # Exercise 202123 END

    elif exercise_id == 2021_31:
        # Exercise 202131 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210602.html

        meses = [
            ["enero", 31, 0],
            ["febrero", 28, 31],
            ["marzo", 31, 59],
            ["abril", 30, 90],
            ["mayo", 31, 120],
            ["junio", 30, 151],
            ["julio", 31, 181],
            ["agosto", 31, 212],
            ["septiembre", 30, 243],
            ["octubre", 31, 273],
            ["noviembre", 30, 304],
            ["diciembre", 31, 334],
        ]

        # Día 0 incorrecto
        d = 0
        mes_d = random.choice(meses)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d, mes_d[0]]],
            [
                "output",
                [
                    "CALENDARIO LUNAR",
                    "Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.",
                    "Indique el día: ",
                    "Indique el mes: ",
                    f"El día {d} de {mes_d[0]} no existe.",
                ],
            ],
        )

        # Día negativo incorrecto
        d = -random.randrange(1, 31)
        mes_d = random.choice(meses)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d, mes_d[0]]],
            [
                "output",
                [
                    "CALENDARIO LUNAR",
                    "Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.",
                    "Indique el día: ",
                    "Indique el mes: ",
                    f"El día {d} de {mes_d[0]} no existe.",
                ],
            ],
        )

        # Día posterior al último del mes incorrecto
        for mes_d in meses:
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", [mes_d[1] + 1, mes_d[0]]],
                [
                    "output",
                    [
                        "CALENDARIO LUNAR",
                        "Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.",
                        "Indique el día: ",
                        "Indique el mes: ",
                        f"El día {mes_d[1] + 1} de {mes_d[0]} no existe.",
                    ],
                ],
            )

        # Día correcto
        for mes_d in meses:
            d = random.randrange(1, mes_d[1] + 1)
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", [d, mes_d[0]]],
                [
                    "output",
                    [
                        "CALENDARIO LUNAR",
                        "Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.",
                        "Indique el día: ",
                        "Indique el mes: ",
                        f"El día {d} de {mes_d[0]} es el día {mes_d[2] + d} del año.",
                        f"Habrán pasado {int((mes_d[2] + d) // 29.53)} lunas y {round((mes_d[2] + d) % 29.53, 2)} días.",
                    ],
                ],
            )

        # Nombre de mes incorrecto
        letras = "abcdefghijklmnñopqrstuvwxyz"
        d = random.randrange(1, 29)
        mes = ""
        for _ in range(random.randrange(5, 10)):
            mes += random.choice(letras)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [d, mes]],
            [
                "output",
                [
                    "CALENDARIO LUNAR",
                    "Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.",
                    "Indique el día: ",
                    "Indique el mes: ",
                    f"El mes {mes} no existe.",
                ],
            ],
        )

        # Exercise 202131 END

    elif exercise_id == 2021_32:
        # Exercise 202132 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210602.html

        def dados_202132(gana):
            d = []
            for _ in range(7):
                d += [random.randrange(1, 7)]
            resC = d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]
            resH = (
                d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]
            )
            if gana == "Cubitus":
                while resC <= resH:
                    d = []
                    for _ in range(7):
                        d += [random.randrange(1, 7)]
                    resC = (
                        d[0] % 2 * d[0]
                        + d[1] % 2 * d[1]
                        + d[2] % 2 * d[2]
                        + d[3] % 2 * d[3]
                    )
                    resH = (
                        d[4]
                        - d[4] % 2 * d[4]
                        + d[5]
                        - d[5] % 2 * d[5]
                        + d[6]
                        - d[6] % 2 * d[6]
                    )
            elif gana == "Humerus":
                while resC >= resH:
                    d = []
                    for _ in range(7):
                        d += [random.randrange(1, 7)]
                    resC = (
                        d[0] % 2 * d[0]
                        + d[1] % 2 * d[1]
                        + d[2] % 2 * d[2]
                        + d[3] % 2 * d[3]
                    )
                    resH = (
                        d[4]
                        - d[4] % 2 * d[4]
                        + d[5]
                        - d[5] % 2 * d[5]
                        + d[6]
                        - d[6] % 2 * d[6]
                    )
            else:
                while resC != resH:
                    d = []
                    for _ in range(7):
                        d += [random.randrange(1, 7)]
                    resC = (
                        d[0] % 2 * d[0]
                        + d[1] % 2 * d[1]
                        + d[2] % 2 * d[2]
                        + d[3] % 2 * d[3]
                    )
                    resH = (
                        d[4]
                        - d[4] % 2 * d[4]
                        + d[5]
                        - d[5] % 2 * d[5]
                        + d[6]
                        - d[6] % 2 * d[6]
                    )
            return d

        # Número de turnos incorrecto 0
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántos turnos va a tener la partida? ",
                    "¡La partida debe tener al menos un turno!",
                ],
            ],
        )

        # Número de turnos incorrecto negativo
        n = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántos turnos va a tener la partida? ",
                    "¡La partida debe tener al menos un turno!",
                ],
            ],
        )

        # 1 turno. Gana Cubitus
        n = 1
        d = dados_202132("Cubitus")
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántos turnos va a tener la partida? ",
                    "  Turno 1",
                    f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                    f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
                    "Ha ganado Cubitus (1 a 0).",
                ],
            ],
        )

        # 1 turno. Gana Humerus
        n = 1
        d = dados_202132("Humerus")
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántos turnos va a tener la partida? ",
                    "  Turno 1",
                    f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                    f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
                    "Ha ganado Humerus (1 a 0).",
                ],
            ],
        )

        # 1 turno. Empate
        n = 1
        d = dados_202132("Empate")
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS",
                    "¿Cuántos turnos va a tener la partida? ",
                    "  Turno 1",
                    f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                    f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
                    "Han empatado (a 0).",
                ],
            ],
        )

        # n turnos. Gana Cubitus
        nc = random.randrange(2, 6)
        nh = random.randrange(nc)
        ne = random.randrange(1, 5)
        dt = []
        for _ in range(nc):
            dt += [dados_202132("Cubitus")]
        for _ in range(nh):
            dt += [dados_202132("Humerus")]
        for _ in range(ne):
            dt += [dados_202132("Empate")]
        random.shuffle(dt)
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántos turnos va a tener la partida? ",
        ]
        dt2 = []
        for i, d in enumerate(dt):
            dt2 += d
            tmp_output += [
                f"  Turno {i+1}",
                f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
            ]
        tmp_output += [f"Ha ganado Cubitus ({nc} a {nh})."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [nc + nh + ne]],
            ["random", dt2],
            ["output", tmp_output],
        )

        # n turnos. Gana Humerus
        nh = random.randrange(2, 6)
        nc = random.randrange(nh)
        ne = random.randrange(1, 5)
        dt = []
        for _ in range(nc):
            dt += [dados_202132("Cubitus")]
        for _ in range(nh):
            dt += [dados_202132("Humerus")]
        for _ in range(ne):
            dt += [dados_202132("Empate")]
        random.shuffle(dt)
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántos turnos va a tener la partida? ",
        ]
        dt2 = []
        for i, d in enumerate(dt):
            dt2 += d
            tmp_output += [
                f"  Turno {i+1}",
                f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
            ]
        tmp_output += [f"Ha ganado Humerus ({nh} a {nc})."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [nc + nh + ne]],
            ["random", dt2],
            ["output", tmp_output],
        )

        # n turnos. Empate
        nc = random.randrange(2, 6)
        nh = nc
        ne = random.randrange(1, 5)
        dt = []
        for _ in range(nc):
            dt += [dados_202132("Cubitus")]
        for _ in range(nh):
            dt += [dados_202132("Humerus")]
        for _ in range(ne):
            dt += [dados_202132("Empate")]
        random.shuffle(dt)
        tmp_output = [
            "JUEGO DE DADOS",
            "¿Cuántos turnos va a tener la partida? ",
        ]
        dt2 = []
        for i, d in enumerate(dt):
            dt2 += d
            tmp_output += [
                f"  Turno {i+1}",
                f"    Tirada de Cubitus: {d[0]} {d[1]} {d[2]} {d[3]} => {d[0] % 2 * d[0] + d[1] % 2 * d[1] + d[2] % 2 * d[2] + d[3] % 2 * d[3]} puntos",
                f"    Tirada de Humerus: {d[4]} {d[5]} {d[6]} => {d[4] - d[4] % 2 * d[4] + d[5] - d[5] % 2 * d[5] + d[6] - d[6] % 2 * d[6]} puntos",
            ]
        tmp_output += [f"Han empatado (a {nc})."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [nc + nh + ne]],
            ["random", dt2],
            ["output", tmp_output],
        )

        # Exercise 202132 END

    elif exercise_id == 2021_33:
        # Exercise 202133 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210602.html

        def monedas_202133(lmax, lmaxn, parejas, lcarasmax):
            # genera una serie de ⚪⚪⚪✖✖✖✖⚪⚪⚪⚪✖✖✖⚪⚪✖✖✖
            # lmax: número de cruces máximo. lmaxn : nñúmero de veces que aparece ese máximo
            # lcarasmax: longitud máxima de los fragmentos de caras
            # parejas: número de secuencias caras+cruces
            lpos = []
            for _ in range(lmaxn):
                pos = random.randrange(parejas)
                while pos in lpos:
                    pos = random.randrange(parejas)
                lpos += [pos]
            d = []
            for i in range(parejas):
                for _ in range(random.randrange(1, lcarasmax + 1)):
                    d += "⚪"
                if i in lpos:
                    for _ in range(lmax):
                        d += "✖"
                else:
                    for _ in range(random.randrange(1, lmax)):
                        d += "✖"
            return d

        # Número de tiradas incorrecto 0
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "¡La moneda se debe tirar al menos dos veces!",
                ],
            ],
        )

        # Número de tiradas incorrecto 1
        n = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "¡La moneda se debe tirar al menos dos veces!",
                ],
            ],
        )

        # Número de tiradas incorrecto negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "¡La moneda se debe tirar al menos dos veces!",
                ],
            ],
        )

        # 2 tiradas: ⚪ ⚪
        n = 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", ["⚪", "⚪"]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "Tirada: ⚪ ⚪",
                    "No ha salido ninguna cruz.",
                ],
            ],
        )

        # 2 tiradas: ✖ ⚪
        n = 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", ["⚪", "✖"]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "Tirada: ⚪ ✖",
                    "Ha salido alguna cruz, pero no han llegado a salir dos cruces seguidas.",
                ],
            ],
        )

        # 2 tiradas: ⚪ ✖
        n = 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", ["✖", "⚪"]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "Tirada: ✖ ⚪",
                    "Ha salido alguna cruz, pero no han llegado a salir dos cruces seguidas.",
                ],
            ],
        )

        # 2 tiradas: ✖ ✖
        n = 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", ["✖", "✖"]],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    "Tirada: ✖ ✖",
                    "Se han llegado a obtener 2 cruces seguidas.",
                ],
            ],
        )

        # n tiradas: solo ⚪
        n = random.randrange(3, 10)
        tmp_choice = []
        tirada = ""
        for _ in range(n):
            tmp_choice += ["⚪"]
            tirada += " ⚪"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    "No ha salido ninguna cruz.",
                ],
            ],
        )

        # n tiradas: solo ✖
        n = random.randrange(3, 10)
        tmp_choice = []
        tirada = ""
        for _ in range(n):
            tmp_choice += ["✖"]
            tirada += " ✖"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {n} cruces seguidas.",
                ],
            ],
        )

        # cruces + caras/cruces, con 1 máximo inicial
        lmax = random.randrange(3, 10)
        tmp_choice = []
        for _ in range(lmax):
            tmp_choice += ["✖"]
        tmp_choice += monedas_202133(
            lmax - 1, 1, random.randrange(5, 10), random.randrange(5, 10)
        )
        tirada = ""
        for i in tmp_choice:
            tirada += f" {i}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [len(tmp_choice)]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {lmax} cruces seguidas.",
                ],
            ],
        )

        # caras/cruces, con 1 máximo final
        lmax = random.randrange(3, 10)
        tmp_choice = []
        tmp_choice += monedas_202133(
            lmax - 1, 1, random.randrange(5, 10), random.randrange(5, 10)
        )
        for _ in range(lmax - 2):
            tmp_choice += ["⚪"]
        for _ in range(lmax):
            tmp_choice += ["✖"]
        tirada = ""
        for i in tmp_choice:
            tirada += f" {i}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [len(tmp_choice)]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {lmax} cruces seguidas.",
                ],
            ],
        )

        # caras/cruces, con 1 máximo intermedio
        lmax = random.randrange(3, 10)
        tmp_choice = []
        tmp_choice += monedas_202133(
            lmax, 1, random.randrange(5, 10), random.randrange(5, 10)
        )
        tirada = ""
        for i in tmp_choice:
            tirada += f" {i}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [len(tmp_choice)]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {lmax} cruces seguidas.",
                ],
            ],
        )

        # cruces + caras/cruces, con 2 máximos máximo inicial + máximo
        lmax = random.randrange(3, 10)
        tmp_choice = []
        for _ in range(lmax):
            tmp_choice += ["✖"]
        tmp_choice += monedas_202133(
            lmax - 1, 2, random.randrange(5, 10), random.randrange(5, 10)
        )
        tirada = ""
        for i in tmp_choice:
            tirada += f" {i}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [len(tmp_choice)]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {lmax} cruces seguidas.",
                ],
            ],
        )

        # caras/cruces, con 2 máximos intermedios
        lmax = random.randrange(3, 10)
        tmp_choice = []
        tmp_choice += monedas_202133(
            lmax, 2, random.randrange(5, 10), random.randrange(5, 10)
        )
        tirada = ""
        for i in tmp_choice:
            tirada += f" {i}"
        mpts_common.add_test(
            LAST_TEST,
            ["input", [len(tmp_choice)]],
            ["choice", tmp_choice],
            [
                "output",
                [
                    "CRUCES SEGUIDAS",
                    "¿Cuántas veces se va a tirar la moneda? ",
                    f"Tirada:{tirada}",
                    f"Se han llegado a obtener {lmax} cruces seguidas.",
                ],
            ],
        )

        # Exercise 202133 END

    elif exercise_id == 2021_41:
        # Exercise 2021_41 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210622.html

        # Precios y descuento
        pv = 0.50
        pc = 0.75
        des = 1

        # Cantidad buñuelos vacíos incorrecta: valor negativo
        bv = -random.randrange(1, 10)
        bc = random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    "No puede indicar cantidades negativas.",
                ],
            ],
        )

        # Cantidad buñuelos calabaza incorrecta: valor negativo
        bv = -random.randrange(1, 10)
        bc = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    "No puede indicar cantidades negativas.",
                ],
            ],
        )

        # Cantidad buñuelos incorrecta: valores negativos
        bv = -random.randrange(1, 10)
        bc = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    "No puede indicar cantidades negativas.",
                ],
            ],
        )

        # Cantidad dinero incorrecto: valor negativo
        bv = random.randrange(1, 10)
        bc = random.randrange(1, 10)
        d = (bv + bc) // 12
        precio = bv * pv + bc * pc - d * des
        d = -random.randrange(1, 1000) / 100

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc, d]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    f"Son {precio} €",
                    "¿Cuánto dinero entrega? ",
                    "Debe entregar una cantidad positiva.",
                ],
            ],
        )

        # 0 buñuelos vacíos y sobra dinero
        bv = 0
        bc = random.randrange(1, 10)
        d = (bv + bc) // 12
        precio = bv * pv + bc * pc - d * des
        d = precio + random.randrange(1, 100) / 100

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc, d]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    f"Son {precio} €",
                    "¿Cuánto dinero entrega? ",
                    f"Su cambio son {round(d - precio, 2)} €.",
                ],
            ],
        )

        # 0 buñuelos rellenos y falta dinero
        bv = random.randrange(1, 10)
        bc = 0
        d = (bv + bc) // 12
        precio = bv * pv + bc * pc - d * des
        d = precio - random.randrange(1, precio * 100) / 100

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc, d]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    f"Son {precio} €",
                    "¿Cuánto dinero entrega? ",
                    f"No ha entregado bastante dinero. Le faltan {round(precio - d, 2)} €.",
                ],
            ],
        )

        # importe exacto, sin llegar a docena
        bv = random.randrange(1, 7)
        bc = random.randrange(1, 6)
        d = (bv + bc) // 12
        precio = bv * pv + bc * pc - d * des
        d = precio

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [bv, bc, d]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    f"Son {precio} €",
                    "¿Cuánto dinero entrega? ",
                    "Ha entregado la cantidad exacta.",
                ],
            ],
        )

        # importe exacto, varias docenas
        bv = random.randrange(30, 50)
        bc = random.randrange(30, 50)
        d = (bv + bc) // 12
        precio = bv * pv + bc * pc - d * des
        d = precio

        mpts_common.add_test(
            LAST_TEST,
            ["input", [bv, bc, d]],
            [
                "output",
                [
                    "PUESTO DE BUÑUELOS",
                    "¿Cuántos buñuelos vacíos quiere? ",
                    "¿Cuántos buñuelos de calabaza quiere? ",
                    f"Son {precio} €",
                    "¿Cuánto dinero entrega? ",
                    "Ha entregado la cantidad exacta.",
                ],
            ],
        )

        # Exercise 2021_41 END

    elif exercise_id == 2021_42:
        # Exercise 2021_42 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210622.html

        # Empatan varios dados
        ndc = random.randrange(2, 7)
        dc = [random.randrange(2, 7)]
        for _ in range(ndc - 1):
            dc += [random.randrange(1, 7)]
        random.shuffle(dc)
        ndh = random.randrange(2, 7)
        dh = [max(dc)]
        for _ in range(ndh - 1):
            dh += [random.randrange(1, max(dc))]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => {max(dh)} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Han empatado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ndc] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Gana Cubitus varios dados
        ndc = random.randrange(2, 7)
        dc = [random.randrange(2, 7)]
        for _ in range(ndc - 1):
            dc += [random.randrange(1, 7)]
        random.shuffle(dc)
        ndh = random.randrange(2, 7)
        dh = []
        for _ in range(ndh):
            dh += [random.randrange(1, max(dc))]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => {max(dh)} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Ha ganado Cubitus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ndc] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Gana Cubitus 1 dado
        dc = [random.randrange(2, 7)]
        ndh = random.randrange(2, 7)
        dh = []
        for _ in range(ndh):
            dh += [random.randrange(1, max(dc))]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "  Primera tirada de Cubitus: 1 dado",
        ]
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus: {dc[0]} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus: {dc[0]} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => {max(dh)} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Ha ganado Cubitus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [1] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Gana Cubitus Humerus 1 punto
        ndc = random.randrange(2, 7)
        dc = [random.randrange(2, 7)]
        for _ in range(ndc - 1):
            dc += [random.randrange(1, 7)]
        random.shuffle(dc)
        ndh = random.randrange(2, 7)
        dh = []
        for _ in range(ndh):
            dh += [1]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Ha ganado Cubitus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ndc] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Gana Humerus varios dados
        ndh = random.randrange(2, 7)
        dh = [random.randrange(2, 7)]
        for _ in range(ndh - 1):
            dh += [random.randrange(1, 7)]
        random.shuffle(dh)
        ndc = random.randrange(2, 7)
        dc = []
        for _ in range(ndc):
            dc += [random.randrange(1, max(dh))]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => {max(dh)} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Ha ganado Humerus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ndc] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Gana Humerus 1 dado
        dh = [random.randrange(2, 7)]
        ndc = random.randrange(2, 7)
        dc = []
        for _ in range(ndc):
            dc += [random.randrange(1, max(dh))]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        if max(dc) > 1:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => {max(dc)} puntos"]
        else:
            tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            "  Primera tirada de Humerus: 1 dado",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus: {dh[0]} => {dh[0]} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus: {dh[0]} => 1 punto"]
        tmp_output += ["  Ha ganado Humerus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ndc] + dc + [1] + dh],
            ["output", tmp_output],
        )

        # Gana Humerus Cubitus 1 punto
        ndh = random.randrange(2, 7)
        dh = [random.randrange(2, 7)]
        for _ in range(ndh - 1):
            dh += [random.randrange(1, 7)]
        random.shuffle(dh)
        ndc = random.randrange(2, 7)
        dc = []
        for _ in range(ndc):
            dc += [1]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            f"  Primera tirada de Cubitus: {ndc} dados",
        ]
        tiradac = ""
        for i in range(len(dc) - 1):
            tiradac += f" {dc[i]} -"
        tiradac += f" {dc[-1]}"
        tmp_output += [f"  Tirada de Cubitus:{tiradac} => 1 punto"]
        tmp_output += [
            f"  Primera tirada de Humerus: {ndh} dados",
        ]
        tiradah = ""
        for i in range(len(dh) - 1):
            tiradah += f" {dh[i]} -"
        tiradah += f" {dh[-1]}"
        if max(dh) > 1:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => {max(dh)} puntos"]
        else:
            tmp_output += [f"  Tirada de Humerus:{tiradah} => 1 punto"]
        tmp_output += ["  Ha ganado Humerus."]
        mpts_common.add_test(
            LAST_TEST,
            ["random", [ndc] + dc + [ndh] + dh],
            ["output", tmp_output],
        )

        # Exercise 2021_42 END

    elif exercise_id == 2021_43:
        # Exercise 2021_43 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210622.html

        # Gana Marcus varias tiradas
        nc = random.randrange(2, 10)
        dc = []
        for _ in range(nc - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dc += [t]
        dc += [5]
        nh = random.randrange(nc + 1, 15)
        dh = []
        for _ in range(nh - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dh += [t]
        dh += [5]
        tmp_output = ["SACAR UN CINCO"]
        tiradac = ""
        for i in dc:
            tiradac += f" {i}"
        tmp_output += [f"  Tiradas de Marcus:{tiradac}"]
        tmp_output += [f"  Marcus ha tenido que tirar {nc} veces."]
        tiradah = ""
        for i in dh:
            tiradah += f" {i}"
        tmp_output += [f"  Tiradas de Julius:{tiradah}"]
        tmp_output += [f"  Julius ha tenido que tirar {nh} veces."]
        tmp_output += ["  Ha ganado Marcus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Gana Marcus 1 tirada
        nc = 1
        dc = [5]
        nh = random.randrange(nc + 1, 15)
        dh = []
        for _ in range(nh - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dh += [t]
        dh += [5]
        tmp_output = ["SACAR UN CINCO"]
        tiradac = ""
        for i in dc:
            tiradac += f" {i}"
        tmp_output += ["  Tiradas de Marcus: 5"]
        tmp_output += ["  Marcus sólo ha tenido que tirar 1 vez."]
        tiradah = ""
        for i in dh:
            tiradah += f" {i}"
        tmp_output += [f"  Tiradas de Julius:{tiradah}"]
        tmp_output += [f"  Julius ha tenido que tirar {nh} veces."]
        tmp_output += ["  Ha ganado Marcus."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Gana Julius varias tiradas
        nh = random.randrange(2, 10)
        dh = []
        for _ in range(nh - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dh += [t]
        dh += [5]
        nc = random.randrange(nh + 1, 15)
        dc = []
        for _ in range(nc - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dc += [t]
        dc += [5]
        tmp_output = ["SACAR UN CINCO"]
        tiradac = ""
        for i in dc:
            tiradac += f" {i}"
        tmp_output += [f"  Tiradas de Marcus:{tiradac}"]
        tmp_output += [f"  Marcus ha tenido que tirar {nc} veces."]
        tiradah = ""
        for i in dh:
            tiradah += f" {i}"
        tmp_output += [f"  Tiradas de Julius:{tiradah}"]
        tmp_output += [f"  Julius ha tenido que tirar {nh} veces."]
        tmp_output += ["  Ha ganado Julius."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Gana Julius 1 tirada
        nh = 1
        dh = [5]
        nc = random.randrange(nh + 1, 15)
        dc = []
        for _ in range(nc - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dc += [t]
        dc += [5]
        tmp_output = ["SACAR UN CINCO"]
        tiradac = ""
        for i in dc:
            tiradac += f" {i}"
        tmp_output += [f"  Tiradas de Marcus:{tiradac}"]
        tmp_output += [f"  Marcus ha tenido que tirar {nc} veces."]
        tiradah = ""
        for i in dh:
            tiradah += f" {i}"
        tmp_output += ["  Tiradas de Julius: 5"]
        tmp_output += ["  Julius sólo ha tenido que tirar 1 vez."]
        tmp_output += ["  Ha ganado Julius."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Empatan varias tiradas
        nh = random.randrange(2, 10)
        dh = []
        for _ in range(nh - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dh += [t]
        dh += [5]
        nc = nh
        dc = []
        for _ in range(nc - 1):
            t = random.randrange(1, 7)
            while t == 5:
                t = random.randrange(1, 7)
            dc += [t]
        dc += [5]
        tmp_output = ["SACAR UN CINCO"]
        tiradac = ""
        for i in dc:
            tiradac += f" {i}"
        tmp_output += [f"  Tiradas de Marcus:{tiradac}"]
        tmp_output += [f"  Marcus ha tenido que tirar {nc} veces."]
        tiradah = ""
        for i in dh:
            tiradah += f" {i}"
        tmp_output += [f"  Tiradas de Julius:{tiradah}"]
        tmp_output += [f"  Julius ha tenido que tirar {nh} veces."]
        tmp_output += ["  Han empatado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Empatan 1 tirada
        nh = 1
        dh = [5]
        nc = 1
        dc = [5]
        tmp_output = [
            "SACAR UN CINCO",
            "  Tiradas de Marcus: 5",
            "  Marcus sólo ha tenido que tirar 1 vez.",
            "  Tiradas de Julius: 5",
            "  Julius sólo ha tenido que tirar 1 vez.",
            "  Han empatado.",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["random", dc + dh],
            ["output", tmp_output],
        )

        # Exercise 2021_43 END
