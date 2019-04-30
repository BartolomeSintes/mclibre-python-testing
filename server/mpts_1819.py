import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 181_911:
        # Exercise 181911 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

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
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

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
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

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
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
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
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

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
