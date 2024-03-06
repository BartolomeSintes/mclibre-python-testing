import math
import random

import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 2223_11:
        # Exercise 2223_11 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230516.html

        # g negativo
        g = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    "Por favor, escriba un número positivo.",
                ],
            ],
        )

        # g = 0
        g = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    "0 gramos son 0 libras, 0 onzas, 0 cuartas y 0 milésimas de cuarta",
                ],
            ],
        )

        # milésimas
        g = random.randrange(1, 8)
        ml = math.floor(g / (355 / 48000))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    f"{g} gramos son 0 libras, 0 onzas, 0 cuartas y {ml} milésimas de cuarta",
                ],
            ],
        )

        # milésimas, cuartas
        g = random.randrange(8, 30)
        c = math.floor(g // (355 / 12 / 4))
        resto = g % (355 / 12 / 4)
        ml = math.floor(resto / (355 / 12 / 4 / 1000))

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    f"{g} gramos son 0 libras, 0 onzas, {c} cuartas y {ml} milésimas de cuarta",
                ],
            ],
        )

        # milésimas, cuartas, onzas
        g = random.randrange(30, 355)
        o = math.floor(g // (355 / 12))
        resto = g % (355 / 12)
        c = math.floor(resto // (355 / 12 / 4))
        resto = g % (355 / 12 / 4)
        ml = math.floor(resto / (355 / 12 / 4 / 1000))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    f"{g} gramos son 0 libras, {o} onzas, {c} cuartas y {ml} milésimas de cuarta",
                ],
            ],
        )

        # milésimas, cuartas, onzas, libras
        g = random.randrange(355, 1000)
        l = math.floor(g // 355)
        resto = g % 355
        o = math.floor(resto // (355 / 12))
        resto = g % (355 / 12)
        c = math.floor(resto // (355 / 12 / 4))
        resto = g % (355 / 12 / 4)
        ml = math.floor(resto / (355 / 12 / 4 / 1000))
        mpts_common.add_test(
            LAST_TEST,
            ["input", [g]],
            [
                "output",
                [
                    "CONVERTIDOR DE GRAMOS EN LIBRAS, ONZAS, CUARTAS Y MILÉSIMAS",
                    "Escriba una cantidad de gramos: ",
                    f"{g} gramos son {l} libras, {o} onzas, {c} cuartas y {ml} milésimas de cuarta",
                ],
            ],
        )

        # Exercise 2223_11 END
