from utils import *

if __name__ == "__main__":
    using = True
    print("Bienvenido a tu primera calculadora hecha en Python!")
    range_values = range(1, 10000)

    for i in range(1, 10000):
        print("¿Qué operación quieres realizar?")
        print("1. Suma de dos números")
        print("2. Producto de dos números")
        print("3. División de dos números")
        print("4. Decir si un número es primo")
        print("5. Calcular el factorial de un número")

        selection = int(input("Ingresa la opción deseada"))


        if selection == 1:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result = suma(x, y)
            print(f"La suma de {x} con {y} es igual a {result}")
        elif selection == 2:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result = producto(x, y)
            print(f"El producto de {x} con {y} es igual a {result}")
        elif selection == 3:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result = division(x, y)
            print(f"La division de {x} entre {y} es igual a {result}")
        elif selection == 4:
            x = int(input("Ingresa un número... "))
            result = prime_detector(x)
            if result == True:
                print(f"El número {x} es primo")
            else:
                print(f"El número {x} no es primo")
        elif selection == 5:
            ## factorial
            pass
        else:
            print("La opción que ingresaste no está disponible")

        answer = int(input("¿Quieres realizar otra operación?  \n 1. Sí \n 2. No"))

        if answer == 1:
            continue
        else:
            break

    print("Gracias por utilizar esta calculadora, hasta pronto!")