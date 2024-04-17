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
                    "¿Cuántas partidas van a jugar? ",
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
                    "¿Cuántas partidas van a jugar? ",
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
                    "¿Cuántas partidas van a jugar? ",
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
                    "¿Cuántas partidas van a jugar? ",
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
                    "¿Cuántas partidas van a jugar? ",
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
                    "¿Cuántas partidas van a jugar? ",
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
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h + bc + bh + cc + ch],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
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

        # n partidas, entre 7 y 12, siempre gana Humerus
        tu = random.randrange(7, 13)
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "",
            "¿Cuántas partidas van a jugar? ",
        ]
        for i in range(tu):
            # partida 2: gana Humerus, Cubitus 2 mínimos
            c1 = random.randrange(1, 3)
            c5 = random.randrange(5, 7)
            c2 = c1
            h1 = random.randrange(1, 3)
            h5 = random.randrange(5, 7)
            tc = th = 0
            while th <= tc:
                c3 = random.randrange(c1 + 1, c5)
                c4 = random.randrange(c1 + 1, c5)
                h2 = random.randrange(h1 + 1, h5)
                h3 = random.randrange(h1 + 1, h5)
                h4 = random.randrange(h1 + 1, h5)
                tc = c3 + c4
                th = h2 + h3 + h4
            c = [c1, c2, c3, c4, c5]
            random.shuffle(c)
            h = [h1, h2, h3, h4, h5]
            random.shuffle(h)
            tmp_random += c + h
            tmp_output += [
                "",
                f"Partida {i + 1}",
                f"  Tirada de Cubitus: {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} => {tc} puntos.",
                f"  Tirada de Humerus: {h[0]} {h[1]} {h[2]} {h[3]} {h[4]} => {th} puntos.",
                "  Ha ganado Humerus.",
            ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [tu]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 2223_12 END

    elif exercise_id == 2223_13:
        # Exercise 2223_13 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230516.html

        # puntos negativo, aviso
        pu = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    "¡Como mínimo se deben conseguir 2 puntos!",
                ],
            ],
        )

        # puntos 0, aviso
        pu = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    "¡Como mínimo se deben conseguir 2 puntos!",
                ],
            ],
        )

        # puntos 1, aviso
        pu = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    "¡Como mínimo se deben conseguir 2 puntos!",
                ],
            ],
        )

        # a la primera, empate. Cubitus saca valor exacto, Humerus lo supera
        pu = random.randrange(2, 6)
        c = pu
        h = random.randrange(pu + 1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {c} ",
                    "Cubitus ha conseguido el objetivo en 1 tirada.",
                    "",
                    f"Tiradas de Humerus: {h} ",
                    "Humerus ha conseguido el objetivo en 1 tirada.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # a la primera, empate. Humerus saca valor exacto, Cubitus lo supera
        pu = random.randrange(2, 6)
        c = random.randrange(pu + 1, 7)
        h = pu
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {c} ",
                    "Cubitus ha conseguido el objetivo en 1 tirada.",
                    "",
                    f"Tiradas de Humerus: {h} ",
                    "Humerus ha conseguido el objetivo en 1 tirada.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # a la primera, empate. Ambos sacan valor exacto
        pu = random.randrange(2, 7)
        c = pu
        h = pu
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {c} ",
                    "Cubitus ha conseguido el objetivo en 1 tirada.",
                    "",
                    f"Tiradas de Humerus: {h} ",
                    "Humerus ha conseguido el objetivo en 1 tirada.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # a la primera, empate. Ambos lo superan
        pu = random.randrange(2, 6)
        c = random.randrange(pu + 1, 7)
        h = random.randrange(pu + 1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {c} ",
                    "Cubitus ha conseguido el objetivo en 1 tirada.",
                    "",
                    f"Tiradas de Humerus: {h} ",
                    "Humerus ha conseguido el objetivo en 1 tirada.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # varias tiradas, gana Cubitus
        nj1 = random.randrange(3, 7)
        dj1 = []
        tij1 = ""
        for _ in range(nj1):
            d = random.randrange(1, 7)
            dj1 += [d]
            tij1 += f"{d} "
        pu = sum(dj1) + 1
        d = random.randrange(2, 7)
        dj1 += [d]
        tij1 += f"{d} "
        dj2 = []
        while len(dj2) == 0 or len(dj2) == len(dj1):
            dj2 = []
            tij2 = ""
            while sum(dj2) < pu:
                d = random.randrange(1, 7)
                dj2 += [d]
                tij2 += f"{d} "

        if len(dj1) > len(dj2):
            c = dj2
            tic = tij2
            h = dj1
            tih = tij1
        else:
            c = dj1
            tic = tij1
            h = dj2
            tih = tij2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {tic}",
                    f"Cubitus ha conseguido el objetivo en {len(c)} tiradas.",
                    "",
                    f"Tiradas de Humerus: {tih}",
                    f"Humerus ha conseguido el objetivo en {len(h)} tiradas.",
                    "",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # varias tiradas, gana Humerus
        nj1 = random.randrange(3, 7)
        dj1 = []
        tij1 = ""
        for _ in range(nj1):
            d = random.randrange(1, 7)
            dj1 += [d]
            tij1 += f"{d} "
        pu = sum(dj1) + 1
        d = random.randrange(2, 7)
        dj1 += [d]
        tij1 += f"{d} "
        dj2 = []
        while len(dj2) == 0 or len(dj2) == len(dj1):
            dj2 = []
            tij2 = ""
            while sum(dj2) < pu:
                d = random.randrange(1, 7)
                dj2 += [d]
                tij2 += f"{d} "

        if len(dj1) > len(dj2):
            c = dj1
            tic = tij1
            h = dj2
            tih = tij2
        else:
            c = dj2
            tic = tij2
            h = dj1
            tih = tij1

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [pu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {tic}",
                    f"Cubitus ha conseguido el objetivo en {len(c)} tiradas.",
                    "",
                    f"Tiradas de Humerus: {tih}",
                    f"Humerus ha conseguido el objetivo en {len(h)} tiradas.",
                    "",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # varias tiradas, empatan
        nc = random.randrange(3, 7)
        c = []
        tic = ""
        for _ in range(nc):
            d = random.randrange(1, 7)
            c += [d]
            tic += f"{d} "
        pu = sum(c) + 1
        h = c[:]
        tih = ""
        random.shuffle(h)
        for i in h:
            tih += f"{i} "
        d = random.randrange(2, 7)
        c += [d]
        tic += f"{d} "
        d = random.randrange(2, 7)
        h += [d]
        tih += f"{d} "
        mpts_common.add_test(
            LAST_TEST,
            ["input", [pu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    "¿Cuántos puntos hay que conseguir? ",
                    "",
                    f"Tiradas de Cubitus: {tic}",
                    f"Cubitus ha conseguido el objetivo en {len(c)} tiradas.",
                    "",
                    f"Tiradas de Humerus: {tih}",
                    f"Humerus ha conseguido el objetivo en {len(h)} tiradas.",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 2223_13 END

    elif exercise_id == 2223_21:
        # Exercise 2223_21 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230530.html

        # turnos negativo, aviso
        tu = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    "¡Como mínimo se debe jugar un turno!",
                ],
            ],
        )

        # turnos cero, aviso
        tu = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    "¡Como mínimo se debe jugar un turno!",
                ],
            ],
        )

        # 1 partida, par - par, gana Cubitus
        tu = 1
        c = random.randrange(1, 4) * 2
        h = random.randrange(1, 4) * 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    f"Turno 1 - Cubitus: {c} - Humerus: {h} - {c + h} puntos para Cubitus.",
                    "",
                    f"Ha ganado Cubitus {c + h} a 0.",
                ],
            ],
        )

        # 1 partida, impar - impar, gana Cubitus
        tu = 1
        c = random.randrange(0, 3) * 2 + 1
        h = random.randrange(0, 3) * 2 + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    f"Turno 1 - Cubitus: {c} - Humerus: {h} - {c + h} puntos para Cubitus.",
                    "",
                    f"Ha ganado Cubitus {c + h} a 0.",
                ],
            ],
        )

        # 1 partida, impar - par, gana Humerus
        tu = 1
        c = random.randrange(0, 3) * 2 + 1
        h = random.randrange(1, 4) * 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    f"Turno 1 - Cubitus: {c} - Humerus: {h} - {c + h} puntos para Humerus.",
                    "",
                    f"Ha ganado Humerus {c + h} a 0.",
                ],
            ],
        )

        # 1 partida, par - impar, gana Humerus
        tu = 1
        c = random.randrange(1, 4) * 2
        h = random.randrange(0, 3) * 2 + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántos turnos van a jugar? ",
                    f"Turno 1 - Cubitus: {c} - Humerus: {h} - {c + h} puntos para Humerus.",
                    "",
                    f"Ha ganado Humerus {c + h} a 0.",
                ],
            ],
        )

        # n partidas, gana Humerus
        tuc = random.randrange(2, 6)
        parc = []
        tc = 0
        for _ in range(tuc):
            if random.randrange(2):
                tmp = [random.randrange(1, 4) * 2, random.randrange(1, 4) * 2]
            else:
                tmp = [random.randrange(0, 3) * 2 + 1, random.randrange(0, 3) * 2 + 1]
            tc += tmp[0] + tmp[1]
            parc += [tmp]
        parh = []
        th = 0
        while th <= tc:
            if random.randrange(2):
                tmp = [random.randrange(1, 4) * 2, random.randrange(0, 3) * 2 + 1]
            else:
                tmp = [random.randrange(0, 3) * 2 + 1, random.randrange(1, 4) * 2]
            th += tmp[0] + tmp[1]
            parh += [tmp]
        tu = len(parc) + len(parh)
        par = parc + parh
        random.shuffle(par)
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "",
            "¿Cuántos turnos van a jugar? ",
        ]
        tir = []
        for i, tirada in enumerate(par):
            if (tirada[0] + tirada[1]) % 2 == 0:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Cubitus.",
                ]
            else:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Humerus.",
                ]
            tir += [tirada[0], tirada[1]]
        tmp_output += [
            "",
            f"Ha ganado Humerus {th} a {tc}.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", tir],
            ["output", tmp_output],
        )

        # n partidas, gana Cubitus
        tuh = random.randrange(2, 6)
        parh = []
        th = 0
        for _ in range(tuh):
            if random.randrange(2):
                tmp = [random.randrange(1, 4) * 2, random.randrange(0, 3) * 2 + 1]
            else:
                tmp = [random.randrange(0, 3) * 2 + 1, random.randrange(1, 4) * 2]
            th += tmp[0] + tmp[1]
            parh += [tmp]
        parc = []
        tc = 0
        while tc <= th:
            if random.randrange(2):
                tmp = [random.randrange(1, 4) * 2, random.randrange(1, 4) * 2]
            else:
                tmp = [random.randrange(0, 3) * 2 + 1, random.randrange(0, 3) * 2 + 1]
            tc += tmp[0] + tmp[1]
            parc += [tmp]
        tu = len(parc) + len(parh)
        par = parc + parh
        random.shuffle(par)
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "",
            "¿Cuántos turnos van a jugar? ",
        ]
        tir = []
        for i, tirada in enumerate(par):
            if (tirada[0] + tirada[1]) % 2 == 0:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Cubitus.",
                ]
            else:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Humerus.",
                ]
            tir += [tirada[0], tirada[1]]
        tmp_output += [
            "",
            f"Ha ganado Cubitus {tc} a {th}.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", tir],
            ["output", tmp_output],
        )

        # n partidas, empate
        tuc = random.randrange(1, 4) * 2
        parc = []
        tc = 0
        for _ in range(tuc):
            if random.randrange(2):
                tmp = [random.randrange(1, 4) * 2, random.randrange(1, 3) * 2]
            else:
                tmp = [random.randrange(0, 3) * 2 + 1, random.randrange(1, 3) * 2 + 1]
            tc += tmp[0] + tmp[1]
            parc += [tmp]
        parh = []
        for i, tirada in enumerate(parc):
            if tirada[0] % 2 == 0:
                tmp = [tirada[0] - 1, tirada[1]]
            else:
                tmp = [tirada[0] + 1, tirada[1]]
            parh += [tmp]
        tu = len(parc) + len(parh)
        par = parc + parh
        random.shuffle(par)
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "",
            "¿Cuántos turnos van a jugar? ",
        ]
        tir = []
        for i, tirada in enumerate(par):
            if (tirada[0] + tirada[1]) % 2 == 0:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Cubitus.",
                ]
            else:
                tmp_output += [
                    f"Turno {i + 1} - Cubitus: {tirada[0]} - Humerus: {tirada[1]} - {tirada[0] + tirada[1]} puntos para Humerus.",
                ]
            tir += [tirada[0], tirada[1]]
        tmp_output += [
            "",
            f"Han empatado a {tc}.",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [tu]],
            ["random", tir],
            ["output", tmp_output],
        )

        # Exercise 2223_21 END

    elif exercise_id == 2223_22:
        # Exercise 2223_22 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230530.html

        # parejas a la primera, gana Cubitus
        c = random.randrange(1, 6)
        h = random.randrange(c + 1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [c, c, h, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus: {c} {c}",
                    f"Tiradas de Humerus: {h} {h}",
                    "",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # parejas a la primera, gana Humerus
        h = random.randrange(1, 6)
        c = random.randrange(h + 1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [c, c, h, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus: {c} {c}",
                    f"Tiradas de Humerus: {h} {h}",
                    "",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # parejas a la primera, empate
        ch = random.randrange(1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [ch, ch, ch, ch]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus: {ch} {ch}",
                    f"Tiradas de Humerus: {ch} {ch}",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # c1 < h1, c2 = h2, gana Cubitus
        # hago dos listas iguales, sin valores iguales seguidos
        ch = random.randrange(1, 7)
        c1 = [ch]
        h1 = [ch]
        for i in range(random.randrange(3, 7)):
            ch = random.randrange(1, 7)
            while ch == c1[-1]:
                ch = random.randrange(1, 7)
            c1 += [ch]
            h1 += [ch]
        random.shuffle(h1)
        iguales_seguidos = False
        for i in range(len(h1) - 1):
            if h1[i] == h1[i + 1]:
                iguales_seguidos = True
        while iguales_seguidos:
            random.shuffle(h1)
            iguales_seguidos = False
            for i in range(len(h1) - 1):
                if h1[i] == h1[i + 1]:
                    iguales_seguidos = True
        # añado un valor a la de humerus y los dados finales iguales (pero que no pueden coincidir con los últimos anteriores)
        hd = random.randrange(1, 7)
        while hd == h1[-1]:
            hd = random.randrange(1, 7)
        h1 += [hd]
        ch = random.randrange(1, 7)
        while ch == c1[-1] or ch == h1[-1]:
            ch = random.randrange(1, 7)
        c1 += [ch, ch]
        h1 += [ch, ch]
        tc = ""
        for i, dc in enumerate(c1):
            tc += f" {dc}"
        th = ""
        for i, dh in enumerate(h1):
            th += f" {dh}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", c1 + h1],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus:{tc}",
                    f"Tiradas de Humerus:{th}",
                    "",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # c1 < h1, c2 > h2, empate
        # hago dos listas iguales, sin valores iguales seguidos
        ch = random.randrange(1, 7)
        c1 = [ch]
        h1 = [ch]
        for i in range(random.randrange(3, 7)):
            ch = random.randrange(1, 7)
            while ch == c1[-1]:
                ch = random.randrange(1, 7)
            c1 += [ch]
            h1 += [ch]
        random.shuffle(h1)
        iguales_seguidos = False
        for i in range(len(h1) - 1):
            if h1[i] == h1[i + 1]:
                iguales_seguidos = True
        while iguales_seguidos:
            random.shuffle(h1)
            iguales_seguidos = False
            for i in range(len(h1) - 1):
                if h1[i] == h1[i + 1]:
                    iguales_seguidos = True
        # añado un valor par a la lista de humerus y los dados finales se llevan ese valor (para que salga empate)
        hd = random.randrange(1, 4) * 2
        while hd == h1[-1]:
            hd = random.randrange(1, 4) * 2
        h1 += [hd]
        ch = random.randrange(1 + hd // 2, 7)
        while ch - hd // 2 == h1[-1] or ch == c1[-1]:
            ch = random.randrange(1 + hd // 2, 7)
        c1 += [ch, ch]
        h1 += [ch - hd // 2, ch - hd // 2]
        tc = ""
        for i, dc in enumerate(c1):
            tc += f" {dc}"
        th = ""
        for i, dh in enumerate(h1):
            th += f" {dh}"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", c1 + h1],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus:{tc}",
                    f"Tiradas de Humerus:{th}",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # c1 < h1, c2 > h2, gana Humerus
        # hago dos listas iguales, sin valores iguales seguidos
        ch = random.randrange(1, 7)
        c1 = [ch]
        h1 = [ch]
        for i in range(random.randrange(3, 7)):
            ch = random.randrange(1, 7)
            while ch == c1[-1]:
                ch = random.randrange(1, 7)
            c1 += [ch]
            h1 += [ch]
        random.shuffle(h1)
        iguales_seguidos = False
        for i in range(len(h1) - 1):
            if h1[i] == h1[i + 1]:
                iguales_seguidos = True
        while iguales_seguidos:
            random.shuffle(h1)
            iguales_seguidos = False
            for i in range(len(h1) - 1):
                if h1[i] == h1[i + 1]:
                    iguales_seguidos = True
        # añado un valor a la lista de humerus y los dados finales se llevan más de ese valor (para que gane humerus)
        hd = random.randrange(1, 4)
        while hd == h1[-1]:
            hd = random.randrange(1, 4)
        h1 += [hd]
        ch = random.randrange(4, 7)
        while ch - 2 == h1[-1] or ch == c1[-1]:
            ch = random.randrange(4, 7)
        c1 += [ch, ch]
        h1 += [ch - 2, ch - 2]
        tc = ""
        for i, dc in enumerate(c1):
            tc += f" {dc}"
        th = ""
        for i, dh in enumerate(h1):
            th += f" {dh}"
        mpts_common.add_test(
            LAST_TEST,
            ["random", c1 + h1],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    "",
                    f"Tiradas de Cubitus:{tc}",
                    f"Tiradas de Humerus:{th}",
                    "",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # Exercise 2223_22 END

    elif exercise_id == 2223_31:
        # Exercise 2223_31 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/22-23/examen-230623.html

        # turnos negativos
        tu = -random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    "¡Como mínimo se debe jugar una partida!",
                ],
            ],
        )

        # turnos cero
        tu = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    "¡Como mínimo se debe jugar una partida!",
                ],
            ],
        )

        # turnos pares
        tu = 2 * random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    "¡El número de partidas debe ser impar!",
                ],
            ],
        )

        # 1 turno, coincide el primer valor de Humerus con alguno de Cubitus, gana Cubitus
        tu = 1
        c = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h = [
            c[random.randrange(1, 3)],
            random.randrange(1, 14),
            random.randrange(1, 14),
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - Cubitus: {c[0]} {c[1]} {c[2]} - Humerus: {h[0]} {h[1]} {h[2]} - Gana Cubitus.",
                    "",
                    "Ha ganado Cubitus 1 partidas a 0.",
                ],
            ],
        )

        # 1 turno, coincide el segundo valor de Humerus con alguno de Cubitus, gana Cubitus
        tu = 1
        c = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h = [
            random.randrange(1, 14),
            c[random.randrange(1, 3)],
            random.randrange(1, 14),
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - Cubitus: {c[0]} {c[1]} {c[2]} - Humerus: {h[0]} {h[1]} {h[2]} - Gana Cubitus.",
                    "",
                    "Ha ganado Cubitus 1 partidas a 0.",
                ],
            ],
        )

        # 1 turno, coincide el tercer valor de Humerus con alguno de Cubitus, gana Cubitus
        tu = 1
        c = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h = [
            random.randrange(1, 14),
            random.randrange(1, 14),
            c[random.randrange(1, 3)],
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - Cubitus: {c[0]} {c[1]} {c[2]} - Humerus: {h[0]} {h[1]} {h[2]} - Gana Cubitus.",
                    "",
                    "Ha ganado Cubitus 1 partidas a 0.",
                ],
            ],
        )

        # 1 turno, no coincide ningún valor, gana Humerus
        tu = 1
        d = list(range(1, 14))
        random.shuffle(d)
        c = [d[0], d[1], d[2]]
        h = [d[3], d[4], d[5]]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c + h],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - Cubitus: {c[0]} {c[1]} {c[2]} - Humerus: {h[0]} {h[1]} {h[2]} - Gana Humerus.",
                    "",
                    "Ha ganado Humerus 1 partidas a 0.",
                ],
            ],
        )

        # 3 turnos, Cubitus gana 2 y Humerus 1
        tu = 3
        c1 = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h1 = [
            random.randrange(1, 14),
            random.randrange(1, 14),
            c1[random.randrange(1, 3)],
        ]
        random.shuffle(h1)
        t1 = f"Cubitus: {c1[0]} {c1[1]} {c1[2]} - Humerus: {h1[0]} {h1[1]} {h1[2]} - Gana Cubitus."
        c2 = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h2 = [
            random.randrange(1, 14),
            random.randrange(1, 14),
            c2[random.randrange(1, 3)],
        ]
        random.shuffle(h2)
        t2 = f"Cubitus: {c2[0]} {c2[1]} {c2[2]} - Humerus: {h2[0]} {h2[1]} {h2[2]} - Gana Cubitus."
        d = list(range(1, 14))
        random.shuffle(d)
        c3 = [d[0], d[1], d[2]]
        h3 = [d[3], d[4], d[5]]
        t3 = f"Cubitus: {c3[0]} {c3[1]} {c3[2]} - Humerus: {h3[0]} {h3[1]} {h3[2]} - Gana Humerus."
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c1 + h1 + c2 + h2 + c3 + h3],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - {t1}",
                    f"Partida 2 - {t2}",
                    f"Partida 3 - {t3}",
                    "",
                    "Ha ganado Cubitus 2 partidas a 1.",
                ],
            ],
        )

        # 3 turnos, Cubitus gana 1 y Humerus 2
        tu = 3
        d = list(range(1, 14))
        random.shuffle(d)
        c1 = [d[0], d[1], d[2]]
        h1 = [d[3], d[4], d[5]]
        t1 = f"Cubitus: {c1[0]} {c1[1]} {c1[2]} - Humerus: {h1[0]} {h1[1]} {h1[2]} - Gana Humerus."
        c2 = [random.randrange(1, 14), random.randrange(1, 14), random.randrange(1, 14)]
        h2 = [
            random.randrange(1, 14),
            random.randrange(1, 14),
            c2[random.randrange(1, 3)],
        ]
        random.shuffle(h2)
        t2 = f"Cubitus: {c2[0]} {c2[1]} {c2[2]} - Humerus: {h2[0]} {h2[1]} {h2[2]} - Gana Cubitus."
        d = list(range(1, 14))
        random.shuffle(d)
        c3 = [d[0], d[1], d[2]]
        h3 = [d[3], d[4], d[5]]
        t3 = f"Cubitus: {c3[0]} {c3[1]} {c3[2]} - Humerus: {h3[0]} {h3[1]} {h3[2]} - Gana Humerus."
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", c1 + h1 + c2 + h2 + c3 + h3],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    "",
                    "¿Cuántas partidas van a jugar? ",
                    "",
                    f"Partida 1 - {t1}",
                    f"Partida 2 - {t2}",
                    f"Partida 3 - {t3}",
                    "",
                    "Ha ganado Humerus 2 partidas a 1.",
                ],
            ],
        )

        # turnos impar
        tu = 2 * random.randrange(1, 4) + 1
        c = []
        h = []
        t = []
        gc = gh = 0
        for i in range(tu):
            if random.randrange(0, 2) == 0:
                ci = [
                    random.randrange(1, 14),
                    random.randrange(1, 14),
                    random.randrange(1, 14),
                ]
                hi = [
                    random.randrange(1, 14),
                    random.randrange(1, 14),
                    ci[random.randrange(1, 3)],
                ]
                random.shuffle(hi)
                t += [
                    f"Partida {i + 1} - Cubitus: {ci[0]} {ci[1]} {ci[2]} - Humerus: {hi[0]} {hi[1]} {hi[2]} - Gana Cubitus."
                ]
                gc += 1
            else:
                di = list(range(1, 14))
                random.shuffle(di)
                ci = [di[0], di[1], di[2]]
                hi = [di[3], di[4], di[5]]
                t += [
                    f"Partida {i + 1} - Cubitus: {ci[0]} {ci[1]} {ci[2]} - Humerus: {hi[0]} {hi[1]} {hi[2]} - Gana Humerus."
                ]
                gh += 1
            c += [ci]
            h += [hi]
        if gc > gh:
            f = f"Ha ganado Cubitus {gc} partidas a {gh}."
        else:
            f = f"Ha ganado Humerus {gc} partidas a {gh}."
        ch = []
        for i in range(tu):
            ch += c[i]
            ch += h[i]
        tmp_output = [
            "JUEGO DE DADOS (1)",
            "",
            "¿Cuántas partidas van a jugar? ",
            "",
        ]
        for i in range(tu):
            tmp_output += [t[i]]
        tmp_output += ["", f]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [tu]],
            ["random", ch],
            ["output", tmp_output],
        )

        # Exercise 2223_31 END
