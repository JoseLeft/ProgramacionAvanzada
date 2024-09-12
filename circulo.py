class Circulo:
    radio = 0

    # Metodo contructor
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print("El radio es de: ", self.radio)
        print("El area es: ", 3.1416*self.radio**2, "m^2")

    def calcular_perimetro(self):
        print("El perimetro es: ", 2*self.radio*3.1416, "m")