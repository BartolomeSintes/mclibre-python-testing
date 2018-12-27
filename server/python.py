#!/usr/bin/python
# -*- coding: utf-8 -*-
# enable debugging
from __future__ import print_function
import cgitb
import random
cgitb.enable()

def imprime_principio():
    print("{")
    print("  \"tests\": [")

def imprime_caso(entrada, salida, coma):
    print("    {")
    print("       \"input\" : [", end="")
    for i in range(len(entrada)-1):
        print(entrada[i], end="")
        print(", ", end="")
    print(entrada[-1], end="")
    print("],")
    print("       \"output\" : [", end="")
    for i in range(len(salida)-1):
        print("\""+salida[i]+"\", ", end="")
    print("\""+salida[-1]+"\"", end="")
    print("]")
    if coma:
        print("    },")
    else:
        print("    }")

def imprime_final():
    print(" ]")
    print("}")

print("Content-Type: 'application/json; charset=utf-8'\n")
print()
imprime_principio()

fecha = 4*random.randrange(400, 600) + 1
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" no es un año bisiesto."], True)

fecha = 4*random.randrange(400, 600) + 2
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" no es un año bisiesto."], True)

fecha = 4*random.randrange(400, 600) + 3
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" no es un año bisiesto."], True)

# Múltiplo de 400: No es bisisesto
fecha = 400*random.randrange(1, 7)
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" es un año bisiesto porque es múltiplo de 400."], True)

# Múltiplo de 100 que no es múltiplo de 400: Es bisisesto
fecha = 400*random.randrange(1, 5) + 100*random.randrange(1, 4)
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400."], True)

#Múltiplo de 4 que no es múltiplo de 100: Es bisiesto
fecha = 100*random.randrange(10, 25) + 4*random.randrange(1, 20)
imprime_caso([fecha], ["COMPROBADOR DE AÑOS BISIESTOS", "Escriba un año y le diré si es bisiesto: ", "El año "+str(fecha)+" es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100."], False)

imprime_final()
