from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital=Hospital()

while True:
    print("Bienvenido al sistema del Hospital")
    print("\nSeleccione una accion a realizar\n")
    print("1. Registrar paciente")
    print("2. Registrar medico")
    print("3. Mostrar pacientes")
    print("4. Mostrar medicos")
    print("5. Eliminar paciente")
    print("6. Eliminar medico")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")

    opcion=input("Selecciona la accion a realizar: ")
    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar un paciente")

        nombre= input("Ingresa el nombre: ")
        año_nacimiento= int(input("Ingresa el año de nacimiento: "))
        peso= float(input("Ingresa el peso: "))
        estatura= float(input("Ingresa la estatura: "))
        direccion= input("Ingresa la direccion: ")

        paciente=Paciente(nombre=nombre, año_nacimiento=año_nacimiento, peso=peso, estatura=estatura, direccion=direccion)

        hospital.registrar_paciente(paciente=paciente)

        print("\nPaciente registrado correctamente\n")

    elif opcion == "2":
        print("\nSeleccionaste la opcion para registrar un medico")

        nombre= input("Ingresa el nombre: ")
        año_nacimiento= int(input("Ingresa el año de nacimiento: "))
        rfc= input("Ingresa el RFC: ")
        direccion= input("Ingresa la direccion: ")

        medico=Medico(nombre=nombre, año_nacimiento=año_nacimiento, rfc=rfc, direccion=direccion)

        hospital.registrar_medico(medico=medico)

        print("\nPaciente registrado correctamente\n")

    elif opcion == "3":
        hospital.mostrar_pacientes()

    elif opcion == "4":
        hospital.mostrar_medicos()

    elif opcion == "5":
        print("\nSeleccionaste la opcion de eliminar un paciente\n")
        id_paciente_eliminar=int(input("Introduzca el id del paciente a eliminar: "))
        hospital.eliminar_paciente(id_paciente_eliminar)

    elif opcion == "6":
        print("\nSeleccionaste la opcion de eliminar un medico\n")
        id_medico_eliminar=int(input("Introduzca el id del medico a eliminar: "))
        hospital.eliminar_medico(id_medico_eliminar)

    elif opcion == "7":
        hospital.mostrar_pacientes_menores()

    elif opcion == "8":
        hospital.mostrar_pacientes_mayores()

    elif opcion == "9":
        print("Hasta luego")
        break