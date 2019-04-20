import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 120:
        # Exercise 120 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Todas correctas
        tmp_input = []
        tmp_random = []
        tmp_output = [
            "OPERACIONES (1)",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        for _ in range(5):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp_random += [a, b]
            tmp_input += [a + b]
            tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += ["Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Algunas incorrectas
        tmp_input = []
        tmp_random = []
        tmp_output = [
            "OPERACIONES (1)",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        tmp = []
        for _ in range(4):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [[[a + b], [a, b], [f"{a} + {b} = ", "¡Respuesta correcta!", ""]]]
        for _ in range(random.randrange(1, 10)):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a + b + random.randrange(1, 11)],
                    [a, b],
                    [f"{a} + {b} = ", "¡Respuesta incorrecta!", ""],
                ]
            ]
        random.shuffle(tmp)
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp += [[[a + b], [a, b], [f"{a} + {b} = ", "¡Respuesta correcta!", ""]]]
        for i in range(len(tmp)):
            tmp_input += tmp[i][0]
            tmp_random += tmp[i][1]
            tmp_output += tmp[i][2]

        tmp_output += ["Programa terminado."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 120 END

    elif exercise_id == 121:
        # Exercise 121 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Valor negativo
        tmp_input = [0, 1]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "El número de operaciones debe ser mayor que cero.",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_input += [a + b]
        tmp_random += [a, b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += ["Ha acertado 1 operación en 1 intento.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varios valores negativos
        tmp_input = []
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
        ]
        for _ in range(random.randrange(2, 10)):
            tmp_input += [-random.randrange(0, 10)]
            tmp_output += [
                "El número de operaciones debe ser mayor que cero.",
                "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            ]
        tmp_input += [1]
        tmp_output += ["", "Escriba el resultado de las siguientes operaciones:"]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_input += [a + b]
        tmp_random += [a, b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += ["Ha acertado 1 operación en 1 intento.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Una correcta
        tmp_input = [1]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_input += [a + b]
        tmp_random += [a, b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += [f"Ha acertado 1 operación en 1 intento.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Todas correctas
        n = random.randrange(2, 10)
        tmp_input = [n]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        for _ in range(n):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp_input += [a + b]
            tmp_random += [a, b]
            tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += [
            f"Ha acertado {n} operaciones en {n} intentos.",
            "Programa terminado.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Una correcta, varios fallos
        tmp_input = [1]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        tmp = []
        m = random.randrange(2, 10)
        for _ in range(m):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a + b + random.randrange(1, 11)],
                    [a, b],
                    [f"{a} + {b} = ", "¡Respuesta incorrecta!", ""],
                ]
            ]
        for i in range(len(tmp)):
            tmp_input += tmp[i][0]
            tmp_random += tmp[i][1]
            tmp_output += tmp[i][2]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_input += [a + b]
        tmp_random += [a, b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += [
            f"Ha acertado 1 operación en {m + 1} intentos.",
            "Programa terminado.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Varias correctas, varios fallos
        n = random.randrange(2, 10)
        tmp_input = [n]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (2)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        tmp = []
        for _ in range(n - 1):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [[[a + b], [a, b], [f"{a} + {b} = ", "¡Respuesta correcta!", ""]]]
        m = random.randrange(2, 10)
        for _ in range(m):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a + b + random.randrange(1, 11)],
                    [a, b],
                    [f"{a} + {b} = ", "¡Respuesta incorrecta!", ""],
                ]
            ]
        random.shuffle(tmp)
        for i in range(len(tmp)):
            tmp_input += tmp[i][0]
            tmp_random += tmp[i][1]
            tmp_output += tmp[i][2]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_input += [a + b]
        tmp_random += [a, b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        tmp_output += [
            f"Ha acertado {n} operaciones en {m + n} intentos.",
            "Programa terminado.",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["output", tmp_output],
        )

        # Exercise 121 END

    elif exercise_id == 122:
        # Exercise 122 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Valor negativo
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_input = [0, 1]
        tmp_time = [t1]
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "El número de operaciones debe ser mayor que cero.",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_random = [a, b]
        tmp_input += [a + b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [
            f"Ha tardado {round(t2-t1, 1)} segundos en acertar 1 operación en 1 intento.",
            "Programa terminado.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Varios valores negativos
        tmp_input = []
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
        ]
        for _ in range(random.randrange(2, 10)):
            tmp_input += [-random.randrange(0, 10)]
            tmp_output += [
                "El número de operaciones debe ser mayor que cero.",
                "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
            ]
        tmp_input += [1]
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_time = [t1]
        tmp_output += ["", "Escriba el resultado de las siguientes operaciones:"]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_random = [a, b]
        tmp_input += [a + b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [  f"Ha tardado {round(t2-t1, 1)} segundos en acertar 1 operación en 1 intento.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Una correcta
        tmp_input = [1]
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
          "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_time = [t1]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_random = [a, b]
        tmp_input += [a + b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [f"Ha tardado {round(t2-t1, 1)} segundos en acertar 1 operación en 1 intento.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Todas correctas
        n = random.randrange(2, 10)
        tmp_input = [n]
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
          "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_time = [t1]
        tmp_random = []
        for _ in range(n):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp_random += [a, b]
            tmp_input += [a + b]
            tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [f"Ha tardado {round(t2-t1, 1)} segundos en acertar {n} operaciones en {n} intentos.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Una correcta, varios fallos
        tmp_input = [1]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
          "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_time = [t1]
        tmp = []
        m = random.randrange(2, 10)
        for _ in range(m):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a, b],
                    [a + b + random.randrange(1, 11)],
                    [f"{a} + {b} = ", "¡Respuesta incorrecta!", ""],
                ]
            ]
        for i in range(len(tmp)):
            tmp_random += tmp[i][0]
            tmp_input += tmp[i][1]
            tmp_output += tmp[i][2]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_random += [a, b]
        tmp_input += [a + b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [f"Ha tardado {round(t2-t1, 1)} segundos en acertar 1 operación en {m + 1} intentos.", "Programa terminado."]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Varias correctas, varios fallos
        n = random.randrange(2, 10)
        tmp_input = [n]
        tmp_random = []
        tmp_output = [
            "OPERACIONES (3)",
            "¿Cuántas operaciones correctas debe contestar para terminar el programa? ",
          "",
            "Escriba el resultado de las siguientes operaciones:",
        ]
        t1 = round(random.randrange(10, 100) / 10.0, 1)
        tmp_time = [t1]
        tmp = []
        for _ in range(n - 1):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a, b],
                    [a + b],
                    [f"{a} + {b} = ", "¡Respuesta correcta!", ""],
                ]
            ]
        m = random.randrange(2, 10)
        for _ in range(m):
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            tmp += [
                [
                    [a, b],
                    [a + b + random.randrange(1, 11)],
                    [f"{a} + {b} = ", "¡Respuesta incorrecta!", ""],
                ]
            ]
        random.shuffle(tmp)
        for i in range(len(tmp)):
            tmp_random += tmp[i][0]
            tmp_input += tmp[i][1]
            tmp_output += tmp[i][2]
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        tmp_random += [a, b]
        tmp_input += [a + b]
        tmp_output += [f"{a} + {b} = ", "¡Respuesta correcta!", ""]

        t2 = t1 + round(random.randrange(10, 100) / 10.0, 1)
        tmp_time += [t2]
        tmp_output += [f"Ha tardado {round(t2-t1, 1)} segundos en acertar {n} operaciones en {m + n} intentos.", "Programa terminado."]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["random", tmp_random],
            ["time", tmp_time],
            ["output", tmp_output],
        )

        # Exercise 122 END
