from empleados.utils.roles import Rol
from empleados.empleado import Empleado
from datetime import datetime
from zoo.zoo import Zoologico

class Mantenimiento(Empleado):
    pass

    def __init__(self, 
                 id: str,nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_ingreso: datetime,
                 rfc: str, curp: str, salario: float, horario: datetime):
        super().__init__(id=id,
                         nombre=nombre,
                         apellidos=apellidos,
                         fecha_nacimiento=fecha_nacimiento,
                         fecha_ingreso=fecha_ingreso,
                         rfc=rfc,
                         curp=curp,
                         salario=salario,
                         horario=horario,
                         rol=Rol.MANTENIMIENTO)
        
    def cuidado_animales(self, id_animal: str, proceso: str, observaciones: str = ""):
        fecha_proceso = datetime.now()
        
        registro_proceso = {
            'empleado': f"{self.nombre} {self.apellidos}",
            'id_animal': id_animal,
            'proceso': proceso,
            'fecha': fecha_proceso.strftime("%Y-%m-%d"),
            'observaciones': observaciones
        }
        
        Zoologico.procesos_realizados.append(registro_proceso)

        print(f"Proceso de {proceso} registrado para el animal {id_animal} y realizado por {self.nombre} {self.apellidos}.")