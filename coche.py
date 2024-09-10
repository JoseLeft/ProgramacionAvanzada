class Coche:
    marca = ""
    modelo = ""
    ano = 0

    # Metodo constructor 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        # Primer metodo
        def mostrar_info(self):
            print("Marca: ", self.marca )
            print("Modelo: ", self.modelo)
            print("Ano: ", self.ano)


