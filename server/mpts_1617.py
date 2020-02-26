import mpts_common
import datetime
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 161_711:
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
            LAST_TEST,
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

        # Exercise 161712 END

    elif exercise_id == 161713:
        # Exercise 161732 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170224.html

        # dia == 0
        opcion = "c"
        mpts_common.add_test(
            LAST_TEST,
            ["input", [opcion]],
            [
                "output",
                [
                    "GALONES Y PINTAS",
                    "",
                    "Este programa permite:",
                    "a. Convertir litros en galones y pintas.",
                    "b. Convertir galones y pintas en litros",
                    "",
                    "Elija una opción: ",
                    "",
                    "Debe escribir a o b.",
                    "",
                    "Programa terminado",
                ],
            ],
        )

        # Exercise 161713 END
