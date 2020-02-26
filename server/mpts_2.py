import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 11:
        # Exercise 11 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # División exacta
        resto = 0
        cociente = random.randrange(1, 20)
        divisor = random.randrange(1, 20)
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división es exacta. Cociente: {cociente}",
                ],
            ],
        )

        # División no exacta
        resto = random.randrange(1, 20)
        cociente = random.randrange(1, 20)
        divisor = random.randrange(
            resto + 1, 30
        )  # el divisor tiene que ser mayor que el resto
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división no es exacta. Cociente: {cociente} Resto: {resto}",
                ],
            ],
        )

        # Cociente 0
        resto = random.randrange(1, 20)
        cociente = 0
        divisor = random.randrange(
            resto + 1, 30
        )  # el divisor tiene que ser mayor que el resto
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división no es exacta. Cociente: {cociente} Resto: {resto}",
                ],
            ],
        )

        # Exercise 11 END

    elif exercise_id == 12:
        # Exercise 12 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # División exacta
        resto = 0
        cociente = random.randrange(1, 20)
        divisor = random.randrange(1, 20)
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división es exacta. Cociente: {cociente}",
                ],
            ],
        )

        # División no exacta
        resto = random.randrange(1, 20)
        cociente = random.randrange(1, 20)
        divisor = random.randrange(
            resto + 1, 30
        )  # el divisor tiene que ser mayor que el resto
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división no es exacta. Cociente: {cociente} Resto: {resto}",
                ],
            ],
        )

        # Cociente 0
        resto = random.randrange(1, 20)
        cociente = 0
        divisor = random.randrange(
            resto + 1, 30
        )  # el divisor tiene que ser mayor que el resto
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    f"La división no es exacta. Cociente: {cociente} Resto: {resto}",
                ],
            ],
        )

        # Divisor 0
        resto = random.randrange(1, 20)
        cociente = random.randrange(1, 20)
        divisor = 0
        dividendo = cociente * divisor + resto
        mpts_common.add_test(
            LAST_TEST,
            ["input", [dividendo, divisor]],
            [
                "output",
                [
                    "DIVISOR DE NÚMEROS",
                    "Escriba el dividendo: ",
                    "Escriba el divisor: ",
                    "No se puede dividir por cero.",
                ],
            ],
        )

        # Exercise 12 END

    elif exercise_id == 13:
        # Exercise 13 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Primer número es menor
        numero_1 = random.randrange(0, 500) / 10
        salto = random.randrange(0, 500) / 10
        numero_2 = numero_1 + salto

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"Menor: {numero_1}; Mayor: {numero_2}",
                ],
            ],
        )

        # Primer número es mayor
        numero_1 = random.randrange(0, 500) / 10
        salto = random.randrange(0, 500) / 10
        numero_2 = numero_1 - salto

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"Menor: {numero_2}; Mayor: {numero_1}",
                ],
            ],
        )

        # Primer número es mayor
        numero_1 = random.randrange(0, 500) / 10
        numero_2 = numero_1

        mpts_common.add_test(
            LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"Los dos números son iguales.",
                ],
            ],
        )

        # Exercise 13 END

    elif exercise_id == 14:
        # Exercise 14 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Primer año es menor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 + random.randrange(1, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Para llegar al año {fecha_2} faltan {fecha_2 - fecha_1} años.",
                ],
            ],
        )

        # Primer año es mayor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 - random.randrange(1, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Desde el año {fecha_2} han pasado {fecha_1 - fecha_2} años.",
                ],
            ],
        )

        # Años iguales
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1

        mpts_common.add_test(
            LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"¡Son el mismo año!",
                ],
            ],
        )

        # Exercise 14 END

    elif exercise_id == 15:
        # Exercise 15 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Primer año es menor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 + random.randrange(2, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Para llegar al año {fecha_2} faltan {fecha_2 - fecha_1} años.",
                ],
            ],
        )

        # Primer año es 1 año menor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 + 1

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Para llegar al año {fecha_2} falta 1 año.",
                ],
            ],
        )

        # Primer año es mayor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 - random.randrange(2, 20)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Desde el año {fecha_2} han pasado {fecha_1 - fecha_2} años.",
                ],
            ],
        )

        # Primer año es 1 año mayor
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1 - 1

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"Desde el año {fecha_2} ha pasado 1 año.",
                ],
            ],
        )

        # Años iguales
        fecha_1 = 2000 + random.randrange(0, 50)
        fecha_2 = fecha_1

        mpts_common.add_test(
            LAST_TEST,
            ["input", [fecha_1, fecha_2]],
            [
                "output",
                [
                    "COMPARADOR DE AÑOS",
                    "¿En qué año estamos?: ",
                    "Escriba un año cualquiera: ",
                    f"¡Son el mismo año!",
                ],
            ],
        )

        # Exercise 15 END

    elif exercise_id == 16:
        # Exercise 16 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Los números son iguales
        numero_1 = random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_1]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_1} es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números son múltiplos, el segundo es mayor que el primero
        numero_1 = random.randrange(1, 50)
        cociente = random.randrange(1, 11)
        numero_2 = numero_1 * cociente

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números son múltiplos, el primero es mayor que el segundo
        numero_2 = random.randrange(1, 50)
        cociente = random.randrange(1, 11)
        numero_1 = numero_2 * cociente

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_1} es múltiplo de {numero_2}.",
                ],
            ],
        )

        # Los números no son múltiplos, el segundo es mayor que el primero
        numero_1 = random.randrange(2, 50)
        cociente = random.randrange(1, 11)
        resto = random.randrange(1, numero_1)
        numero_2 = numero_1 * cociente + resto

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} no es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números no son múltiplos, el primero es mayor que el segundo
        numero_1 = random.randrange(2, 50)
        cociente = random.randrange(1, 11)
        resto = random.randrange(1, numero_1)
        numero_2 = numero_1 * cociente + resto

        mpts_common.add_test(
            LAST_TEST,
            ["input", [numero_2, numero_1]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} no es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Exercise 16 END

    elif exercise_id == 17:
        # Exercise 17 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Un valor es cero
        numero_1 = random.randrange(1, 50)
        numero_2 = 0

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Lo siento, este programa no admite valores nulos.",
                ],
            ],
        )

        # Un valor es cero
        numero_1 = 0
        numero_2 = random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Lo siento, este programa no admite valores nulos.",
                ],
            ],
        )

        # Los números son iguales
        numero_1 = random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_1]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_1} es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números son múltiplos, el segundo es mayor que el primero
        numero_1 = random.randrange(1, 50)
        cociente = random.randrange(1, 11)
        numero_2 = numero_1 * cociente

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números son múltiplos, el primero es mayor que el segundo
        numero_2 = random.randrange(1, 50)
        cociente = random.randrange(1, 11)
        numero_1 = numero_2 * cociente

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_1} es múltiplo de {numero_2}.",
                ],
            ],
        )

        # Los números no son múltiplos, el segundo es mayor que el primero
        numero_1 = random.randrange(2, 50)
        cociente = random.randrange(1, 11)
        resto = random.randrange(1, numero_1)
        numero_2 = numero_1 * cociente + resto

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} no es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Los números no son múltiplos, el primero es mayor que el segundo
        numero_1 = random.randrange(2, 50)
        cociente = random.randrange(1, 11)
        resto = random.randrange(1, numero_1)
        numero_2 = numero_1 * cociente + resto

        mpts_common.add_test(
            LAST_TEST,
            ["input", [numero_2, numero_1]],
            [
                "output",
                [
                    "COMPARADOR DE MÚLTIPLOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"{numero_2} no es múltiplo de {numero_1}.",
                ],
            ],
        )

        # Exercise 17 END

    elif exercise_id == 18:
        # Exercise 18 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # Los tres valores son iguales
        numero_1 = random.randrange(1, 50)
        numero_2 = numero_1
        numero_3 = numero_1

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2, numero_3]],
            [
                "output",
                [
                    "COMPARADOR DE TRES NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    "Ha escrito tres veces el mismo número.",
                ],
            ],
        )

        # Valores 1 y 2 son iguales
        numero_1 = random.randrange(1, 50)
        numero_2 = numero_1
        numero_3 = numero_1 + random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2, numero_3]],
            [
                "output",
                [
                    "COMPARADOR DE TRES NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    "Ha escrito uno de los números dos veces.",
                ],
            ],
        )

        # Valores 1 y 3 son iguales
        numero_1 = random.randrange(1, 50)
        numero_3 = numero_1
        numero_2 = numero_1 + random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2, numero_3]],
            [
                "output",
                [
                    "COMPARADOR DE TRES NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    "Ha escrito uno de los números dos veces.",
                ],
            ],
        )

        # Valores 2 y 3 son iguales
        numero_2 = random.randrange(1, 50)
        numero_3 = numero_2
        numero_1 = numero_2 + random.randrange(1, 50)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [numero_1, numero_2, numero_3]],
            [
                "output",
                [
                    "COMPARADOR DE TRES NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    "Ha escrito uno de los números dos veces.",
                ],
            ],
        )

        # Los tres valores son distintos
        numero_1 = random.randrange(1, 50)
        numero_2 = numero_1 + random.randrange(1, 50)
        numero_3 = numero_2 + random.randrange(1, 50)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [numero_1, numero_2, numero_3]],
            [
                "output",
                [
                    "COMPARADOR DE TRES NÚMEROS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    "Los tres números que ha escrito son distintos.",
                ],
            ],
        )
        # Exercise 18 END

    elif exercise_id == 19:
        # Exercise 19 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html
        fecha = 4 * random.randrange(400, 600) + 1
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} no es un año bisiesto.",
                ],
            ],
        )

        fecha = 4 * random.randrange(400, 600) + 2
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} no es un año bisiesto.",
                ],
            ],
        )

        fecha = 4 * random.randrange(400, 600) + 3
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} no es un año bisiesto.",
                ],
            ],
        )

        # Múltiplo de 400: No es bisisesto
        fecha = 400 * random.randrange(1, 7)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} es un año bisiesto porque es múltiplo de 400.",
                ],
            ],
        )

        # Múltiplo de 100 que no es múltiplo de 400: Es bisisesto
        fecha = 400 * random.randrange(1, 5) + 100 * random.randrange(1, 4)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.",
                ],
            ],
        )

        # Múltiplo de 4 que no es múltiplo de 100: Es bisiesto
        fecha = 100 * random.randrange(10, 25) + 4 * random.randrange(1, 20)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [fecha]],
            [
                "output",
                [
                    "COMPROBADOR DE AÑOS BISIESTOS",
                    "Escriba un año y le diré si es bisiesto: ",
                    f"El año {fecha} es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.",
                ],
            ],
        )

        # Exercise 19 END

    elif exercise_id == 20:
        # Exercise 20 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # a, b son cero
        a = 0
        b = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ECUACIÓN A X + B = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Todos los números son solución.",
                ],
            ],
        )

        # a es cero, b no es cero
        a = 0.0
        b = random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ECUACIÓN A X + B = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "La ecuación no tiene solución.",
                ],
            ],
        )

        # a no es cero, b es cero
        a = float(random.randrange(1, 100))
        b = 0.0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ECUACIÓN A X + B = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    f"La ecuación tiene una solución: {-b / a}",
                ],
            ],
        )

        # a y b no son cero
        a = float(random.randrange(1, 100))
        b = float(random.randrange(1, 100))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ECUACIÓN A X + B = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    f"La ecuación tiene una solución: {-b / a}",
                ],
            ],
        )

        # a y b no son cero
        a = float(random.randrange(1, 100))
        b = float(-random.randrange(1, 100))
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "ECUACIÓN A X + B = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    f"La ecuación tiene una solución: {-b / a}",
                ],
            ],
        )

        # Exercise 20 END

    elif exercise_id == 21:
        # Exercise 21 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # a, b, c son cero
        a = 0
        b = 0
        c = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    "Todos los números son solución.",
                ],
            ],
        )

        # a es cero, b es cero, c no es cero
        a = 0.0
        b = 0
        c = random.randrange(1, 100)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    "La ecuación no tiene solución.",
                ],
            ],
        )

        # a es cero, b y c no son cero
        a = 0
        b = float(random.randrange(1, 100))
        c = float(random.randrange(1, 100))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    f"La ecuación tiene una solución: {-c / b}",
                ],
            ],
        )

        # a no es cero, Delta negativo
        a = float(random.randrange(1, 100))
        b = float(random.randrange(1, 100))
        x = round(b * b / (4 * a))
        c = float(random.randrange(x + 1, x + 100))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    "La ecuación no tiene solución real.",
                ],
            ],
        )

        # a no es cero, Delta nulo
        a = float(random.randrange(1, 100))
        b = float(random.randrange(1, 100))
        c = b * b / (4 * a)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    f"La ecuación tiene una solución: {-b / (2 * a)}",
                ],
            ],
        )

        # a no es cero, Delta nulo
        a = float(random.randrange(1, 100))
        n = float(random.randrange(1, 20))
        b = 2 * a * n
        c = a * n * n
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    f"La ecuación tiene una solución: {-n}",
                ],
            ],
        )

        # a no es cero, Delta positivo
        a = float(random.randrange(1, 100))
        b = float(random.randrange(1, 100))
        x = round(b * b / (4 * a))
        c = float(random.randrange(-100, x - 1))
        d = b * b - 4 * a * c
        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "ECUACIÓN A X² + B X + C = 0",
                    "Escriba el valor del coeficiente a: ",
                    "Escriba el valor del coeficiente b: ",
                    "Escriba el valor del coeficiente c: ",
                    f"La ecuación tiene dos soluciones: {(-b - d ** 0.5) / (2*a)} y {(-b + d**0.5) / (2*a)}",
                ],
            ],
        )

        # Exercise 21 END

    elif exercise_id == 22:
        # Exercise 22 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # triángulo
        t_c = "T"
        b = float(random.randrange(1, 100))
        h = float(random.randrange(1, 100))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [t_c, b, h]],
            [
                "output",
                [
                    "CÁLCULO DE ÁREAS",
                    "Elija una figura geométrica:",
                    "a) Triángulo",
                    "b) Círculo",
                    "¿Qué figura quiere calcular (Escriba T o C)? ",
                    "Escriba la base: ",
                    "Escriba la altura: ",
                    f"Un triángulo de base {b} y altura {h} tiene un área de { b * h / 2}",
                ],
            ],
        )

        # triángulo
        t_c = "t"
        b = float(random.randrange(1, 1000) / 10)
        h = float(random.randrange(1, 1000) / 10)
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [t_c, b, h]],
            [
                "output",
                [
                    "CÁLCULO DE ÁREAS",
                    "Elija una figura geométrica:",
                    "a) Triángulo",
                    "b) Círculo",
                    "¿Qué figura quiere calcular (Escriba T o C)? ",
                    "Escriba la base: ",
                    "Escriba la altura: ",
                    f"Un triángulo de base {b} y altura {h} tiene un área de { b * h / 2}",
                ],
            ],
        )

        # círculo
        t_c = "C"
        r = float(random.randrange(1, 100))
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [t_c, r]],
            [
                "output",
                [
                    "CÁLCULO DE ÁREAS",
                    "Elija una figura geométrica:",
                    "a) Triángulo",
                    "b) Círculo",
                    "¿Qué figura quiere calcular (Escriba T o C)? ",
                    "Escriba el radio: ",
                    f"Un círculo de radio {r} tiene un área de {3.141592 * r * r}",
                ],
            ],
        )

        # círculo
        t_c = "c"
        r = float(random.randrange(1, 1000) / 10)
        mpts_common.add_test(
            LAST_TEST,
            ["input", [t_c, r]],
            [
                "output",
                [
                    "CÁLCULO DE ÁREAS",
                    "Elija una figura geométrica:",
                    "a) Triángulo",
                    "b) Círculo",
                    "¿Qué figura quiere calcular (Escriba T o C)? ",
                    "Escriba el radio: ",
                    f"Un círculo de radio {r} tiene un área de {3.141592 * r * r}",
                ],
            ],
        )

        # Exercise 22 END

    elif exercise_id == 23:
        # Exercise 23 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # cero
        cm = 0
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    "Escriba una distancia mayor que cero.",
                ],
            ],
        )

        # negativa
        cm = -random.randrange(1, 100)
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    "Escriba una distancia mayor que cero.",
                ],
            ],
        )

        # cm
        cm = random.randrange(1, 100)
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {m} m {resto} cm.",
                ],
            ],
        )

        # m y cm
        cm = random.randrange(100, 100_000)
        km = 0
        m = cm // 100
        resto = cm % 100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {m} m {resto} cm.",
                ],
            ],
        )

        # km, m y cm
        cm = random.randrange(100_000, 10_000_000)
        km = cm // 100_000
        m = cm % 100_000 // 100
        resto = cm % 100
        mpts_common.add_test(
            LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {m} m {resto} cm.",
                ],
            ],
        )

        # Exercise 23 END

    elif exercise_id == 24:
        # TODO NO SE PUEDE VALIDAR LA SOLUCIÓN PORQUE UTILIZA END="" EN EL PRINT
        # Exercise 24 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html

        # cero
        cm = 0
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    "Escriba una distancia mayor que cero.",
                ],
            ],
        )

        # negativa
        cm = -random.randrange(1, 100)
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    "Escriba una distancia mayor que cero.",
                ],
            ],
        )

        # sólo cm
        cm = random.randrange(1, 100)
        km = 0
        m = 0
        resto = cm
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {resto} cm.",
                ],
            ],
        )

        # sólo m
        cm = random.randrange(1, 1000) * 100
        km = 0
        m = cm // 100
        resto = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {m} m.",
                ],
            ],
        )

        # solo km
        cm = random.randrange(1, 100) * 100_000
        km = cm // 100_000
        m = 0
        resto = 0
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km.",
                ],
            ],
        )

        # sólo m y cm
        cm = random.randrange(1, 1000) * 100 + random.randrange(1, 100)
        km = cm // 100_000
        m = cm % 100_000 // 100
        resto = cm % 100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {m} m {resto} cm.",
                ],
            ],
        )

        # sólo km y cm
        cm = random.randrange(1, 100) * 100_000 + random.randrange(1, 100)
        km = cm // 100_000
        m = cm % 100_000 // 100
        resto = cm % 100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {resto} cm.",
                ],
            ],
        )

        # sólo km y m
        cm = random.randrange(1, 100) * 100_000 + random.randrange(1, 100) * 100
        km = cm // 100_000
        m = cm % 100_000 // 100
        resto = cm % 100
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {m} m.",
                ],
            ],
        )

        # sólo km, m y cm
        cm = (
            random.randrange(1, 100) * 100_000
            + random.randrange(1, 100) * 100
            + random.randrange(1, 100)
        )
        km = cm // 100_000
        m = cm % 100_000 // 100
        resto = cm % 100
        mpts_common.add_test(
            LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CM A KM, M Y CM",
                    "Escriba una distancia en centímetros: ",
                    f"{cm} centímetros son {km} km {m} m {resto} cm.",
                ],
            ],
        )

        # Exercise 24 END

