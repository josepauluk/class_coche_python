'''En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    Color
    Ruedas
    Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
    Velocidad
    Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
'''

class Vehículo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehículo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (f'Color: {self.color}\n'
                f'Ruedas: {self.ruedas}\n'
                f'Puertas: {self.puertas}\n'
                f'Velocidad: {self.velocidad}\n'
                f'Cilindrada: {self.cilindrada}')

coche = Coche('champagne', 4, 4, 180, 3000)
print(coche)
