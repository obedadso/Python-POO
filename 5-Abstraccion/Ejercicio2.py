
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamiento
        self.__edad = edad

    @abstractmethod
    def calcular_salario(self):
        pass
    
    def mostrar_informacion(self):  # Método común (abstracción)
        return f"Empleado: {self.__nombre}, Edad: {self.__edad}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, edad, salario_mensual):
        super().__init__(nombre, edad) # Herencia
        self.__salario_mensual = salario_mensual

    def calcular_salario(self):  # Polimorfismo
        return self.__salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, edad) # Herencia
        self.__horas_trabajadas = horas_trabajadas
        self.__tarifa_hora = tarifa_hora

    def calcular_salario(self):   # Polimorfismo
        return self.__horas_trabajadas * self.__tarifa_hora

# Uso de las clases
empleado_tc = EmpleadoTiempoCompleto("Lilibeth", 27, 65000)
empleado_ph = EmpleadoPorHoras("Saireth", 20, 8000, 7)

print(empleado_tc.mostrar_informacion())
print(f"(Salario Tiempo Completo): {empleado_tc.calcular_salario()}")

print(empleado_ph.mostrar_informacion())
print(f"(Salario Por Horas): {empleado_ph.calcular_salario()}")