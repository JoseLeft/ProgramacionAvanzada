from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    matricula_carrera: str
    materias: List[Materia] = []
    grupos: List[Grupo] = []

    def __init__(self, numero: int, matricula_carrera: str):
        self.id=self.generar_id(numero_semestre=numero)
        self.matricula_carrera=matricula_carrera
        self.numero=numero

    def generar_id(self, numero_semestre) -> str:
        return f"{numero_semestre}-{randint(0, 100000)}-{randint(0, 100000)}"

    def registrar_grupo_en_semestre(self, grupo:Grupo):
        self.grupos.append(grupo)

    def mostrar_info_semestre(self):
        info=f"-ID: {self.id}\n-Numero: {self.numero}\n-Matricula de carrera: {self.matricula_carrera}\n"
        return info