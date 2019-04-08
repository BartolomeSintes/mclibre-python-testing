import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 1:
        # Exercise 1 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # envía dos números enteros positivos
        numero_1 = random.randrange(0, 20)
        numero_2 = random.randrange(0, 20)
        resultado = (numero_1 + numero_2) / 2
        mpts_common.add_test(
            [numero_1, numero_2],
            [],
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
        mpts_common.add_test(
            [numero_1, numero_2],
            [],
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
        mpts_common.add_test(
            [numero_1, numero_2],
            [],
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

        mpts_common.add_test(
            [peso, altura],
            [],
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

        mpts_common.add_test(
            [peso, altura],
            [],
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

        mpts_common.add_test(
            [peso, altura],
            [],
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

    elif exercise_id == 3:
        # Exercise 3 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        pies = float(random.randrange(0, 10))
        pulgadas = float(random.randrange(0, 10))
        cm = (pies * 12 + pulgadas) * 2.54

        mpts_common.add_test(
            [pies, pulgadas],
            [],
            [
                "CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                "Escriba una cantidad de pulgadas: ",
                f"{pies} pies y {pulgadas} pulgadas son {cm} cm",
            ],
            NOT_LAST_TEST,
        )
        # números medianos decimales
        pies = float(random.randrange(100, 300) / 10)
        pulgadas = float(random.randrange(100, 300) / 10)
        cm = (pies * 12 + pulgadas) * 2.54

        mpts_common.add_test(
            [pies, pulgadas],
            [],
            [
                "CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                "Escriba una cantidad de pulgadas: ",
                f"{pies} pies y {pulgadas} pulgadas son {cm} cm",
            ],
            NOT_LAST_TEST,
        )

        # números grandes
        pies = float(random.randrange(10, 100))
        pulgadas = float(random.randrange(10, 100))
        cm = (pies * 12 + pulgadas) * 2.54

        mpts_common.add_test(
            [pies, pulgadas],
            [],
            [
                "CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                "Escriba una cantidad de pulgadas: ",
                f"{pies} pies y {pulgadas} pulgadas son {cm} cm",
            ],
            LAST_TEST,
        )
        # Exercise 3 END

    elif exercise_id == 4:
        # Exercise 4 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        pulgadas = float(random.randrange(0, 10))
        cm = pulgadas * 2.54

        mpts_common.add_test(
            [pulgadas],
            [],
            [
                "CONVERTIDOR DE PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pulgadas: ",
                f"{pulgadas} pulgadas son {cm} cm",
            ],
            NOT_LAST_TEST,
        )
        # números medianos decimales
        pulgadas = random.randrange(100, 300) / 10
        cm = pulgadas * 2.54

        mpts_common.add_test(
            [pulgadas],
            [],
            [
                "CONVERTIDOR DE PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pulgadas: ",
                f"{pulgadas} pulgadas son {cm} cm",
            ],
            NOT_LAST_TEST,
        )

        # números grandes
        pulgadas = float(random.randrange(10, 100))
        cm = pulgadas * 2.54

        mpts_common.add_test(
            [pulgadas],
            [],
            [
                "CONVERTIDOR DE PULGADAS A CENTÍMETROS",
                "Escriba una cantidad de pulgadas: ",
                f"{pulgadas} pulgadas son {cm} cm",
            ],
            LAST_TEST,
        )
        # Exercise 4 END

    elif exercise_id == 5:
        # Exercise 5 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        pies = float(random.randrange(0, 10))
        cm = pies * 12 * 2.54

        mpts_common.add_test(
            [pies],
            [],
            [
                "CONVERTIDOR DE PIES A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                f"{pies} pies son {cm} cm",
            ],
            NOT_LAST_TEST,
        )
        # números medianos decimales
        pies = random.randrange(100, 300) / 10
        cm = pies * 12 * 2.54

        mpts_common.add_test(
            [pies],
            [],
            [
                "CONVERTIDOR DE PIES A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                f"{pies} pies son {cm} cm",
            ],
            NOT_LAST_TEST,
        )

        # números grandes
        pies = float(random.randrange(10, 100))
        cm = pies * 12 * 2.54

        mpts_common.add_test(
            [pies],
            [],
            [
                "CONVERTIDOR DE PIES A CENTÍMETROS",
                "Escriba una cantidad de pies: ",
                f"{pies} pies son {cm} cm",
            ],
            LAST_TEST,
        )
        # Exercise 5 END

    elif exercise_id == 6:
        # Exercise 6 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        celsius = float(random.randrange(0, 100))
        fahrenheit = round(1.8 * celsius + 32, 1)

        mpts_common.add_test(
            [celsius],
            [],
            [
                "CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT",
                "Escriba una temperatura en grados Celsius: ",
                f"{celsius} ºC son {fahrenheit} ºF",
            ],
            NOT_LAST_TEST,
        )

        # números negativos decimales
        celsius = random.randrange(-27315, 0) / 100
        fahrenheit = round(1.8 * celsius + 32, 1)

        mpts_common.add_test(
            [celsius],
            [],
            [
                "CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT",
                "Escriba una temperatura en grados Celsius: ",
                f"{celsius} ºC son {fahrenheit} ºF",
            ],
            NOT_LAST_TEST,
        )
        # números grandes enteros
        celsius = float(random.randrange(0, 1000))
        fahrenheit = round(1.8 * celsius + 32, 1)

        mpts_common.add_test(
            [celsius],
            [],
            [
                "CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT",
                "Escriba una temperatura en grados Celsius: ",
                f"{celsius} ºC son {fahrenheit} ºF",
            ],
            LAST_TEST,
        )
        # Exercise 6 END

    elif exercise_id == 7:
        # Exercise 7 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        fahrenheit = float(random.randrange(0, 100))
        celsius = (fahrenheit - 32) / 1.8

        mpts_common.add_test(
            [fahrenheit],
            [],
            [
                "CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS",
                "Escriba una temperatura en grados Fahrenheit: ",
                f"{fahrenheit} ºF son {round(celsius, 1)} ºC",
            ],
            NOT_LAST_TEST,
        )

        # números negativos decimales
        fahrenheit = random.randrange(-4597, 0) / 10
        celsius = (fahrenheit - 32) / 1.8

        mpts_common.add_test(
            [fahrenheit],
            [],
            [
                "CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS",
                "Escriba una temperatura en grados Fahrenheit: ",
                f"{fahrenheit} ºF son {round(celsius, 1)} ºC",
            ],
            NOT_LAST_TEST,
        )
        # números grandes enteros
        fahrenheit = float(random.randrange(0, 1000))
        celsius = (fahrenheit - 32) / 1.8

        mpts_common.add_test(
            [fahrenheit],
            [],
            [
                "CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS",
                "Escriba una temperatura en grados Fahrenheit: ",
                f"{fahrenheit} ºF son {round(celsius, 1)} ºC",
            ],
            LAST_TEST,
        )
        # Exercise 7 END

    elif exercise_id == 8:
        # Exercise 8 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        segundos = random.randrange(0, 60)
        minutos = segundos // 60
        resto = segundos % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {minutos} minutos y {resto} segundos",
            ],
            NOT_LAST_TEST,
        )

        # números medianos enteros
        segundos = random.randrange(60, 3600)
        minutos = segundos // 60
        resto = segundos % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {minutos} minutos y {resto} segundos",
            ],
            NOT_LAST_TEST,
        )

        # números grandes enteros
        segundos = random.randrange(3600, 20000)
        minutos = segundos // 60
        resto = segundos % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {minutos} minutos y {resto} segundos",
            ],
            LAST_TEST,
        )
        # Exercise 8 END

    elif exercise_id == 9:
        # Exercise 9 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        segundos = random.randrange(0, 60)

        horas = segundos // 3600
        resto_1 = segundos % 3600
        minutos = resto_1 // 60
        resto = resto_1 % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {horas} horas, {minutos} minutos y {resto} segundos",
            ],
            NOT_LAST_TEST,
        )

        # números medianos enteros
        segundos = random.randrange(60, 3600)

        horas = segundos // 3600
        resto_1 = segundos % 3600
        minutos = resto_1 // 60
        resto = resto_1 % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {horas} horas, {minutos} minutos y {resto} segundos",
            ],
            NOT_LAST_TEST,
        )

        # números grandes enteros
        segundos = random.randrange(3600, 20000)

        horas = segundos // 3600
        resto_1 = segundos % 3600
        minutos = resto_1 // 60
        resto = resto_1 % 60

        mpts_common.add_test(
            [segundos],
            [],
            [
                "CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS",
                "Escriba una cantidad de segundos: ",
                f"{segundos} segundos son {horas} horas, {minutos} minutos y {resto} segundos",
            ],
            LAST_TEST,
        )
        # Exercise 9 END

    elif exercise_id == 10:
        # Exercise 10 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # números pequeños enteros
        unidades = random.randrange(0, 12)

        gruesas = unidades // 144
        docenas = unidades % 144 // 12
        resto = unidades % 12

        mpts_common.add_test(
            [unidades],
            [],
            [
                "CONVERTIDOR A GRUESAS Y DOCENAS",
                "Escriba una cantidad (entera): ",
                f"{unidades} unidades son {gruesas} gruesas, {docenas} docenas y {resto} unidades",
            ],
            NOT_LAST_TEST,
        )

        # números medianos enteros
        unidades = random.randrange(12, 144)

        gruesas = unidades // 144
        docenas = unidades % 144 // 12
        resto = unidades % 12

        mpts_common.add_test(
            [unidades],
            [],
            [
                "CONVERTIDOR A GRUESAS Y DOCENAS",
                "Escriba una cantidad (entera): ",
                f"{unidades} unidades son {gruesas} gruesas, {docenas} docenas y {resto} unidades",
            ],
            NOT_LAST_TEST,
        )

        # números grandes enteros
        unidades = random.randrange(144, 1000)

        gruesas = unidades // 144
        docenas = unidades % 144 // 12
        resto = unidades % 12

        mpts_common.add_test(
            [unidades],
            [],
            [
                "CONVERTIDOR A GRUESAS Y DOCENAS",
                "Escriba una cantidad (entera): ",
                f"{unidades} unidades son {gruesas} gruesas, {docenas} docenas y {resto} unidades",
            ],
            LAST_TEST,
        )
        # Exercise 10 END
