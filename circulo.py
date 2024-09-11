class Circulo:
    radio = 0

    # Metodo contructor
    def __init__(self, radio):
        self.radio = radio

    def mostrar_info(self):
        print("El area es: ", 3.1416*self.radio**2, "m^2")
        print("El perimetro es: ", 2*self.radio*3.1416, "m")