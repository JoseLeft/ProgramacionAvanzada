from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from materias.materia import Materia
from maestros.maestro import Maestro


escuela = Escuela()

while True:
    print("\n** MINDBOX **")
    print("1. Registar estudiante")
    print("2. Registar maestro")
    print("3. Registar materia")
    print("4. Registar grupo")
    print("5. Registar horario")
    print("6. Mostrar Estudiantes")
    print("7. Mostrar Maestros") #Tarea
    print("8. Mostrar Materias") #Tarea
    print("9. Mostrar Grupos")
    print("10. Eliminar Estudiante")
    print("11. Eliminar Maestro")#Tarea
    print("12. Eliminar Materia")#Tarea
    print("13. Salir")
    
    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        print("\n Seleccionaste la opcion para registrar un estudiante")

        numero_control = escuela.generar_numero_control()
        print(numero_control)


        nombre = input("ingresa el nombre del estudiante: ")
        apellido = input("ingresa el apellido del estudiante: ") 
        curp = input("ingresa la curp del estudiante: ")
        año = int(input("ingrese el año de nacimiento del estudiante: "))
        mes = int(input("ingrese el mes de nacimiento del estudiante: "))
        dia = int(input("ingrese el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(año, mes, dia)

        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)


        escuela.registrar_estudiante(estudiante)
        print(f"Estudiante {nombre} {apellido} registrado exitosamente.\n")

    if opcion == "2":
        print("\n Seleccionaste la opcion para registrar un maestro")

        nombre_maestro = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ") 
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        año = int(input("Ingresa el año de nacimiento del maestro: "))
        mes = int(input("Ingresa el mes de nacimiento del maestro: "))
        dia = int(input("Ingresa el día de nacimiento del maestro: "))
        fecha_nacimiento = datetime(año, mes, dia)

        numero_control_maestro = escuela.generar_numero_control_maestro(nombre_maestro, rfc, año)
        print(f"Número de control del Maestro: {numero_control_maestro}")

        maestro = Maestro(nombre_maestro=nombre_maestro, apellido=apellido, rfc=rfc, fecha_nacimiento=fecha_nacimiento, numero_control=numero_control_maestro, sueldo=sueldo)

        escuela.registrar_maestro(maestro)
        print(f"Maestro {nombre_maestro} {apellido} registrado exitosamente.\n")



    if opcion == "3":
        print("\n Seleccionaste la opcion para registrar una materia")

        nombre_materia = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ") 
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa los creditos de la materia: "))

        numero_control_materia = escuela.generar_numero_control_materia(nombre_materia, semestre, creditos)
        print(f"\nNúmero de control de la materia: {numero_control_materia}")

        materia = Materia(numero_control=numero_control_materia, nombre_materia=nombre_materia, descripcion=descripcion, semestre=semestre, creditos=creditos)

        escuela.registrar_materia(materia)
        print(f"Materia {nombre_materia} registrada exitosamente.\n")

    if opcion == "4":
        pass
    if opcion == "5":
        pass
    if opcion == "6":
        escuela.listar_estudiantes()

    if opcion == "7":
        escuela.listar_maestros()

    if opcion == "8":
        escuela.listar_materias()

    if opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante")

        numero_control = input("Ingresa el numero de control del estudiante que deseas eliminar: ")

        escuela.eliminar_estudiante(numero_control=numero_control)

    if opcion == "11":
        print("\nSeleccionaste la opcion para eliminar un maestro")

        numero_control = input("Ingresa el numero de control del maestro que deseas eliminar: ")

        escuela.eliminar_maestro(numero_control=numero_control)

    if opcion == "12":
        print("\nSeleccionaste la opcion para eliminar una materia")

        numero_control = input("Ingresa el numero de control de la materia que deseas eliminar: ")

        escuela.eliminar_materia(numero_control=numero_control)

    if opcion == "13":
        print("Hasta Luego")
        break