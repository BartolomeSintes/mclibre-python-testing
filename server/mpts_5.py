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
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # gana Alberto
        a = random.randrange(2, 7)
        b = a - random.randrange(1, a)
        mpts_common.add_test(
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Ha ganado Alberto.",
            ],
            NOT_LAST_TEST,
        )

        # gana Bárbara
        a = random.randrange(1, 6)
        b = random.randrange(a + 1, 7)
        mpts_common.add_test(
            [a, b],
            [
                "JUEGO DE DADOS (1)",
                f"Alberto ha sacado un {a}.",
                f"Bárbara ha sacado un {b}.",
                "Ha ganado Bárbara.",
            ],
            LAST_TEST,
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
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Ha ganado David.",
            ],
            NOT_LAST_TEST,
        )

        # Los mayores coinciden, gana un jugador
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(2, a_1)
        b_2 = random.randrange(1, a_2)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Carmen.",
            ],
            NOT_LAST_TEST,
        )

        # Los mayores coinciden, gana el otro
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(1, a_1 - 1)
        b_2 = random.randrange(a_2 + 1, a_1)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Ha ganado David.",
            ],
            NOT_LAST_TEST,
        )

        # Empate
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_1
        b_2 = a_2
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # Empate, cruzado
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_2
        b_2 = a_1
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # Los dos dados son mayores
        a_1 = random.randrange(2, 6)
        a_2 = random.randrange(2, 6)
        b_1 = random.randrange(1, a_2)
        b_2 = random.randrange(1, a_1)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Carmen.",
            ],
            NOT_LAST_TEST,
        )

        # Los dos dados son mayores, cruzados
        b_1 = random.randrange(2, 6)
        b_2 = random.randrange(2, 6)
        a_1 = random.randrange(1, b_1)
        a_2 = random.randrange(1, b_2)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (2)",
                f"Carmen ha sacado un {a_1} y un {a_2}.",
                f"David ha sacado un {b_1} y un {b_2}.",
                "Ha ganado David.",
            ],
            LAST_TEST,
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
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Elena.",
            ],
            NOT_LAST_TEST,
        )

        # Los mayores coinciden, gana un jugador
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(2, a_1)
        b_2 = random.randrange(1, a_2)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Elena.",
            ],
            NOT_LAST_TEST,
        )

        # Los mayores coinciden, gana el otro
        a_1 = random.randrange(3, 6)
        b_1 = a_1
        a_2 = random.randrange(1, a_1 - 1)
        b_2 = random.randrange(a_2 + 1, a_1)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Fernando.",
            ],
            NOT_LAST_TEST,
        )

        # Empate
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_1
        b_2 = a_2
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # Empate, cruzado
        a_1 = random.randrange(1, 7)
        a_2 = random.randrange(1, 7)
        b_1 = a_2
        b_2 = a_1
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )

        # Los dos dados son mayores
        a_1 = random.randrange(2, 6)
        a_2 = random.randrange(2, 6)
        b_1 = random.randrange(1, a_2)
        b_2 = random.randrange(1, a_1)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Elena.",
            ],
            NOT_LAST_TEST,
        )

        # Los dos dados son mayores, cruzados
        b_1 = random.randrange(2, 6)
        b_2 = random.randrange(2, 6)
        a_1 = random.randrange(1, b_1)
        a_2 = random.randrange(1, b_2)
        mpts_common.add_test(
            [a_1, a_2, b_1, b_2],
            [
                "JUEGO DE DADOS (3)",
                f"Elena ha sacado un {a_1} y un {a_2}.",
                f"Fernando ha sacado un {b_1} y un {b_2}.",
                "Ha ganado Fernando.",
            ],
            LAST_TEST,
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
            [a_1, a_2, a_3, b_1, b_2, b_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                "No ha ganado nadie.",
            ],
            NOT_LAST_TEST,
        )

        # El primero se pasa y el segundo no
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(max(1, 5 - a_1 + 1), 11)
        a_3 = random.randrange(max(1, 15 - a_1 - a_2 + 1), 11)
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(1, min(11, 15 - b_1))
        b_3 = random.randrange(1, min(11, 15 - b_1 - b_2 + 1))
        mpts_common.add_test(
            [a_1, a_2, a_3, b_1, b_2, b_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                "Ha ganado Héctor.",
            ],
            NOT_LAST_TEST,
        )

        # El segundo se pasa y el primero no
        a_1 = random.randrange(1, 11)
        a_2 = random.randrange(1, min(11, 15 - a_1))
        a_3 = random.randrange(1, min(11, 15 - a_1 - a_2 + 1))
        b_1 = random.randrange(1, 11)
        b_2 = random.randrange(max(1, 5 - b_1 + 1), 11)
        b_3 = random.randrange(max(1, 15 - b_1 - b_2 + 1), 11)
        mpts_common.add_test(
            [a_1, a_2, a_3, b_1, b_2, b_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                "Ha ganado Gloria.",
            ],
            NOT_LAST_TEST,
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
            [a_1, a_2, a_3, b_1, b_2, b_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                "Ha ganado Gloria.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [b_1, b_2, b_3, a_1, a_2, a_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {b_1}, un {b_2} y un {b_3}.",
                f"Héctor ha sacado un {a_1}, un {a_2} y un {a_3}.",
                "Ha ganado Héctor.",
            ],
            NOT_LAST_TEST,
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
            [a_1, a_2, a_3, b_1, b_2, b_3],
            [
                "JUEGO DEL QUINCE",
                f"Gloria ha sacado un {a_1}, un {a_2} y un {a_3}.",
                f"Héctor ha sacado un {b_1}, un {b_2} y un {b_3}.",
                "Han empatado.",
            ],
            LAST_TEST,
        )

        # Exercise 54 END

    elif exercise_id == 55:
        # Exercise 55 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html

        mpts_common.add_test(
            [1, 1],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado piedra.",
                "Juan ha sacado piedra.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [1, 2],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado piedra.",
                "Juan ha sacado papel.",
                "Ha ganado Juan.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [1, 3],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado piedra.",
                "Juan ha sacado tijera.",
                "Ha ganado Inés.",
            ],
            NOT_LAST_TEST,
        )

        mpts_common.add_test(
            [2, 1],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado papel.",
                "Juan ha sacado piedra.",
                "Ha ganado Inés.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [2, 2],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado papel.",
                "Juan ha sacado papel.",
                "Han empatado.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [2, 3],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado papel.",
                "Juan ha sacado tijera.",
                "Ha ganado Juan.",
            ],
            NOT_LAST_TEST,
        )

        mpts_common.add_test(
            [3, 1],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado tijera.",
                "Juan ha sacado piedra.",
                "Ha ganado Juan.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [3, 2],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado tijera.",
                "Juan ha sacado papel.",
                "Ha ganado Inés.",
            ],
            NOT_LAST_TEST,
        )
        mpts_common.add_test(
            [3, 3],
            [
                "PIEDRA, PAPEL, ... ¡TIJERA!",
                "Inés ha sacado tijera.",
                "Juan ha sacado tijera.",
                "Han empatado.",
            ],
            LAST_TEST,
        )

        # Exercise 54 END
