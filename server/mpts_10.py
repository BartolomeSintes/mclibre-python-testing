import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 101:
        # Exercise 101 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Mayor a la primera
        a = random.randrange(-10, 11)
        b = a + random.randrange(2, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "NÚMERO MAYOR",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    "",
                    f"Los números que ha escrito son {a} y {b}.",
                ],
            ],
        )

        # Mayor a la segunda
        a = random.randrange(-10, 11)
        b = a + random.randrange(2, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, a, b]],
            [
                "output",
                [
                    "NÚMERO MAYOR",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    f"{a} no es mayor que {a}. Inténtelo de nuevo: ",
                    "",
                    f"Los números que ha escrito son {a} y {b}.",
                ],
            ],
        )

        # n intentos
        a = random.randrange(2, 11)
        n = random.randrange(3, 8)
        tmp_input = [a]
        tmp_output = [
            "NÚMERO MAYOR",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
        ]
        for _ in range(n):
            b = random.randrange(0, 11)
            tmp_input += [a - b]
            tmp_output += [f"{a - b} no es mayor que {a}. Inténtelo de nuevo: "]
        b = random.randrange(1, 11)
        tmp_input += [a + b]
        tmp_output += ["", f"Los números que ha escrito son {a} y {a + b}."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 101 END

    elif exercise_id == 102:
        # Exercise 102 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Menor a la primera
        a = round(random.randrange(-100, 110) / 10.0, 1)
        b = a - round(random.randrange(1, 110) / 10.0, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "NÚMEROS MAYORES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    "",
                    f"{b} no es mayor que {a}.",
                ],
            ],
        )

        # Igual a la primera
        a = round(random.randrange(-100, 110) / 10.0, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, a]],
            [
                "output",
                [
                    "NÚMEROS MAYORES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    "",
                    f"{a} no es mayor que {a}.",
                ],
            ],
        )

        # Menor a la segunda
        a = round(random.randrange(-100, 110) / 10.0, 1)
        b = a + round(random.randrange(1, 110) / 10.0, 1)
        c = a - round(random.randrange(1, 110) / 10.0, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "NÚMEROS MAYORES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    f"Escriba otro número mayor que {a}: ",
                    "",
                    f"{c} no es mayor que {a}.",
                ],
            ],
        )

        # n intentos
        a = round(random.randrange(-100, 110) / 10.0, 1)
        n = random.randrange(3, 8)
        tmp_input = [a]
        tmp_output = [
            "NÚMEROS MAYORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
        ]
        for _ in range(n):
            b = round(random.randrange(0, 101) / 10.0, 1)
            tmp_input += [a + b]
            tmp_output += [f"Escriba otro número mayor que {a}: "]
        b = round(random.randrange(0, 101) / 10.0, 1)
        tmp_input += [a - b]
        tmp_output += ["", f"{a - b} no es mayor que {a}."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 102 END

    elif exercise_id == 103:
        # Exercise 103 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Menor a la primera
        a = random.randrange(-10, 11)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "CADA VEZ MÁS GRANDES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    "",
                    f"{b} no es mayor que {a}.",
                ],
            ],
        )

        # Igual a la primera
        a = random.randrange(-10, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, a]],
            [
                "output",
                [
                    "CADA VEZ MÁS GRANDES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    "",
                    f"{a} no es mayor que {a}.",
                ],
            ],
        )

        # Menor a la segunda
        a = random.randrange(-10, 11)
        b = a + random.randrange(1, 11)
        c = a - random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "CADA VEZ MÁS GRANDES",
                    "Escriba un número: ",
                    f"Escriba un número mayor que {a}: ",
                    f"Escriba un número mayor que {b}: ",
                    "",
                    f"{c} no es mayor que {b}.",
                ],
            ],
        )

        # n intentos
        a = random.randrange(-10, 11)
        n = random.randrange(3, 8)
        tmp_input = [a]
        tmp_output = [
            "CADA VEZ MÁS GRANDES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
        ]
        for _ in range(n):
            b = random.randrange(1, 11)
            a += b
            tmp_input += [a]
            tmp_output += [f"Escriba un número mayor que {a}: "]

        b = random.randrange(0, 11)
        tmp_input += [a - b]
        tmp_output += ["", f"{a - b} no es mayor que {a}."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 103 END

    elif exercise_id == 104:
        # Exercise 104 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Cantidad negativa
        a = -random.randrange(1, 11)
        b = 1
        c = random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "NÚMEROS POSITIVOS",
                    "Escriba la cantidad de números positivos a escribir: ",
                    "La cantidad debe ser mayor que 0. Inténtelo de nuevo: ",
                    "",
                    "Escriba un número: ",
                    "",
                    "Ha escrito 1 número positivo.",
                ],
            ],
        )

        # Cantidad cero
        a = 0
        b = 1
        c = random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "NÚMEROS POSITIVOS",
                    "Escriba la cantidad de números positivos a escribir: ",
                    "La cantidad debe ser mayor que 0. Inténtelo de nuevo: ",
                    "",
                    "Escriba un número: ",
                    "",
                    "Ha escrito 1 número positivo.",
                ],
            ],
        )

        # Varios negativos
        tmp_input = []
        tmp_output = [
            "NÚMEROS POSITIVOS",
            "Escriba la cantidad de números positivos a escribir: ",
        ]
        for _ in range(random.randrange(3, 8)):
            a = -random.randrange(0, 11)
            tmp_input += [a]
            tmp_output += ["La cantidad debe ser mayor que 0. Inténtelo de nuevo: "]
        b = 1
        c = random.randrange(1, 11)
        tmp_input += [b, c]
        tmp_output += ["", "Escriba un número: ", "", "Ha escrito 1 número positivo."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Todos positivos
        a = random.randrange(2, 11)
        b = random.randrange(1, 100)
        tmp_input = [a, b]
        tmp_output = [
            "NÚMEROS POSITIVOS",
            "Escriba la cantidad de números positivos a escribir: ",
            "",
            "Escriba un número: ",
        ]
        for _ in range(a - 1):
            b = random.randrange(1, 100)
            tmp_input += [b]
            tmp_output += ["Escriba otro número: "]
        tmp_output += ["", f"Ha escrito {a} números, {a} de ellos positivos."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # 1 Positivo y negativos
        a = random.randrange(5, 11)
        neg = a - 1
        lista = []
        for _ in range(a):
            lista += [random.randrange(1, 100)]
        for i in range(neg):
            lista[i] = -lista[i]
        tmp_input = [a - neg] + lista

        tmp_output = [
            "NÚMEROS POSITIVOS",
            "Escriba la cantidad de números positivos a escribir: ",
            "",
            "Escriba un número: ",
        ]
        for _ in range(a - 1):
            tmp_output += ["Escriba otro número: "]
        tmp_output += ["", f"Ha escrito {a} números, {a - neg} de ellos positivo."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Positivos y negativos
        a = random.randrange(5, 11)
        neg = random.randrange(1, a - 1)
        lista = []
        for _ in range(a):
            lista += [random.randrange(1, 100)]
        for i in range(neg):
            lista[i] = -lista[i]
        tmp_input = [a - neg] + lista

        tmp_output = [
            "NÚMEROS POSITIVOS",
            "Escriba la cantidad de números positivos a escribir: ",
            "",
            "Escriba un número: ",
        ]
        for _ in range(a - 1):
            tmp_output += ["Escriba otro número: "]
        tmp_output += ["", f"Ha escrito {a} números, {a - neg} de ellos positivos."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 104 END

    elif exercise_id == 105:
        # Exercise 105 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Primero negativo
        a = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "SUMA DE NÚMEROS",
                    "Escriba un número: ",
                    "",
                    "La suma de los números positivos introducidos es 0.",
                ],
            ],
        )

        # Segundo negativo
        a = random.randrange(1, 11)
        b = -random.randrange(1, 11)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "SUMA DE NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "",
                    f"La suma de los números positivos introducidos es {a}.",
                ],
            ],
        )

        # n positivos
        n = random.randrange(3, 8)
        a = random.randrange(1, 100)
        tmp_input = [a]
        total = a
        tmp_output = ["SUMA DE NÚMEROS", "Escriba un número: "]
        for _ in range(n - 1):
            a = random.randrange(1, 100)
            tmp_input += [a]
            total += a
            tmp_output += ["Escriba otro número: "]
        a = -random.randrange(1, 100)
        tmp_input += [a]
        tmp_output += [
            "Escriba otro número: ",
            "",
            f"La suma de los números positivos introducidos es {total}.",
        ]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 105 END

    elif exercise_id == 106:
        # Exercise 106 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Cantidad negativa
        a = -round(random.randrange(1, 101) / 10.0, 1)
        b = round(random.randrange(1, 101) / 10.0, 1)
        c = b + round(random.randrange(1, 101) / 10.0, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "HASTA EL LÍMITE",
                    "Escriba el valor límite: ",
                    "El límite debe ser mayor que 0. Inténtelo de nuevo: ",
                    "",
                    "Escriba un número: ",
                    "",
                    f"Ha superado el límite. La suma de los números introducidos es {c}.",
                ],
            ],
        )

        # Cantidad cero
        a = 0
        b = round(random.randrange(1, 101) / 10.0, 1)
        c = b + round(random.randrange(1, 101) / 10.0, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "HASTA EL LÍMITE",
                    "Escriba el valor límite: ",
                    "El límite debe ser mayor que 0. Inténtelo de nuevo: ",
                    "",
                    "Escriba un número: ",
                    "",
                    f"Ha superado el límite. La suma de los números introducidos es {c}.",
                ],
            ],
        )

        # Varias cantidades negativas
        tmp_input = []
        tmp_output = ["HASTA EL LÍMITE", "Escriba el valor límite: "]
        for _ in range(random.randrange(3, 8)):
            a = -round(random.randrange(1, 101) / 10.0, 1)
            tmp_input += [a]
            tmp_output += ["El límite debe ser mayor que 0. Inténtelo de nuevo: "]
        b = round(random.randrange(1, 101) / 10.0, 1)
        c = b + round(random.randrange(1, 101) / 10.0, 1)
        tmp_input += [b, c]
        tmp_output += [
            "",
            "Escriba un número: ",
            "",
            f"Ha superado el límite. La suma de los números introducidos es {c}.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Varias cantidades negativas
        tmp_input = []
        tmp_output = [
            "HASTA EL LÍMITE",
            "Escriba el valor límite: ",
            "",
            "Escriba un número: ",
        ]

        a = round(random.randrange(1, 101) / 10.0, 1)
        tmp_input = [a]
        total = a
        n = random.randrange(3, 8)
        for _ in range(n):
            a = round(random.randrange(1, 101) / 10.0, 1)
            tmp_input += [a]
            total += a
            tmp_output += ["Escriba otro número: "]
        b = round(random.randrange(1, 101) / 10.0, 1)
        limite = total + b
        a = b + round(random.randrange(1, 101) / 10.0, 1)
        tmp_input += [a]
        total += a
        tmp_output += ["Escriba otro número: "]
        tmp_input = [limite] + tmp_input
        tmp_output += [
            "",
            f"Ha superado el límite. La suma de los números introducidos es {total}.",
        ]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 106 END

    elif exercise_id == 107:
        # Exercise 107 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # Segundo valor igual al primero
        a = random.randrange(1, 21)
        tmp_input = [a]
        tmp_output = [
            "ENTRE DOS VALORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
        ]
        n = random.randrange(2, 6)
        for _ in range(n):
            b = a
            tmp_input += [b]
            tmp_output += [f"{b} no es mayor que {a}. Inténtelo de nuevo: "]
        b = a + random.randrange(1, 21)
        tmp_input += [b]
        tmp_output += ["", f"Escriba un número entre {a} y {b}: "]
        c = a - random.randrange(1, 21)
        tmp_input += [c]
        tmp_output += ["", f"No ha escrito ningún número entre {a} y {b}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Segundo valor inferior al primero
        a = random.randrange(1, 21)
        tmp_input = [a]
        tmp_output = [
            "ENTRE DOS VALORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
        ]
        n = random.randrange(5, 10)
        for _ in range(n):
            b = a - random.randrange(0, 10)
            tmp_input += [b]
            tmp_output += [f"{b} no es mayor que {a}. Inténtelo de nuevo: "]
        b = a + random.randrange(1, 21)
        tmp_input += [b]
        tmp_output += ["", f"Escriba un número entre {a} y {b}: "]
        c = a - random.randrange(1, 21)
        tmp_input += [c]
        tmp_output += ["", f"No ha escrito ningún número entre {a} y {b}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # 1 valor en medio
        a = random.randrange(1, 21)
        b = a + random.randrange(10, 21)
        tmp_input = [a, b]
        tmp_output = [
            "ENTRE DOS VALORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
            "",
            f"Escriba un número entre {a} y {b}: ",
        ]
        c = random.randrange(a + 1, b)
        d = a - random.randrange(1, 21)
        tmp_input += [c, d]
        tmp_output += [f"Escriba otro número entre {a} y {b}: "]
        tmp_output += ["", f"Ha escrito 1 número entre {a} y {b}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # 2 valores en medio (extremos)
        a = random.randrange(1, 21)
        b = a + random.randrange(10, 21)
        tmp_input = [a, b]
        tmp_output = [
            "ENTRE DOS VALORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
            "",
            f"Escriba un número entre {a} y {b}: ",
        ]
        c = a - random.randrange(1, 21)
        tmp_input += [a, b, c]
        tmp_output += [
            f"Escriba otro número entre {a} y {b}: ",
            f"Escriba otro número entre {a} y {b}: ",
        ]
        tmp_output += ["", f"Ha escrito 2 números entre {a} y {b}."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # n valores en medio
        a = random.randrange(1, 21)
        b = a + random.randrange(10, 21)
        tmp_input = [a, b]
        tmp_output = [
            "ENTRE DOS VALORES",
            "Escriba un número: ",
            f"Escriba un número mayor que {a}: ",
            "",
            f"Escriba un número entre {a} y {b}: ",
        ]
        n = random.randrange(3, 7)
        for _ in range(n):
            c = random.randrange(a, b + 1)
            tmp_input += [c]
            tmp_output += [f"Escriba otro número entre {a} y {b}: "]
        d = b + random.randrange(1, 21)
        tmp_input += [d]
        tmp_output += ["", f"Ha escrito {n} números entre {a} y {b}."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 107 END

    elif exercise_id == 108:
        # Exercise 108 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        termina = "abcdefghijklmnñopqrtuvwxyzABCDEFGHIJKLMNÑOPQRTUVWXYZ"

        # Un sólo número par
        a = random.randrange(1, 21) * 2
        b = termina[random.randrange(len(termina))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "CUENTA PARES (1)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Un sólo número par
        a = random.randrange(1, 21) * 2
        b = termina[random.randrange(len(termina))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "CUENTA PARES (1)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Dos números pares, sigue con S
        a = random.randrange(1, 21) * 2
        b = "S"
        c = random.randrange(1, 21) * 2
        d = termina[random.randrange(len(termina))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, d]],
            [
                "output",
                [
                    "CUENTA PARES (1)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 2 números pares.",
                ],
            ],
        )

        # Dos números pares, sigue con s
        a = random.randrange(1, 21) * 2
        b = "s"
        c = random.randrange(1, 21) * 2
        d = termina[random.randrange(len(termina))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, d]],
            [
                "output",
                [
                    "CUENTA PARES (1)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 2 números pares.",
                ],
            ],
        )

        # Varios pares
        n = random.randrange(2, 6)
        tmp_input = []
        tmp_output = ["CUENTA PARES (1)", "Escriba un número par: "]
        for i in range(n):
            a = random.randrange(1, 21) * 2
            tmp_input += [a, "S"]
            tmp_output += [
                "¿Quiere escribir otro número par? (S/N): ",
                "Escriba un número par: ",
            ]
        b = random.randrange(1, 21) * 2
        c = termina[random.randrange(len(termina))]
        tmp_input += [b, c]
        tmp_output += [
            "¿Quiere escribir otro número par? (S/N): ",
            "",
            f"Ha escrito {n+1} números pares.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Número impar
        a = random.randrange(1, 21) * 2 + 1
        b = random.randrange(1, 21) * 2
        c = termina[random.randrange(len(termina))]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "CUENTA PARES (1)",
                    "Escriba un número par: ",
                    f"{a} no es un número par. Inténtelo de nuevo: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Varios impares
        n = random.randrange(2, 6)
        tmp_input = []
        tmp_output = ["CUENTA PARES (1)", "Escriba un número par: "]
        for i in range(n):
            a = random.randrange(1, 21) * 2 + 1
            tmp_input += [a]
            tmp_output += [f"{a} no es un número par. Inténtelo de nuevo: "]
        b = random.randrange(1, 21) * 2
        c = termina[random.randrange(len(termina))]
        tmp_input += [b, c]
        tmp_output += [
            "¿Quiere escribir otro número par? (S/N): ",
            "",
            "Ha escrito 1 número par.",
        ]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 108 END

    elif exercise_id == 109:
        # Exercise 109 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        repite = "abcdefghijklmñopqrtuvwxyzABCDEFGHIJKLMÑOPQRTUVWXYZ"

        # Un sólo número par
        a = random.randrange(1, 21) * 2
        b = "N"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "CUENTA PARES (2)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Un sólo número par
        a = random.randrange(1, 21) * 2
        b = "n"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "CUENTA PARES (2)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Dos números pares, sigue con S
        a = random.randrange(1, 21) * 2
        b = "S"
        c = random.randrange(1, 21) * 2
        d = "N"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, d]],
            [
                "output",
                [
                    "CUENTA PARES (2)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 2 números pares.",
                ],
            ],
        )

        # Dos números pares, sigue con s
        a = random.randrange(1, 21) * 2
        b = "s"
        c = random.randrange(1, 21) * 2
        d = "n"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, d]],
            [
                "output",
                [
                    "CUENTA PARES (2)",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "Escriba un número par: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 2 números pares.",
                ],
            ],
        )

        # Varios pares
        n = random.randrange(2, 6)
        tmp_input = []
        tmp_output = ["CUENTA PARES (2)", "Escriba un número par: "]
        for i in range(n):
            a = random.randrange(1, 21) * 2
            tmp_input += [a, "S"]
            tmp_output += [
                "¿Quiere escribir otro número par? (S/N): ",
                "Escriba un número par: ",
            ]
        b = random.randrange(1, 21) * 2
        c = "N"
        tmp_input += [b, c]
        tmp_output += [
            "¿Quiere escribir otro número par? (S/N): ",
            "",
            f"Ha escrito {n+1} números pares.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Número impar
        a = random.randrange(1, 21) * 2 + 1
        b = random.randrange(1, 21) * 2
        c = "n"
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "CUENTA PARES (2)",
                    "Escriba un número par: ",
                    f"{a} no es un número par. Inténtelo de nuevo: ",
                    "¿Quiere escribir otro número par? (S/N): ",
                    "",
                    "Ha escrito 1 número par.",
                ],
            ],
        )

        # Varios impares
        n = random.randrange(2, 6)
        tmp_input = []
        tmp_output = ["CUENTA PARES (2)", "Escriba un número par: "]
        for i in range(n):
            a = random.randrange(1, 21) * 2 + 1
            tmp_input += [a]
            tmp_output += [f"{a} no es un número par. Inténtelo de nuevo: "]
        b = random.randrange(1, 21) * 2
        c = "N"
        tmp_input += [b, c]
        tmp_output += [
            "¿Quiere escribir otro número par? (S/N): ",
            "",
            "Ha escrito 1 número par.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", tmp_input], ["output", tmp_output]
        )

        # Repite pregunta
        a = random.randrange(1, 21) * 2
        tmp_input = [a]
        tmp_output = [
            "CUENTA PARES (2)",
            "Escriba un número par: ",
            "¿Quiere escribir otro número par? (S/N): ",
        ]
        n = random.randrange(2, 6)
        for i in range(n):
            a = repite[random.randrange(len(repite))]
            tmp_input += [a]
            tmp_output += ["¿Quiere escribir otro número par? (S/N): "]
        b = "N"
        tmp_input += [b]
        tmp_output += ["", "Ha escrito 1 número par."]
        mpts_common.add_test(LAST_TEST, ["input", tmp_input], ["output", tmp_output])

        # Exercise 109 END

    elif exercise_id == 110:
        # Exercise 110 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html

        # 1 y primo
        a = 1
        b = mpts_common.generate_prime(random.randrange(2, 20))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "DESCOMPOSICIÓN EN NÚMEROS PRIMOS",
                    "Escriba un número entero mayor que 1: ",
                    f"{a} no es mayor que 1. Inténtelo de nuevo: ",
                    f"Descomposición en factores primos: {b}",
                ],
            ],
        )

        # 0 y compuesto
        a = 0
        b = mpts_common.generate_prime(random.randrange(2, 10))
        c = mpts_common.generate_prime(random.randrange(11, 20))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b * c]],
            [
                "output",
                [
                    "DESCOMPOSICIÓN EN NÚMEROS PRIMOS",
                    "Escriba un número entero mayor que 1: ",
                    f"{a} no es mayor que 1. Inténtelo de nuevo: ",
                    f"Descomposición en factores primos: {b} {c}",
                ],
            ],
        )

        # primo
        a = mpts_common.generate_prime(random.randrange(20, 30))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "DESCOMPOSICIÓN EN NÚMEROS PRIMOS",
                    "Escriba un número entero mayor que 1: ",
                    f"Descomposición en factores primos: {a}",
                ],
            ],
        )

        # compuesto
        n_1 = random.randrange(1, 5)
        a_1 = mpts_common.generate_prime(random.randrange(2, 4))
        n_2 = random.randrange(1, 5)
        a_2 = mpts_common.generate_prime(random.randrange(4, 6))
        n_3 = random.randrange(1, 5)
        a_3 = mpts_common.generate_prime(random.randrange(6, 8))
        a = a_1 ** n_1 * a_2 ** n_2 * a_3 ** n_3
        desc = ""
        for i in range(n_1):
            desc += f"{a_1} "
        for i in range(n_2):
            desc += f"{a_2} "
        for i in range(n_3 - 1):
            desc += f"{a_3} "
        desc += f"{a_3}"

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "DESCOMPOSICIÓN EN NÚMEROS PRIMOS",
                    "Escriba un número entero mayor que 1: ",
                    f"Descomposición en factores primos: {desc}",
                ],
            ],
        )

        # Exercise 110 END
