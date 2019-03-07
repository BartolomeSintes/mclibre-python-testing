import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 81:
        # Exercise 81 BEGINNING
        # http://localhost/mclibre/consultar/python/ejercicios/ej-for-1.html

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

        # Exercise 81 END

    elif exercise_id == 82:
        # Exercise 82 BEGINNING
        # http://localhost/mclibre/consultar/python/ejercicios/ej-for-1.html

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

        # Exercise 82 END

    elif exercise_id == 83:
        # Exercise 83 BEGINNING
        # http://localhost/mclibre/consultar/python/ejercicios/ej-for-1.html

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
        a = 1  # random.randrange(1, 11)
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

        # Exercise 83 END

    elif exercise_id == 84:
        # Exercise 84 BEGINNING
        # http://localhost/mclibre/consultar/python/ejercicios/ej-for-1.html

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
        tmp_output = [
            "OBTENER VALOR (2)",
            "Número de dados: ",
            "Valor a conseguir: ",
        ]
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
        # Cambia uno cualqueira por el objetivo
        tmp_input[random.randrange(2, a + 2)] = b
        tmp_output = [
            "OBTENER VALOR (2)",
            "Número de dados: ",
            "Valor a conseguir: ",
        ]
        tmp = "Dados: "
        for i in range(a):
            tmp += f"{tmp_input[i + 2]} "
        tmp_output += [tmp]
        tmp_output += ["El jugador ha perdido."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)
        # Exercise 84 END
