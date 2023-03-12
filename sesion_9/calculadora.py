"""
    Clase calculadora que nos permite hacer varias cosas divertidas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Calculadora:
    """
        Esto es una calculadora que nos permitirá realizar diferentes 
        operaciones
    """
    def __init__(self, memoria, pantalla, color):
        """
            Este es el constructos
        """
        self.memoria = memoria
        self.pantalla = pantalla
        self.color = color
        self.prohibido = 0
        plt.style.use("ggplot")

    def suma(self, x, y):
        return x + y

    def producto(self, x, y):
        return x*y

    def division(self, x, y):
        if y != self.prohibido:
            return x/y
        else:
            print("No es válida la división por cero")

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)

    def fibonacci(self, n):
        fibo = [1, 1]
        
        for i in range(2, n):
            fib = fibo[i-1] + fibo[i-2]
            fibo.append(fib)
            
        return fibo[n-1]

    def graficar(self, function, dominio):
        if self.pantalla == False:
            print("Lo siento no tengo la tecnología para graficar")
        else:
            imagen = [function(x) for x in dominio]
            plt.plot(dominio, imagen)
            plt.show()

    def pricing_transportacion(self, origen, contenedor, linea):
        pass
    def read_excel(self, path):
        return pd.read_excel(
            path
        )