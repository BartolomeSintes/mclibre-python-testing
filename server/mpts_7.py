import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 71:
        # Exercise 71 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Cero
        a = 0
        mpts_common.add_test(
            [a], ["TIRADA DE DADOS", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a], ["TIRADA DE DADOS", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Varios
        a = random.randrange(1, 11)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_output = ["TIRADA DE DADOS", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varios
        a = random.randrange(10, 21)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_output = ["TIRADA DE DADOS", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 71 END

    elif exercise_id == 72:
        # Exercise 72 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        mpts_common.add_test(
            [a],
            ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["TIRADAS DE DADO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Varios
        a = random.randrange(2, 11)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_output = ["TIRADAS DE DADO", "Número de jugadores: "]
        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 1]} "]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varios
        a = random.randrange(11, 21)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_output = ["TIRADAS DE DADO", "Número de jugadores: "]
        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 1]} "]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 72 END

    elif exercise_id == 73:
        # Exercise 73 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["OBTENER VALOR (1)", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["OBTENER VALOR (1)", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Objetivo: Cero
        a = random.randrange(1, 20)
        b = 0
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (1)",
                "Número de jugadores: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: negativo
        a = random.randrange(1, 20)
        b = -random.randrange(1, 20)
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (1)",
                "Número de jugadores: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: Siete
        a = random.randrange(1, 20)
        b = 7
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (1)",
                "Número de jugadores: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: mayor que siete
        a = random.randrange(1, 20)
        b = random.randrange(8, 20)
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (1)",
                "Número de jugadores: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Varios
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_output = [
            "OBTENER VALOR (1)",
            "Número de jugadores: ",
            "Valor a conseguir: ",
        ]
        for i in range(a):
            if tmp_input[i + 2] == b:
                tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 2]} CONSEGUIDO"]
            else:
                tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 2]}"]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varios (algún acierto)
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        tmp_input[random.randrange(2, a + 2)] = b
        tmp_output = [
            "OBTENER VALOR (1)",
            "Número de jugadores: ",
            "Valor a conseguir: ",
        ]
        for i in range(a):
            if tmp_input[i + 2] == b:
                tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 2]} CONSEGUIDO"]
            else:
                tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 2]}"]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 73 END

    elif exercise_id == 74:
        # Exercise 74 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["OBTENER VALOR (2)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["OBTENER VALOR (2)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Objetivo: Cero
        a = random.randrange(1, 20)
        b = 0
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (2)",
                "Número de dados: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: negativo
        a = random.randrange(1, 20)
        b = -random.randrange(1, 20)
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (2)",
                "Número de dados: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: Siete
        a = random.randrange(1, 20)
        b = 7
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (2)",
                "Número de dados: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Objetivo: mayor que siete
        a = random.randrange(1, 20)
        b = random.randrange(8, 20)
        mpts_common.add_test(
            [a, b],
            [
                "OBTENER VALOR (2)",
                "Número de dados: ",
                "Valor a conseguir: ",
                f"¡Imposible conseguir un {b}!",
            ],
            NOT_LAST_TEST,
        )

        # Varios: pierde
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        for i in range(a):
            dado = random.randrange(1, 7)
            # si coincide con el objetivo, lo vuelve a tirar
            while dado == b:
                dado = random.randrange(1, 7)
            tmp_input += [dado]
        tmp_output = ["OBTENER VALOR (2)", "Número de dados: ", "Valor a conseguir: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 2]} "
        tmp_output += [tmp]
        tmp_output += ["El jugador ha perdido."]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varios: gana
        a = random.randrange(1, 11)
        b = random.randrange(1, 7)
        tmp_input = [a, b]
        for i in range(a):
            tmp_input += [random.randrange(1, 7)]
        # Cambia uno cualquiera por el objetivo
        tmp_input[random.randrange(2, a + 2)] = b
        tmp_output = ["OBTENER VALOR (2)", "Número de dados: ", "Valor a conseguir: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 2]} "
        tmp_output += [tmp]
        tmp_output += ["El jugador ha ganado."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 74 END

    elif exercise_id == 75:
        # Exercise 75 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS ALTO (1)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS ALTO (1)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Dado máximo entre 1 y 3
        a = random.randrange(1, 11)
        b = random.randrange(1, 4)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(1, a + 1)] = b
        tmp_output = ["EL DADO MÁS ALTO (1)", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        tmp_output += [f"El dado más alto es {b}."]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Dado máximo entre 4 y 6
        a = random.randrange(1, 11)
        b = random.randrange(4, 7)
        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(1, a + 1)] = b
        tmp_output = ["EL DADO MÁS ALTO (1)", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        tmp_output += [f"El dado más alto es {b}."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 75 END

    elif exercise_id == 76:
        # Exercise 76 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS ALTO (2)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS ALTO (2)", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Gana el jugador 1
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(5, 7)
        for i in range(a):
            tmp_input += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(1, a + 1)] = b

        c = random.randrange(1, 5)
        for i in range(a):
            tmp_input += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(a + 1, a + a + 1)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador 1."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Gana el jugador 2
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(1, 5)
        for i in range(a):
            tmp_input += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(1, a + 1)] = b

        c = random.randrange(5, 7)
        for i in range(a):
            tmp_input += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(a + 1, a + a + 1)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador 2."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Empate
        a = random.randrange(1, 11)
        tmp_input = [a]

        b = random.randrange(3, 7)
        for i in range(a):
            tmp_input += [random.randrange(1, b + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(1, a + 1)] = b

        c = b
        for i in range(a):
            tmp_input += [random.randrange(1, c + 1)]
        # Cambia uno cualquiera por el mayor
        tmp_input[random.randrange(a + 1, a + a + 1)] = c

        tmp_output = ["EL DADO MÁS ALTO (2)", "Número de dados: "]

        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp = "Jugador 2: "
        for i in range(a, a + a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Han empatado."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 76 END

    elif exercise_id == 77:
        # Exercise 77 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a], ["PARES Y NONES", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a], ["PARES Y NONES", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Gana el jugador pares
        a = random.randrange(1, 11)
        tmp_input = [2 * a + 1]

        tmp = []
        for i in range(a + 1):
            tmp += [2 * random.randrange(1, 4)]
        for i in range(a):
            tmp += [2 * random.randrange(3) + 1]
        random.shuffle(tmp)
        tmp_input += tmp

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a + 1):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador de los pares."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Gana el jugador impares
        a = random.randrange(1, 11)
        tmp_input = [2 * a + 1]

        tmp = []
        for i in range(a):
            tmp += [2 * random.randrange(1, 4)]
        for i in range(a + 1):
            tmp += [2 * random.randrange(3) + 1]
        random.shuffle(tmp)
        tmp_input += tmp

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a + 1):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Ha ganado el jugador de los impares."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Empate
        a = random.randrange(1, 11)
        tmp_input = [2 * a]

        tmp = []
        for i in range(a):
            tmp += [2 * random.randrange(1, 4)]
        for i in range(a):
            tmp += [2 * random.randrange(3) + 1]
        random.shuffle(tmp)
        tmp_input += tmp

        tmp_output = ["PARES Y NONES", "Número de dados: "]

        tmp = "Dados: "
        for i in range(2 * a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["Han empatado."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 77 END

    elif exercise_id == 78:
        # Exercise 78 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["EL DADO MÁS BAJO", "Número de jugadores: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Dado más bajo: sólo hay uno
        a = random.randrange(2, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b + 1, 7)]
        ganador = random.randrange(1, a + 1)
        tmp_input[ganador] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 1]}"]

        tmp_output += [f"Ha ganado el jugador {ganador}."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Dado más bajo: hay dos
        a = random.randrange(2, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b + 1, 7)]

        lista = random.sample(range(1, a + 1), k=2)
        for i in lista:
            tmp_input[i] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 1]}"]

        tmp_output += [f"Ha ganado el jugador {max(lista)}."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Dado más bajo: hay más de dos
        a = random.randrange(8, 11)
        b = random.randrange(1, 4)

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b + 1, 7)]

        lista = random.sample(range(1, a + 1), k=random.randrange(3, 6))
        for i in lista:
            tmp_input[i] = b

        tmp_output = ["EL DADO MÁS BAJO", "Número de jugadores: "]

        for i in range(a):
            tmp_output += [f"Jugador {i + 1}: {tmp_input[i + 1]}"]

        tmp_output += [f"Ha ganado el jugador {max(lista)}."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)
        # Exercise 78 END

    elif exercise_id == 79:
        # Exercise 79 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a],
            ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            [a],
            ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a],
            ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Gana el jugador 2
        a = random.randrange(2, 11)
        b_1 = random.randrange(1, 4)
        b_2 = b_1
        c_1 = random.randrange(4, 6)
        c_2 = random.randrange(c_1 + 1, 7)

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(1, a + 1), 2)
        tmp_input[uno] = b_1
        tmp_input[dos] = c_1
        for i in range(a):
            tmp_input += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a + 1, a + a + 1), 2)
        tmp_input[uno] = b_2
        tmp_input[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_input[a + i + 1]} "
        tmp_output += [tmp]

        tmp_output += [f"Ha ganado el jugador 2."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Gana el jugador 1
        a = random.randrange(2, 11)
        b_1 = random.randrange(2, 4)
        b_2 = random.randrange(1, b_1)
        c_1 = random.randrange(4, 6)
        c_2 = c_1

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(1, a + 1), 2)
        tmp_input[uno] = b_1
        tmp_input[dos] = c_1
        for i in range(a):
            tmp_input += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a + 1, a + a + 1), 2)
        tmp_input[uno] = b_2
        tmp_input[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_input[a + i + 1]} "
        tmp_output += [tmp]

        tmp_output += [f"Ha ganado el jugador 1."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Empatan
        a = random.randrange(2, 11)
        b_1 = random.randrange(1, 4)
        b_2 = b_1
        c_1 = random.randrange(4, 7)
        c_2 = c_1

        tmp_input = [a]
        for i in range(a):
            tmp_input += [random.randrange(b_1, c_1 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(1, a + 1), 2)
        tmp_input[uno] = b_1
        tmp_input[dos] = c_1
        for i in range(a):
            tmp_input += [random.randrange(b_2, c_2 + 1)]
        # Cambia dos al azar  por el menor y el mayor
        uno, dos = random.sample(range(a + 1, a + a + 1), 2)
        tmp_input[uno] = b_2
        tmp_input[dos] = c_2

        tmp_output = ["DADO MÁS ALTO Y MÁS BAJO", "Número de dados: "]
        tmp = "Jugador 1: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]
        tmp = "Jugador 2: "
        for i in range(a):
            tmp += f"{tmp_input[a + i + 1]} "
        tmp_output += [tmp]

        tmp_output += [f"Han empatado."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 79 END

    elif exercise_id == 80:
        # Exercise 80 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html

        # Jugadores: Cero
        a = 0
        mpts_common.add_test(
            [a], ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Jugadores: Uno
        a = 1
        mpts_common.add_test(
            [a], ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Jugadores: Negativo
        a = -random.randrange(1, 10)
        mpts_common.add_test(
            [a], ["DADOS IGUALES", "Número de dados: ", "¡Imposible!"], NOT_LAST_TEST
        )

        # Gana
        a = random.randrange(2, 11)

        tmp_input = [a]
        anterior = random.randrange(1, 7)
        tmp_input += [anterior]
        for i in range(a):
            dado = random.randrange(1, 7)
            while dado == anterior:
                dado = random.randrange(1, 7)
            tmp_input += [dado]
            anterior = dado
        # # Cambia dos al azar  por el menor y el mayor
        # uno, dos = random.sample(range(1, a + 1), 2)
        # tmp_input[uno] = b_1
        # tmp_input[dos] = c_1

        tmp_output = ["DADOS IGUALES", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["El jugador ha ganado."]

        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Pierde
        a = random.randrange(2, 11)

        tmp_input = [a]
        anterior = random.randrange(1, 7)
        tmp_input += [anterior]
        for i in range(a):
            dado = random.randrange(1, 7)
            while dado == anterior:
                dado = random.randrange(1, 7)
            tmp_input += [dado]
            anterior = dado
        # Cambia dos al azar  por el menor y el mayor
        c = random.randrange(1, a)
        tmp_input[c + 1] = tmp_input[c]

        tmp_output = ["DADOS IGUALES", "Número de dados: "]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 1]} "
        tmp_output += [tmp]

        tmp_output += ["El jugador ha perdido."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 80 END
