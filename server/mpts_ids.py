valid_exercise_ids = [
    # EJERCICIOS DE CLASE
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-variables.html
    [1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-1.html
    [2, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-2.html
    [3, [31, 32, 33, 34]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-if-else-minijuegos.html
    [5, [51, 52, 53, 54, 55]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-range.html
    [6, [61, 62, 63, 64, 65, 66, 67, 68, 69]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-for-minijuegos.html
    [7, [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-for-1.html
    [8, [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-for-2.html
    [9, [93, 94, 95, 96, 97, 98]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-while-2.html
    [10, [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-while-3.html
    [11, [111, 112, 113, 114, 115]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-while-3.html
    [12, [120, 121, 122]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-sucesiones.html
    [13, [131, 132]],
    #
    # https://www.mclibre.org/consultar/python/ejercicios/ej-while-1.html
    [14, [141, 142, 143, 144, 145, 146, 147, 148, 149, 150]],
    #
    # EJEMPLOS DE USO DE MPTC
    #
    # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html
    [100, [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]],
    #
    # https://www.mclibre.org/consultar/python/otros/python-testing-ejemplos.html
    [101, [1011, 1012, 1013, 1014, 1015]],
    #
    # Ejemplos de programas incorrectos para ver qué dice MPTC
    [102, [1021, 1022, 1023, 1024]],
    #
    #
    # EXÁMENES
    #
    # /examenes/11-12/examen-120601-2.html
    [1112, [111221]],
    #
    # /examenes/11-12/examen-120607.html
    [1112, [111231]],
    #
    # /examenes/12-13/examen-130129.html
    [1213, [121311, 121312, 121313]],
    #
    # /examenes/12-13/examen-140307.html
    [1314, [131422]],
    #
    # /examenes/14-15/examen-150520.html
    [1415, [141511]],
    #
    # /examenes/14-15/examen-150525.html
    [1415, [141521, 141522]],
    #
    # /examenes/15-16/examen-160525.html
    [1516, [151611, 151612]],
    #
    # /examenes/15-16/examen-160608.html
    [1516, [151621, 151622]],
    #
    # /examenes/15-16/examen-160628.html
    [1516, [151631]],
    #
    # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170224.html
    [1617, [161711, 161712, 161713]],
    #
    # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170505.html
    [1617, [161721, 161722, 161723]],
    #
    # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170606.html
    [1617, [161731, 161732, 161733]],
    #
    # https://www.mclibre.org/consultar/python/examenes/16-17/examen-170628.html
    [1617, [161741, 161742]],
    #
    # https://www.mclibre.org/consultar/python/examenes/17-18/examen-180228.html
    [1718, [171811, 171812, 171813]],
    #
    # https://www.mclibre.org/consultar/python/examenes/17-18/examen-180523.html
    [1718, [171821, 171822, 171823]],
    #
    # https://www.mclibre.org/consultar/python/examenes/17-18/examen-180606.html
    [1718, [171831, 171832, 171833]],
    #
    # https://www.mclibre.org/consultar/python/examenes/17-18/examen-180625.html
    [1718, [171841, 171842]],
    #
    # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190225.html
    [1819, [181911, 181912, 181913, 181914]],
    #
    # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190521.html
    [1819, [181921, 181922, 181923]],
    #
    # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190530.html
    [1819, [181931, 181932, 181933]],
    #
    # https://www.mclibre.org/consultar/python/examenes/18-19/examen-190618.html
    [1819, [181941, 181942]],
    #
    # https://www.mclibre.org/consultar/python/examenes/19-20/examen-200221.html
    [1920, [192011, 192012, 192013, 192014]],
    #
    # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210519.html
    [2021, [202111, 202112, 202113]],
    #
    # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210526.html
    [2021, [202122, 202123]],
    #
    # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210602.html
    [2021, [202131, 202132, 202133]],
    #
    # https://www.mclibre.org/consultar/python/examenes/20-21/examen-210622.html
    [2021, [202141, 202142, 202143]],
    #
    # https://www.mclibre.org/consultar/python/examenes/21-22/examen-220517.html
    [2122, [212211, 212212, 212213]],
    #
    # https://www.mclibre.org/consultar/python/examenes/21-22/examen-220623.html
    [2122, [212221, 212222]],
]
