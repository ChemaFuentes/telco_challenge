class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        Persona.__init__(self, nombre, edad)

        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        super().presentation()
        print(f"Trabajo como {self.puesto} en {self.departamento}")


nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

nombre = 'Chema'
puesto = 'Data Engineer'
departamento = 'IT'
persona_2 = Trabajador(nombre, 38, departamento, puesto)
persona_2.presentation()
