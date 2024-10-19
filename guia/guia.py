from empleados.empleado import Empleado
from empleados.utils.roles import Rol
from datetime import datetime

class Guia(Empleado):
    
    def __init__(self, id: str, nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, rfc: str, curp: str,
                 salario: float, horario: datetime, rol: Rol.GUIA): 
        super().__init__(id=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_ingreso, rfc=rfc, curp=curp,salario=salario, horario=horario, rol=rol)