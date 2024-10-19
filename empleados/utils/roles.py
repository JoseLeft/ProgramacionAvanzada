from enum import Enum
  
class Rol(Enum):
    DIRECTOR = "Director"
    GUIA = "Guia"
    VETERINARIO = "Veterinario"
    MANTENIMIENTO = "Mantenimiento"
    ADMINISTRATIVO = "Administrativo"
    
    VISITANTE = "Visitante"

class Tipo_Animal(Enum):
    ACUATICO = "Acuatico"
    TERRESTRE = "Terrestre"
    AEREO = "Aereo"
    def validar_animal():
         while True:
            tipo_input = input("Tipo de animal (Acuatico, Aereo, Terrestre): ").capitalize()
            if tipo_input in [animal.value.capitalize() for animal in Tipo_Animal]: 
                return Tipo_Animal[tipo_input.upper()] 
            else:
                print("Tipo de animal no válido. Intenta de nuevo.\n")
    
class Alimentacion(Enum):
    CARNIVORO = "Carnivoro"
    HERBIVORO = "Herbivoro"
    def validar_tipo_alimentacion():
        while True:
            tipo_input = input("Tipo de alimentación (Carnivoro, Herbivoro): ").capitalize()
            if tipo_input in [alimentacion.value.capitalize() for alimentacion in Alimentacion]:
                return Alimentacion[tipo_input.upper()]
            else:
                print("Tipo de alimentación no válida. Intenta de nuevo.\n")