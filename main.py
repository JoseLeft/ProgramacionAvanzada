from curso import Curso
from estudiante import Estudiante 

estudiante_uno = Estudiante("José Lázaro Izquierdo", 19, 22121051)
estudiante_dos = Estudiante("Edson Jared Martinez Gomez", 19, 22121069)

curso_uno = Curso("Calculo Diferencial", 23654, "Dante")
curso_dos = Curso("Calculo Integral", 24983, "Norma Liliana")
curso_tres = Curso("Calculo Vectorial", 23233, "Juan Carlos")
curso_cuatro = Curso("Ecuaciones Diferenciales", 24542, "Beatriz")

estudiante_uno.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_dos)
estudiante_uno.agregar_curso(curso_tres)

estudiante_dos.agregar_curso(curso_dos)
estudiante_dos.agregar_curso(curso_tres)
estudiante_dos.agregar_curso(curso_cuatro)

estudiante_uno.mostrar_info()
estudiante_dos.mostrar_info()

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()
curso_cuatro.mostrar_info_curso()
