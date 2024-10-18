from usuario.utils.roles import Roles

class Usuario:
    numero_control: str
    nombre: str
    apellido: str
    contraseña: str
    rol: Roles

    def __init__(self, nuemro_de_control: str, nombre: str, apellido: str, contraseña: str, rol: Roles):
        self.numero_control=nuemro_de_control
        self.nombre=nombre
        self.apellido=apellido
        self.contraseña=contraseña
        self.rol=rol