class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        total=self.precio*self.cantidad
        return total

    def mostrar_detalles(self):
        info=f"Nombre del producto: {self.nombre}\nPrecio por unidad: ${self.precio}\nCantidad en inventario: {self.cantidad}\nPrecio total: ${self.precio*self.cantidad}"
        return info