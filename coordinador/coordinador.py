from usuario.usuario import Usuario
from usuario.utils.roles import Roles

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    años_antiguedad: int

    def __init__(self, nombre: str, apellido: str, numero_control: str, contraseña: str, sueldo: float, rfc: str, años_antiguedad: int):
        super().__init__(nuemro_de_control=numero_control, nombre=nombre, apellido= apellido, contraseña=contraseña, rol=Roles.COORDINADOR)
        self.sueldo=sueldo
        self.rfc=rfc
        self.años_antiguedad=años_antiguedad

    def mostrar_info_coordinador(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        info=f"-Numero de control: {self.numero_control}\n, -Nombre completo: {nombre_completo}\n, -Rol: {self.rol.value}\n"
        return info
    