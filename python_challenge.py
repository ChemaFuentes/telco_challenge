class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento='Data', puesto='Analyst'):
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

"""
La variable nombre es una variable de alcance global definida en el cuerpo del programa.
La variable self.nombre es una propiedad o variable asociada a un objeto o clase. Esta variable solo existe asociada
a una instancia de un objeto de la clase Persona (o Trabajador, que hereda de la misma) 
"""

persona_3 = Trabajador(nombre, 38)
persona_3.presentation()

my_var_list = ['Andrea', 42, 'Ventas', 'Manager']
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()

my_var_dict = {'nombre': 'Andrea', 'edad': 42, 'departamento': 'Ventas', 'puesto': 'Manager'}
trabajador_3 = Trabajador(**my_var_dict)
trabajador_3.presentation()
