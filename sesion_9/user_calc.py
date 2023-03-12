from calculadora import * ## Importamos todas los objetos que declaremos en el archivo utils

if __name__ == "__main__":

    using = True
    print("Bienvenido a tu primera calculadora hecha en Python!")
    calculadora = Calculadora(120, True, "gris")

    while using == True:
        print("¿Qué operación quieres realizar?")
        print("1. Suma de dos números")
        print("2. Producto de dos números")
        print("3. División de dos números")
        print("4. Decir si un número es primo")
        print("5. Calcular el factorial de un número")
        print("6. Calcular una anualidad en valor presente")

        selection = int(input("Ingresa la opción deseada"))

        if selection == 1:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result = calculadora.suma(x, y)
            print(f"La suma de {x} con {y} es igual a {result}")
        elif selection == 2:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result =  calculadora.producto(x, y)
            print(f"El producto de {x} con {y} es igual a {result}")
        elif selection == 3:
            x = float(input("Ingresa un número... "))
            y = float(input("Ingresa otro número... "))
            result = calculadora.division(x, y)
            print(f"La division de {x} entre {y} es igual a {result}")
        elif selection == 5:
            n = int(input("Ingresa un número"))
            result = calculadora.factorial(n)
            print(f"El factorial de {n} es {result}")
        elif selection == 6:
            n = int(input("Cuantos periodos contemplra la anualidad"))
            i = float(input("Qué tasa de interés quieres? "))
            a_n = (1 - (1/(1+i)) ** n )/ i
            
            print(f"El valor presente de la anualidad es {a_n}")
            
        else:
            print("La opción que ingresaste no está disponible")

        answer = int(input("¿Quieres realizar otra operación?  \n 1. Sí \n 2. No"))
        if answer == 1:
            using = True
        else:
            using = False

    print("Gracias por utilizar esta calculadora, hasta pronto!")