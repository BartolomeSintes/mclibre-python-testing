import mpts_common
import random
import math

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 93:
        # Exercise 93 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Respuesta correcta
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                ],
            ],
        )

        # Respuesta incorrecta
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b + random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta incorrecta!",
                ],
            ],
        )

        # Respuesta incorrecta
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b - random.randrange(1, 10)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta incorrecta!",
                ],
            ],
        )

        # Exercise 93 END

    elif exercise_id == 94:
        # Exercise 94 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Número preguntas negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (2)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (2)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas 1 - Respuesta correcta
        n = 1
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                ],
            ],
        )

        # Número preguntas 1 - Respuesta incorrecta
        n = 1
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b + random.randrange(1, 21)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta incorrecta!",
                ],
            ],
        )

        # Número preguntas n - Respuestas correctas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (2)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            tmp_random += [a, b]
            tmp_input += [c]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas incorrectas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (2)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b + random.randrange(1, 20)
            tmp_random += [a, b]
            tmp_input += [c]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas correctas e incorrectas
        n = random.randrange(5, 10)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (2)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b + random.randrange(0, 2)
            tmp_random += [a, b]
            tmp_input += [c]
            if c == a * b:
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
            else:
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]

        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 94 END

    elif exercise_id == 95:
        # Exercise 95 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Número preguntas negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (3)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (3)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas 1 - Respuesta correcta
        n = 1
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                    "",
                    "Ha contestado correctamente 1 pregunta.",
                    "Le corresponde una nota de 10.0.",
                    "¡Enhorabuena!",
                ],
            ],
        )

        # Número preguntas 1 - Respuesta incorrecta
        n = 1
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b + random.randrange(1, 21)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "TABLAS DE MULTIPLICAR (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta incorrecta!",
                    "",
                    "Ha contestado correctamente 0 preguntas.",
                    "Le corresponde una nota de 0.0.",
                ],
            ],
        )

        # Número preguntas n - Respuestas correctas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (3)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            tmp_input += [c]
            tmp_random += [a, b]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        tmp_output += [
            "",
            f"Ha contestado correctamente {n} preguntas.",
            "Le corresponde una nota de 10.0.",
            "¡Enhorabuena!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas incorrectas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (3)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b + random.randrange(1, 20)
            tmp_input += [c]
            tmp_random += [a, b]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]
        tmp_output += [
            "",
            "Ha contestado correctamente 0 preguntas.",
            "Le corresponde una nota de 0.0.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas correctas e incorrectas, nota < 9
        n = random.randrange(5, 10)
        nok = random.randrange(1, n)
        nota = round((n - nok) / n * 10, 1)
        lista = random.sample(range(n), k=nok)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (3)", "Número de preguntas: "]
        for i in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            if i in lista:
                tmp_input += [c + random.randrange(1, 21)]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]
            else:
                tmp_input += [c]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        tmp_output += [
            "",
            f"Ha contestado correctamente {n - nok} preguntas.",
            f"Le corresponde una nota de {nota}.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas correctas e incorrectas, nota 9
        n = 10
        nok = 1
        nota = 9.0
        lista = random.sample(range(n), k=nok)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (3)", "Número de preguntas: "]
        for i in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            if i in lista:
                tmp_input += [c + random.randrange(1, 21)]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]
            else:
                tmp_input += [c]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        tmp_output += [
            "",
            f"Ha contestado correctamente {n - nok} preguntas.",
            f"Le corresponde una nota de {nota}.",
            "¡Enhorabuena!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Número preguntas n - Respuestas correctas e incorrectas, nota mayor que 9
        n = random.randrange(11, 21)
        nok = 1
        nota = round((n - nok) / n * 10, 1)
        lista = random.sample(range(n), k=nok)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["TABLAS DE MULTIPLICAR (3)", "Número de preguntas: "]
        for i in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            if i in lista:
                tmp_input += [c + random.randrange(1, 21)]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta incorrecta!"]
            else:
                tmp_input += [c]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        tmp_output += [
            "",
            f"Ha contestado correctamente {n - nok} preguntas.",
            f"Le corresponde una nota de {nota}.",
            "¡Enhorabuena!",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )
        # Exercise 95 END

    elif exercise_id == 96:
        # Exercise 96 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Respuesta correcta
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                ],
            ],
        )

        # Respuesta incorrecta < 10% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(1, round(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Respuesta incorrecta < 10% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(1, round(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Respuesta incorrecta < 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(round(c / 10), round(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Respuesta incorrecta < 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(round(c / 10), round(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Respuesta incorrecta > 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(round(c / 10 * 3), c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Respuesta incorrecta > 30% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(round(c / 10 * 3), c)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (1)",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # Exercise 96 END

    elif exercise_id == 97:
        # Exercise 97 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Número preguntas negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # 1 pregunta - Respuesta correcta
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 10% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(1, math.ceil(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 10% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(1, math.ceil(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 30% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta > 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(math.ceil(c / 10 * 3), c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta > 30% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        d = random.randrange(round(c / 10 * 3), c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (2)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ],
            ],
        )

        # n preguntas - Respuestas correctas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["CÁLCULO ESTIMADO (2)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(11, 100)
            b = random.randrange(11, 100)
            c = a * b
            tmp_input += [c]
            tmp_random += [a, b]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # n preguntas - 1 de cada
        n = 7
        lista = random.sample(range(7), k=7)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["CÁLCULO ESTIMADO (2)", "Número de preguntas: "]
        a = random.randrange(11, 100)
        b = random.randrange(11, 100)
        c = a * b
        for i in lista:
            if i == 0:
                tmp_input += [c]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
            elif i == 1:
                d = random.randrange(1, math.ceil(c / 10))
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ]
            elif i == 2:
                d = random.randrange(1, math.ceil(c / 10))
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ]
            elif i == 3:
                d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 4:
                d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 5:
                d = random.randrange(math.ceil(c / 10 * 3), c)
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 6:
                d = random.randrange(math.ceil(c / 10 * 3), c)
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 97 END

    elif exercise_id == 98:
        # Exercise 98 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html

        # Número preguntas negativo
        n = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # Número preguntas cero
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [n]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "El número de preguntas debe ser al menos 1.",
                ],
            ],
        )

        # 1 pregunta - Respuesta correcta
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    "¡Respuesta correcta!",
                    "",
                    "Le corresponde una nota de 10.0.",
                    "¡Enhorabuena!",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 10% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(1, math.ceil(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 6.7.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 10% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(1, math.ceil(c / 10))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 6.7.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 3.3.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta < 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 3.3.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta > 30% por arriba
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(math.ceil(c / 10 * 3), c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c + d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 0.0.",
                ],
            ],
        )

        # 1 pregunta - Respuesta incorrecta > 30% por abajo
        a = random.randrange(11, 100)
        b = random.randrange(11, 110)
        c = a * b
        d = random.randrange(math.ceil(c / 10 * 3), c)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, c - d]],
            ["random", [a, b]],
            [
                "output",
                [
                    "CÁLCULO ESTIMADO (3)",
                    "Número de preguntas: ",
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                    "",
                    "Le corresponde una nota de 0.0.",
                ],
            ],
        )

        # n preguntas - Respuestas correctas
        n = random.randrange(3, 8)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["CÁLCULO ESTIMADO (3)", "Número de preguntas: "]
        for _ in range(n):
            a = random.randrange(2, 11)
            b = random.randrange(2, 11)
            c = a * b
            tmp_input += [c]
            tmp_random += [a, b]
            tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
        tmp_output += ["", "Le corresponde una nota de 10.0.", "¡Enhorabuena!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # n preguntas - 1 de cada
        n = 7
        lista = random.sample(range(7), k=7)
        tmp_input = [n]
        tmp_random = []
        tmp_output = ["CÁLCULO ESTIMADO (3)", "Número de preguntas: "]
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
        c = a * b
        for i in lista:
            if i == 0:
                tmp_input += [c]
                tmp_random += [a, b]
                tmp_output += ["", f"¿Cuánto es {a} x {b}? ", "¡Respuesta correcta!"]
            elif i == 1:
                d = random.randrange(1, math.ceil(c / 10))
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ]
            elif i == 2:
                d = random.randrange(1, math.ceil(c / 10))
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 10%! La respuesta correcta era {c}.",
                ]
            elif i == 3:
                d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 4:
                d = random.randrange(math.ceil(c / 10), math.ceil(c / 10 * 3))
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por menos del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 5:
                d = random.randrange(math.ceil(c / 10 * 3), c)
                tmp_input += [c + d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ]
            elif i == 6:
                d = random.randrange(math.ceil(c / 10 * 3), c)
                tmp_input += [c - d]
                tmp_random += [a, b]
                tmp_output += [
                    "",
                    f"¿Cuánto es {a} x {b}? ",
                    f"¡Ha fallado por más del 30%! La respuesta correcta era {c}.",
                ]
        tmp_output += ["", "Le corresponde una nota de 4.3."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 98 END

