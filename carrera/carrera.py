from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestres.semestre import Semestre
from random import randint

class Carrera:
    matricula: str
    nombre: str
    numero_semestres: int=0
    materias: List[Materia]=[]
    estudiantes: List[Estudiante]=[]
    semestre: List[Semestre]=[]

    def __init__(self, nombre: str):
        self.matricula=self.generar_matricula(nombre=nombre)
        self.nombre=nombre

    def generar_matricula(self, nombre: str) -> str:
        return f"{nombre}-{randint(0, 100000)}-{randint(0, 100000)}"
    
    def registrar_semestre(self, semestre: Semestre):
        self.numero_semestres += 1
        self.semestre.append(semestre)

    def mostrar_info(self):
        info=f"-Matricula: {self.matricula}\n-Nombre: {self.nombre}\n-Numero de semestres: {self.numero_semestres}\n"
        return info