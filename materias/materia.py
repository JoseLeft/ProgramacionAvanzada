class Materia:
    
    numero_control: str
    nombre_materia: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, numero_control: str, nombre_materia: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre_materia = nombre_materia
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos

    def mostrar_info_materia(self):
        info = f"\n-Numero de control: {self.numero_control}, nombre de la materia: {self.nombre_materia}, semestre: {self.semestre}, creditos: {self.creditos}, descripción: {self.descripcion}"      
        return info  