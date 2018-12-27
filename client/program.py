def main():
    print("COMPROBADOR DE AÑOS BISIESTOS")
    fecha = int(input("Escriba un año y le diré si es bisiesto: "))

    if fecha %4 != 0:
        print(f"El año {fecha} no es un año bisiesto.")
    elif fecha % 100 == 0 and fecha % 400 != 0:
        print(f"El año {fecha} no es un año bisiesto porque es múltiplo de 100 "
              f"sin ser múltiplo de 400.")
#    elif fecha % 4 == 0 and fecha % 100 != 0:
#        print(f"El año {fecha} es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.")
    else:
        print(f"El año {fecha} es un año bisiesto porque es múltiplo de 400.")

if __name__ == '__main__':
    main()
