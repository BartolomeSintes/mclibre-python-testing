import random

NOT_LAST_TEST = True
LAST_TEST = False


def add_test(input, output, comma):
    print("    {")
    print('       "input" : [', end="")
    for i in range(len(input) - 1):
        print(input[i], end="")
        print(", ", end="")
    print(input[-1], end="")
    print("],")
    print('       "output" : [', end="")
    for i in range(len(output) - 1):
        print('"' + output[i] + '", ', end="")
    print('"' + output[-1] + '"', end="")
    print("]")
    if comma:
        print("    },")
    else:
        print("    }")


def exercise(exercise_id):
    if exercise_id == 1:
        # Exercise 1 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # envía dos números enteros positivos
        numero_1 = random.randrange(0, 20)
        numero_2 = random.randrange(0, 20)
        resultado = (numero_1 + numero_2) / 2
        add_test(
            [numero_1, numero_2],
            [
                "CÁLCULO DE LA MEDIA DE DOS NÚMEROS",
                "Escriba un número: ",
                "Escriba otro número: ",
                f"La media aritmética de {str(float(numero_1))} y {str(float(numero_2))} es {str(resultado)}",
            ],
            NOT_LAST_TEST,
        )

        # envía dos números enteros negativos
        numero_1 = random.randrange(-21, 0)
        numero_2 = random.randrange(-21, 0)
        resultado = (numero_1 + numero_2) / 2
        add_test(
            [numero_1, numero_2],
            [
                "CÁLCULO DE LA MEDIA DE DOS NÚMEROS",
                "Escriba un número: ",
                "Escriba otro número: ",
                f"La media aritmética de {str(float(numero_1))} y {str(float(numero_2))} es {str(resultado)}",
            ],
            NOT_LAST_TEST,
        )

        # envía dos números decimales positivos
        numero_1 = random.randrange(0, 100) / 10.0
        numero_2 = random.randrange(0, 100) / 10.0
        resultado = (numero_1 + numero_2) / 2
        add_test(
            [numero_1, numero_2],
            [
                "CÁLCULO DE LA MEDIA DE DOS NÚMEROS",
                "Escriba un número: ",
                "Escriba otro número: ",
                f"La media aritmética de {str(float(numero_1))} y {str(float(numero_2))} es {str(resultado)}",
            ],
            LAST_TEST,
        )
        # Exercise 1 END

    elif exercise_id == 2:
        # Exercise 2 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # imc bajo
        imc = random.randrange(150, 200) / 10.0
        altura = random.randrange(60, 200) / 100.0
        peso = round(imc * altura ** 2)
        imc = round(peso / altura ** 2, 1)

        add_test(
            [peso, altura],
            [
                "CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)",
                "¿Cuánto pesa? ",
                "¿Cuánto mide en metros? ",
                f"Su imc es {imc}",
                "Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,",
                "pero esos límites dependen de la edad, del sexo, de la constitución física, etc.",
            ],
            NOT_LAST_TEST,
        )
        # imc medio
        imc = random.randrange(200, 250) / 10.0
        altura = random.randrange(60, 200) / 100.0
        peso = round(imc * altura ** 2)
        imc = round(peso / altura ** 2, 1)

        add_test(
            [peso, altura],
            [
                "CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)",
                "¿Cuánto pesa? ",
                "¿Cuánto mide en metros? ",
                f"Su imc es {imc}",
                "Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,",
                "pero esos límites dependen de la edad, del sexo, de la constitución física, etc.",
            ],
            NOT_LAST_TEST,
        )
        # imc alto
        imc = random.randrange(250, 400) / 10.0
        altura = random.randrange(60, 200) / 100.0
        peso = round(imc * altura ** 2)
        imc = round(peso / altura ** 2, 1)

        add_test(
            [peso, altura],
            [
                "CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)",
                "¿Cuánto pesa? ",
                "¿Cuánto mide en metros? ",
                f"Su imc es {imc}",
                "Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,",
                "pero esos límites dependen de la edad, del sexo, de la constitución física, etc.",
            ],
            LAST_TEST,
        )
        # Exercise 2 END
