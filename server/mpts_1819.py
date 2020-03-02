import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 181_911:
        # Exercise 181911 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    "Ha indicado una cantidad negativa.",
                ],
            ],
        )

        # Cantidad no múltiplo de cien
        a = 100 * random.randrange(0, 100) + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    "No ha indicado una cantidad múltiplo de cien.",
                ],
            ],
        )

        # Sólo billetes de 100
        b500 = 0
        b200 = 0
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Sólo billetes de 200
        b500 = 0
        b200 = random.randrange(1, 3)
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Sólo billetes de 500
        b500 = random.randrange(1, 50)
        b200 = 0
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Billetes de 100 y 200
        b500 = 0
        b200 = 1
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Billetes de 100 y 500
        b500 = random.randrange(1, 50)
        b200 = 0
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Billetes de 200 y 500
        b500 = random.randrange(1, 50)
        b200 = random.randrange(1, 3)
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Billetes de 100, 200 y 500
        b500 = random.randrange(1, 50)
        b200 = 1
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "CONTANDO BILLETES",
                    "Escriba una cantidad de dinero (múltiplo de 100): ",
                    f"Puede pagar {a} con:",
                    f"* {b500} billete(s) de 500 €",
                    f"* {b200} billete(s) de 200 €",
                    f"* {b100} billete(s) de 100 €",
                ],
            ],
        )

        # Exercise 181911 END

    elif exercise_id == 181_912:
        # Exercise 181912 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "Ha indicado una cantidad negativa.",
                ],
            ],
        )

        # Billetes 200 negativos
        a = random.randrange(1, 10000)
        b200 = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b200]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "¿Cuántos billetes de 200 € entrega? ",
                    "Ha indicado una cantidad negativa.",
                ],
            ],
        )

        # Billetes 100 negativos
        a = random.randrange(1, 10000)
        b200 = random.randrange(1, 10)
        b100 = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b200, b100]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "¿Cuántos billetes de 200 € entrega? ",
                    "¿Cuántos billetes de 100 € entrega? ",
                    "Ha indicado una cantidad negativa.",
                ],
            ],
        )

        # Cantidad exacta
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        a = 200 * b200 + 100 * b100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b200, b100]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "¿Cuántos billetes de 200 € entrega? ",
                    "¿Cuántos billetes de 100 € entrega? ",
                    "Ha entregado la cantidad exacta.",
                ],
            ],
        )

        # Falta dinero
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        b = random.randrange(1, 500)
        a = 200 * b200 + 100 * b100 + b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b200, b100]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "¿Cuántos billetes de 200 € entrega? ",
                    "¿Cuántos billetes de 100 € entrega? ",
                    f"Le falta entregar {b} €.",
                ],
            ],
        )

        # Sobra dinero
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        b = random.randrange(1, 200 * b200 + 100 * b100)
        a = 200 * b200 + 100 * b100 - b
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b200, b100]],
            [
                "output",
                [
                    "SU CAMBIO",
                    "¿Cuánto tiene que pagar? ",
                    "¿Cuántos billetes de 200 € entrega? ",
                    "¿Cuántos billetes de 100 € entrega? ",
                    f"Su cambio es de {b} €.",
                ],
            ],
        )

        # Exercise 181912 END

    elif exercise_id == 181_913:
        # Exercise 181913 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # lado1: cantidad negativa
        a = -random.randrange(2, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado1: 0
        a = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado2: cantidad negativa
        a = random.randrange(2, 100)
        b = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado2: 0
        a = random.randrange(2, 100)
        b = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado2: mayor que lado1
        a = random.randrange(2, 100)
        b = a + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "¡Le he pedido que escribiera primero el lado más largo!",
                ],
            ],
        )

        # lado3: cantidad negativa
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = -random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado3: 0
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    "¡El valor debe ser positivo!",
                ],
            ],
        )

        # lado3: mayor que lado1
        a = random.randrange(2, 100)
        b = random.randrange(1, a + 1)
        c = a + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    "¡Le he pedido que escribiera primero el lado más largo!",
                ],
            ],
        )

        # lado3: triángulo posible
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = random.randrange(a - b + 1, a + 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    f"Un triángulo puede tener como lados {a}, {b} y {c}.",
                ],
            ],
        )

        # lado3: triángulo imposible
        a = random.randrange(3, 100)
        b = random.randrange(1, a - 1)
        c = random.randrange(1, a - b)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    f"Un triángulo no puede tener como lados {a}, {b} y {c}.",
                ],
            ],
        )

        # lado3: triángulo degenerado
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = a - b
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ANALIZADOR DE TRIÁNGULOS",
                    "Escriba la longitud del lado más largo: ",
                    "Escriba la longitud del segundo lado: ",
                    "Escriba la longitud del tercer lado: ",
                    "Los datos corresponden a un triángulo degenerado.",
                ],
            ],
        )

        # Exercise 181913 END

    elif exercise_id == 181_914:
        # Exercise 181914 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # a y b iguales
        a = random.randrange(-100, 101)
        b = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "¡Ha repetido el número!",
                ],
            ],
        )

        # a y c iguales
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = a
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    "¡Ha repetido algún número!",
                ],
            ],
        )

        # b y c iguales
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = b
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    "¡Ha repetido algún número!",
                ],
            ],
        )

        # orden c - a - b
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = a - random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{a} está entre {b} y {c}.",
                ],
            ],
        )

        # orden b - a - c
        a = random.randrange(-100, 101)
        b = a - random.randrange(1, 100)
        c = a + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{a} está entre {b} y {c}.",
                ],
            ],
        )

        # orden a - b - c
        b = random.randrange(-100, 101)
        c = b + random.randrange(1, 100)
        a = b - random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{b} está entre {a} y {c}.",
                ],
            ],
        )

        # orden c - b - a
        b = random.randrange(-100, 101)
        c = b - random.randrange(1, 100)
        a = b + random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{b} está entre {a} y {c}.",
                ],
            ],
        )

        # orden a - c - b
        c = random.randrange(-100, 101)
        b = c + random.randrange(1, 100)
        a = c - random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{c} está entre {a} y {b}.",
                ],
            ],
        )

        # orden b - c - a
        c = random.randrange(-100, 101)
        b = c - random.randrange(1, 100)
        a = c + random.randrange(1, 100)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "EL NÚMERO DE EN MEDIO",
                    "Escriba un número entero: ",
                    "Escriba otro número entero distinto: ",
                    "Escriba otro número entero distinto a los anteriores: ",
                    f"{c} está entre {a} y {b}.",
                ],
            ],
        )

        # Exercise 181914 END

    if exercise_id == 181921:
        # Exercise 181921 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190521.html

        # Valor negativo
        cm = -random.randrange(100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    "Por favor, escriba un número positivo.",
                ],
            ],
        )

        # Cero cm
        cm = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    "0 cm son 0 millas naúticas, 0 cables y 0.0 brazas.",
                ],
            ],
        )

        # Solo brazas
        cm = random.randrange(1, 18200)
        b = round(cm / 182.91, 1)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son 0 millas naúticas, 0 cables y {b} brazas.",
                ],
            ],
        )

        # Solo cables
        c = random.randrange(1, 11)
        cm = 18291 * c
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son 0 millas naúticas, {c} cables y 0.0 brazas.",
                ],
            ],
        )

        # Solo millas
        m = random.randrange(1, 4) * 8
        cm = round(18291 * 10.125 * m)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son {m} millas naúticas, 0 cables y 0.0 brazas.",
                ],
            ],
        )

        # millas, cables, brazas
        b = random.randrange(1, 1000) / 10
        c = random.randrange(
            1, 10
        )  # solo hasta 9 porque 10 cables y 12.5 brazas es una milla
        m = random.randrange(1, 10)
        cm = round((b + c * 100 + m * 1012.5) * 182.91)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son {m} millas naúticas, {c} cables y {b} brazas.",
                ],
            ],
        )

        # millas, cables, brazas
        b = random.randrange(1, 125) / 10
        c = 10
        m = random.randrange(1, 10)
        cm = round((b + c * 100 + m * 1012.5) * 182.91)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son {m} millas naúticas, {c} cables y {b} brazas.",
                ],
            ],
        )

        # Exercise 181921 END

    elif exercise_id == 181922:
        # Exercise 181922 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190521.html

        # Valor incorrecto < 0
        d = -random.randrange(1, 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [d]],
            [
                "output",
                [
                    "JUEGO DADOS REPETIDOS",
                    "¿Cuántos dados quiere tirar? ",
                    "¡Debe tirar al menos un dado!",
                ],
            ],
        )

        # Sin repeticiones
        d = 6
        dados = [1, 2, 3, 4, 5, 6]
        random.shuffle(dados)
        tmp_output = [
            "JUEGO DADOS REPETIDOS",
            "¿Cuántos dados quiere tirar? ",
        ]
        for i in range(len(dados)):
            tmp_output += [f"Dado {i+1}: {dados[i]}"]
        tmp_output += ["Ha obtenido 6 puntos."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [d]], ["random", dados], ["output", tmp_output],
        )

        # Todos iguales
        d = random.randrange(5, 20)  # Número de dados
        dd = random.randrange(1, 7)  # Valor de todos los dados
        dados = []
        for i in range(d):
            dados += [f"{dd}"]
        tmp_output = [
            "JUEGO DADOS REPETIDOS",
            "¿Cuántos dados quiere tirar? ",
        ]
        for i in range(d):
            tmp_output += [f"Dado {i+1}: {dd}"]
        tmp_output += [f"Ha obtenido {d * dd} puntos."]
        mpts_common.add_test(
            NOT_LAST_TEST, ["input", [d]], ["random", dados], ["output", tmp_output],
        )

        # un sólo dado
        dd = random.randrange(1, 7)  # Valor del dado
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1]],
            ["random", [dd]],
            [
                "output",
                [
                    "JUEGO DADOS REPETIDOS",
                    "¿Cuántos dados quiere tirar? ",
                    f"Dado 1: {dd}",
                    f"Ha obtenido {dd} puntos.",
                ],
            ],
        )

        # Cada vez gana uno de los dados
        for i in range(1, 7):
            dados = [1, 2, 3, 4, 5, 6]
            tirada = []
            ni = random.randrange(8 - i, 15)  # cantidad de dados del ganador
            for j in range(ni):
                tirada += [i]
            dados.remove(i)
            pg = ni * i  # puntuación ganadora
            for j in dados:
                nj = random.randrange(0, pg // j + 1)
                for _ in range(nj):
                    tirada += [j]
            random.shuffle(tirada)
            d = len(tirada)
            tmp_output = [
                "JUEGO DADOS REPETIDOS",
                "¿Cuántos dados quiere tirar? ",
            ]
            for j in range(len(tirada)):
                tmp_output += [f"Dado {j + 1}: {tirada[j]}"]
            tmp_output += [f"Ha obtenido {ni * i} puntos."]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", [d]],
                ["random", tirada],
                ["output", tmp_output],
            )

        # Varios unos, pero máximo es otro con menos dados
        tirada = []
        n1 = random.randrange(7, 15)  # número de unos
        for i in range(n1):
            tirada += [1]
        dw = random.randrange(2, 7)  # número que va a ganar
        nw = n1 // dw + 1
        for i in range(nw):
            tirada += [dw]
        dados = [1, 2, 3, 4, 5, 6]
        dados.remove(1)
        dados.remove(dw)
        for i in dados:
            nl = random.randrange(1, n1 // i + 1)
            for j in range(nl):
                tirada += [i]
        random.shuffle(tirada)
        d = len(tirada)
        tmp_output = [
            "JUEGO DADOS REPETIDOS",
            "¿Cuántos dados quiere tirar? ",
        ]
        for i in range(len(tirada)):
            tmp_output += [f"Dado {i+1}: {tirada[i]}"]
        tmp_output += [f"Ha obtenido {dw * nw} puntos."]
        mpts_common.add_test(
            LAST_TEST, ["input", [d]], ["random", tirada], ["output", tmp_output],
        )

        # Exercise 181922 END

    elif exercise_id == 181923:
        # Exercise 181923 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190521.html

        # Gana Cubitus
        nc = random.randrange(5, 10)  # Número de dados de Cubitus
        tc = [random.randrange(nc, 101)]  # Primer dado
        for i in range(2, nc):
            tc += [random.randrange(nc - i + 1, tc[-1])]
        tc += [random.randrange(tc[0], 101)]  # Último dado
        output_c = "Cubitus: "
        for i in tc:
            output_c += f"{i} "

        nh = random.randrange(2, nc)  # Número de dados de Humerus
        th = [random.randrange(nh, 101)]  # Primer dado
        for i in range(2, nh):
            th += [random.randrange(nh - i + 1, th[-1])]
        th += [random.randrange(th[0], 101)]  # Último dado
        output_h = "Humerus: "
        for i in th:
            output_h += f"{i} "

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", tc + th],
            [
                "output",
                ["JUEGO DADO A TIERRA", output_c, output_h, "Ha ganado Cubitus.",],
            ],
        )

        # Gana Humerus
        nc = random.randrange(2, 5)  # Número de dados de Cubitus
        tc = [random.randrange(nc, 101)]  # Primer dado
        for i in range(2, nc):
            tc += [random.randrange(nc - i + 1, tc[-1])]
        tc += [random.randrange(tc[0], 101)]  # Último dado
        output_c = "Cubitus: "
        for i in tc:
            output_c += f"{i} "

        nh = random.randrange(nc + 1, 10)  # Número de dados de Humerus
        th = [random.randrange(nh, 101)]  # Primer dado
        for i in range(2, nh):
            th += [random.randrange(nh - i + 1, th[-1])]
        th += [random.randrange(th[0], 101)]  # Último dado
        output_h = "Humerus: "
        for i in th:
            output_h += f"{i} "

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", tc + th],
            [
                "output",
                ["JUEGO DADO A TIERRA", output_c, output_h, "Ha ganado Humerus.",],
            ],
        )

        # Empate
        nc = random.randrange(2, 10)  # Número de dados de Cubitus
        tc = [random.randrange(nc, 101)]  # Primer dado
        for i in range(2, nc):
            tc += [random.randrange(nc - i + 1, tc[-1])]
        tc += [random.randrange(tc[0], 101)]  # Último dado
        output_c = "Cubitus: "
        for i in tc:
            output_c += f"{i} "

        nh = nc  # Número de dados de Humerus
        th = [random.randrange(nh, 101)]  # Primer dado
        for i in range(2, nh):
            th += [random.randrange(nh - i + 1, th[-1])]
        th += [random.randrange(th[0], 101)]  # Último dado
        output_h = "Humerus: "
        for i in th:
            output_h += f"{i} "

        mpts_common.add_test(
            LAST_TEST,
            ["random", tc + th],
            ["output", ["JUEGO DADO A TIERRA", output_c, output_h, "Han empatado.",],],
        )

        # Exercise 181923 END

    elif exercise_id == 181931:
        # Exercise 181931 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190530.html

        # Valor negativo
        a = -random.randrange(100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "¡No ha escrito un número positivo menor que 1000!",
                ],
            ],
        )

        a = random.randrange(1000, 2000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "¡No ha escrito un número positivo menor que 1000!",
                ],
            ],
        )

        a = random.randrange(1000)
        b = -random.randrange(100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    "¡No ha escrito un número positivo menor que 1000!",
                ],
            ],
        )

        a = random.randrange(1000)
        b = random.randrange(1000, 2000)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    "¡No ha escrito un número positivo menor que 1000!",
                ],
            ],
        )

        # Como hay un montón de casos posibles, no he forzado que d1, d2 y d3 sean iguales o distintas

        # mismas cifras 1/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d1 * 100 + d2 * 10 + d3
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d1}, {d2} y {d3}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # mismas cifras 2/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d1 * 100 + d3 * 10 + d2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d1}, {d3} y {d2}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # mismas cifras 3/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d2 * 100 + d1 * 10 + d3
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d2}, {d1} y {d3}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # mismas cifras 4/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d2 * 100 + d3 * 10 + d1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d2}, {d3} y {d1}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # mismas cifras 5/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d3 * 100 + d1 * 10 + d2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d3}, {d1} y {d2}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # mismas cifras 6/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        a = d1 * 100 + d2 * 10 + d3
        b = d3 * 100 + d2 * 10 + d1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d3}, {d2} y {d1}.",
                    "¡Son las mismas cifras!",
                ],
            ],
        )

        # coinciden dos cifras 1/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d1 * 100 + d2 * 10 + d4
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d1}, {d2} y {d4}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coinciden dos cifras 2/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d2 * 100 + d1 * 10 + d4
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d2}, {d1} y {d4}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coinciden dos cifras 3/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d1 * 100 + d4 * 10 + d2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d1}, {d4} y {d2}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coinciden dos cifras 4/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d2 * 100 + d4 * 10 + d1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d2}, {d4} y {d1}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coinciden dos cifras 5/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d4 * 100 + d1 * 10 + d2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d4}, {d1} y {d2}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coinciden dos cifras 6/6
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d3)
        d4 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d4 * 100 + d2 * 10 + d1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d4}, {d2} y {d1}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coincide una cifra 1/3
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d2)
        if d3 in d:
            d.remove(d3)
        d4 = random.choice(d)
        d5 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d1 * 100 + d4 * 10 + d5
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d1}, {d4} y {d5}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coincide una cifra 2/3
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d2)
        if d3 in d:
            d.remove(d3)
        d4 = random.choice(d)
        d5 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d4 * 100 + d1 * 10 + d5
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d4}, {d1} y {d5}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # coincide una cifra 3/3
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d2)
        if d3 in d:
            d.remove(d3)
        d4 = random.choice(d)
        d5 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d4 * 100 + d5 * 10 + d1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d4}, {d5} y {d1}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # cifras distintas 1/1
        d1 = random.randrange(0, 10)
        d2 = random.randrange(0, 10)
        d3 = random.randrange(0, 10)
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.remove(d1)
        if d2 in d:
            d.remove(d2)
        if d3 in d:
            d.remove(d3)
        d4 = random.choice(d)
        d5 = random.choice(d)
        d6 = random.choice(d)
        a = d1 * 100 + d2 * 10 + d3
        b = d4 * 100 + d5 * 10 + d6
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "LAS MISMAS CIFRAS",
                    "Escriba un número positivo menor que 1000: ",
                    "Escriba otro número positivo menor que 1000: ",
                    f"Las cifras del primer número son {d1}, {d2} y {d3}.",
                    f"Las cifras del segundo número son {d4}, {d5} y {d6}.",
                    "¡Las cifras son distintas!",
                ],
            ],
        )

        # Exercise 181931 END

    elif exercise_id == 181932:
        # Exercise 181932 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190530.html

        # Valor negativo
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        n = -random.randrange(1, 20)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, n]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TRES VALORES",
                    "Elija un valor del 1 al 6: ",
                    "Elija otro valor del 1 al 6: ",
                    "Elija otro valor más del 1 al 6: ",
                    "¿Cuántos dados quiere tirar? ",
                    "¡Imposible!",
                ],
            ],
        )

        # Cero
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        n = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, n]],
            [
                "output",
                [
                    "JUEGO DE DADOS: TRES VALORES",
                    "Elija un valor del 1 al 6: ",
                    "Elija otro valor del 1 al 6: ",
                    "Elija otro valor más del 1 al 6: ",
                    "¿Cuántos dados quiere tirar? ",
                    "¡Imposible!",
                ],
            ],
        )

        # Gana
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        dg = [a, b, c]
        dp = [1, 2, 3, 4, 5, 6]
        for i in dg:
            if i in dp:
                dp.remove(i)
        ng = random.randrange(6, 11)
        np = random.randrange(1, ng)
        g = []
        for _ in range(ng):
            g += [random.choice(dg)]
        p = []
        for _ in range(np):
            p += [random.choice(dp)]
        d = p + g
        random.shuffle(d)
        tmp_tirada = ""
        for i in d:
            tmp_tirada += f"{i} "
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, ng + np]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS: TRES VALORES",
                    "Elija un valor del 1 al 6: ",
                    "Elija otro valor del 1 al 6: ",
                    "Elija otro valor más del 1 al 6: ",
                    "¿Cuántos dados quiere tirar? ",
                    f"Tirada de dados: {tmp_tirada}",
                    f"Ha sacado {ng} dados de los valores elegidos. Ha ganado.",
                ],
            ],
        )

        # Pierde
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        dg = [a, b, c]
        dp = [1, 2, 3, 4, 5, 6]
        for i in dg:
            if i in dp:
                dp.remove(i)
        ng = random.randrange(1, 5)
        np = random.randrange(ng + 1, 11)
        g = []
        for _ in range(ng):
            g += [random.choice(dg)]
        p = []
        for _ in range(np):
            p += [random.choice(dp)]
        d = p + g
        random.shuffle(d)
        tmp_tirada = ""
        for i in d:
            tmp_tirada += f"{i} "
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c, ng + np]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS: TRES VALORES",
                    "Elija un valor del 1 al 6: ",
                    "Elija otro valor del 1 al 6: ",
                    "Elija otro valor más del 1 al 6: ",
                    "¿Cuántos dados quiere tirar? ",
                    f"Tirada de dados: {tmp_tirada}",
                    f"Ha sacado {ng} dados de los valores elegidos. Ha perdido.",
                ],
            ],
        )

        # Empata
        a = random.randrange(1, 7)
        b = random.randrange(1, 7)
        c = random.randrange(1, 7)
        dg = [a, b, c]
        dp = [1, 2, 3, 4, 5, 6]
        for i in dg:
            if i in dp:
                dp.remove(i)
        ng = random.randrange(1, 11)
        np = ng
        g = []
        for _ in range(ng):
            g += [random.choice(dg)]
        p = []
        for _ in range(np):
            p += [random.choice(dp)]
        d = p + g
        random.shuffle(d)
        tmp_tirada = ""
        for i in d:
            tmp_tirada += f"{i} "
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c, ng + np]],
            ["random", d],
            [
                "output",
                [
                    "JUEGO DE DADOS: TRES VALORES",
                    "Elija un valor del 1 al 6: ",
                    "Elija otro valor del 1 al 6: ",
                    "Elija otro valor más del 1 al 6: ",
                    "¿Cuántos dados quiere tirar? ",
                    f"Tirada de dados: {tmp_tirada}",
                    f"Ha sacado {ng} dados de los valores elegidos. Ni ha ganado ni perdido.",
                ],
            ],
        )

        # Exercise 181932 END

    elif exercise_id == 181933:
        # Exercise 181933 BEGINNING
        # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190530.html

        # Gana primer jugador
        na = random.randrange(2, 10)
        da = random.randrange(2, 7)
        ta = []
        for _ in range(na - 3):
            d = [1, 2, 3, 4, 5, 6]
            if ta != []:
                d.remove(ta[-1])
            ta += [random.choice(d)]
        if na >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if ta != [] and ta[-1] in d:
                d.remove(ta[-1])
            if da in d:
                d.remove(da)
            xa = random.choice(d)
            ta += [xa]
        ta += [da, da]
        texta = ""
        for _ in ta:
            texta += f"{_} "

        nb = random.randrange(2, 10)
        db = random.randrange(1, da)
        tb = []
        for _ in range(nb - 3):
            d = [1, 2, 3, 4, 5, 6]
            if tb != []:
                d.remove(tb[-1])
            tb += [random.choice(d)]
        if nb >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if tb != [] and tb[-1] in d:
                d.remove(tb[-1])
            if db in d:
                d.remove(db)
            xb = random.choice(d)
            tb += [xb]
        tb += [db, db]
        textb = ""
        for _ in tb:
            textb += f"{_} "

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", ta + tb],
            [
                "output",
                [
                    "JUEGO DE DADOS: HASTA REPETIR",
                    f"Tirada de Cubitus: {texta}",
                    f"Tirada de Humerus: {textb}",
                    f"Cubitus ha sacado un {da} y Humerus ha sacado un {db}.",
                    "Ha ganado Cubitus.",
                ],
            ],
        )

        # Gana segundo jugador
        na = random.randrange(2, 10)
        da = random.randrange(1, 6)
        ta = []
        for _ in range(na - 3):
            d = [1, 2, 3, 4, 5, 6]
            if ta != []:
                d.remove(ta[-1])
            ta += [random.choice(d)]
        if na >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if ta != [] and ta[-1] in d:
                d.remove(ta[-1])
            if da in d:
                d.remove(da)
            xa = random.choice(d)
            ta += [xa]
        ta += [da, da]
        texta = ""
        for _ in ta:
            texta += f"{_} "

        nb = random.randrange(2, 10)
        db = random.randrange(da + 1, 7)
        tb = []
        for _ in range(nb - 3):
            d = [1, 2, 3, 4, 5, 6]
            if tb != []:
                d.remove(tb[-1])
            tb += [random.choice(d)]
        if nb >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if tb != [] and tb[-1] in d:
                d.remove(tb[-1])
            if db in d:
                d.remove(db)
            xb = random.choice(d)
            tb += [xb]
        tb += [db, db]
        textb = ""
        for _ in tb:
            textb += f"{_} "

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["random", ta + tb],
            [
                "output",
                [
                    "JUEGO DE DADOS: HASTA REPETIR",
                    f"Tirada de Cubitus: {texta}",
                    f"Tirada de Humerus: {textb}",
                    f"Cubitus ha sacado un {da} y Humerus ha sacado un {db}.",
                    "Ha ganado Humerus.",
                ],
            ],
        )

        # Empatan
        na = random.randrange(2, 10)
        da = random.randrange(1, 7)
        ta = []
        for _ in range(na - 3):
            d = [1, 2, 3, 4, 5, 6]
            if ta != []:
                d.remove(ta[-1])
            ta += [random.choice(d)]
        if na >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if ta != [] and ta[-1] in d:
                d.remove(ta[-1])
            if da in d:
                d.remove(da)
            xa = random.choice(d)
            ta += [xa]
        ta += [da, da]
        texta = ""
        for _ in ta:
            texta += f"{_} "

        nb = random.randrange(2, 10)
        db = da
        tb = []
        for _ in range(nb - 3):
            d = [1, 2, 3, 4, 5, 6]
            if tb != []:
                d.remove(tb[-1])
            tb += [random.choice(d)]
        if nb >= 3:
            d = [1, 2, 3, 4, 5, 6]
            if tb != [] and tb[-1] in d:
                d.remove(tb[-1])
            if db in d:
                d.remove(db)
            xb = random.choice(d)
            tb += [xb]
        tb += [db, db]
        textb = ""
        for _ in tb:
            textb += f"{_} "

        mpts_common.add_test(
            LAST_TEST,
            ["random", ta + tb],
            [
                "output",
                [
                    "JUEGO DE DADOS: HASTA REPETIR",
                    f"Tirada de Cubitus: {texta}",
                    f"Tirada de Humerus: {textb}",
                    f"Cubitus ha sacado un {da} y Humerus ha sacado un {db}.",
                    "Han empatado.",
                ],
            ],
        )

        # Exercise 181933 END
