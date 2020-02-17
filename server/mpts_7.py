import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 71:
        # Exercise 71 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["TIRADA DE DADOS", "Número de dados: ", "¡Imposible!"]],
        )

        # Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["TIRADA DE DADOS", "Número de dados: ", "¡Imposible!"]],
        )

        # Varios
        a = random.randrange(1, 11)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_output = ["TIRADA DE DADOS", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varios
        a = random.randrange(10, 21)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_output = ["TIRADA DE DADOS", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 71 END

    elif exercise_id == 72:
        # Exercise 72 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Uno
        a = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Varios
        a = random.randrange(2, 11)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_output = ["TIRADAS DE DADO", "Número de jugadores: "]
        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_random[i]} "]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varios
        a = random.randrange(11, 21)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_output = ["TIRADAS DE DADO", "Número de jugadores: "]
        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_random[i]} "]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 72 END

    elif exercise_id == 73:
        # Exercise 73 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["OBTENER VALOR (1)", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["OBTENER VALOR (1)", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Objetivo: Cero
        a = random.randrange(1, 20)
        b = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (1)",
                    "Número de jugadores: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: negativo
        a = random.randrange(1, 20)
        b = -random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (1)",
                    "Número de jugadores: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: Siete
        a = random.randrange(1, 20)
        b = 7
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (1)",
                    "Número de jugadores: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: mayor que siete
        a = random.randrange(1, 20)
        b = random.randrange(8, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (1)",
                    "Número de jugadores: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Varios
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_output = [
            "OBTENER VALOR (1)",
            "Número de jugadores: ",
            "Valor a conseguir: ",
        ]
        for i in range(a):
            if tmp_random[i] == b:
                tmp_output += [f"Jugador {i + 1}: {tmp_random[i]} CONSEGUIDO"]
            else:
                tmp_output += [f"Jugador {i + 1}: {tmp_random[i]}"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varios (algún acierto)
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        tmp_random[random.randrange(a)] = b
        tmp_output = [
            "OBTENER VALOR (1)",
            "Número de jugadores: ",
            "Valor a conseguir: ",
        ]
        for i in range(a):
            if tmp_random[i] == b:
                tmp_output += [f"Jugador {i + 1}: {tmp_random[i]} CONSEGUIDO"]
            else:
                tmp_output += [f"Jugador {i + 1}: {tmp_random[i]}"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 73 END

    elif exercise_id == 74:
        # Exercise 74 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["OBTENER VALOR (2)", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["OBTENER VALOR (2)", "Número de dados: ", "¡Imposible!"]],
        )

        # Objetivo: Cero
        a = random.randrange(1, 20)
        b = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (2)",
                    "Número de dados: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: negativo
        a = random.randrange(1, 20)
        b = -random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (2)",
                    "Número de dados: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: Siete
        a = random.randrange(1, 20)
        b = 7
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (2)",
                    "Número de dados: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Objetivo: mayor que siete
        a = random.randrange(1, 20)
        b = random.randrange(8, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "OBTENER VALOR (2)",
                    "Número de dados: ",
                    "Valor a conseguir: ",
                    f"¡Imposible conseguir un {b}!",
                ],
            ],
        )

        # Varios: pierde
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        tmp_random = []
        for i in range(a):
            dado = random.randrange(1, 7)
            # si coincide con el objetivo, lo vuelve a tirar
            while dado == b:
                dado = random.randrange(1, 7)
            tmp_random += [dado]
        tmp_output = ["OBTENER VALOR (2)", "Número de dados: ", "Valor a conseguir: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp_output += ["El jugador ha perdido."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varios: gana
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, 7)]
        # Cambia uno cualquiera por el objetivo
        tmp_random[random.randrange(a)] = b
        tmp_output = ["OBTENER VALOR (2)", "Número de dados: ", "Valor a conseguir: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp_output += ["El jugador ha ganado."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 74 END

    elif exercise_id == 75:
        # Exercise 75 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS ALTO (1)", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS ALTO (1)", "Número de dados: ", "¡Imposible!"]],
        )

        # Dado máximo entre 1 y 3
        a = random.randrange(1, 11)
        b = random.randrange(1, 4)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a)] = b
        tmp_output = ["EL DADO MÁS ALTO (1)", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp_output += [f"El dado más alto es {b}."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Dado máximo entre 4 y 6
        a = random.randrange(1, 11)
        b = random.randrange(4, 7)
        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a)] = b
        tmp_output = ["EL DADO MÁS ALTO (1)", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp_output += [f"El dado más alto es {b}."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 75 END

    elif exercise_id == 76:
        # Exercise 76 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS ALTO (2)", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS ALTO (2)", "Número de dados: ", "¡Imposible!"]],
        )

        # Gana el jugador 1
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(5, 7)
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a)] = b

        c = random.randrange(1, 5)
        for i in range(a):
            tmp_random += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a, a + a)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador 1."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # # Gana el jugador 2
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(1, 5)
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a)] = b

        c = random.randrange(5, 7)
        for i in range(a):
            tmp_random += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a, a + a)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador 2."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Empate
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(3, 7)
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a)] = b

        c = b
        for i in range(a):
            tmp_random += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_random[random.randrange(a, a + a)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Han empatado."]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 76 END

    elif exercise_id == 77:
        # Exercise 77 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["PARES Y NONES", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["PARES Y NONES", "Número de dados: ", "¡Imposible!"]],
        )

        # Gana el jugador pares
        a = random.randrange(1, 11)
        tmp_input = [2 * a + 1]

        tmp_random = []
        for i in range(a + 1):
            tmp_random += [2 * random.randrange(1, 4)]
        for i in range(a):
            tmp_random += [2 * random.randrange(3) + 1]
        random.shuffle(tmp_random)

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a + 1):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador de los pares."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Gana el jugador impares
        a = random.randrange(1, 11)
        tmp_input = [2 * a + 1]

        tmp_random = []
        for i in range(a):
            tmp_random += [2 * random.randrange(1, 4)]
        for i in range(a + 1):
            tmp_random += [2 * random.randrange(3) + 1]
        random.shuffle(tmp_random)

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a + 1):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador de los impares."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Empate
        a = random.randrange(1, 11)
        tmp_input = [2 * a]

        tmp_random = []
        for i in range(a):
            tmp_random += [2 * random.randrange(1, 4)]
        for i in range(a):
            tmp_random += [2 * random.randrange(3) + 1]
        random.shuffle(tmp_random)

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["Han empatado."]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )
        # Exercise 77 END

    elif exercise_id == 78:
        # Exercise 78 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"]],
        )

        # Dado más bajo: sólo hay uno
        a = random.randrange(2, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b + 1, 7)]
        ganador = random.randrange(a)
        tmp_random[ganador] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_random[i]}"]

        tmp_output += [f"Ha ganado el jugador {ganador + 1}."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Dado más bajo: hay dos
        a = random.randrange(2, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b + 1, 7)]

        lista = random.sample(range(a), k=2)
        for i in lista:
            tmp_random[i] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_random[i]}"]

        tmp_output += [f"Ha ganado el jugador {max(lista) + 1}."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Dado más bajo: hay más de dos
        a = random.randrange(8, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b + 1, 7)]

        lista = random.sample(range(a), k=random.randrange(3, 6))
        for i in lista:
            tmp_random[i] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_random[i]}"]

        tmp_output += [f"Ha ganado el jugador {max(lista) + 1}."]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 78 END

    elif exercise_id == 79:
        # Exercise 79 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            ],
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            ],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            ],
        )

        # Gana el jugador 2
        a = random.randrange(2, 11)
        b_1 = random.randrange(1, 4)
        b_2 = b_1
        c_1 = random.randrange(4, 6)
        c_2 = random.randrange(c_1 + 1, 7)

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a), 2)
        tmp_random[uno] = b_1
        tmp_random[dos] = c_1
        for i in range(a):
            tmp_random += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a, a + a), 2)
        tmp_random[uno] = b_2
        tmp_random[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_random[a + i]} "
        tmp_output += [tmp]

        tmp_output += [f"Ha ganado el jugador 2."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Gana el jugador 1
        a = random.randrange(2, 11)
        b_1 = random.randrange(2, 4)
        b_2 = random.randrange(1, b_1)
        c_1 = random.randrange(4, 6)
        c_2 = c_1

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a), 2)
        tmp_random[uno] = b_1
        tmp_random[dos] = c_1
        for i in range(a):
            tmp_random += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a, a + a), 2)
        tmp_random[uno] = b_2
        tmp_random[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_random[a + i]} "
        tmp_output += [tmp]

        tmp_output += [f"Ha ganado el jugador 1."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Empatan
        a = random.randrange(2, 11)
        b_1 = random.randrange(1, 4)
        b_2 = b_1
        c_1 = random.randrange(4, 7)
        c_2 = c_1

        tmp_input = [a]
        tmp_random = []
        for i in range(a):
            tmp_random += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a), 2)
        tmp_random[uno] = b_1
        tmp_random[dos] = c_1
        for i in range(a):
            tmp_random += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a, a + a), 2)
        tmp_random[uno] = b_2
        tmp_random[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_random[a + i]} "
        tmp_output += [tmp]

        tmp_output += [f"Han empatado."]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 79 END

    elif exercise_id == 80:
        # Exercise 80 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"]],
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            ["output", ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"]],
        )

        # Gana
        a = random.randrange(2, 11)

        tmp_input = [a]
        tmp_random = []
        anterior = random.randrange(1, 7)
        tmp_random += [anterior]
        for i in range(a):
            dado = random.randrange(1, 7)
            while dado == anterior:
                dado = random.randrange(1, 7)
            tmp_random += [dado]
            anterior = dado

        tmp_output = ["DADOS IGUALES", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["El jugador ha ganado."]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Pierde
        a = random.randrange(2, 11)

        tmp_input = [a]
        tmp_random = []
        anterior = random.randrange(1, 7)
        tmp_random += [anterior]
        for i in range(a):
            dado = random.randrange(1, 7)
            while dado == anterior:
                dado = random.randrange(1, 7)
            tmp_random += [dado]
            anterior = dado
        # Cambia uno al azar por el anterior
        c = random.randrange(a - 1)
        tmp_random[c + 1] = tmp_random[c]

        tmp_output = ["DADOS IGUALES", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_random[i]} "
        tmp_output += [tmp]

        tmp_output += ["El jugador ha perdido."]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 80 END
