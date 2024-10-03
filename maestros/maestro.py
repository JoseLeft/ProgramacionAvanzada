from datetime import datetime

class Maestro:

    numero_control: str
    nombre_maestro: str
    apellido: str
    fecha_nacimiento: datetime
    rfc: str 
    sueldo: float

    def __init__(self, numero_control: str, nombre_maestro: str, apellido: str, fecha_nacimiento: datetime, rfc: str, sueldo:float):
        self.numero_control = numero_control
        self.nombre_maestro = nombre_maestro
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre_maestro} {self.apellido}"
        info = f"\n-Numero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, fecha de nacimineto: {self.fecha_nacimiento}, sueldo: {self.sueldo}"      
        return info  