import mpts_common
import datetime
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 161711:
        # Exercise 161711 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170224.html

        semana = [
            "lunes",
            "martes",
            "miércoles",
            "jueves",
            "viernes",
            "sábado",
            "domingo",
        ]

        # Anterior a 1583
        y, m, d = mpts_common.generate_date()
        y = random.randrange(1583)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d, m, y]],
            [
                "output",
                [
                    "CÁLCULO DEL DÍA DE LA SEMANA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año (a partir de 1583): ",
                    "¡Le he pedido un año posterior a 1582!",
                ],
            ],
        )

        # De lunes a domingo
        for i in range(0, 7):
            y, m, d = mpts_common.generate_date()
            wd = datetime.date(y, m, d).weekday()
            if d > wd and d - wd + i < 28:
                d = d - wd + i
            elif d - wd + i >= 28:
                d = d - wd + i - 7
            else:
                d = d - wd + i + 7
            mpts_common.add_test(
                i != 6,  # LAST_LEST / NOT_LAST_TEST
                ["input", [d, m, y]],
                [
                    "output",
                    [
                        "CÁLCULO DEL DÍA DE LA SEMANA",
                        "Escriba el número de día: ",
                        "Escriba el número de mes: ",
                        "Escriba el número de año (a partir de 1583): ",
                        f"El día {d} del mes {m} de {y} es {semana[datetime.date(y, m, d).weekday()]}",
                    ],
                ],
            )

        # Exercise 161711 END

    elif exercise_id == 161712:
        # Exercise 161712 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170224.html

        # dia == 0
        dia = 0
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia < 0
        dia = -random.randrange(1, 29)
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia >= 32
        dia = random.randrange(32, 50)
        mes = random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # mes == 0
        dia = random.randrange(1, 29)
        mes = 0
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # mes < 0
        dia = random.randrange(1, 29)
        mes = -random.randrange(1, 13)
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # mes >= 13
        dia = random.randrange(1, 29)
        mes = random.randrange(13, 20)
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia 31 de mes con 31 días
        dia = 31
        mes = random.choice([1, 3, 5, 7, 8, 10, 12])
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} existe",
                ],
            ],
        )

        # dia 31 de mes con menos de 31 días
        dia = 31
        mes = random.choice([2, 4, 6, 9, 11])
        anyo = random.randrange(1583, 5000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia 29 febrero múltiplo de 400
        dia = 29
        mes = 2
        anyo = random.randrange(1600, 5000, 400)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} existe",
                ],
            ],
        )

        # dia 29 febrero múltiplo de 100 (no de 400)
        dia = 29
        mes = 2
        anyo = 1600 + 400 * random.randrange(0, 11) + 100 * random.randrange(1, 4)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia 29 febrero múltiplo de 4 (no de 100)
        dia = 29
        mes = 2
        anyo = 1600 + 100 * random.randrange(0, 5) + 4 * random.randrange(1, 25)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} existe",
                ],
            ],
        )

        # dia 29 febrero no múltiplo de 4
        dia = 29
        mes = 2
        anyo = 1584 + 4 * random.randrange(0, 150) + random.randrange(1, 4)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} no existe",
                ],
            ],
        )

        # dia que existe
        dia = random.randrange(1, 29)
        mes = random.randrange(1, 13)
        anyo = random.randrange(1584, 10000)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [dia, mes, anyo]],
            [
                "output",
                [
                    "COMPROBACIÓN DE FECHA",
                    "Escriba el número de día: ",
                    "Escriba el número de mes: ",
                    "Escriba el número de año: ",
                    f"El día {dia} del mes {mes} del año {anyo} existe",
                ],
            ],
        )

        # Exercise 161712 END

    elif exercise_id == 161713:
        # Exercise 161713 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170224.html

        # segundo valor igual que el primero
        a = random.randrange(-100, 101)
        b = a
        c = b + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    "¡No ha escrito números válidos!",
                ],
            ],
        )

        # tercer valor igual que el segundo
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    "¡No ha escrito números válidos!",
                ],
            ],
        )

        # tres valores iguales
        a = random.randrange(-100, 101)
        b = a
        c = b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    "¡No ha escrito números válidos!",
                ],
            ],
        )

        # tercer valor igual que el primero (correcto)
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = a
        resp = list(range(a, b)) + list(range(b, a - 1, -1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    resp,
                ],
            ],
        )

        # primero < segundo < tercero
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = b + random.randrange(1, 100)
        resp = list(range(a, c + 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    resp,
                ],
            ],
        )

        # primero < segundo > tercero
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = b - random.randrange(1, 100)
        resp = list(range(a, b)) + list(range(b, c - 1, -1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    resp,
                ],
            ],
        )

        # primero > segundo < tercero
        a = random.randrange(-100, 101)
        b = a - random.randrange(1, 100)
        c = b + random.randrange(1, 100)
        resp = list(range(a, b, -1)) + list(range(b, c + 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    resp,
                ],
            ],
        )

        # primero > segundo > tercero
        a = random.randrange(-100, 101)
        b = a - random.randrange(1, 100)
        c = b - random.randrange(1, 100)
        resp = list(range(a, c - 1, -1))
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ESCALERA DE NÚMEROS",
                    "Escriba el primer número: ",
                    "Escriba el segundo número distinto del primero: ",
                    "Escriba el tercer número distinto del segundo: ",
                    resp,
                ],
            ],
        )

        # Exercise 161713 END

    elif exercise_id == 161721:
        # Exercise 161721 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170505.html

        # Gana el primer jugador
        a = random.randrange(2, 7)
        b = random.randrange(1, a)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"El jugador 1 ha sacado un {a}. El jugador 2 ha sacado un {b}. Por tanto, ha ganado el jugador 1.",
                ],
            ],
        )

        # Gana el segundo jugador
        a = random.randrange(1, 6)
        b = random.randrange(a + 1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"El jugador 1 ha sacado un {a}. El jugador 2 ha sacado un {b}. Por tanto, ha ganado el jugador 2.",
                ],
            ],
        )

        # Empatan
        a = random.randrange(1, 7)
        b = a
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"El jugador 1 ha sacado un {a}. El jugador 2 ha sacado un {b}. Por tanto, han empatado.",
                ],
            ],
        )

        # Exercise 161721 END

    elif exercise_id == 161722:
        # Exercise 161722 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170505.html

        # Número de partidas negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "¿Cuántas partidas se van a jugar? ",
                    "El número de partidas debe ser superior a cero.",
                ],
            ],
        )

        # Número de partidas cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "¿Cuántas partidas se van a jugar? ",
                    "El número de partidas debe ser superior a cero.",
                ],
            ],
        )

        # Gana el primer jugador
        na = random.randrange(1, 8)
        nb = random.randrange(0, na)
        ne = random.randrange(0, 8)
        n = na + nb + ne
        d = []
        for i in range(na):
            a = random.randrange(2, 7)
            b = random.randrange(1, a)
            d += [[a, b]]
        for i in range(nb):
            a = random.randrange(1, 6)
            b = random.randrange(a + 1, 7)
            d += [[a, b]]
        for i in range(ne):
            a = random.randrange(1, 6)
            b = a
            d += [[a, b]]
        random.shuffle(d)
        p = []
        df = []
        for i in d:
            if i[0] > i[1]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            elif i[1] > i[0]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            else:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            df += [i[0], i[1]]
        p = (
            ["JUEGO DE DADOS (2)", "¿Cuántas partidas se van a jugar? ",]
            + p
            + [
                f"De las {n} partidas, el jugador 1 ha ganado {na} y el jugador 2 ha ganado {nb}.",
                "Por tanto, ha ganado el jugador 1.",
            ]
        )
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", df,], ["output", p,],
        )

        # Gana el segundo jugador
        na = random.randrange(0, 8)
        nb = random.randrange(na + 1, 10)
        ne = random.randrange(0, 8)
        n = na + nb + ne
        d = []
        for i in range(na):
            a = random.randrange(2, 7)
            b = random.randrange(1, a)
            d += [[a, b]]
        for i in range(nb):
            a = random.randrange(1, 6)
            b = random.randrange(a + 1, 7)
            d += [[a, b]]
        for i in range(ne):
            a = random.randrange(1, 6)
            b = a
            d += [[a, b]]
        random.shuffle(d)
        p = []
        df = []
        for i in d:
            if i[0] > i[1]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            elif i[1] > i[0]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            else:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            df += [i[0], i[1]]
        p = (
            ["JUEGO DE DADOS (2)", "¿Cuántas partidas se van a jugar? ",]
            + p
            + [
                f"De las {n} partidas, el jugador 1 ha ganado {na} y el jugador 2 ha ganado {nb}.",
                "Por tanto, ha ganado el jugador 2.",
            ]
        )
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", df,], ["output", p,],
        )

        # Empate
        na = random.randrange(0, 8)
        nb = na
        ne = random.randrange(1, 8)
        n = na + nb + ne
        d = []
        for i in range(na):
            a = random.randrange(2, 7)
            b = random.randrange(1, a)
            d += [[a, b]]
        for i in range(nb):
            a = random.randrange(1, 6)
            b = random.randrange(a + 1, 7)
            d += [[a, b]]
        for i in range(ne):
            a = random.randrange(1, 6)
            b = a
            d += [[a, b]]
        random.shuffle(d)
        p = []
        df = []
        for i in d:
            if i[0] > i[1]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            elif i[1] > i[0]:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            else:
                p += [
                    f"El jugador 1 ha sacado un {i[0]}. El jugador 2 ha sacado un {i[1]}."
                ]
            df += [i[0], i[1]]
        p = (
            ["JUEGO DE DADOS (2)", "¿Cuántas partidas se van a jugar? ",]
            + p
            + [
                f"De las {n} partidas, el jugador 1 ha ganado {na} y el jugador 2 ha ganado {nb}.",
                "Por tanto, han empatado.",
            ]
        )
        mpts_common.add_test(
            LAST_TEST, ["input", [n]], ["random", df,], ["output", p,],
        )

        # Exercise 161722 END

    elif exercise_id == 161723:
        # Exercise 161723 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170505.html

        # Número de jugadores negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    "¿Cuántos jugadores van a jugar? ",
                    "El número de jugadores debe ser como mínimo dos.",
                ],
            ],
        )

        # Número de jugadores cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    "¿Cuántos jugadores van a jugar? ",
                    "El número de jugadores debe ser como mínimo dos.",
                ],
            ],
        )

        # Número de jugadores uno
        n = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    "¿Cuántos jugadores van a jugar? ",
                    "El número de jugadores debe ser como mínimo dos.",
                ],
            ],
        )

        # Gana el primer jugador
        n = random.randrange(2, 11)
        d = [random.randrange(2, 7)]
        for _ in range(n - 1):
            d += [random.randrange(1, d[0])]
        tmp_output = [
            "JUEGO DE DADOS (3)",
            "¿Cuántos jugadores van a jugar? ",
        ]
        for i in range(n):
            tmp_output += [f"El jugador {i+1} ha sacado un {d[i]}."]
        tmp_output += [f"Ha ganado el jugador 1, que ha sacado un {d[0]}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", d], ["output", tmp_output],
        )

        # Gana el último jugador
        n = random.randrange(2, 11)
        max = random.randrange(2, 7)
        d = []
        for _ in range(n - 1):
            d += [random.randrange(1, max)]
        d += [max]
        tmp_output = [
            "JUEGO DE DADOS (3)",
            "¿Cuántos jugadores van a jugar? ",
        ]
        for i in range(n):
            tmp_output += [f"El jugador {i+1} ha sacado un {d[i]}."]
        tmp_output += [f"Ha ganado el jugador {n}, que ha sacado un {max}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [n]], ["random", d], ["output", tmp_output],
        )

        # Gana otro jugador
        n1 = random.randrange(1, 6)
        n2 = random.randrange(1, 6)
        max = random.randrange(2, 7)
        d = []
        for _ in range(n1):
            d += [random.randrange(1, max)]
        d += [max]
        for _ in range(n2):
            d += [random.randrange(1, max)]
        tmp_output = [
            "JUEGO DE DADOS (3)",
            "¿Cuántos jugadores van a jugar? ",
        ]
        for i in range(n1 + n2 + 1):
            tmp_output += [f"El jugador {i+1} ha sacado un {d[i]}."]
        tmp_output += [f"Ha ganado el jugador {n1 + 1}, que ha sacado un {max}."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n1 + n2 + 1]],
            ["random", d],
            ["output", tmp_output],
        )

        # Empate
        n = random.randrange(2, 11)
        max = random.randrange(2, 7)
        d = []
        for _ in range(n - 1):
            d += [max]
        d += [max]
        tmp_output = [
            "JUEGO DE DADOS (3)",
            "¿Cuántos jugadores van a jugar? ",
        ]
        for i in range(n):
            tmp_output += [f"El jugador {i+1} ha sacado un {d[i]}."]
        tmp_output += ["Ningún jugador ha sacado más que los demás."]
        mpts_common.add_test(
            LAST_TEST, ["input", [n]], ["random", d], ["output", tmp_output],
        )

        # Exercise 161723 END
