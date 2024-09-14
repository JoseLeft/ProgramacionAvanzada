class Curso:
    nombre_del_curso = ""
    codigo_del_curso = 0
    nombre_del_instructor = ""

    def __init__(self, nombre_del_curso, codigo_del_curso, nombre_del_instructor):
        self.nombre_del_curso = nombre_del_curso
        self.codigo_del_curso = codigo_del_curso
        self.nombre_del_instructor = nombre_del_instructor

    def mostrar_info_curso(self):
        print("Informacion del curso:")
        print("El nombre del curso es:", self.nombre_del_curso)
        print("El codigo del curso es:", self.codigo_del_curso)
        print("El nombre del instructor es:", self.nombre_del_instructor)