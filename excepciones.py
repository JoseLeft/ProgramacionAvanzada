class ProductoInvalido(Exception):
    def __init__(self):
        self.mensaje="Ingresa el nombre del producto"
        super().__init__(self.mensaje)


class PrecioInvalido(Exception):
    def __init__(self):
        self.mensaje="Ingresaste un precio incorrecto"
        super().__init__(self.mensaje)


class CantidadInvalida(Exception):
    def __init__(self):
        self.mensaje="Ingresaste una cantidad incorrecta"
        super().__init__(self.mensaje)