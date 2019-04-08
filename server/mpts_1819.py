import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 181_901:
        # Exercise 181901 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                "Ha indicado una cantidad negativa.",
            ],
            NOT_LAST_TEST,
        )

        # Cantidad no múltiplo de cien
        a = 100 * random.randrange(0, 100) + random.randrange(1, 100)
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                "No ha indicado una cantidad múltiplo de cien.",
            ],
            NOT_LAST_TEST,
        )

        # Sólo billetes de 100
        b500 = 0
        b200 = 0
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Sólo billetes de 200
        b500 = 0
        b200 = random.randrange(1, 3)
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Sólo billetes de 500
        b500 = random.randrange(1, 50)
        b200 = 0
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Billetes de 100 y 200
        b500 = 0
        b200 = 1
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Billetes de 100 y 500
        b500 = random.randrange(1, 50)
        b200 = 0
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Billetes de 200 y 500
        b500 = random.randrange(1, 50)
        b200 = random.randrange(1, 3)
        b100 = 0
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            NOT_LAST_TEST,
        )

        # Billetes de 100, 200 y 500
        b500 = random.randrange(1, 50)
        b200 = 1
        b100 = 1
        a = 500 * b500 + 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTANDO BILLETES",
                "Escriba una cantidad de dinero (múltiplo de 100): ",
                f"Puede pagar {a} con:",
                f"* {b500} billete(s) de 500 €",
                f"* {b200} billete(s) de 200 €",
                f"* {b100} billete(s) de 100 €",
            ],
            LAST_TEST,
        )

        # Exercise 181901 END

    elif exercise_id == 181_902:
        # Exercise 181902 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # Cantidad negativa
        a = -random.randrange(1, 10000)
        mpts_common.add_test(
            [a],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "Ha indicado una cantidad negativa.",
            ],
            NOT_LAST_TEST,
        )

        # Billetes 200 negativos
        a = random.randrange(1, 10000)
        b200 = -random.randrange(1, 10)
        mpts_common.add_test(
            [a, b200],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "¿Cuántos billetes de 200 € entrega? ",
                "Ha indicado una cantidad negativa.",
            ],
            NOT_LAST_TEST,
        )

        # Billetes 100 negativos
        a = random.randrange(1, 10000)
        b200 = random.randrange(1, 10)
        b100 = -random.randrange(1, 10)
        mpts_common.add_test(
            [a, b200, b100],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "¿Cuántos billetes de 200 € entrega? ",
                "¿Cuántos billetes de 100 € entrega? ",
                "Ha indicado una cantidad negativa.",
            ],
            NOT_LAST_TEST,
        )

        # Cantidad exacta
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        a = 200 * b200 + 100 * b100
        mpts_common.add_test(
            [a, b200, b100],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "¿Cuántos billetes de 200 € entrega? ",
                "¿Cuántos billetes de 100 € entrega? ",
                "Ha entregado la cantidad exacta.",
            ],
            NOT_LAST_TEST,
        )

        # Falta dinero
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        b = random.randrange(1, 500)
        a = 200 * b200 + 100 * b100 + b
        mpts_common.add_test(
            [a, b200, b100],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "¿Cuántos billetes de 200 € entrega? ",
                "¿Cuántos billetes de 100 € entrega? ",
                f"Le falta entregar {b} €.",
            ],
            NOT_LAST_TEST,
        )

        # Sobra dinero
        b200 = random.randrange(1, 10)
        b100 = random.randrange(1, 10)
        b = random.randrange(1, 200 * b200 + 100 * b100)
        a = 200 * b200 + 100 * b100 - b
        mpts_common.add_test(
            [a, b200, b100],
            [],
            [
                "SU CAMBIO",
                "¿Cuánto tiene que pagar? ",
                "¿Cuántos billetes de 200 € entrega? ",
                "¿Cuántos billetes de 100 € entrega? ",
                f"Su cambio es de {b} €.",
            ],
            LAST_TEST,
        )

        # Exercise 181902 END

    elif exercise_id == 181_903:
        # Exercise 181903 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # lado1: cantidad negativa
        a = -random.randrange(2, 100)
        mpts_common.add_test(
            [a],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado1: 0
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado2: cantidad negativa
        a = random.randrange(2, 100)
        b = -random.randrange(1, 100)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado2: 0
        a = random.randrange(2, 100)
        b = 0
        mpts_common.add_test(
            [a, b],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado2: mayor que lado1
        a = random.randrange(2, 100)
        b = a + random.randrange(1, 100)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "¡Le he pedido que escribiera primero el lado más largo!",
            ],
            NOT_LAST_TEST,
        )

        # lado3: cantidad negativa
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = -random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado3: 0
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = 0
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                "¡El valor debe ser positivo!",
            ],
            NOT_LAST_TEST,
        )

        # lado3: mayor que lado1
        a = random.randrange(2, 100)
        b = random.randrange(1, a + 1)
        c = a + random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                "¡Le he pedido que escribiera primero el lado más largo!",
            ],
            NOT_LAST_TEST,
        )

        # lado3: triángulo posible
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = random.randrange(a - b + 1, a + 1)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                f"Un triángulo puede tener como lados {a}, {b} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # lado3: triángulo imposible
        a = random.randrange(2, 100)
        b = random.randrange(1, a)
        c = random.randrange(1, a - b)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                f"Un triángulo no puede tener como lados {a}, {b} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # lado3: triángulo degenerado
        a = random.randrange(1, 100)
        b = random.randrange(1, a)
        c = a - b
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "ANALIZADOR DE TRIÁNGULOS",
                "Escriba la longitud del lado más largo: ",
                "Escriba la longitud del segundo lado: ",
                "Escriba la longitud del tercer lado: ",
                "Los datos corresponden a un triángulo degenerado.",
            ],
            LAST_TEST,
        )

        # Exercise 181903 END

    elif exercise_id == 181_904:
        # Exercise 181904 BEGINNING
        # http://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html

        # a y b iguales
        a = random.randrange(-100, 101)
        b = a
        mpts_common.add_test(
            [a, b],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "¡Ha repetido el número!",
            ],
            NOT_LAST_TEST,
        )

        # a y c iguales
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = a
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                "¡Ha repetido algún número!",
            ],
            NOT_LAST_TEST,
        )

        # b y c iguales
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = b
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                "¡Ha repetido algún número!",
            ],
            NOT_LAST_TEST,
        )

        # orden c - a - b
        a = random.randrange(-100, 101)
        b = a + random.randrange(1, 100)
        c = a - random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{a} está entre {b} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # orden b - a - c
        a = random.randrange(-100, 101)
        b = a - random.randrange(1, 100)
        c = a + random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{a} está entre {b} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # orden a - b - c
        b = random.randrange(-100, 101)
        c = b + random.randrange(1, 100)
        a = b - random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{b} está entre {a} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # orden c - b - a
        b = random.randrange(-100, 101)
        c = b - random.randrange(1, 100)
        a = b + random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{b} está entre {a} y {c}.",
            ],
            NOT_LAST_TEST,
        )

        # orden a - c - b
        c = random.randrange(-100, 101)
        b = c + random.randrange(1, 100)
        a = c - random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{c} está entre {a} y {b}.",
            ],
            NOT_LAST_TEST,
        )

        # orden b - c - a
        c = random.randrange(-100, 101)
        b = c - random.randrange(1, 100)
        a = c + random.randrange(1, 100)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "EL NÚMERO DE EN MEDIO",
                "Escriba un número entero: ",
                "Escriba otro número entero distinto: ",
                "Escriba otro número entero distinto a los anteriores: ",
                f"{c} está entre {a} y {b}.",
            ],
            LAST_TEST,
        )

        # Exercise 181904 END
