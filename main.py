from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("Bienvenido al sistema del hospital")
    print("1. Registrar paciente ")
    print("2. Registrar medico")    
    print("3. Mostrar pacientes")    
    print("4. Mostrar medicos")    
    print("5. Eliminar pacientes")    
    print("6. Eliminar medicos")    
    print("7. Mostrar paceintes menores de edad")    
    print("8. Mostrar pacientes mayores de edad")    
    print("9. Salir")    

    opcion_usuario = input("Selecciona la opcion deseada")

    if opcion_usuario == "1":
        print("Sleccionaste la opcion para registrar pacientes")

        nombre = input("Ingresa el nombre:")
        ano_nacimiento = input("Ingresa el año de nacimiento:")
        peso = input("Ingresa el peso:")
        estatura = input("Ingresa la estatura:")
        direccion = input("Ingresa la direccion:")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)

        print("Paciente registrado correctamente")


    elif opcion_usuario == "2":
        #registrar medico
        pass

    elif opcion_usuario == "3":
        hospital.mostrar_pacientes()

    elif opcion_usuario == "9":
        print("Hasta Luego")
        break        
