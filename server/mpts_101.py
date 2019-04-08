import mpts_common
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):
    if exercise_id == 1011:
        # Exercise 1011 BEGINNING

        # Del 1 al 6
        mpts_common.add_test(
            [1, 2, 3, 4], [], ["MPTC (1)", "1", "2", "3", "4"], NOT_LAST_TEST
        )
        mpts_common.add_test(
            [1, 2, 3, 4], [], ["MPTC (1)", "1", "2", "3", "4"], LAST_TEST
        )

        # Exercise 1011 END

    elif exercise_id == 1012:
        # Exercise 1012 BEGINNING

        # Del 1 al 6
        mpts_common.add_test(
            [1, 2, 3, 4], [], ["MPTC (1)", "1", "2", "3", "5"], NOT_LAST_TEST
        )
        mpts_common.add_test(
            [1, 2, 3, 4], [], ["MPTC (1)", "1", "2", "3", "4"], LAST_TEST
        )

        # Exercise 1012 END

    elif exercise_id == 1013:
        # Exercise 1013 BEGINNING

        # Del 1 al 6
        mpts_common.add_test([3.5, 0, 0], [], ["MPTC (1)", "Duración: 3.5"], LAST_TEST)

        # Exercise 1013 END

    elif exercise_id == 1014:
        # Exercise 1014 BEGINNING

        # Test mptc 0.24
        mpts_common.add_test(
            ["Barto"], [], ["Díme tu nombre: ", "Tu nombre es Barto."], LAST_TEST
        )

        # Exercise 1014 END

    elif exercise_id == 1015:
        # Exercise 1014 BEGINNING

        # Test mptc 0.23
        mpts_common.add_test([2], [], ["0.5"], NOT_LAST_TEST)
        mpts_common.add_test([0], [], ["0"], LAST_TEST)

        # Exercise 1015 END
