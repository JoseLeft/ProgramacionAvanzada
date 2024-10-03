from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from semestre.semestre import Semestre
from carrera.carrera import Carrera

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def listar_estudiantes(self):
        print("*** ESTUDIANTES ***")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())


    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("\nEstudiante Eliminado")
                return

        print(f"No se encontró el estudiante con id: {numero_control}")
    

    def generar_numero_control(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0, 10000)
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"
        return numero_control
    

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestro(self, nombre_maestro: str, rfc: str, año_nacimiento: int):
        # M-{año de nacimiento}-{dia actual}-{numero aleatorio entre 500 y 5000}-{las primeras 2 letras de su nombre}-{las ultimas 2 letras de su RFC}-{la longitud de la lista de los profesores más uno}
        numero_control = f"M{año_nacimiento}{datetime.now().day}{randint(500, 5000)}{nombre_maestro[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros) + 1}"
        return numero_control
    
    def listar_maestros(self):
        print("*** MAESTROS ***")

        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())

    
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("\nMaestro Eliminado")
                return

        print(f"No se encontró el maestro con id: {numero_control}")
    
    
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def generar_numero_control_materia(self, nombre_materia: str, semestre: int, creditos: int):
        # "MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{random 1, 1000}"
        numero_control = f"MT{nombre_materia[-2:].upper()}{semestre}{creditos}{randint(500, 5000)}"
        return numero_control
    
    def listar_materias(self):
        print("*** MATERIAS ***")

        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
    

    def eliminar_materia(self, numero_control: str):
        for materia in self.lista_materias:
            if materia.numero_control == numero_control:
                self.lista_materias.remove(materia)
                print("\nMateria Eliminada")
                return

        print(f"No se encontró la materia con id: {numero_control}")

    def registrar_carrera(self, carrera: Carrera):
        self.lista_materias.append(carrera)

    def listar_carreras(self):
        print("*** CARRERAS ***")

        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())


    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id

        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break

        self.lista_semestres.append(semestre)


    def listar_semestres(self):
        print("*** SEMESTRES ***")

        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())


    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break

        self.lista_grupos.append(grupo)


    def listar_grupos(self):
        print("*** GRUPOS ***")

        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
        