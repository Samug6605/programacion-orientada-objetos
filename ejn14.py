class Numero:
    def __init__(self, valor):
        self.valor = valor  # Atributo

    def calcular_cuadrado(self):
        return self.valor ** 2

    def calcular_cubo(self):
        return self.valor ** 3

    def mostrar_resultados(self):
        print("Número ingresado:", self.valor)
        print("Cuadrado:", self.calcular_cuadrado())
        print("Cubo:", self.calcular_cubo())


# Programa principal
numero_ingresado = float(input("Ingrese un número: "))
numero = Numero(numero_ingresado)
numero.mostrar_resultados()
