import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 2122_11:
        # Exercise 2122_11 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/21-22/examen-220517.html

        # kg negativo
        kg = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    "Por favor, escriba un número positivo.",
                ],
            ],
        )

        # kg = 0
        kg = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    "0.0 kg son 0 berkovets, 0 puds, 0 funts y 0.0 lots.",
                ],
            ],
        )

        # lots
        l = round(random.randrange(1, 320) / 10, 1)
        kg = round(l * 12.7974 / 1000, 3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    f"{kg} kg son 0 berkovets, 0 puds, 0 funts y {l} lots.",
                ],
            ],
        )

        # lots, funts
        l = round(random.randrange(1, 320) / 10, 1)
        f = random.randrange(1, 40)
        kg = round((l + 32 * f) * 12.7974 / 1000, 3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    f"{kg} kg son 0 berkovets, 0 puds, {f} funts y {l} lots.",
                ],
            ],
        )

        # lots, funts, puds
        l = round(random.randrange(1, 320) / 10, 1)
        f = random.randrange(1, 40)
        p = random.randrange(1, 10)
        kg = round((l + 32 * f + 40 * 32 * p) * 12.7974 / 1000, 3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    f"{kg} kg son 0 berkovets, {p} puds, {f} funts y {l} lots.",
                ],
            ],
        )

        # lots, funts, puds, berkovet
        l = round(random.randrange(1, 320) / 10, 1)
        f = random.randrange(1, 40)
        p = random.randrange(1, 10)
        b = random.randrange(1, 20)
        kg = round((l + 32 * f + 40 * 32 * p + 10 * 40 * 32 * b) * 12.7974 / 1000, 3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    f"{kg} kg son {b} berkovets, {p} puds, {f} funts y {l} lots.",
                ],
            ],
        )

        # lots, funts, puds, berkovet
        l = 31.9
        f = 39
        p = 9
        b = random.randrange(1, 20)
        kg = round((l + 32 * f + 40 * 32 * p + 10 * 40 * 32 * b) * 12.7974 / 1000, 3)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [kg]],
            [
                "output",
                [
                    "CONVERTIDOR DE KILOGRAMOS EN LOTS, FUNTS, PUDS y BERKOVETS",
                    "Escriba una cantidad de kilogramos: ",
                    f"{kg} kg son {b} berkovets, {p} puds, {f} funts y {l} lots.",
                ],
            ],
        )

        # Exercise 2122_11 END

    elif exercise_id == 2122_12:
        # Exercise 2122_12 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/21-22/examen-220517.html

        # turnos negativo
        tu = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "¡No se puede jugar menos de un turno!",
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
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "¡No se puede jugar menos de un turno!",
                ],
            ],
        )

        # 1 turno, gana Cubitus
        tu = 1
        c = random.randrange(2, 7)
        h = random.randrange(1, c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c}",
                    f"Tirada de Humerus: {h}",
                    "Cubitus ha ganado el turno.",
                    f"Cubitus tiene {c + h} punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Cubitus ha ganado la partida {c + h} a 0.",
                ],
            ],
        )

        # 1 turno, gana Humerus
        tu = 1
        h = random.randrange(2, 7)
        c = random.randrange(1, h)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c}",
                    f"Tirada de Humerus: {h}",
                    "Humerus ha ganado el turno.",
                    f"Cubitus tiene 0 punto(s) y Humerus tiene {c + h} punto(s).",
                    "",
                    f"Humerus ha ganado la partida {c + h} a 0.",
                ],
            ],
        )

        # 1 turno, empate
        tu = 1
        c = random.randrange(1, 7)
        h = c
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c, h]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c}",
                    f"Tirada de Humerus: {h}",
                    f"Se acumulan {c + h} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # 2 turnos, Empate + Cubitus: gana Cubitus
        tu = 2
        c1 = random.randrange(1, 7)
        h1 = c1
        c2 = random.randrange(2, 7)
        h2 = random.randrange(1, c2)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c1, h1, c2, h2]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c1}",
                    f"Tirada de Humerus: {h1}",
                    f"Se acumulan {c1 + h1} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Tirada de Cubitus: {c2}",
                    f"Tirada de Humerus: {h2}",
                    "Cubitus ha ganado el turno.",
                    f"Cubitus tiene {c1 + h1 + c2 + h2} punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Cubitus ha ganado la partida {c1 + h1 + c2 + h2} a 0.",
                ],
            ],
        )

        # 2 turnos, Humerus + Empate: gana Humerus
        tu = 2
        h1 = random.randrange(2, 7)
        c1 = random.randrange(1, h1)
        c2 = random.randrange(1, 7)
        h2 = c2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c1, h1, c2, h2]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c1}",
                    f"Tirada de Humerus: {h1}",
                    "Humerus ha ganado el turno.",
                    f"Cubitus tiene 0 punto(s) y Humerus tiene {c1 + h1} punto(s).",
                    "",
                    f"Tirada de Cubitus: {c2}",
                    f"Tirada de Humerus: {h2}",
                    f"Se acumulan {c2 + h2} puntos para el próximo turno.",
                    f"Cubitus tiene 0 punto(s) y Humerus tiene {c1 + h1} punto(s).",
                    "",
                    f"Humerus ha ganado la partida {c1 + h1} a 0.",
                ],
            ],
        )

        # 2 turnos, Humerus + Cubitus: Empate
        tu = 2
        h1 = random.randrange(2, 7)
        c1 = random.randrange(1, h1)
        c2 = h1
        h2 = c1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c1, h1, c2, h2]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c1}",
                    f"Tirada de Humerus: {h1}",
                    "Humerus ha ganado el turno.",
                    f"Cubitus tiene 0 punto(s) y Humerus tiene {c1 + h1} punto(s).",
                    "",
                    f"Tirada de Cubitus: {c2}",
                    f"Tirada de Humerus: {h2}",
                    "Cubitus ha ganado el turno.",
                    f"Cubitus tiene {c1 + c2} punto(s) y Humerus tiene {h1 + h2} punto(s).",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # 3 turnos, Empate + Empate + Cubitus: gana Cubitus
        tu = 3
        h1 = random.randrange(1, 7)
        c1 = h1
        c2 = random.randrange(1, 7)
        h2 = c2
        c3 = random.randrange(2, 7)
        h3 = random.randrange(1, c3)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c1, h1, c2, h2, c3, h3]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c1}",
                    f"Tirada de Humerus: {h1}",
                    f"Se acumulan {c1 + h1} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Tirada de Cubitus: {c2}",
                    f"Tirada de Humerus: {h2}",
                    f"Se acumulan {c1 + h1 + c2 + h2} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Tirada de Cubitus: {c3}",
                    f"Tirada de Humerus: {h3}",
                    "Cubitus ha ganado el turno.",
                    f"Cubitus tiene {c1 + h1 + c2 + h2 + c3 + h3} punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Cubitus ha ganado la partida {c1 + h1 + c2 + h2 + c3 + h3} a 0.",
                ],
            ],
        )

        # 3 turnos, Empate + Empate + Empate: Empate
        tu = 3
        h1 = random.randrange(1, 7)
        c1 = h1
        c2 = random.randrange(1, 7)
        h2 = c2
        c3 = random.randrange(2, 7)
        h3 = c3
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [tu]],
            ["random", [c1, h1, c2, h2, c3, h3]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TODO PARA EL GANADOR",
                    "¿Cuántos turnos se van a jugar? ",
                    "",
                    f"Tirada de Cubitus: {c1}",
                    f"Tirada de Humerus: {h1}",
                    f"Se acumulan {c1 + h1} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Tirada de Cubitus: {c2}",
                    f"Tirada de Humerus: {h2}",
                    f"Se acumulan {c1 + h1 + c2 + h2} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    f"Tirada de Cubitus: {c3}",
                    f"Tirada de Humerus: {h3}",
                    f"Se acumulan {c1 + h1 + c2 + h2 + c3 + h3} puntos para el próximo turno.",
                    "Cubitus tiene 0 punto(s) y Humerus tiene 0 punto(s).",
                    "",
                    "Han empatado.",
                ],
            ],
        )

        # n turnos, Humerus/Cubitus/Empate al azar: gana quien sea
        tu = random.randrange(8, 15)
        tmp_random = []
        tmp_output = [
            "JUEGO DE DADOS: TODO PARA EL GANADOR",
            "¿Cuántos turnos se van a jugar? ",
            "",
        ]
        th = tc = tmphc = 0
        for _ in range(tu):
            c = random.randrange(1, 7)
            h = random.randrange(1, 7)
            tmp_random += [c, h]
            tmp_output += [
                f"Tirada de Cubitus: {c}",
                f"Tirada de Humerus: {h}",
            ]
            if c > h:
                tc += c + h + tmphc
                tmphc = 0
                tmp_output += ["Cubitus ha ganado el turno."]
            elif h > c:
                th += c + h + tmphc
                tmphc = 0
                tmp_output += ["Humerus ha ganado el turno."]
            else:
                tmphc += c + h
                tmp_output += [f"Se acumulan {tmphc} puntos para el próximo turno."]
            tmp_output += [
                f"Cubitus tiene {tc} punto(s) y Humerus tiene {th} punto(s)."
            ]
            tmp_output += [""]
        if tc > th:
            tmp_output += [f"Cubitus ha ganado la partida {tc} a {th}."]
        elif th > tc:
            tmp_output += [f"Humerus ha ganado la partida {th} a {tc}."]
        else:
            tmp_output += ["Han empatado."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", [tu]],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 2122_12 END

    elif exercise_id == 2122_13:
        # Exercise 2122_13 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/21-22/examen-220517.html

        caracteres = "abcdefghijklmnñopqrstuvwxyz"

        # Errores: primer jugador sin nombre, segundo jugador sin nombre, nombres iguales, puntos inferiores a 10
        tmp_input = []
        tmp_output = ["JUEGO DE DADOS: IGUALES O DISTINTOS"]
        # Número de veces que deja en blanco el nombre del primer jugador
        nja = random.randrange(2, 7)
        ja = ""
        for _ in range(random.randrange(3, 10)):
            ja += caracteres[random.randrange(len(caracteres))]
        for _ in range(nja):
            tmp_input += [""]
            tmp_output += [
                "¿Cómo se llama el primer jugador? ",
                "¡No ha escrito ningún nombre!",
            ]
        tmp_output += ["¿Cómo se llama el primer jugador? "]
        tmp_input += [ja]
        # Número de veces que deja en blanco el nombre del segundo jugador
        njb = random.randrange(2, 7)
        jb = ""
        for _ in range(random.randrange(3, 10)):
            jb += caracteres[random.randrange(len(caracteres))]
        for _ in range(njb):
            tmp_input += [""]
            tmp_output += [
                "¿Cómo se llama el segundo jugador? ",
                "¡No ha escrito ningún nombre!",
            ]
        # Número de veces que el nombre del segundo jugador coincide con el del primero
        njc = random.randrange(2, 7)
        for _ in range(njc):
            tmp_input += [ja]
            tmp_output += [
                "¿Cómo se llama el segundo jugador? ",
                "¡Los jugadores no se pueden llamar igual!",
            ]
        tmp_output += ["¿Cómo se llama el segundo jugador? "]
        tmp_input += [jb]
        # Número de veces que el número de puntos es insuficiente
        for _ in range(njc):
            njd = random.randrange(-10, 10)
            tmp_input += [njd]
            tmp_output += [
                "¿Cuántos puntos se necesitan para ganar la partida (como mínimo, 10)? ",
                "¡El valor mínimo es 10!",
            ]
        tmp_input += [10]
        tmp_output += [
            "¿Cuántos puntos se necesitan para ganar la partida (como mínimo, 10)? ",
            "",
        ]
        # Gana Cubitus a la primera
        tmp_random = [6, 6]
        tmp_output += [
            f"Dado {ja}: 6 - Dado {jb}: 6",
            f"12 puntos para {jb}",
            f"Puntos acumulados. {ja}: 0 - {jb}: 12",
            "",
            f"Ha ganado {jb}.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Gana Jugador 1
        ja = ""
        for _ in range(random.randrange(3, 10)):
            ja += caracteres[random.randrange(len(caracteres))]
        jb = ""
        for _ in range(random.randrange(3, 10)):
            jb += caracteres[random.randrange(len(caracteres))]
        tmp_input = [ja, jb]
        tmp_output = [
            "JUEGO DE DADOS: IGUALES O DISTINTOS",
            "¿Cómo se llama el primer jugador? ",
            "¿Cómo se llama el segundo jugador? ",
            "¿Cuántos puntos se necesitan para ganar la partida (como mínimo, 10)? ",
            "",
        ]
        # Genero tiradas
        tiradas = []
        # saco un valor mayor que 10
        tope = random.randrange(10, 20)
        # añado tiradas con valores repetidos hasta superar a tope
        p2 = 0
        while p2 <= tope:
            d = random.randrange(1, 7)
            tiradas += [[d,d]]
            p2 += d + d
        # el valor para ganar es p2 + 1 (no tope)
        tmp_input += [p2 + 1]
        # añado tiradas con valores distintos hasta igualar o superar p2 + 1
        p1 = 0
        while p1 < p2 + 1:
            d1 = random.randrange(2, 7)
            d2 = random.randrange(1, d1)
            if random.randrange(1):
                tiradas += [[d1, d2]]
            else:
                tiradas += [[d2, d1]]
            p1 += d2
        # barajo las tiradas (mantengo la última para asegurar que el jugador 1 gane al final)
        ultima = tiradas[-1]
        del tiradas[-1]
        random.shuffle(tiradas)
        tiradas += [ultima]
        # añado tiras a tmp_random y tmp_output
        tmp_random = []
        ta = tb = 0
        for tirada in tiradas:
            tmp_random += tirada
            tmp_output += [f"Dado {ja}: {tirada[0]} - Dado {jb}: {tirada[1]}"]
            if tirada[0] == tirada[1]:
                tmp_output += [f"{tirada[0] + tirada[1]} puntos para {jb}"]
                tb += tirada[0] + tirada[1]
            else:
                tmp_output += [f"{min(tirada[0], tirada[1])} punto(s) para {ja}"]
                ta += min(tirada[0], tirada[1])
            tmp_output += [f"Puntos acumulados. {ja}: {ta} - {jb}: {tb}"]
            tmp_output += [""]
        tmp_output += [f"Ha ganado {ja}."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )


        # Gana Jugador 2
        ja = ""
        for _ in range(random.randrange(3, 10)):
            ja += caracteres[random.randrange(len(caracteres))]
        jb = ""
        for _ in range(random.randrange(3, 10)):
            jb += caracteres[random.randrange(len(caracteres))]
        tmp_input = [ja, jb]
        tmp_output = [
            "JUEGO DE DADOS: IGUALES O DISTINTOS",
            "¿Cómo se llama el primer jugador? ",
            "¿Cómo se llama el segundo jugador? ",
            "¿Cuántos puntos se necesitan para ganar la partida (como mínimo, 10)? ",
            "",
        ]
        # Genero tiradas
        tiradas = []
        # saco un valor mayor que 10
        tope = random.randrange(10, 20)
        # añado tiradas con valores distintos que supere a tope
        p1 = 0
        while p1 <= tope:
            d1 = random.randrange(1, 7)
            d2 = random.randrange(1, 7)
            while d2 == d1:
                d2 = random.randrange(1, 7)
            tiradas += [[d1,d2]]
            p1 += min(d1, d2)
        # el valor para ganar es p1 + 1 (no tope)
        tmp_input += [p1 + 1]
        # añado tiradas con valores iguales hasta igualar o superar p1 + 1
        p2 = 0
        while p2 < p1 + 1:
            d = random.randrange(1, 7)
            tiradas += [[d, d]]
            p2 += d + d
        # barajo las tiradas (mantengo la última para asegurar que el jugador 1 gane al final)
        ultima = tiradas[-1]
        del tiradas[-1]
        random.shuffle(tiradas)
        tiradas += [ultima]
        # añado tiras a tmp_random y tmp_output
        tmp_random = []
        ta = tb = 0
        for tirada in tiradas:
            tmp_random += tirada
            tmp_output += [f"Dado {ja}: {tirada[0]} - Dado {jb}: {tirada[1]}"]
            if tirada[0] == tirada[1]:
                tmp_output += [f"{tirada[0] + tirada[1]} puntos para {jb}"]
                tb += tirada[0] + tirada[1]
            else:
                tmp_output += [f"{min(tirada[0], tirada[1])} punto(s) para {ja}"]
                ta += min(tirada[0], tirada[1])
            tmp_output += [f"Puntos acumulados. {ja}: {ta} - {jb}: {tb}"]
            tmp_output += [""]
        tmp_output += [f"Ha ganado {jb}."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 2122_13 END
