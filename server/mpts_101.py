import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 1011:
        # Exercise 1011 BEGINNING

        # Del 1 al 6
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, 2, 3, 4]],
            ["output", ["MPTC (1)", "1", "2", "3", "4"]],
        )
        mpts_common.add_test(
            LAST_TEST,
            ["input", [1, 2, 3, 4]],
            ["output", ["MPTC (1)", "1", "2", "3", "4"]],
        )

        # Exercise 1011 END

    elif exercise_id == 1012:
        # Exercise 1012 BEGINNING

        # Del 1 al 6
        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [1, 2, 3, 4]],
            ["output", ["MPTC (1)", "1", "2", "3", "5"]],
        )
        mpts_common.add_test(
            LAST_TEST,
            ["input", [1, 2, 3, 4]],
            ["output", ["MPTC (1)", "1", "2", "3", "4"]],
        )

        # Exercise 1012 END

    elif exercise_id == 1013:
        # Exercise 1013 BEGINNING

        # Del 1 al 6
        mpts_common.add_test(
            LAST_TEST, ["input", [3.5, 0, 0]], ["output", ["MPTC (1)", "Duración: 3.5"]]
        )

        # Exercise 1013 END

    elif exercise_id == 1014:
        # Exercise 1014 BEGINNING

        # Test mptc 0.24
        mpts_common.add_test(
            LAST_TEST,
            ["input", ["Barto"]],
            ["output", ["Díme tu nombre: ", "Tu nombre es Barto."]],
        )

        # Exercise 1014 END

    elif exercise_id == 1015:
        # Exercise 1014 BEGINNING

        # Test mptc 0.23
        mpts_common.add_test(NOT_LAST_TEST, ["input", [2]], ["output", ["0.5"]])
        mpts_common.add_test(LAST_TEST, ["input", [0]], ["output", ["0"]])

        # Exercise 1015 END
