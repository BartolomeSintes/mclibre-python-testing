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

    elif exercise_id == 2223_12:
        # Exercise 2223_12 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230516.html

        # turnos negativo
        tu = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "¡Como mínimo se debe jugar una partida!",
                ],
            ],
        )

        # turnos 0
        tu = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "¡Como mínimo se debe jugar una partida!",
                ],
            ],
        )

        # 1 partida, gana Cubitus, 1 máximo, 1 mínimo
        tu = 1
        c1 = random.randrange(1, 3)
        c5 = random.randrange(5, 7)
        h1 = random.randrange(1, 3)
        h5 = random.randrange(5, 7)
        tc = th = 0
        while tc <= th:
            c2 = random.randrange(c1 + 1, c5)
            c3 = random.randrange(c1 + 1, c5)
            c4 = random.randrange(c1 + 1, c5)
            h2 = random.randrange(h1 + 1, h5)
            h3 = random.randrange(h1 + 1, h5)
            h4 = random.randrange(h1 + 1, h5)
            tc = c2 + c3 + c4
            th = h2 + h3 + h4
        c = [c1, c2, c3, c4, c5]
        random.shuffle(c)
        h = [h1, h2, h3, h4, h5]
        random.shuffle(h)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "",
                    "Partida 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                    f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                    "  Ha ganado Cubitus.",
                ],
            ],
        )

        # 1 partida, gana Humerus, 1 máximo, 1 mínimo
        tu = 1
        c1 = random.randrange(1, 3)
        c5 = random.randrange(5, 7)
        h1 = random.randrange(1, 3)
        h5 = random.randrange(5, 7)
        tc = th = 0
        while th <= tc:
            c2 = random.randrange(c1 + 1, c5)
            c3 = random.randrange(c1 + 1, c5)
            c4 = random.randrange(c1 + 1, c5)
            h2 = random.randrange(h1 + 1, h5)
            h3 = random.randrange(h1 + 1, h5)
            h4 = random.randrange(h1 + 1, h5)
            tc = c2 + c3 + c4
            th = h2 + h3 + h4
        c = [c1, c2, c3, c4, c5]
        random.shuffle(c)
        h = [h1, h2, h3, h4, h5]
        random.shuffle(h)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "",
                    "Partida 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                    f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                    "  Ha ganado Humerus.",
                ],
            ],
        )

        # 1 partida, empatan, 1 máximo, 1 mínimo
        tu = 1
        c1 = random.randrange(1, 3)
        c5 = random.randrange(5, 7)
        h1 = random.randrange(1, 3)
        h5 = random.randrange(5, 7)
        tc = 1
        th = 0
        while th != tc:
            c2 = random.randrange(c1 + 1, c5)
            c3 = random.randrange(c1 + 1, c5)
            c4 = random.randrange(c1 + 1, c5)
            h2 = random.randrange(h1 + 1, h5)
            h3 = random.randrange(h1 + 1, h5)
            h4 = random.randrange(h1 + 1, h5)
            tc = c2 + c3 + c4
            th = h2 + h3 + h4
        c = [c1, c2, c3, c4, c5]
        random.shuffle(c)
        h = [h1, h2, h3, h4, h5]
        random.shuffle(h)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "",
                    "Partida 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                    f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                    "  Han empatado.",
                ],
            ],
        )

        # 2 partidas,
        tu = 2
        # partida 1: gana Cubitus, Cubitus 2 máximos, Humerus 2 mínimos
        c1 = random.randrange(1, 3)
        c5 = random.randrange(5, 7)
        c4 = c5
        h1 = random.randrange(1, 3)
        h2 = h1
        h5 = random.randrange(5, 7)
        tc = th = 0
        while tc <= th:
            c2 = random.randrange(c1 + 1, c5)
            c3 = random.randrange(c1 + 1, c5)
            h3 = random.randrange(h1 + 1, h5)
            h4 = random.randrange(h1 + 1, h5)
            tc = c2 + c3
            th = h3 + h4
        c = [c1, c2, c3, c4, c5]
        random.shuffle(c)
        h = [h1, h2, h3, h4, h5]
        random.shuffle(h)
        # partida 2: empatan, todos máximos o mínimos
        bc1 = random.randrange(1, 4)
        bc3 = bc2 = bc1
        bc5 = random.randrange(4, 7)
        bc4 = bc5
        bh1 = random.randrange(1, 4)
        bh2 = bh1
        bh5 = random.randrange(4, 7)
        bh4 = bh3 = bh5
        btc = bth = 0
        bc = [bc1, bc2, bc3, bc4, bc5]
        random.shuffle(bc)
        bh = [bh1, bh2, bh3, bh4, bh5]
        random.shuffle(bh)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h + bc + bh],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "",
                    "Partida 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                    f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                    "  Ha ganado Cubitus.",
                    "",
                    "Partida 2",
                    f"  Tirada de Cubitus: {bc[0]} {bc[1]} {bc[2]} {bc[3]} {bc[4]} => {btc} puntos.",
                    f"  Tirada de Humerus: {bh[0]} {bh[1]} {bh[2]} {bh[3]} {bh[4]} => {bth} puntos.",
                    "  Han empatado.",
                ],
            ],
        )

        # 3 partidas,
        tu = 3
        # partida 1: empatan, 1 máximo, 1 mínimo
        c1 = random.randrange(1, 3)
        c5 = random.randrange(5, 7)
        h1 = random.randrange(1, 3)
        h5 = random.randrange(5, 7)
        tc = 1
        th = 0
        while th != tc:
            c2 = random.randrange(c1 + 1, c5)
            c3 = random.randrange(c1 + 1, c5)
            c4 = random.randrange(c1 + 1, c5)
            h2 = random.randrange(h1 + 1, h5)
            h3 = random.randrange(h1 + 1, h5)
            h4 = random.randrange(h1 + 1, h5)
            tc = c2 + c3 + c4
            th = h2 + h3 + h4
        c = [c1, c2, c3, c4, c5]
        random.shuffle(c)
        h = [h1, h2, h3, h4, h5]
        random.shuffle(h)
        # partida 2: gana Humerus, Cubitus 2 mínimos
        bc1 = random.randrange(1, 3)
        bc5 = random.randrange(5, 7)
        bc2 = bc1
        bh1 = random.randrange(1, 3)
        bh5 = random.randrange(5, 7)
        btc = bth = 0
        while bth <= btc:
            bc3 = random.randrange(bc1 + 1, bc5)
            bc4 = random.randrange(bc1 + 1, bc5)
            bh2 = random.randrange(bh1 + 1, bh5)
            bh3 = random.randrange(bh1 + 1, bh5)
            bh4 = random.randrange(bh1 + 1, bh5)
            btc = bc3 + bc4
            bth = bh2 + bh3 + bh4
        bc = [bc1, bc2, bc3, bc4, bc5]
        random.shuffle(bc)
        bh = [bh1, bh2, bh3, bh4, bh5]
        random.shuffle(bh)
        # partida 3: gana Cubitus, Humerus 3 máximos
        cc1 = random.randrange(1, 3)
        cc5 = random.randrange(5, 7)
        ch1 = random.randrange(1, 3)
        ch5 = random.randrange(5, 7)
        ch3 = ch4 = ch5
        ctc = cth = 0
        while ctc <= cth:
            cc2 = random.randrange(cc1 + 1, cc5)
            cc3 = random.randrange(cc1 + 1, cc5)
            cc4 = random.randrange(cc1 + 1, cc5)
            ch2 = random.randrange(ch1 + 1, ch5)
            ctc = cc2 + cc3 + cc4
            cth = ch2
        cc = [cc1, cc2, cc3, cc4, cc5]
        random.shuffle(cc)
        ch = [ch1, ch2, ch3, ch4, ch5]
        random.shuffle(ch)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [tu]],
            ["random", c + h + bc + bh + cc + ch],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos partidas van a jugar? ",
                    "",
                    "Partida 1",
                    f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                    f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                    "  Han empatado.",
                    "",
                    "Partida 2",
                    f"  Tirada de Cubitus: {bc[0]} {bc[1]} {bc[2]} {bc[3]} {bc[4]} => {btc} puntos.",
                    f"  Tirada de Humerus: {bh[0]} {bh[1]} {bh[2]} {bh[3]} {bh[4]} => {bth} puntos.",
                    "  Ha ganado Humerus.",
                    "",
                    "Partida 3",
                    f"  Tirada de Cubitus: {cc[0]} {cc[1]} {cc[2]} {cc[3]} {cc[4]} => {ctc} puntos.",
                    f"  Tirada de Humerus: {ch[0]} {ch[1]} {ch[2]} {ch[3]} {ch[4]} => {cth} puntos.",
                    "  Ha ganado Cubitus.",
                ],
            ],
        )


        # Exercise 2223_11 END
