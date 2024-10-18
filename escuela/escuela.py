from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from carrera.carrera import Carrera
from semestres.semestre import Semestre
from coordinador.coordinador import Coordinador
from usuario.usuario import Usuario
from coordinador.coordinador import Coordinador

class Escuela:
    lista_usuarios: List[Usuario]= []
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_grupos: List[Grupo] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    lista_coordinadores: List[Coordinador] = []

    def __init__(self):
        coordinador=Coordinador(nombre="José", apellido="Lázaro", numero_control="22121051", contraseña="1234*", sueldo=100.00, rfc="20041214",años_antiguedad=10)
        self.lista_usuarios.append(coordinador)

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def registrar_carrera(self, carrera:Carrera):
        self.lista_carreras.append(carrera)

    def registrar_semestre(self, semestre:Semestre):
        matricula_carrera=semestre.matricula_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula==matricula_carrera:
                carrera.registrar_semestre(semestre=semestre)
                self.lista_semestres.append(semestre)
                return
        print("\nNo existe la carrera para registrar el semestre")

    def registrar_grupo(self, grupo:Grupo):
        id_semestre=grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre==semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                self.lista_grupos.append(grupo)
                return
        print("\nNo existe el semestre para registrar el grupo")

    def listar_estudiantes(self):
        print("\n---ESTUDIANTES---\n")
        for estudainte in self.lista_estudiantes:
            print(estudainte.mostrar_info_estudiante())  

    def listar_maestros(self):
        print("\n---MAESTROS---\n")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())  

    def listar_materias(self):
        print("\n---MATERIAS---\n")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())

    def listar_carreras(self):
        print("\n-----CARRERAS-----\n")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info())

    def listar_semestres(self):
        print("\n-----SEMESTRES-----\n")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())

    def listar_grupos(self):
        print("\n-----GRUPOS-----")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupos())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if numero_control==estudiante.numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("\nEstudiante eliminado\n")
                return
        print("\nEstudiante no encontrado\n")

    def eliminar_maestro(self, numero_control_maestro):
        for maestro in self.lista_maestros:
            if numero_control_maestro==maestro.numero_control:
                self.lista_maestros.remove(maestro)
                print("\nMaestro eliminado\n")
                return
        print("\nMaestro no encontrado\n")

    def eliminar_materia(self, id_materia):
        for materia in self.lista_materias:
            if id_materia==materia.id:
                self.lista_materias.remove(materia)
                print("\nMateria eliminada\n")
                return
        print("\nMateria no encontrada\n")

    def generar_numero_control(self):
        mes=datetime.now().month
        año=datetime.now().year
        numero_control=f"L{año}{mes}{(len(self.lista_estudiantes)+1)}{randint(1, 10000)}"
        return numero_control
    
    def generar_numero_control_maestro(self, nombre, rfc, año_nacimiento):
        dia=datetime.now().day
        digitos_nombre=nombre[0:2].upper()
        digitos_rfc=rfc[-2:].upper()
        numero_control=f"M{año_nacimiento}{dia}{randint(500, 5000)}{digitos_nombre}{digitos_rfc}{(len(self.lista_maestros)+1)}"
        return numero_control
    
    def generar_id_materia(self, nombre, semestre, creditos):
        digitos_nombre=nombre[-2:].upper()
        id=f"MT{digitos_nombre}{semestre}{creditos}{randint(1, 1000)}"
        return id

    def validar_inicio_secion(self, numero_control: str, contraseña: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contraseña == contraseña:
                    return usuario
                
        return None