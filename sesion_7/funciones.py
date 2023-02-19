### Funciones

### Definición de la función
def squared(x: float) -> float:
    return x**2

def cubic(x: float) -> float:
    return x**3

if __name__ == "__main__":
    number = int(input("Ingresa un número por favor"))
    result = squared(number)
    print(f"El cuadrado de {number} es igual a {result}")
    cubo = cubic(number)
    print(f"El cubo de {number} es igual a {cubo}")