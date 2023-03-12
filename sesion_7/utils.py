
### Definición de la función
def squared(x):
    return x**2

def cubic(x: float) -> float:
    return x**3

def suma(x :float, y: float) -> float:
    return x + y

def producto(x: float, y: float) -> float:
    return x*y

def division(x: float, y: float) -> float:
    return x/y

### Docstring: Documentación de una función, o sea, qué hace la función

def prime_detector(x: int) -> bool:
    """
        This is a funcion for detecting if a given number is prime or not.
    """
    prime_flag = True
    
    for i in range(2, x):
        if x % i == 0:
            prime_flag = False
            break
    
    return prime_flag