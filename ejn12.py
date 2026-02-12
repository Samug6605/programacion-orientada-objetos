class Empleado:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.porcentaje_retencion

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()

    def mostrar_resultados(self):
        print("Salario Bruto: $", self.calcular_salario_bruto())
        print("Retención en la fuente: $", self.calcular_retencion())
        print("Salario Neto: $", self.calcular_salario_neto())


# Programa principal
empleado = Empleado(48, 5000, 0.125)
empleado.mostrar_resultados()
