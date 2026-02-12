class Familia:
    def __init__(self, edad_juan):
        # Atributo
        self.edad_juan = edad_juan

    # Método para calcular la edad de Alberto
    def calcular_edad_alberto(self):
        return (2/3) * self.edad_juan

    # Método para calcular la edad de Ana
    def calcular_edad_ana(self):
        return (4/3) * self.edad_juan

    # Método para calcular la edad de la mamá
    def calcular_edad_mama(self):
        edad_alberto = self.calcular_edad_alberto()
        edad_ana = self.calcular_edad_ana()
        return edad_alberto + self.edad_juan + edad_ana

    # Método para mostrar todas las edades
    def mostrar_edades(self):
        print("Edad de Juan:", self.edad_juan)
        print("Edad de Alberto:", self.calcular_edad_alberto())
        print("Edad de Ana:", self.calcular_edad_ana())
        print("Edad de la mamá:", self.calcular_edad_mama())


# Programa principal
edad = float(input("Ingrese la edad de Juan: "))
familia = Familia(edad)
familia.mostrar_edades()