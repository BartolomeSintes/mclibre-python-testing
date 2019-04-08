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
            [],
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

        mpts_common.add_test([a, b], [], c, NOT_LAST_TEST)

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

        mpts_common.add_test([a, b], [], c, NOT_LAST_TEST)

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

        mpts_common.add_test([a, b], [], c, NOT_LAST_TEST)

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

        mpts_common.add_test([a, b], [], c, LAST_TEST)

        # Exercise 81 END

    elif exercise_id == 82:
        # Exercise 82 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
        for i in range(a - 1):
            tmp_output += [f"Escriba un número más grande que {b}: "]
            c = random.randrange(-100, 101)
            tmp_input += [c]
            if c <= b:
                tmp_output += [f"¡{c} no es mayor que {b}!"]
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 83 END

    elif exercise_id == 84:
        # Exercise 84 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
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
            [],
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
            [],
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
            [],
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
            [],
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
        for i in range(a - 1):
            tmp_output += [f"Escriba un número más grande que {d}: "]
            c = random.randrange(-100, 101)
            tmp_input += [c]
            if c <= d:
                tmp_output += [f"¡{c} no es mayor que {d}!"]
            d = c
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 84 END

    elif exercise_id == 85:
        # Exercise 85 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
            ["NÚMEROS NEGATIVOS", "¿Cuántos valores va a introducir? ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMEROS NEGATIVOS",
                "¿Cuántos valores va a introducir? ",
                "No ha escrito ningún número negativo.",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        b = random.randrange(1, 101)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "NÚMEROS NEGATIVOS",
                "¿Cuántos valores va a introducir? ",
                "Escriba el número 1: ",
                "No ha escrito ningún número negativo.",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        b = random.randrange(-100, 0)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "NÚMEROS NEGATIVOS",
                "¿Cuántos valores va a introducir? ",
                "Escriba el número 1: ",
                "Ha escrito 1 número negativo.",
            ],
            NOT_LAST_TEST,
        )

        # Varios números, 0 negativos
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = ["NÚMEROS NEGATIVOS", "¿Cuántos valores va a introducir? "]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(0, 1000)
            tmp_input += [c]
        tmp_output += ["No ha escrito ningún número negativo."]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Varios números, 1 negativo
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = ["NÚMEROS NEGATIVOS", "¿Cuántos valores va a introducir? "]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(0, 1000)
            tmp_input += [c]
        # cambio un número a negativo
        b = random.randrange(1, a + 1)
        tmp_input[b] = random.randrange(-1000, 0)

        tmp_output += ["Ha escrito 1 número negativo."]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Varios números, varios negativos
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = ["NÚMEROS NEGATIVOS", "¿Cuántos valores va a introducir? "]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(0, 1000)
            tmp_input += [c]
        # cambio varios a negativos
        b = random.randrange(2, a + 1)
        lista = random.sample(range(1, a + 1), k=b)
        for i in lista:
            tmp_input[i] = random.randrange(-1000, 0)

        tmp_output += [f"Ha escrito {b} números negativos."]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 85 END

    elif exercise_id == 86:
        # Exercise 86 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTADOR DE PARES E IMPARES",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "CONTADOR DE PARES E IMPARES",
                "¿Cuántos valores va a introducir? ",
                "Ha escrito 0 números pares y 0 números impares.",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Un par
        a = 1
        b = 2 * random.randrange(1, 101)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "CONTADOR DE PARES E IMPARES",
                "¿Cuántos valores va a introducir? ",
                "Escriba el valor 1: ",
                "Ha escrito 1 números pares y 0 números impares.",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Un impar
        a = 1
        b = 2 * random.randrange(1, 101) + 1
        mpts_common.add_test(
            [a, b],
            [],
            [
                "CONTADOR DE PARES E IMPARES",
                "¿Cuántos valores va a introducir? ",
                "Escriba el valor 1: ",
                "Ha escrito 0 números pares y 1 números impares.",
                "Gracias por su colaboración.",
            ],
            NOT_LAST_TEST,
        )

        # Varios números, 0 impares
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = [
            "CONTADOR DE PARES E IMPARES",
            "¿Cuántos valores va a introducir? ",
        ]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el valor {i}: "]
            c = 2 * random.randrange(0, 500)
            tmp_input += [c]
        tmp_output += [f"Ha escrito {a} números pares y 0 números impares."]
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Varios números, 0 pares
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = [
            "CONTADOR DE PARES E IMPARES",
            "¿Cuántos valores va a introducir? ",
        ]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el valor {i}: "]
            c = 2 * random.randrange(0, 500) + 1
            tmp_input += [c]
        tmp_output += [f"Ha escrito 0 números pares y {a} números impares."]
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Varios pares, varios impares
        a = random.randrange(5, 21)
        tmp_input = [a]
        tmp_output = [
            "CONTADOR DE PARES E IMPARES",
            "¿Cuántos valores va a introducir? ",
        ]
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el valor {i}: "]
            c = 2 * random.randrange(0, 500)
            tmp_input += [c]
        # cambio varios a impares
        b = random.randrange(2, a + 1)
        lista = random.sample(range(1, a + 1), k=b)
        for i in lista:
            tmp_input[i] = 2 * random.randrange(0, 500) + 1

        tmp_output += [f"Ha escrito {a - b} números pares y {b} números impares."]
        tmp_output += ["Gracias por su colaboración."]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 86 END

    elif exercise_id == 87:
        # Exercise 87 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                "¡Le he pedido un número entero mayor que 1!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                "¡Le he pedido un número entero mayor que 1!",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                "¡Le he pedido un número entero mayor que 1!",
            ],
            NOT_LAST_TEST,
        )

        # Primo pequeño
        a = mpts_common.generate_prime(random.randrange(100, 501))
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                f"{a} es primo.",
            ],
            NOT_LAST_TEST,
        )

        # Primo grande
        a = mpts_common.generate_prime(random.randrange(1000, 2001))
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                f"{a} es primo.",
            ],
            NOT_LAST_TEST,
        )

        # No primo pequeño
        a = 1
        for _ in range(2):
            a *= mpts_common.generate_prime(random.randrange(2, 10))
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                f"{a} no es primo.",
            ],
            NOT_LAST_TEST,
        )

        # No primo grande
        a = 1
        for _ in range(3):
            a *= mpts_common.generate_prime(random.randrange(10, 51))
        mpts_common.add_test(
            [a],
            [],
            [
                "NÚMERO PRIMO",
                "Escriba un número entero mayor que 1: ",
                f"{a} no es primo.",
            ],
            LAST_TEST,
        )

        # Exercise 87 END

    elif exercise_id == 88:
        # Exercise 88 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = random.randrange(-1000, 0)
        mpts_common.add_test(
            [a],
            [],
            ["SUMA DE VALORES", "¿Cuántos valores va a introducir? ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            ["SUMA DE VALORES", "¿Cuántos valores va a introducir? ", "¡Imposible!"],
            NOT_LAST_TEST,
        )

        # Pocos números
        a = random.randrange(1, 11)
        tmp_input = [a]
        tmp_output = ["SUMA DE VALORES", "¿Cuántos valores va a introducir? "]
        suma = 0
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(-1000, 1001) / 10
            tmp_input += [c]
            suma += c
        tmp_output += [f"La suma de los números que ha escrito es {suma}"]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Muchos números
        a = random.randrange(11, 21)
        tmp_input = [a]
        tmp_output = ["SUMA DE VALORES", "¿Cuántos valores va a introducir? "]
        suma = 0
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(-10000, 10001) / 100
            tmp_input += [c]
            suma += c
        tmp_output += [f"La suma de los números que ha escrito es {suma}"]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 88 END

    elif exercise_id == 89:
        # Exercise 89 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Primero negativo
        a = -random.randrange(1, 101)
        mpts_common.add_test(
            [a],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                "¡Le he pedido un número entero positivo!",
            ],
            NOT_LAST_TEST,
        )

        # Primero cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                "¡Le he pedido un número entero positivo!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo menor que primero
        a = random.randrange(0, 1001)
        b = random.randrange(0, a)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"¡Le he pedido un número entero mayor que {a}!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo igual a primero
        a = random.randrange(0, 1001)
        b = a
        mpts_common.add_test(
            [a, b],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"¡Le he pedido un número entero mayor que {a}!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo mayor que el primero, pocos
        a = random.randrange(0, 1001)
        b = a + random.randrange(1, 10)
        c = int(b * (b + 1) / 2 - (a - 1) * a / 2)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"La suma desde {a} hasta {b} es {c}",
            ],
            NOT_LAST_TEST,
        )

        # Segundo mayor que el primero, muchos
        a = random.randrange(0, 1001)
        b = a + random.randrange(10, 30)
        c = int(b * (b + 1) / 2 - (a - 1) * a / 2)
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"La suma desde {a} hasta {b} es {c}",
            ],
            LAST_TEST,
        )

        # Exercise 89 END

    elif exercise_id == 90:
        # Exercise 90 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Primero negativo
        a = -random.randrange(1, 101)
        mpts_common.add_test(
            [a],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                "¡Le he pedido un número entero positivo!",
            ],
            NOT_LAST_TEST,
        )

        # Primero cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                "¡Le he pedido un número entero positivo!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo menor que primero
        a = random.randrange(0, 1001)
        b = random.randrange(0, a)
        mpts_common.add_test(
            [a, b],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"¡Le he pedido un número entero mayor que {a}!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo igual a primero
        a = random.randrange(0, 1001)
        b = a
        mpts_common.add_test(
            [a, b],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"¡Le he pedido un número entero mayor que {a}!",
            ],
            NOT_LAST_TEST,
        )

        # Segundo mayor que el primero, pocos
        a = random.randrange(0, 1001)
        b = a + random.randrange(1, 10)
        c = int(b * (b + 1) / 2 - (a - 1) * a / 2)
        tmp_output = ""
        for i in range(a, b):
            tmp_output += f"{i} + "
        tmp_output += f"{b} = {c}"
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"La suma desde {a} hasta {b} es {c}",
                tmp_output,
            ],
            NOT_LAST_TEST,
        )

        # Segundo mayor que el primero, muchos
        a = random.randrange(0, 1001)
        b = a + random.randrange(10, 30)
        c = int(b * (b + 1) / 2 - (a - 1) * a / 2)
        tmp_output = ""
        for i in range(a, b):
            tmp_output += f"{i} + "
        tmp_output += f"{b} = {c}"
        mpts_common.add_test(
            [a, b, c],
            [],
            [
                "SUMA ENTRE VALORES",
                "Escriba un número entero positivo: ",
                f"Escriba un número entero mayor que {a}: ",
                f"La suma desde {a} hasta {b} es {c}",
                tmp_output,
            ],
            LAST_TEST,
        )

        # Exercise 90 END

    elif exercise_id == 91:
        # Exercise 91 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Primero negativo
        a = -random.randrange(1, 101)
        mpts_common.add_test(
            [a],
            [],
            [
                "MAYOR, MENOR Y MEDIA ARITMÉTICA",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Primero cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "MAYOR, MENOR Y MEDIA ARITMÉTICA",
                "¿Cuántos valores va a introducir? ",
                "¡Imposible!",
            ],
            NOT_LAST_TEST,
        )

        # Pocos números, positivos
        a = random.randrange(3, 11)
        tmp_input = [a]
        tmp_output = [
            "MAYOR, MENOR Y MEDIA ARITMÉTICA",
            "¿Cuántos valores va a introducir? ",
        ]
        menor = 2000
        mayor = -2000
        media = 0
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(0, 1001)
            tmp_input += [c]
            if c < menor:
                menor = c
            if c > mayor:
                mayor = c
            media += c
        media /= a
        tmp_output += [f"El número más pequeño de los introducidos es {float(menor)}"]
        tmp_output += [f"El número más grande de los introducidos es {float(mayor)}"]
        tmp_output += [f"La media de los números introducidos es {media}"]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Más números, positivos y negativos
        a = random.randrange(11, 21)
        tmp_input = [a]
        tmp_output = [
            "MAYOR, MENOR Y MEDIA ARITMÉTICA",
            "¿Cuántos valores va a introducir? ",
        ]
        menor = 2000
        mayor = -2000
        media = 0
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(-1000, 1001)
            tmp_input += [c]
            if c < menor:
                menor = c
            if c > mayor:
                mayor = c
            media += c
        media /= a
        tmp_output += [f"El número más pequeño de los introducidos es {float(menor)}"]
        tmp_output += [f"El número más grande de los introducidos es {float(mayor)}"]
        tmp_output += [f"La media de los números introducidos es {media}"]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Más números, positivos y negativos, decimales
        a = random.randrange(11, 21)
        tmp_input = [a]
        tmp_output = [
            "MAYOR, MENOR Y MEDIA ARITMÉTICA",
            "¿Cuántos valores va a introducir? ",
        ]
        menor = 2000
        mayor = -2000
        media = 0
        for i in range(1, a + 1):
            tmp_output += [f"Escriba el número {i}: "]
            c = random.randrange(-10000, 10001) / 10
            tmp_input += [c]
            if c < menor:
                menor = c
            if c > mayor:
                mayor = c
            media += c
        media /= a
        tmp_output += [f"El número más pequeño de los introducidos es {float(menor)}"]
        tmp_output += [f"El número más grande de los introducidos es {float(mayor)}"]
        tmp_output += [f"La media de los números introducidos es {media}"]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 91 END

    elif exercise_id == 92:
        # Exercise 92 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html

        # Negativo
        a = -random.randrange(1, 101)
        mpts_common.add_test(
            [a],
            [],
            [
                "FACTORIAL",
                "Escriba un número entero mayor que cero: ",
                "¡Le he pedido un número entero mayor que cero!",
            ],
            NOT_LAST_TEST,
        )

        # Cero
        a = 0
        mpts_common.add_test(
            [a],
            [],
            [
                "FACTORIAL",
                "Escriba un número entero mayor que cero: ",
                "¡Le he pedido un número entero mayor que cero!",
            ],
            NOT_LAST_TEST,
        )

        # Uno
        a = 1
        b = 1
        tmp_input = [a]
        tmp_output = [
            "FACTORIAL",
            "Escriba un número entero mayor que cero: ",
            f"El factorial de {a} es {b}.",
        ]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Factorial pequeño
        a = random.randrange(2, 20)
        b = 1
        for i in range(2, a + 1):
            b *= i
        tmp_input = [a]
        tmp_output = [
            "FACTORIAL",
            "Escriba un número entero mayor que cero: ",
            f"El factorial de {a} es {b}.",
        ]
        mpts_common.add_test(tmp_input, [], tmp_output, NOT_LAST_TEST)

        # Factorial grande
        a = random.randrange(20, 41)
        b = 1
        for i in range(2, a + 1):
            b *= i
        tmp_input = [a]
        tmp_output = [
            "FACTORIAL",
            "Escriba un número entero mayor que cero: ",
            f"El factorial de {a} es {b}.",
        ]
        mpts_common.add_test(tmp_input, [], tmp_output, LAST_TEST)

        # Exercise 92 END
