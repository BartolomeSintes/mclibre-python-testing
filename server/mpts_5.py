import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 51:
        # Exercise 51 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        # Empate
        a = random.randrange(1, 7)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Alberto ha sacado un {a}.",
                    f"Bárbara ha sacado un {b}.",
                    "Han empatado.",
                ],
            ],
        )

        # gana Alberto
        a = random.randrange(2, 7)
        b = a - random.randrange(1, a)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Alberto ha sacado un {a}.",
                    f"Bárbara ha sacado un {b}.",
                    "Ha ganado Alberto.",
                ],
            ],
        )

        # gana Bárbara
        a = random.randrange(1, 6)
        b = random.randrange(a + 1, 7)
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a, b]],
            [
                "output",
                [
                    "JUEGO DE DADOS (1)",
                    f"Alberto ha sacado un {a}.",
                    f"Bárbara ha sacado un {b}.",
                    "Ha ganado Bárbara.",
                ],
            ],
        )

        # Exercise 51 END

    elif exercise_id == 52:
        # Exercise 52 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        # el mayor es de un jugador, pero gana el otro
        a_1 = random.randrange(5, 7)
        b_1 = random.randrange(4, a_1)
        b_2 = random.randrange(4, a_1)
        a_2 = random.randrange(1, b_1 + b_2 - a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado David.",
                ],
            ],
        )

        # Los mayores coinciden, gana un jugador
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(2, a_1)
        b_2 = random.randrange(1, a_2)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Carmen.",
                ],
            ],
        )

        # Los mayores coinciden, gana el otro
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(1, a_1 - 1)
        b_2 = random.randrange(a_2 + 1, a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado David.",
                ],
            ],
        )

        # Empate
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_1
        b_2 = a_2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Han empatado.",
                ],
            ],
        )

        # Empate, cruzado
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_2
        b_2 = a_1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Han empatado.",
                ],
            ],
        )

        # Los dos dados son mayores
        a_1 = random.randrange(2, 6)
        a_2 = random.randrange(2, 6)
        b_1 = random.randrange(1, a_2)
        b_2 = random.randrange(1, a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Carmen.",
                ],
            ],
        )

        # Los dos dados son mayores, cruzados
        b_1 = random.randrange(2, 6)
        b_2 = random.randrange(2, 6)
        a_1 = random.randrange(1, b_1)
        a_2 = random.randrange(1, b_2)
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (2)",
                    f"Carmen ha sacado un {a_1} y un {a_2}.",
                    f"David ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado David.",
                ],
            ],
        )

        # Exercise 52 END

    elif exercise_id == 53:
        # Exercise 53 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        # el mayor es de un jugador, la suma del otro es mayor
        a_1 = random.randrange(5, 7)
        b_1 = random.randrange(4, a_1)
        b_2 = random.randrange(4, a_1)
        a_2 = random.randrange(1, b_1 + b_2 - a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Elena.",
                ],
            ],
        )

        # Los mayores coinciden, gana un jugador
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(2, a_1)
        b_2 = random.randrange(1, a_2)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Elena.",
                ],
            ],
        )

        # Los mayores coinciden, gana el otro
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(1, a_1 - 1)
        b_2 = random.randrange(a_2 + 1, a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Fernando.",
                ],
            ],
        )

        # Empate
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_1
        b_2 = a_2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Han empatado.",
                ],
            ],
        )

        # Empate, cruzado
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_2
        b_2 = a_1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Han empatado.",
                ],
            ],
        )

        # Los dos dados son mayores
        a_1 = random.randrange(2, 6)
        a_2 = random.randrange(2, 6)
        b_1 = random.randrange(1, a_2)
        b_2 = random.randrange(1, a_1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Elena.",
                ],
            ],
        )

        # Los dos dados son mayores, cruzados
        b_1 = random.randrange(2, 6)
        b_2 = random.randrange(2, 6)
        a_1 = random.randrange(1, b_1)
        a_2 = random.randrange(1, b_2)
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a_1, a_2, b_1, b_2]],
            [
                "output",
                [
                    "JUEGO DE DADOS (3)",
                    f"Elena ha sacado un {a_1} y un {a_2}.",
                    f"Fernando ha sacado un {b_1} y un {b_2}.",
                    "Ha ganado Fernando.",
                ],
            ],
        )

        # Exercise 53 END

    elif exercise_id == 54:
        # Exercise 54 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        # Se pasan los dos
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(max(1, 5 - a_1 + 1), 11)
        a_3 = random.randrange(max(1, 15 - a_1 - a_2 + 1), 11)
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(max(1, 5 - b_1 + 1), 11)
        b_3 = random.randrange(max(1, 15 - b_1 - b_2 + 1), 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, a_3, b_1, b_2, b_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    "No ha ganado nadie.",
                ],
            ],
        )

        # El primero se pasa y el segundo no
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(max(1, 5 - a_1 + 1), 11)
        a_3 = random.randrange(max(1, 15 - a_1 - a_2 + 1), 11)
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(1, min(11, 15 - b_1))
        b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, a_3, b_1, b_2, b_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    "Ha ganado Héctor.",
                ],
            ],
        )

        # El segundo se pasa y el primero no
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(1, min(11, 15 - a_1))
        a_3 = random.randrange(1, min(11, 15 - a_1 - a_2 + 1))
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(max(1, 5 - b_1 + 1), 11)
        b_3 = random.randrange(max(1, 15 - b_1 - b_2 + 1), 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, a_3, b_1, b_2, b_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    "Ha ganado Gloria.",
                ],
            ],
        )

        # Ninguno se pasa, pero no empatan
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(1, min(11, 15 - a_1))
        a_3 = random.randrange(1, min(11, 15 - a_1 - a_2 + 1))
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(1, min(11, 15 - b_1))
        b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        while a_1 + a_2 + a_3 == b_1 + b_2 + b_3:
            b_1 = random.randrange(1, 11)
            b_2 = random.randrange(1, min(11, 15 - b_1))
            b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        if a_1 + a_2 + a_3 < b_1 + b_2 + b_3:
            a_1, a_2, a_3, b_1, b_2, b_3 = b_1, b_2, b_3, a_1, a_2, a_3
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [a_1, a_2, a_3, b_1, b_2, b_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    "Ha ganado Gloria.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [b_1, b_2, b_3, a_1, a_2, a_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    f"Héctor ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    "Ha ganado Héctor.",
                ],
            ],
        )

        # Empatan sin pasarse
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(1, min(11, 15 - a_1))
        a_3 = random.randrange(1, min(11, 15 - a_1 - a_2 + 1))
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(1, min(11, 15 - b_1))
        b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        while a_1 + a_2 + a_3 != b_1 + b_2 + b_3:
            b_1 = random.randrange(1, 11)
            b_2 = random.randrange(1, min(11, 15 - b_1))
            b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        mpts_common.add_test(
            LAST_TEST,
            ["random", [a_1, a_2, a_3, b_1, b_2, b_3]],
            [
                "output",
                [
                    "JUEGO DEL QUINCE",
                    f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                    f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 54 END

    elif exercise_id == 55:
        # Exercise 55 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [1, 1]],
            ["choice", ["piedra", "piedra"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado piedra.",
                    "Juan ha sacado piedra.",
                    "Han empatado.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [1, 2]],
            ["choice", ["piedra", "papel"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado piedra.",
                    "Juan ha sacado papel.",
                    "Ha ganado Juan.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [1, 3]],
            ["choice", ["piedra", "tijera"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado piedra.",
                    "Juan ha sacado tijera.",
                    "Ha ganado Inés.",
                ],
            ],
        )

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [2, 1]],
            ["choice", ["papel", "piedra"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado papel.",
                    "Juan ha sacado piedra.",
                    "Ha ganado Inés.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [2, 2]],
            ["choice", ["papel", "papel"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado papel.",
                    "Juan ha sacado papel.",
                    "Han empatado.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [2, 3]],
            ["choice", ["papel", "tijera"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado papel.",
                    "Juan ha sacado tijera.",
                    "Ha ganado Juan.",
                ],
            ],
        )

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [3, 1]],
            ["choice", ["tijera", "piedra"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado tijera.",
                    "Juan ha sacado piedra.",
                    "Ha ganado Juan.",
                ],
            ],
        )
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", [3, 2]],
            ["choice", ["tijera", "papel"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado tijera.",
                    "Juan ha sacado papel.",
                    "Ha ganado Inés.",
                ],
            ],
        )
        mpts_common.add_test(
            LAST_TEST,
            ["random", [3, 3]],
            ["choice", ["tijera", "tijera"]],
            [
                "output",
                [
                    "PIEDRA, PAPEL, ... ¡TIJERA!",
                    "Inés ha sacado tijera.",
                    "Juan ha sacado tijera.",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 55 END