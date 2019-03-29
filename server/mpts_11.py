import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 111:
        # Exercise 111 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        termina = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        # Termina a la primera
        a = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a],
            [
                "LOS 20 (1)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada
        a = ""
        b = random.randrange(1, 7)
        c = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c],
            [
                "LOS 20 (1)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                f"Tirada: {b}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Varias tiradas
        n = random.randrange(2, 10)
        tmp_input = []
        tmp_output = [
            "LOS 20 (1)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        for _ in range(n):
            a = ""
            b = random.randrange(1, 7)
            tmp_input += [a, b]
            tmp_output += [
                f"Tirada: {b}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
            ]
        c = termina[random.randrange(len(termina))]
        tmp_input += [c]
        tmp_output += ["Programa terminado."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 111 END

    elif exercise_id == 112:
        # Exercise 112 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        termina = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        # Termina a la primera
        a = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a],
            [
                "LOS 20 (2)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada
        a = ""
        b = random.randrange(1, 7)
        c = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c],
            [
                "LOS 20 (2)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                f"Tirada: {b} - Suma: {b}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Varias tiradas
        n = random.randrange(2, 10)
        tmp_input = []
        tmp_output = [
            "LOS 20 (2)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        suma = 0
        for _ in range(n):
            a = ""
            b = random.randrange(1, 7)
            suma += b
            tmp_input += [a, b]
            tmp_output += [
                f"Tirada: {b} - Suma: {suma}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
            ]
        c = termina[random.randrange(len(termina))]
        tmp_input += [c]
        tmp_output += ["Programa terminado."]

        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 112 END

    elif exercise_id == 113:
        # Exercise 113 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        termina = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        # Termina a la primera
        a = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a],
            [
                "LOS 20 (3)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "No se ha lanzado ningún dado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, empate
        a = ""
        b = random.randrange(1, 7)
        c = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, b, c],
            [
                "LOS 20 (3)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                f"Jugador 1 - Tirada: {b} - Suma: {b}",
                f"Jugador 2 - Tirada: {b} - Suma: {b}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "¡Empate!",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, gana 1
        a = ""
        b = random.randrange(2, 7)
        c = random.randrange(1, b)
        d = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c, d],
            [
                "LOS 20 (3)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                f"Jugador 1 - Tirada: {b} - Suma: {b}",
                f"Jugador 2 - Tirada: {c} - Suma: {c}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Ha ganado el jugador 1.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, gana 2
        a = ""
        b = random.randrange(1, 6)
        c = random.randrange(b + 1, 7)
        d = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c, d],
            [
                "LOS 20 (3)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                f"Jugador 1 - Tirada: {b} - Suma: {b}",
                f"Jugador 2 - Tirada: {c} - Suma: {c}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "Ha ganado el jugador 2.",
            ],
            NOT_LAST_TEST,
        )

        # Varias tiradas, empate
        n = 2 * random.randrange(1, 5)
        a = ""
        d = termina[random.randrange(len(termina))]
        tmp_input = []
        tmp_output = [
            "LOS 20 (3)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n):
            a = random.randrange(1, 7)
            tmp1 += [a]
        tmp2 = tmp1.copy()
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
            ]
        tmp_input += [d]
        tmp_output += ["¡Empate!"]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varias tiradas, gana 1
        n = 2 * random.randrange(1, 5)
        a = ""
        d = termina[random.randrange(len(termina))]
        tmp_input = []
        tmp_output = [
            "LOS 20 (3)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n - 1):
            a = random.randrange(1, 7)
            tmp1 += [a]
        tmp2 = tmp1.copy()
        e = random.randrange(2, 7)
        tmp1 += [e]
        tmp2 += [random.randrange(1, e)]
        random.shuffle(tmp1)
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
            ]
        tmp_input += [d]
        tmp_output += ["Ha ganado el jugador 1."]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varias tiradas, gana 2
        n = 2 * random.randrange(1, 5)
        a = ""
        d = termina[random.randrange(len(termina))]
        tmp_input = []
        tmp_output = [
            "LOS 20 (3)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n - 1):
            a = random.randrange(1, 7)
            tmp1 += [a]
        tmp2 = tmp1.copy()
        e = random.randrange(1, 6)
        tmp1 += [e]
        tmp2 += [random.randrange(e + 1, 7)]
        random.shuffle(tmp1)
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
                "",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
            ]
        tmp_input += [d]
        tmp_output += ["Ha ganado el jugador 2."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 113 END

    elif exercise_id == 114:
        # Exercise 114 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        termina = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        # Termina a la primera
        a = termina[random.randrange(len(termina))]
        b = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b],
            [
                "LOS 20 (4)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                "",
                "Jugador 1 - Suma: 0",
                "Jugador 2 - Suma: 0",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, empate
        a = ""
        b = ""
        c = random.randrange(1, 7)
        d = c
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c, d, e, f],
            [
                "LOS 20 (4)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {c} - Suma: {c}",
                f"Jugador 2 - Tirada: {d} - Suma: {d}",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                "",
                f"Jugador 1 - Suma: {c}",
                f"Jugador 2 - Suma: {d}",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, gana 1
        a = ""
        b = ""
        c = random.randrange(2, 7)
        d = random.randrange(1, c)
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c, d, e, f],
            [
                "LOS 20 (4)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {c} - Suma: {c}",
                f"Jugador 2 - Tirada: {d} - Suma: {d}",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                "",
                f"Jugador 1 - Suma: {c}",
                f"Jugador 2 - Suma: {d}",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Una tirada, gana 2
        a = ""
        b = ""
        c = random.randrange(1, 6)
        d = random.randrange(c, 7)
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]

        mpts_common.add_test(
            [a, b, c, d, e, f],
            [
                "LOS 20 (4)",
                "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {c} - Suma: {c}",
                f"Jugador 2 - Tirada: {d} - Suma: {d}",
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                "",
                f"Jugador 1 - Suma: {c}",
                f"Jugador 2 - Suma: {d}",
                "Programa terminado.",
            ],
            NOT_LAST_TEST,
        )

        # Varias tiradas, empate
        n = 2 * random.randrange(1, 5)
        tmp_input = []
        tmp_output = [
            "LOS 20 (4)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n):
            c = random.randrange(1, 7)
            tmp1 += [c]
        tmp2 = tmp1.copy()
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", "", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
            ]
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]
        tmp_input += [e, f]
        tmp_output += [
            "",
            "Jugador 1: ",
            "Jugador 2: ",
            "",
            f"Jugador 1 - Suma: {suma1}",
            f"Jugador 2 - Suma: {suma2}",
            "Programa terminado.",
        ]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varias tiradas, gana 1
        n = 2 * random.randrange(1, 5)
        tmp_input = []
        tmp_output = [
            "LOS 20 (4)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n):
            c = random.randrange(1, 7)
            tmp1 += [c]
        tmp2 = tmp1.copy()
        c = random.randrange(2, 7)
        d = random.randrange(1, c)
        tmp1 += [c]
        tmp2 += [d]
        random.shuffle(tmp1)
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", "", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
            ]
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]
        tmp_input += [e, f]
        tmp_output += [
            "",
            "Jugador 1: ",
            "Jugador 2: ",
            "",
            f"Jugador 1 - Suma: {suma1}",
            f"Jugador 2 - Suma: {suma2}",
            "Programa terminado.",
        ]
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varias tiradas, gana 2
        n = 2 * random.randrange(1, 5)
        tmp_input = []
        tmp_output = [
            "LOS 20 (4)",
            "Pulse Intro para lanzar el dado. Pulse otra tecla e Intro para terminar: ",
        ]
        tmp1 = []
        for _ in range(n):
            c = random.randrange(1, 7)
            tmp1 += [c]
        tmp2 = tmp1.copy()
        c = random.randrange(1, 6)
        d = random.randrange(c, 7)
        tmp1 += [c]
        tmp2 += [d]
        random.shuffle(tmp1)
        random.shuffle(tmp2)
        suma1 = suma2 = 0
        for i in range(n):
            tmp_input += ["", "", tmp1[i], tmp2[i]]
            suma1 += tmp1[i]
            suma2 += tmp2[i]
            tmp_output += [
                "",
                "Jugador 1: ",
                "Jugador 2: ",
                f"Jugador 1 - Tirada: {tmp1[i]} - Suma: {suma1}",
                f"Jugador 2 - Tirada: {tmp2[i]} - Suma: {suma2}",
            ]
        e = termina[random.randrange(len(termina))]
        f = termina[random.randrange(len(termina))]
        tmp_input += [e, f]
        tmp_output += [
            "",
            "Jugador 1: ",
            "Jugador 2: ",
            "",
            f"Jugador 1 - Suma: {suma1}",
            f"Jugador 2 - Suma: {suma2}",
            "Programa terminado.",
        ]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 114 END
