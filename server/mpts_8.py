import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 81:
        # Exercise 81 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Segundo menor
        a = random.randrange(0, 20)
        b = random.randrange(-10, a)
        mpts_common.add_test(
            [a, b],
            [
                "PARES E IMPARES",
                "Escriba un número entero: ",
                f"Escriba un número entero mayor o igual que {a}: ",
                f"¡Le he pedido un número entero mayor o igual que {a}!",
            ],
            NOT_LAST_TEST,
        )

        # De par a par
        a = 2 * random.randrange(0, 10)
        b = a + 2 * random.randrange(10, 20)
        c = [
            "PARES E IMPARES",
            "Escriba un número entero: ",
            f"Escriba un número entero mayor o igual que {a}: ",
        ]
        for i in range(a, b + 1):
            if i % 2 == 0:
                c += [f"El número {i} es par."]
            else:
                c += [f"El número {i} es impar."]

        mpts_common.add_test([a, b], c, NOT_LAST_TEST)

        # De par (negativo) a impar
        a = -2 * random.randrange(0, 10)
        b = a + 2 * random.randrange(10, 20) + 1
        c = [
            "PARES E IMPARES",
            "Escriba un número entero: ",
            f"Escriba un número entero mayor o igual que {a}: ",
        ]
        for i in range(a, b + 1):
            if i % 2 == 0:
                c += [f"El número {i} es par."]
            else:
                c += [f"El número {i} es impar."]

        mpts_common.add_test([a, b], c, NOT_LAST_TEST)

        # De impar (negativo) a par
        a = -2 * random.randrange(0, 10) - 1
        b = a + 2 * random.randrange(10, 20) + 1
        c = [
            "PARES E IMPARES",
            "Escriba un número entero: ",
            f"Escriba un número entero mayor o igual que {a}: ",
        ]
        for i in range(a, b + 1):
            if i % 2 == 0:
                c += [f"El número {i} es par."]
            else:
                c += [f"El número {i} es impar."]

        mpts_common.add_test([a, b], c, NOT_LAST_TEST)

        # De impar a impar
        a = 2 * random.randrange(0, 10) + 1
        b = a + 2 * random.randrange(10, 20)
        c = [
            "PARES E IMPARES",
            "Escriba un número entero: ",
            f"Escriba un número entero mayor o igual que {a}: ",
        ]
        for i in range(a, b + 1):
            if i % 2 == 0:
                c += [f"El número {i} es par."]
            else:
                c += [f"El número {i} es impar."]

        mpts_common.add_test([a, b], c, LAST_TEST)

        # Exercise 81 END

    elif exercise_id == 82:
        # Exercise 82 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                "¡Le he pedido un número entero mayor que cero!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                "¡Le he pedido un número entero mayor que cero!",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        mpts_common.add_test(
            [a],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                "Los divisores de 1 son 1 ",
            ],
            NOT_LAST_TEST,
        )

        # Primo
        a = mpts_common.generate_prime(random.randrange(100, 1001))
        mpts_common.add_test(
            [a],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                f"Los divisores de {a} son 1 {a} ",
            ],
            NOT_LAST_TEST,
        )

        # No primo impar
        a = mpts_common.generate_prime(random.randrange(2, 11))
        b = mpts_common.generate_prime(random.randrange(11, 21))
        c = mpts_common.generate_prime(random.randrange(21, 31))
        numero = a * b * c
        resp = ""
        for i in range(1, numero // 2 + 1):
            if numero % i == 0:
                resp += f"{i} "
        resp += f"{numero } "

        mpts_common.add_test(
            [numero],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                f"Los divisores de {numero} son {resp}",
            ],
            NOT_LAST_TEST,
        )

        # No primo par
        a = mpts_common.generate_prime(random.randrange(2, 11))
        b = mpts_common.generate_prime(random.randrange(11, 21))
        c = mpts_common.generate_prime(random.randrange(21, 31))
        numero = 2 * a * b * c
        resp = ""
        for i in range(1, numero // 2 + 1):
            if numero % i == 0:
                resp += f"{i} "
        resp += f"{numero } "

        mpts_common.add_test(
            [numero],
            [
                "DIVISORES",
                "Escriba un número entero mayor que cero: ",
                f"Los divisores de {numero} son {resp}",
            ],
            LAST_TEST,
        )

        # Exercise 82 END

    elif exercise_id == 83:
        # Exercise 83 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [
                "MAYORES QUE EL PRIMERO",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [
                "MAYORES QUE EL PRIMERO",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        b = random.randrange(-100, 101)
        mpts_common.add_test(
            [a, b],
            [
                "MAYORES QUE EL PRIMERO",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Dos
        a = 2
        b = random.randrange(0, 101)
        c = random.randrange(101, 200)
        mpts_common.add_test(
            [a, b, c],
            [
                "MAYORES QUE EL PRIMERO",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                f"Escriba un número más grande que {b}: ",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Dos
        a = 2
        b = random.randrange(0, 101)
        c = random.randrange(-100, 0)
        mpts_common.add_test(
            [a, b, c],
            [
                "MAYORES QUE EL PRIMERO",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                f"Escriba un número más grande que {b}: ",
                f"¡{c} no es mayor que {b}!",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Varios
        a = random.randrange(5, 11)
        b = random.randrange(-100, 101)
        tmp_input = [a, b]
        tmp_output = [
            "MAYORES QUE EL PRIMERO",
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        for i in range(a-1):
            tmp_output += [f"Escriba un número más grande que {b}: "]
            c = random.randrange(-100, 101)
            tmp_input += [c]
            if c <= b:
                tmp_output += [f"¡{c} no es mayor que {b}!"]
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(
            tmp_input,
            tmp_output,
            LAST_TEST,
        )

        # Exercise 83 END

    elif exercise_id == 84:
        # Exercise 84 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [
                "MAYORES QUE EL ANTERIOR",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [
                "MAYORES QUE EL ANTERIOR",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        b = random.randrange(-100, 101)
        mpts_common.add_test(
            [a, b],
            [
                "MAYORES QUE EL ANTERIOR",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Dos
        a = 2
        b = random.randrange(0, 101)
        c = random.randrange(101, 200)
        mpts_common.add_test(
            [a, b, c],
            [
                "MAYORES QUE EL ANTERIOR",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                f"Escriba un número más grande que {b}: ",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Dos
        a = 2
        b = random.randrange(0, 101)
        c = random.randrange(-100, 0)
        mpts_common.add_test(
            [a, b, c],
            [
                "MAYORES QUE EL ANTERIOR",
                "¿Cuántos valores va a introducir? ",
                "Escriba un número: ",
                f"Escriba un número más grande que {b}: ",
                f"¡{c} no es mayor que {b}!",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Varios
        a = random.randrange(5, 11)
        b = random.randrange(-100, 101)
        tmp_input = [a, b]
        tmp_output = [
            "MAYORES QUE EL ANTERIOR",
            "¿Cuántos valores va a introducir? ",
            "Escriba un número: ",
        ]
        d = b
        for i in range(a-1):
            tmp_output += [f"Escriba un número más grande que {d}: "]
            c = random.randrange(-100, 101)
            tmp_input += [c]
            if c <= d:
                tmp_output += [f"¡{c} no es mayor que {d}!"]
            d = c
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(
            tmp_input,
            tmp_output,
            LAST_TEST,
        )

        # Exercise 84 END
