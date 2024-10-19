from empleados.utils.roles import Rol
from empleados.utils.roles import Tipo_Animal
from empleados.utils.roles import Alimentacion
from zoo.zoo import Zoologico
from empleados.empleado import Empleado
from animales.animal import Animal
from visitantes.visitante import Visitante
from visitas.visita import Visita
from datetime import datetime


class Menu:
    zoo: Zoologico = Zoologico()
    
    def login(self):
        intentos = 0
        
        while intentos < 5:
            print("\n------BIENVENIDO AL ZOOLÓGICO------\n")
            print("Inicia sesión para continuar: ")
            
            id = input("Ingresa tu ID de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            
            usuario = self.zoo.validar_inicio_sesion(id=id, contrasena=contrasena) 
            
            if usuario is None:
                intentos = self.mostrar_intentos_sesion_fallidos(intentos_usuario=intentos) 
            
            else: 
                self.mostrar_menu()
                intentos = 0
        
        print("\n Intentos maximos alcanzados. Vuelva mas tarde.")
        
    def mostrar_intentos_sesion_fallidos(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intentelo de nuevo\n")
        return intentos_usuario + 1
    
    def mostrar_menu(self):
        while True:

            print("""
    ******* M E N Ú *******
    1. Registrar
    2. Modificar
    3. Asignar mantenimientos
    4. Eliminar
    5. Consultar
    6. Salir
            """)
            
            opcion = int(input("Selecciona una opción para continuar: "))
            
            if opcion == 1:
                while True:
                    print("""
    ¿QUE DESEA REGISTRAR?
    1. Registrar empleado
    2. Registrar animal
    3. Registrar visitante
    4. Registrar visita
    5. Salir
                    """)
                
                    opcion_registro = int(input("Selecciona una opción para continuar: "))
                    
                    if opcion_registro == 1:
                        print("\nIngresa los datos del empleado a registrar:\n")
                    
                        nombre = input("Nombre: ")
                        apellidos = input("Apellidos: ")
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        salario = float(input("Salario: "))
                        rfc = input("RFC: ").upper()
                        curp = input("CURP: ").upper()
                        horario = input("Horario: ")
                        while True:
                            ano_ingreso = int(input("Año de ingreso: "))
                            mes_ingreso = int(input("Mes de ingreso: "))
                            dia_ingreso = int(input("Día de ingreso: "))
                            
                            fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                            fecha_ingreso = datetime(ano_ingreso, mes_ingreso, dia_ingreso)
                            
                            if fecha_ingreso > fecha_nacimiento:
                                break
                            else:
                                print("Fecha de ingreso imposible. Intente de nuevo")
                        
                        id, rol = self.zoo.generar_id_empleados(nombre=nombre, ano_nacimiento=ano_nacimiento)
                        print("ID: ", id)

                        empleado = Empleado(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_ingreso, rfc=rfc, curp=curp, salario=salario, horario=horario, id=id, rol=rol)
                        self.zoo.registrar_empleado(empleado = empleado, id = id)
                
                    elif opcion_registro == 2:
                        print("\nIngresa los datos del animal a registrar:\n")
                        
                        tipo_animal = Tipo_Animal.validar_animal()
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        
                        while True:
                            ano_llegada = int(input("Año de ingreso: "))
                            mes_llegada = int(input("Mes de ingreso: "))
                            dia_llegada = int(input("Día de ingreso: "))
                            fecha_llegada_zoo = datetime(ano_llegada, mes_llegada, dia_llegada)
                            
                            if fecha_llegada_zoo >= fecha_nacimiento:
                                break
                            else:
                                print("Fecha de llegada incorrecta. Intentalo nuevamente.\n")
                        
                        peso = float(input("Peso del animal: "))
                        enfermedades = input("Enfermedades del animal: ")
                        frecuencia_alimentacion = input("Frecuencia de alimentación: ")
                        tipo_alimentacion = Alimentacion.validar_tipo_alimentacion()
                        vacunas = bool(input("Cuenta con vacunas 1. Sí / 0. No: "))
                        
                        id = self.zoo.generar_id_animal(tipo_animal=tipo_animal, ano_llegada=ano_llegada, ano_nacimiento=ano_nacimiento)
                        print("ID: ", id)
                        
                        animal = Animal(id=id, tipo_animal=tipo_animal, fecha_nacimiento=fecha_nacimiento, fecha_llegada_zoo=fecha_llegada_zoo, peso=peso, enfermedades=enfermedades, frecuencia_alimentacion=frecuencia_alimentacion, tipo_alimentacion=tipo_alimentacion, vacunas=vacunas)
                        self.zoo.registrar_animal(animal=animal)
                
                    elif opcion_registro == 3:
                        print("\nIngresa los datos del visitante a registrar:\n")
                        
                        nombre = input("Nombre: ")
                        apellidos = input("Apellidos: ")
                        ano_nacimiento = int(input("Año de nacimiento: "))
                        mes_nacimiento = int(input("Mes de nacimiento: "))
                        dia_nacimiento = int(input("Día de nacimiento: "))
                        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                        
                        curp = input("CURP: ").upper()
                        ano = datetime.now().year
                        mes = datetime.now().month
                        dia = datetime.now().day
                        fecha_registro = datetime(ano, mes, dia)
                        id = self.zoo.generar_id_visitante(ano_nacimiento)
                        print("ID: ", id)
                        visitante = Visitante(id_visitante=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento,numero_visitas=0, curp=curp, fecha_registro=fecha_registro)
                        self.zoo.registrar_visitante(visitante = visitante)
                    
                    elif opcion_registro == 4:
                        print("Ingresa los datos de la visita a registrar:")
                        id = self.zoo.generar_id_visita()
                        print("\nEmpleados disponibles para ser Guía:")
                        guia_seleccionado = None
                        while not guia_seleccionado:
                            
                            for guia in Zoologico.lista_guia:
                                print(f"\nID: {guia.id} \nNombre: {guia.nombre} {guia.apellidos}")
                                
                            seleccion = input("\nIngresa el ID de el Guía a seleccionar:")
                            for guia in Zoologico.lista_guia:
                                if seleccion == guia.id:
                                    guia_seleccionado= guia
                                    break
                                
                            
                            if not guia_seleccionado:
                                print("ID de Guía no valido, intentalo de nuevamente.")
                                    
                        visitantes_seleccionados = []
                        
                        while True:
                            print("\nLista de visitantes registrados: ")
                            for visitante in Zoologico.lista_visitantes:
                                if visitante not in visitantes_seleccionados:
                                    print(f"\nID: {visitante.id_visitante} \nNombre: {visitante.nombre} {visitante.apellidos}")
                                
                            seleccion = input("\nIngresa el ID del visitante seleccionado: ")
                            visitante_seleccionado = None
                            for visitante in Zoologico.lista_visitantes:
                                if seleccion == visitante.id_visitante:
                                    visitante_seleccionado = visitante
                                
                                    if visitante_seleccionado in visitantes_seleccionados:
                                        print("\n\tNo se puede registrar, visitante ya registrado")
                                        
                                    else:
                                        visitantes_seleccionados.append(visitante_seleccionado)
                                        visitante =+ 1
                                    break
                            if not visitante_seleccionado:
                                print("ID incorrecto, intentalo nuevamente.")
                            else:
                                agregar_otro=input("\nDesea agregar a otro visitante 1)si; 2)no: ").lower()
                                if agregar_otro != "1":
                                    break
                                       
                        visita = Visita(id=id, guia=guia_seleccionado, visitantes=visitantes_seleccionados)
                        self.zoo.registrar_visita(visita = visita)
                        print(f"\nVisita registrada con exito. ID: {id}")
                        
                    elif opcion_registro == 5:
                        break
                    
                    else:
                        print("\tOpción NO válida\n")
            
            elif opcion == 2:
                while True:
                    print("""
    ¿QUÉ DESEA MODIFICAR?
    1. Modificar empleado
    2. Modificar animal
    3. Modificar visitante
    4. Salir
                    """)
                
                    opcion_modificar = int(input("Seleccione una opción para continuar: "))
                    
                    if opcion_modificar == 1:
                        id_empleado_modificar = input("Ingresa el ID del empleado: ")
                        for empleado in Zoologico.lista_empleados:
                            if id_empleado_modificar == empleado.id:
                                while True:
                                    menu = """
    MODIFICAR:
    1. Nombre
    2. Apellidos
    3. Fecha de nacimiento
    4. Fecha de ingreso
    5. RFC
    6. CURP
    7. Salario
    8. Horario
    9. Salir                                          
                                    """
                                    print(menu)
                                    opcion_cambiar = int(input("Ingresar dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                                        empleado.nombre = nuevo_nombre
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_apellido = input("Ingresa los nuevos apellidos: ")
                                        empleado.apellidos = nuevo_apellido

                                    elif opcion_cambiar == 3:
                                        nuevo_ano = int(input("Ingresa el nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresa el nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresa el nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        empleado.fecha_nacimiento = nueva_fecha_nacimiento

                                    elif opcion_cambiar == 4:
                                        nuevo_ano = int(input("Ingresa el nuevo año de ingreso : ")) 
                                        nuevo_mes = int(input("Ingresa el nuevo mes de ingreso : ")) 
                                        nuevo_dia = int(input("Ingresa el nuevo dia de ingreso : "))
                                        nueva_fecha_ingreso = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        empleado.fecha_ingreso = nueva_fecha_ingreso

                                    elif opcion_cambiar == 5:
                                        nuevo_rfc = input("Ingresa el nuevo RFC: ").upper()
                                        empleado.rfc = nuevo_rfc

                                    elif opcion_cambiar == 6:
                                        nuevo_curp = input("Ingresa el nuevo CURP: ").upper()
                                        empleado.curp = nuevo_curp

                                    elif opcion_cambiar == 7:
                                        nuevo_salario = float(input("Ingresa el nuevo salario: "))
                                        empleado.salario = nuevo_salario

                                    elif opcion_cambiar == 8:
                                        nuevo_horario = input("Ingresa el nuevo horario: ")
                                        empleado.horario = nuevo_horario

                                    elif opcion_cambiar == 9:
                                        break
                                        
                                    else:
                                        print("\tOpción NO válida\n")
                                        
                        if not id_empleado_modificar:        
                            print("No se encontró empleado con el ID ingresado: ", id_empleado_modificar)
                                
                    
                    elif opcion_modificar == 2:
                        id_animal_modificar = input("Ingresa el ID del animal: ")
                        for animal in Zoologico.lista_animales:
                            if id_animal_modificar == animal.id:
                                while True:
                                    print("""
    MODIFICAR:
    1. Fecha de nacimiento
    2. Fecha de llegada
    3. Peso
    4. Enfermedades
    5. Frecuancia de alimentación
    6. Vacunas
    7. Salir               
                                    """)
                                    opcion_cambiar = int(input("Ingresar dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_ano = int(input("Ingresar nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        animal.fecha_nacimiento = nueva_fecha_nacimiento
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_ano = int(input("Ingresar nuevo año de llegada : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de llegada : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de llegada : "))
                                        nueva_fecha_llegada_zoo = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        animal.fecha_llegada_zoo = nueva_fecha_llegada_zoo

                                    elif opcion_cambiar == 3:
                                        nuevo_peso = float(input("Ingresar el nuevo peso: "))
                                        animal.peso = nuevo_peso

                                    elif opcion_cambiar == 4:
                                        nuevas_enfermedades = input("Ingresar las nuevas enfermedades: ")
                                        animal.enfermedades = nuevas_enfermedades

                                    elif opcion_cambiar == 5:
                                        nueva_frecuencia_alimentacion = input("Ingresar la nueva frecuencia de alimentación: ")
                                        animal.frecuencia_alimentacion = nueva_frecuencia_alimentacion

                                    elif opcion_cambiar == 6:
                                        nuevas_vacunas = bool(input("Cuenta con vacunas 1. Sí / 0. No: "))
                                        animal.vacunas = nuevas_vacunas

                                    elif opcion_cambiar == 7:
                                        break
                                        
                                    else:
                                        print("\tOpción NO válida\n")
                                        
                        if not id_animal_modificar:        
                            print("No se encontro animal con el ID ingresado: ", id_animal_modificar)
                    
                    elif opcion_modificar == 3:
                        id_visitante_modificar = input("Ingrese el ID del visitante: ")
                        for visitante in Zoologico.lista_visitantes:
                            if id_visitante_modificar == visitante.id_visitante:
                                while True:
                                    print("""
    MODIFICAR:
    1. Nombre
    2. Apellidos
    3. Fecha de nacimiento
    4. Fecha de ingreso
    5. CURP
    6. Salir
                                    """)
                                    opcion_cambiar = int(input("Ingresar el dato a modificar: "))
                                    
                                    if opcion_cambiar == 1:
                                        nuevo_nombre = input("Ingresar el nuevo nombre: ")
                                        visitante.nombre = nuevo_nombre
                                    
                                    elif opcion_cambiar == 2:
                                        nuevo_apellido = input("Ingresar los nuevos apellidos: ")
                                        visitante.apellidos = nuevo_apellido

                                    elif opcion_cambiar == 3:
                                        nuevo_ano = int(input("Ingresar nuevo año de nacimiento : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de nacimiento : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de nacimiento : "))
                                        nueva_fecha_nacimiento = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        visitante.fecha_nacimiento = nueva_fecha_nacimiento

                                    elif opcion_cambiar == 4:
                                        nuevo_ano = int(input("Ingresar nuevo año de ingreso : ")) 
                                        nuevo_mes = int(input("Ingresar nuevo mes de ingreso : ")) 
                                        nuevo_dia = int(input("Ingresar nuevo dia de ingreso : "))
                                        nueva_fecha_ingreso = datetime(nuevo_ano,nuevo_mes,nuevo_dia)
                                        visitante.fecha_registro = nueva_fecha_ingreso

                                    elif opcion_cambiar == 5:
                                        nuevo_curp = input("Ingresar el nuevo CURP: ").upper()
                                        visitante.curp = nuevo_curp

                                    elif opcion_cambiar == 6:
                                        break
                                        
                                    else:
                                        print("\tOpción NO válida\n")
                                        
                        if not id_visitante_modificar:        
                            print("No se encontró visitante con el ID ingresado: ", id_visitante_modificar)
                                
                    
                    elif opcion_modificar == 4:
                        break
                    
                    else:
                        print("\tOpción NO válida\n")
            
            elif opcion == 3:
                    print("\nLista de empleados disponibles para mantenimiento:")
                    empleado_seleccionado = None
                    while not empleado_seleccionado:
                        for empleado in Zoologico.lista_empleados:
                            if empleado.rol == Rol.MANTENIMIENTO:
                                print(f"ID: {empleado.id}\nNombre: {empleado.nombre} {empleado.apellidos}\n")
                        
                        seleccion_empleado = input("Ingrese el ID del empleado seleccionado: \n")
                        
                        for empleado in Zoologico.lista_empleados:
                            if seleccion_empleado == empleado.id and empleado.rol == Rol.MANTENIMIENTO:
                                empleado_seleccionado = empleado
                                break
                        if not empleado_seleccionado:
                            print("ID de empleado no válido. Intenta nuevamente.")
                            
                    print("\nLista de animales: \n")
                    for animal in Zoologico.lista_animales:
                        print(f"ID: {animal.id}\nTipo de animal: {animal.tipo_animal.value}\nEnfermedades: {animal.enfermedades}\n")
                        
                    id_animal = input("Ingresar el ID del animal: ")                   
                    print("\nSelecciona el tipo de proceso a realizar:")
                    print("1. Alimentación")
                    print("2. Limpieza")
                    print("3. Mantenimiento")
                    tipo_proceso = input("Proceso a realizar: ")
                    if tipo_proceso == "1":
                        proceso = "Alimentación"
                    elif tipo_proceso == "2":
                        proceso = "Limpieza"
                    elif tipo_proceso == "3":
                        proceso = "Mantenimiento"
                    else:
                        print("Opción no válida. Se asignará el proceso como 'Mantenimiento'.")
                        proceso = "Mantenimiento"
                    
                    fecha_proceso = datetime.now().strftime("%Y-%m-%d")
                    observaciones = input("Ingresa observaciones (opcional, presiona Enter si no hay): ")
                    
                    registro_proceso = {
                        "empleado": empleado_seleccionado,
                        "id_animal": id_animal,
                        "proceso": proceso,
                        "fecha_proceso": fecha_proceso,
                        "observaciones": observaciones
                    }
                    
                    Zoologico.procesos_realizados.append(registro_proceso)
                    
                    print(f"\nProceso de {proceso} registrado exitosamente para el animal con ID: {id_animal}.")
            
            elif opcion == 4:
                while True:
                    print("""
    ¿QUÉ DESEA ELIMINAR?
    1. Eliminar empleado
    2. Eliminar animal
    3. Eliminar visitante
    4. Salir
                    """)
                    opcion_eliminar = int(input("Seleccione una opción para continuar: "))
                    
                    if opcion_eliminar == 1:
                        id = input("Ingresa el ID del empleado a eliminar: ")
                        self.zoo.eliminar_empleado(id = id)
                    
                    elif opcion_eliminar == 2:
                        id = input("Ingresa el ID del animal a eliminar: ")
                        self.zoo.eliminar_animal(id = id)
                    
                    elif opcion_eliminar == 3:
                        id = input("Ingresa el ID del visitante a eliminar: ")
                        self.zoo.eliminar_visitante(id = id)
                    
                    elif opcion_eliminar == 4:
                        break
                    
                    else: 
                        print("\tOpción NO válida\n")
                
            elif opcion == 5:
                while True:
                    print("""
    CONSULTAR:
    1. Empleados
    2. Personal veterinario
    3. Personal mantenimiento
    4. Personal guías
    5. Personal administrativo
    6. Animales
    7. Visitantes
    8. Visitas
    9. Salir
                    """)
                    opcion_consultar = int(input("Ingresar una opción para continuar: "))
                    
                    if opcion_consultar == 1:
                        self.zoo.listar_empleados()
                        
                    elif opcion_consultar == 2:
                        self.zoo.listar_veterinarios()
                        
                    elif opcion_consultar == 3:
                        self.zoo.listar_mantenimiento()
                    
                    elif opcion_consultar == 4:
                        self.zoo.listar_guias()
                    
                    elif opcion_consultar == 5:
                        self.zoo.listar_administrativos()
                        
                    elif opcion_consultar == 6:
                        self.zoo.listar_animales()

                    elif opcion_consultar == 7:
                        self.zoo.listar_visitantes()

                    elif opcion_consultar == 8:
                        self.zoo.listar_visitas()

                    elif opcion_consultar == 9:
                        break
                    
                    else: 
                        print("\tOpción NO válida\n")
            
            elif opcion == 6:
                break
            
            else:  
                print("\tOpción NO válida\n")