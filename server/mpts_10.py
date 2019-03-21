import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 101:
        # Exercise 101 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Mayor a la primera
        a = random.randrange(-10, 11)
        b = a + random.randrange(2, 11)
        mpts_common.add_test(
            [a, b],
            [
                "NÚMERO MAYOR",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"Los números que ha escrito son {a} y {b}.",
            ],
            NOT_LAST_TEST,
        )

        # Mayor a la segunda
        a = random.randrange(-10, 11)
        b = a + random.randrange(2, 11)
        mpts_common.add_test(
            [a, a, b],
            [
                "NÚMERO MAYOR",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                f"{a} no es mayor que {a}. Inténtelo de nuevo: ",
                "",
                f"Los números que ha escrito son {a} y {b}.",
            ],
            NOT_LAST_TEST,
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
        b = random.randrange(0, 11)
        tmp_input += [a + b]
        tmp_output += ["", f"Los números que ha escrito son {a} y {a + b}."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 101 END

    if exercise_id == 102:
        # Exercise 102 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Menor a la primera
        a = round(random.randrange(-100, 110) / 10.0, 1)
        b = a - round(random.randrange(1, 110) / 10.0, 1)
        mpts_common.add_test(
            [a, b],
            [
                "NÚMEROS MAYORES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"{b} no es mayor que {a}.",
            ],
            NOT_LAST_TEST,
        )

        # Igual a la primera
        a = round(random.randrange(-100, 110) / 10.0, 1)
        mpts_common.add_test(
            [a, a],
            [
                "NÚMEROS MAYORES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"{a} no es mayor que {a}.",
            ],
            NOT_LAST_TEST,
        )

        # Menor a la segunda
        a = round(random.randrange(-100, 110) / 10.0, 1)
        b = a + round(random.randrange(1, 110) / 10.0, 1)
        c = a - round(random.randrange(1, 110) / 10.0, 1)
        mpts_common.add_test(
            [a, b, c],
            [
                "NÚMEROS MAYORES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"{c} no es mayor que {a}.",
            ],
            NOT_LAST_TEST,
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
            tmp_output += [f"Escriba un número mayor que {a}: "]
        b = round(random.randrange(0, 101) / 10.0, 1)
        tmp_input += [a - b]
        tmp_output += ["", f"{a - b} no es mayor que {a}."]
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 102 END

    if exercise_id == 103:
        # Exercise 103 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Menor a la primera
        a = random.randrange(-10, 11)
        b = a - random.randrange(1, 11)
        mpts_common.add_test(
            [a, b],
            [
                "CADA VEZ MÁS GRANDES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"{b} no es mayor que {a}.",
            ],
            NOT_LAST_TEST,
        )

        # Igual a la primera
        a = random.randrange(-10, 11)
        mpts_common.add_test(
            [a, a],
            [
                "CADA VEZ MÁS GRANDES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                "",
                f"{a} no es mayor que {a}.",
            ],
            NOT_LAST_TEST,
        )

        # Menor a la segunda
        a = random.randrange(-10, 11)
        b = a + random.randrange(1, 11)
        c = a - random.randrange(1, 11)
        mpts_common.add_test(
            [a, b, c],
            [
                "CADA VEZ MÁS GRANDES",
                "Escriba un número: ",
                f"Escriba un número mayor que {a}: ",
                f"Escriba un número mayor que {b}: ",
                "",
                f"{c} no es mayor que {b}.",
            ],
            NOT_LAST_TEST,
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
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 103 END

    if exercise_id == 104:
        # Exercise 104 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Cantidad negativa
        a = -random.randrange(1, 11)
        b = 1
        c = random.randrange(1, 11)
        mpts_common.add_test(
            [a, b, c],
            [
                "NÚMEROS POSITIVOS",
                "Escriba la cantidad de números positivos a escribir: ",
                "La cantidad debe ser mayor que 0. Inténtelo de nuevo: ",
                "",
                "Escriba un número: ",
                "",
                "Ha escrito 1 número positivo.",
            ],
            NOT_LAST_TEST,
        )

        # Cantidad cero
        a = 0
        b = 1
        c = random.randrange(1, 11)
        mpts_common.add_test(
            [a, b, c],
            [
                "NÚMEROS POSITIVOS",
                "Escriba la cantidad de números positivos a escribir: ",
                "La cantidad debe ser mayor que 0. Inténtelo de nuevo: ",
                "",
                "Escriba un número: ",
                "",
                "Ha escrito 1 número positivo.",
            ],
            NOT_LAST_TEST,
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
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

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
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

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
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

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
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 104 END

    if exercise_id == 105:
        # Exercise 105 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Primero negativo
        a = -random.randrange(1, 11)
        mpts_common.add_test(
            [a],
            [
                "SUMA DE NÚMEROS",
                "Escriba un número: ",
                "",
                "La suma de los números positivos introducidos es 0.",
            ],
            NOT_LAST_TEST,
        )

        # Segundo negativo
        a = random.randrange(1, 11)
        b = -random.randrange(1, 11)
        mpts_common.add_test(
            [a, b],
            [
                "SUMA DE NÚMEROS",
                "Escriba un número: ",
                "Escriba otro número: ",
                "",
                f"La suma de los números positivos introducidos es {a}.",
            ],
            NOT_LAST_TEST,
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
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 105 END

    if exercise_id == 106:
        # Exercise 106 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # Cantidad negativa
        a = -round(random.randrange(1, 101) / 10.0, 1)
        b = round(random.randrange(1, 101) / 10.0, 1)
        c = b + round(random.randrange(1, 101) / 10.0, 1)
        mpts_common.add_test(
            [a, b, c],
            [
                "HASTA EL LÍMITE",
                "Escriba el valor límite: ",
                "El límite debe ser mayor que 0. Inténtelo de nuevo: ",
                "",
                "Escriba un número: ",
                "",
                f"Ha superado el límite. La suma de los números introducidos es {c}.",
            ],
            NOT_LAST_TEST,
        )

        # Cantidad cero
        a = 0
        b = round(random.randrange(1, 101) / 10.0, 1)
        c = b + round(random.randrange(1, 101) / 10.0, 1)
        mpts_common.add_test(
            [a, b, c],
            [
                "HASTA EL LÍMITE",
                "Escriba el valor límite: ",
                "El límite debe ser mayor que 0. Inténtelo de nuevo: ",
                "",
                "Escriba un número: ",
                "",
                f"Ha superado el límite. La suma de los números introducidos es {c}.",
            ],
            NOT_LAST_TEST,
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
        mpts_common.add_test(tmp_input, tmp_output, NOT_LAST_TEST)

        # Varias cantidades negativas
        tmp_input = []
        tmp_output = ["HASTA EL LÍMITE", "Escriba el valor límite: ", "", "Escriba un número: "]

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
        mpts_common.add_test(tmp_input, tmp_output, LAST_TEST)

        # Exercise 106 END
