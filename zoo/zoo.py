from typing import List
from datetime import datetime, date
from random import randint
from empleados.empleado import Empleado
from visitantes.visitante import Visitante
from animales.animal import Animal
from visitas.visita import Visita
from empleados.utils.roles import Rol
from empleados.utils.roles import Tipo_Animal
from empleados.utils.roles import Alimentacion
from director.director import Director


class Zoologico:
    lista_empleados: List [Empleado] = []
    lista_guia : List [Empleado] = []
    lista_veterinario : List [Empleado] = []
    lista_mantenimiento : List [Empleado] = []
    lista_administrativo : List [Empleado] = []
    lista_visitantes: List [Visitante] = []
    lista_animales: List [Animal] = []
    lista_visitas: List [Visita] = []
    procesos_realizados= []
    
    
    def __init__(self):
        director = Director(id="505050", nombre="Eder", apellidos= "Rivera", fecha_nacimiento= "25/01/1991", fecha_ingreso= "10/11/22", rfc= "ERKI34F", curp= "EDRMEOE3R4D", salario= 120000, horario= "9-15", contrasena="131")
        self.lista_empleados.append(director) 
    
        guia1 = Empleado(id="GI22121069", nombre="Edson", apellidos="Martínez", fecha_nacimiento=date(2000,6,12,), fecha_ingreso=date(2023,1,1), rfc="39ujfoi2m'", curp="EIJIJAD4G35", salario= 5500, horario=8, rol=Rol.GUIA)
        guia2 = Empleado(id="GI22121052", nombre="Jesus", apellidos="Alcantara", fecha_nacimiento=date(2004,2,10,), fecha_ingreso=date(2020,11,9), rfc="jlksjflkdsjlkf", curp="MAGEOJ39JF", salario=55000, horario=8, rol=Rol.GUIA)
        self.lista_empleados.append(guia1) 
        self.lista_empleados.append(guia2) 
        Zoologico.lista_guia.append(guia1)
        Zoologico.lista_guia.append(guia2)
        
        animal1 = Animal(id="AE04093", tipo_animal=Tipo_Animal.AEREO, fecha_nacimiento=(2009,5,7), fecha_llegada_zoo=(2017,10,10), peso=200, enfermedades="ninguna", frecuencia_alimentacion=3, tipo_alimentacion=Alimentacion.CARNIVORO, vacunas=True)
        animal2 = Animal(id="TE83624", tipo_animal=Tipo_Animal.TERRESTRE, fecha_nacimiento=(2018,4,12), fecha_llegada_zoo=(2021,1,12), peso=200, enfermedades="ninguna", frecuencia_alimentacion=3, tipo_alimentacion=Alimentacion.HERBIVORO, vacunas=True)
        animal3 = Animal(id="AC89328", tipo_animal=Tipo_Animal.ACUATICO, fecha_nacimiento=(2015,2,2), fecha_llegada_zoo=(2021,3,8), peso=500, enfermedades="ninguna", frecuencia_alimentacion=3, tipo_alimentacion=Alimentacion.CARNIVORO, vacunas=True)
        self.lista_animales.append(animal1) 
        self.lista_animales.append(animal2) 
        self.lista_animales.append(animal3) 
        Zoologico.lista_animales.append(animal1)
        Zoologico.lista_animales.append(animal2)
        Zoologico.lista_animales.append(animal3)
        
        visitante1 = Visitante(id_visitante="VISITANTE6458768312", nombre="Laura", apellidos="Ramos", fecha_nacimiento=date(2004,6,1), curp="ijfdjf", fecha_registro=date(2024,5,5), numero_visitas=0)
        visitante2 = Visitante(id_visitante="VISITANTE643435312", nombre="Yaha", apellidos="Villegas", fecha_nacimiento=date(2000,7,10), curp="sfvsdfl", fecha_registro=date(2021,3,30), numero_visitas=0)
        visitante3 = Visitante(id_visitante="VISITANTE64576312", nombre="Jesus", apellidos="Alcantara", fecha_nacimiento=date(2014,6,9), curp="ldfvñl", fecha_registro=date(2022,11,18), numero_visitas=0)
        visitante4 = Visitante(id_visitante="VISITANTE645326412", nombre="Jared", apellidos="Gomez", fecha_nacimiento=date(2004,12,1), curp="dfvdfgk", fecha_registro=date(2024,1,4), numero_visitas=0)
        Zoologico.lista_visitantes.append(visitante1)
        Zoologico.lista_visitantes.append(visitante2)
        Zoologico.lista_visitantes.append(visitante3)
        Zoologico.lista_visitantes.append(visitante4)
    
    
    def registrar_empleado(self, empleado: Empleado, id: str):
        self.lista_empleados.append(empleado)
        letras_id = id[:2]
        if letras_id == "GI":
            self.lista_guia.append(empleado)
        
        elif letras_id == "VE":
            self.lista_veterinario.append(empleado)
            
        elif letras_id == "MA":
            self.lista_mantenimiento.append(empleado)
        
        elif letras_id == "AD":
            self.lista_administrativo.append(empleado)

    
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        
    def registrar_visita(self, visita: Visita):
        precio_final = 0
        precio_adulto = 100
        precio_niño = 50
        precio_final = 0
        for visitante in visita.visitantes:
            visitante.numero_visitas =+ 1
            if visitante.numero_visitas % 6 == 0:
                print(f"Descuento del 20% para {visitante.nombre}")
                
                precio = precio_adulto*.8 if visitante.es_adulto() else precio_niño *.8
                visitante.numero_visitas = 0
            else:
                precio = precio_adulto if visitante.es_adulto() else precio_niño
                
            print(f"Visitante: {visitante.nombre} \nPrecio boleto: ${precio}")
            precio_final = precio_final + precio
        self.lista_visitas.append(visita)
        print(f"Visita registrada con ID: {visita.id}")
        print(f"Precio final: ${precio_final}")
        
    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)
        
    
    def generar_id_empleados(self, nombre, ano_nacimiento):
        ano_nacimiento = ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(100,3000)
        letras_nombre = nombre[:2]
        letras_nombre = letras_nombre.upper()
        longitud_mas_uno = len(self.lista_empleados) +1
        
        print("""
        ** EMPLEADOS **
        
        1. Guía
        2. Veterinario
        3. Mantenimiento
        4. Administrador
    
        """  )
        opcion = int(input("Rol del empleado: "))
        
        if opcion == 1:
            rol=Rol.GUIA
            id = f"GI{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            
            return id, rol
        
        elif opcion == 2:
            rol=Rol.VETERINARIO
            id = f"VE{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
        
        elif opcion == 3:
            rol=Rol.MANTENIMIENTO
            id = f"MA{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
        
        elif opcion == 4:
            rol=Rol.ADMINISTRATIVO
            id = f"AD{letras_nombre}{aleatorio}{ano_nacimiento}{dia}{longitud_mas_uno}"
            return id, rol
    
    def generar_id_animal(self, tipo_animal, ano_llegada, ano_nacimiento):
        dos_letras = tipo_animal.value[:2].upper()
        longitud_mas_dos = len(self.lista_animales) + 2
        
        id = f"{dos_letras}-{ano_nacimiento}{ano_llegada}{longitud_mas_dos}"
        return id
    
    def generar_id_visitante(self, ano_nacimiento):
        longitud_mas_uno = len(self.lista_visitantes) + 1
        numero_random = randint(10,900)
        
        id = f"VISITANTE{ano_nacimiento}{numero_random}{longitud_mas_uno}"
        return id
    
    def generar_id_visita(self):
        numero_random = randint(100,1000)
        longitud_mas_tres = len(self.lista_visitas) + 3
        
        id = f"VISITA{numero_random}{longitud_mas_tres}"
        return id
    
    def eliminar_empleado(self, id:str):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                id_eliminar = id[:2]
                
                if id_eliminar == "VE":
                    self.lista_veterinario.remove(empleado)
                    
                elif id_eliminar == "MA":
                    self.lista_mantenimiento.remove(empleado)
                
                elif id_eliminar == "AD":
                    self.lista_administrativo.remove(empleado)
                
                elif id_eliminar == "GI":
                    self.lista_guia.remove(empleado)
                
                else:
                    print("Hay un error")
                    
                print("Empleado eliminado con éxito")
                return
        print(f"\n\tNo se encontró al empleado con el ID: {id}")
    
    def eliminar_animal(self, id: str):
        for animal in self.lista_animales:
            if animal.id == id:
                self.lista_animales.remove(animal)
                print("\n\tAnimal eliminado con exito")
                return
        print(f"\n\tNo hay animal con el id: {id}")
    
    def eliminar_visitante(self, id: str):
        for visitante in self.lista_visitantes:
            if visitante.id_visitante == id:
                self.lista_visitantes.remove(visitante)
                print("\n\tvisitante eliminado con éxito")
                return
        print(f"\n\tNo se encontró al visitantes con el id: {id}")
        
    
    def listar_empleados(self):
        print("\n***************Empleados***************\n")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_info_empl())
            
    def listar_veterinarios(self):
        print("\n***************Veterinarios***************\n")
        for empleado in self.lista_veterinario:
            print(empleado.mostrar_info_empl())
            
    def listar_guias(self):
        print("\n****************Guías****************\n")
        for empleado in self.lista_guia:
            print(empleado.mostrar_info_empl())
            
    def listar_mantenimiento(self):
        print("\n***************Mantenimiento**************\n")
        for empleado in self.lista_mantenimiento:
            print(empleado.mostrar_info_empl())
            
    def listar_administrativos(self):
        print("\n***************Administrativos***************\n")
        for empleado in self.lista_administrativo:
            print(empleado.mostrar_info_empl())
            
    def listar_animales(self):
        print("\n***************Animales***************\n")
        for animal in self.lista_animales:
            print(animal.mostar_info_animal())
            
    def listar_visitas(self):
        print("\n***************Visitas***************\n")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visitas())
    
    def listar_visitantes(self):
        print("\n***************Visitantes***************\n")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
    
    
    def validar_inicio_sesion(self, id: str, contrasena: str):
        for director in self.lista_empleados:
            if director.id == id:
                if director.contrasena == contrasena:
                    return director
                
        return None
    
    def cambiar_nombre(self, nuevo_nombre: str):
        for empleado in self.lista_empleados:
            empleado.nombre = nuevo_nombre
            print(self.mostrar_info_empl())