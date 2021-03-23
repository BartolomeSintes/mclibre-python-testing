import mpts_common
import random

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
            "NO"
            "No",
            "nO",
            "no"
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
