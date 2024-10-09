from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre  # Atributo privado (encapsulamiento)
        self.__especialidad = especialidad

    @abstractmethod
    def realizar_tarea(self):
        pass

    def mostrar_informacion(self):  # Método común para todas las subclases (abstracción)
        return f"Empleado: {self.__nombre}- Especialidad: {self.__especialidad}"

class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, especialidad, proyecto):
        super().__init__(nombre, especialidad)
        self.__proyecto = proyecto

    def realizar_tarea(self):  # Implementación específica para Ingeniero (polimorfismo)
        return f"Trabajando en el proyecto: {self.__proyecto}"

class Doctor(TareaEmpleado):
    def __init__(self, nombre, especialidad, pacientes):
        super().__init__(nombre, especialidad)
        self.__pacientes = pacientes

    def realizar_tarea(self):  # Implementación específica para Doctor (polimorfismo)
        return f"Le realizo la operacion a {self.__pacientes} pacientes en este dia."

# Uso de las clases
ingeniero = Ingeniero("Mayra Alvarez", "Ingeniería Industrial", "Mejora de la eficiencia en la linea de produccion de una fabrica de alimentos.")
doctor = Doctor("Edgardo Bonett", "Cirujano", 3)

print(ingeniero.mostrar_informacion())
print(ingeniero.realizar_tarea())

print(doctor.mostrar_informacion())
print(doctor.realizar_tarea())