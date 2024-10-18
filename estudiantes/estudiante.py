from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Roles

class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime
    

    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contraseña: str):
        super().__init__(nuemro_de_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Roles.ESTUDIANTE)
        self.curp=curp
        self.fecha_nacimiento=fecha_nacimiento

    def mostrar_info_estudiante(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        info=f"\n-Numero de control: {self.numero_control}\n-Nombre completo: {nombre_completo}\n-CURP: {self.curp}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Rol: {self.rol.value}"
        return info