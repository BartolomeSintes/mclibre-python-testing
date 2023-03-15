import random
import mpts_common

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 141:
        # Exercise 141 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        sigue = ["sí"]
        acaba = [
            "SI",
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "S",
            "s",
            "NO",
            "No",
            "nO",
            "no",
            "N",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA sí PARA CONTINUAR"]
        for _ in range(n):
            tmp_input += [sigue[0]]
            tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        tmp_input = []
        tmp_output = ["DIGA sí PARA CONTINUAR"]
        tmp_input += [sigue[0]]
        tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # variantes acaba
        for i in acaba[0:9]:
            tmp_input = []
            tmp_output = ["DIGA sí PARA CONTINUAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA sí PARA CONTINUAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA sí PARA CONTINUAR"]
        tmp_input += [random.choice(acaba[9:])]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 141 END

    elif exercise_id == 142:
        # Exercise 142 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        acaba = ["SI"]
        sigue = [
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "sí",
            "S",
            "s",
            "NO",
            "No",
            "nO",
            "no",
            "N",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA SI PARA TERMINAR"]
        for _ in range(n):
            tmp_input += [random.choice(sigue)]
            tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        tmp_input = []
        tmp_output = ["DIGA SI PARA TERMINAR"]
        tmp_input += [random.choice(sigue)]
        tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # variantes sigue
        tmp_input = []
        tmp_output = ["DIGA SI PARA TERMINAR"]
        for i in sigue[0:9]:
            tmp_input += [i]
            tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA SI PARA TERMINAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA SI PARA TERMINAR"]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 142 END

    elif exercise_id == 143:
        # Exercise 143 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        sigue = ["N"]
        acaba = [
            "SI",
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "sí",
            "S",
            "s",
            "NO",
            "No",
            "nO",
            "no",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA N PARA CONTINUAR"]
        for _ in range(n):
            tmp_input += [sigue[0]]
            tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        tmp_input = []
        tmp_output = ["DIGA N PARA CONTINUAR"]
        tmp_input += [sigue[0]]
        tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # variantes acaba
        for i in acaba[10:15]:
            tmp_input = []
            tmp_output = ["DIGA N PARA CONTINUAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA N PARA CONTINUAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA N PARA CONTINUAR"]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 143 END

    elif exercise_id == 144:
        # Exercise 144 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        acaba = ["no"]
        sigue = [
            "SI",
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "sí",
            "S",
            "s",
            "NO",
            "No",
            "nO",
            "N",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA no PARA TERMINAR"]
        for _ in range(n):
            tmp_input += [random.choice(sigue)]
            tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        tmp_input = []
        tmp_output = ["DIGA no PARA TERMINAR"]
        tmp_input += [random.choice(sigue)]
        tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # variantes sigue
        tmp_input = []
        tmp_output = ["DIGA no PARA TERMINAR"]
        for i in sigue[10:15]:
            tmp_input += [i]
            tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA no PARA TERMINAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA no PARA TERMINAR"]
        tmp_input += [acaba[0]]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 144 END

    elif exercise_id == 145:
        # Exercise 145 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        sigue = ["S", "s"]
        acaba = [
            "SI",
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "sí",
            "NO",
            "No",
            "nO",
            "no",
            "N",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA S O s PARA CONTINUAR"]
        for _ in range(n):
            tmp_input += [random.choice(sigue)]
            tmp_output += ["¿Desea continuar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        for i in sigue:
            tmp_input = []
            tmp_output = ["DIGA S O s PARA CONTINUAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea continuar el programa?: "]
            tmp_input += [random.choice(acaba)]
            tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # variantes acaba
        for i in acaba[0:8]:
            tmp_input = []
            tmp_output = ["DIGA S O s PARA CONTINUAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA S O s PARA CONTINUAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA S O s PARA CONTINUAR"]
        tmp_input += [random.choice(acaba[8:])]
        tmp_output += ["¿Desea continuar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 145 END

    elif exercise_id == 146:
        # Exercise 146 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        acaba = ["S", "s"]
        sigue = [
            "SI",
            "SÍ",
            "Si",
            "Sí",
            "sI",
            "sÍ",
            "si",
            "sí",
            "NO",
            "No",
            "nO",
            "no",
            "N",
            "n",
            "puede",
            "tal vez",
            "",
            " ",
        ]

        # varios sigue
        n = random.randrange(4, 11)
        tmp_input = []
        tmp_output = ["DIGA S O s PARA TERMINAR"]
        for _ in range(n):
            tmp_input += [random.choice(sigue)]
            tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # un solo sigue
        for i in sigue[0:8]:
            tmp_input = []
            tmp_output = ["DIGA S O s PARA TERMINAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea terminar el programa?: "]
            tmp_input += [random.choice(acaba)]
            tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # variantes acaba
        for i in acaba:
            tmp_input = []
            tmp_output = ["DIGA S O s PARA TERMINAR"]
            tmp_input += [i]
            tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
            mpts_common.add_test(
                NOT_LAST_TEST,
                ["input", tmp_input],
                ["output", tmp_output],
            )

        # Vacío
        tmp_input = []
        tmp_output = ["DIGA S O s PARA TERMINAR"]
        tmp_input += [""]
        tmp_output += ["¿Desea terminar el programa?: "]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ningún sigue
        tmp_input = []
        tmp_output = ["DIGA S O s PARA TERMINAR"]
        tmp_input += [random.choice(acaba)]
        tmp_output += ["¿Desea terminar el programa?: ", "¡Hasta la vista!"]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 146 END

    elif exercise_id == 147:
        # Exercise 147 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # contraseñas iguales a la primera
        longitud = random.randrange(6, 20)
        cadena = mpts_common.genera_string(longitud)
        tmp_input = [cadena, cadena]
        tmp_output = [
            "CONFIRME SU CONTRASEÑA",
            "Escriba su contraseña: ",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # una vez contraseñas distintas
        longitud = random.randrange(6, 20)
        cadena_1 = mpts_common.genera_string(longitud)
        cadena_2 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_2:
            cadena_2 = mpts_common.genera_string(longitud)
        tmp_input = [cadena_1, cadena_2]
        tmp_output = ["CONFIRME SU CONTRASEÑA"]
        tmp_output += [
            "Escriba su contraseña: ",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
        ]
        cadena = mpts_common.genera_string(longitud)
        tmp_input += [cadena, cadena]
        tmp_output += [
            "Escriba su contraseña: ",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varias veces contraseñas distintas
        n = random.randrange(3, 7)
        tmp_input = []
        for _ in range(n):
            longitud = random.randrange(6, 20)
            cadena_1 = mpts_common.genera_string(longitud)
            cadena_2 = mpts_common.genera_string(longitud)
            while cadena_1 == cadena_2:
                cadena_2 = mpts_common.genera_string(longitud)
            tmp_input += [cadena_1, cadena_2]
        cadena = mpts_common.genera_string(longitud)
        tmp_input += [cadena, cadena]
        tmp_output = ["CONFIRME SU CONTRASEÑA"]
        for _ in range(n):
            tmp_output += [
                "Escriba su contraseña: ",
                "Escriba de nuevo su contraseña: ",
                "Las contraseñas no coinciden. Inténtelo de nuevo.",
            ]
        tmp_output += [
            "Escriba su contraseña: ",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 147 END

    elif exercise_id == 148:
        # Exercise 148 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # ahorro cero
        objetivo = 0.0
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA",
            "¿Cuántos euros quiere ahorrar?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # objetivo superado a la primera
        objetivo = float(random.randrange(1, 100))
        ahorrado = float(objetivo + random.randrange(1, 10))
        tmp_input = [objetivo, ahorrado]
        tmp_output = [
            "HUCHA",
            "¿Cuántos euros quiere ahorrar?: ",
            "¿Cuántos euros quiere meter en la hucha?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # objetivo igualado a la primera
        objetivo = float(random.randrange(1, 100))
        ahorrado = float(objetivo)
        tmp_input = [objetivo, ahorrado]
        tmp_output = [
            "HUCHA",
            "¿Cuántos euros quiere ahorrar?: ",
            "¿Cuántos euros quiere meter en la hucha?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros hasta superar el objetivo
        objetivo = float(random.randrange(100, 1000))
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA",
            "¿Cuántos euros quiere ahorrar?: ",
        ]
        ahorrado = 0
        while ahorrado < objetivo:
            ahorro = float(random.randrange(1, 50))
            # para asegurarse de que ahorrado > objetivo
            if ahorro + ahorrado == objetivo:
                ahorro += float(random.randrange(1, 10))
            ahorrado += ahorro
            tmp_input += [ahorro]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
        tmp_output += [
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros hasta igualar el objetivo
        objetivo = float(random.randrange(100, 1000))
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA",
            "¿Cuántos euros quiere ahorrar?: ",
        ]
        ahorrado = 0
        while ahorrado < objetivo:
            ahorro = float(random.randrange(1, 50))
            # para asegurarse de que ahorrado == objetivo
            if ahorro + ahorrado > objetivo:
                ahorro = objetivo - ahorrado
            ahorrado += ahorro
            tmp_input += [ahorro]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
        tmp_output += [
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 148 END

    elif exercise_id == 149:
        # Exercise 149 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # ahorro cero
        objetivo = 0.0
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # ahorro negativo y luego cero
        objetivo = -float(random.randrange(1, 100))
        tmp_input = [objetivo]
        objetivo = 0.0
        tmp_input += [objetivo]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
            "Por favor, escriba una cantidad positiva.",
            "¿Cuántos euros quiere ahorrar?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros negativos y luego cero
        tmp_input = []
        tmp_output = ["HUCHA MEJORADA"]
        for i in range(random.randrange(2, 6)):
            objetivo = -float(random.randrange(1, 100))
            tmp_input += [objetivo]
            tmp_output += [
                "¿Cuántos euros quiere ahorrar?: ",
                "Por favor, escriba una cantidad positiva.",
            ]
        objetivo = 0.0
        tmp_input += [objetivo]
        tmp_output += [
            "¿Cuántos euros quiere ahorrar?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # objetivo superado a la primera
        objetivo = float(random.randrange(1, 100))
        ahorrado = float(objetivo + random.randrange(1, 10))
        tmp_input = [objetivo, ahorrado]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
            "¿Cuántos euros quiere meter en la hucha?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros negativos y luego objetivo superado a la primera
        tmp_input = []
        tmp_output = ["HUCHA MEJORADA"]
        for i in range(random.randrange(2, 6)):
            objetivo = -float(random.randrange(1, 100))
            tmp_input += [objetivo]
            tmp_output += [
                "¿Cuántos euros quiere ahorrar?: ",
                "Por favor, escriba una cantidad positiva.",
            ]
        objetivo = float(random.randrange(1, 100))
        ahorrado = float(objetivo + random.randrange(1, 10))
        tmp_input += [objetivo, ahorrado]
        tmp_output += [
            "¿Cuántos euros quiere ahorrar?: ",
            "¿Cuántos euros quiere meter en la hucha?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # objetivo igualado a la primera
        objetivo = float(random.randrange(1, 100))
        ahorrado = float(objetivo)
        tmp_input = [objetivo, ahorrado]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
            "¿Cuántos euros quiere meter en la hucha?: ",
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros hasta superar el objetivo
        objetivo = float(random.randrange(100, 1000))
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
        ]
        ahorrado = 0
        while ahorrado < objetivo:
            ahorro = float(random.randrange(1, 50))
            # para asegurarse de que ahorrado > objetivo
            if ahorro + ahorrado == objetivo:
                ahorro += float(random.randrange(1, 10))
            ahorrado += ahorro
            tmp_input += [ahorro]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
        tmp_output += [
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros hasta igualar el objetivo
        objetivo = float(random.randrange(100, 1000))
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
        ]
        ahorrado = 0
        while ahorrado < objetivo:
            ahorro = float(random.randrange(1, 50))
            # para asegurarse de que ahorrado == objetivo
            if ahorro + ahorrado > objetivo:
                ahorro = objetivo - ahorrado
            ahorrado += ahorro
            tmp_input += [ahorro]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
        tmp_output += [
            f"¡Objetivo conseguido! Ha ahorrado usted {objetivo} euros.",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # varios ahorros negativos hasta superar el objetivo
        objetivo = float(random.randrange(100, 1000))
        tmp_input = [objetivo]
        tmp_output = [
            "HUCHA MEJORADA",
            "¿Cuántos euros quiere ahorrar?: ",
        ]
        ahorrado = 0
        ahorro = -float(random.randrange(1, 50))
        tmp_input += [ahorro]
        tmp_output += [
            "¿Cuántos euros quiere meter en la hucha?: ",
            "Por favor, escriba una cantidad positiva.",
        ]
        for i in range(3):
            ahorro_positivo = float(random.randrange(1, 5))
            ahorrado += ahorro_positivo
            tmp_input += [ahorro_positivo]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
            for _ in range(random.randrange(2, 6)):
                ahorro = -float(random.randrange(1, 50))
                tmp_input += [ahorro]
                tmp_output += [
                    "¿Cuántos euros quiere meter en la hucha?: ",
                    "Por favor, escriba una cantidad positiva.",
                ]
        while ahorrado < objetivo:
            ahorro = float(random.randrange(1, 50))
            # para asegurarse de que ahorrado > objetivo
            if ahorro + ahorrado == objetivo:
                ahorro += float(random.randrange(1, 10))
            ahorrado += ahorro
            tmp_input += [ahorro]
            tmp_output += ["¿Cuántos euros quiere meter en la hucha?: "]
        tmp_output += [
            f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 149 END

    elif exercise_id == 150:
        # Exercise 50 BEGINNING
        # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html

        # contraseñas iguales a la primera
        longitud = random.randrange(6, 20)
        cadena = mpts_common.genera_string(longitud)
        tmp_input = [cadena, cadena]
        tmp_output = [
            "CONFIRME SU CONTRASEÑA (2)",
            "Escriba su contraseña: ",
            "Tiene 3 intentos para confirmar su contraseña.",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # contraseñas iguales a la segunda
        longitud = random.randrange(6, 20)
        cadena_1 = mpts_common.genera_string(longitud)
        cadena_2 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_2:
            cadena_2 = mpts_common.genera_string(longitud)
        tmp_input = [cadena_1, cadena_2, cadena_1]
        tmp_output = [
            "CONFIRME SU CONTRASEÑA (2)",
            "Escriba su contraseña: ",
            "Tiene 3 intentos para confirmar su contraseña.",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # contraseñas iguales a la tercera
        longitud = random.randrange(6, 20)
        cadena_1 = mpts_common.genera_string(longitud)
        cadena_2 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_2:
            cadena_2 = mpts_common.genera_string(longitud)
        cadena_3 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_3:
            cadena_3 = mpts_common.genera_string(longitud)
        tmp_input = [cadena_1, cadena_2, cadena_3, cadena_1]
        tmp_output = [
            "CONFIRME SU CONTRASEÑA (2)",
            "Escriba su contraseña: ",
            "Tiene 3 intentos para confirmar su contraseña.",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
            "Escriba de nuevo su contraseña: ",
            "Contraseña confirmada. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # contraseñas no iguales a la tercera
        longitud = random.randrange(6, 20)
        cadena_1 = mpts_common.genera_string(longitud)
        cadena_2 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_2:
            cadena_2 = mpts_common.genera_string(longitud)
        cadena_3 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_3:
            cadena_3 = mpts_common.genera_string(longitud)
        cadena_4 = mpts_common.genera_string(longitud)
        while cadena_1 == cadena_4:
            cadena_4 = mpts_common.genera_string(longitud)
        tmp_input = [cadena_1, cadena_2, cadena_3, cadena_4]
        tmp_output = [
            "CONFIRME SU CONTRASEÑA (2)",
            "Escriba su contraseña: ",
            "Tiene 3 intentos para confirmar su contraseña.",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
            "Escriba de nuevo su contraseña: ",
            "Las contraseñas no coinciden. Inténtelo de nuevo.",
            "Escriba de nuevo su contraseña: ",
            "Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!",
        ]
        mpts_common.add_test(
            LAST_TEST,
            ["input", tmp_input],
            ["output", tmp_output],
        )

        # Exercise 150 END
