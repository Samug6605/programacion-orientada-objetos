import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio  # Atributo

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_longitud(self):
        return 2 * math.pi * self.radio

    def mostrar_resultados(self):
        print("Radio:", self.radio)
        print("Área del círculo:", self.calcular_area())
        print("Longitud de la circunferencia:", self.calcular_longitud())


# Programa principal
radio_ingresado = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio_ingresado)
circulo.mostrar_resultados()
