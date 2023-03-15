import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 131:
        # Exercise 131 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-sucesiones.html

        # La salida es siempre la misma
        tmp_output = [
            "2 4 6 8 10 12 14 16 18 20 ",
            "20 22 24 26 28 30 32 34 ",
            "10 14 18 22 26 30 ",
            "40 35 30 25 20 15 10 5 0 ",
            "1 2 3 4 5 6 7 8 9 10 "
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["output", tmp_output],
        )

        # Exercise 131 END

    elif exercise_id == 132:
        # Exercise 132 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-sucesiones.html

        # La salida es siempre la misma
        tmp_output = [
            "1 4 9 16 25 36 49 64 81 100 ",
            "2 5 10 17 26 37 50 65 82 101 ",
            "8 27 64 125 216 343 ",
            "1.0 0.5 0.3333333333333333 0.25 0.2 0.16666666666666666 ",
            "2 6 12 20 30 42 56 ",
            "1 10 100 1000 10000 100000 ",
            "1.0 0.1 0.01 0.001 0.0001 ",
            "1 -1 1 -1 1 -1 1 -1 "
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["output", tmp_output],
        )

        # Exercise 132 END
