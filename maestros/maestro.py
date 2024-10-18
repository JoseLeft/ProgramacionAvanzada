from usuario.usuario import Usuario
from usuario.utils.roles import Roles

class Maestro(Usuario):
    rfc: str
    sueldo: float
    año_nacimiento: int

    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, año: int, contraseña: str):
        super().__init__(nuemro_de_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Roles.MAESTRO)
        self.rfc=rfc
        self.sueldo=sueldo
        self.año_nacimiento=año

    def mostrar_info_maestro(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        info=f"\n-Numero de control: {self.numero_control}\n-Nombre completo: {nombre_completo}\n-RFC: {self.rfc}\n-Sueldo: {self.sueldo}\n-Rol{self.rol.value}"
        return info