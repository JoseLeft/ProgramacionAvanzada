import tkinter as tk
from productos import Producto
from excepciones import ProductoInvalido, PrecioInvalido, CantidadInvalida
from typing import List

lista_productos: List[Producto]= []

def registrar():

    global producto
    try:
        nombre=str(entry_producto.get())
        precio=float(entry_precio.get())
        cantidad=int(entry_cantidad.get())

        if(nombre == ""):
            raise ProductoInvalido
        
        elif(precio <= 0):
            raise PrecioInvalido
        
        elif(cantidad < 0):
            raise CantidadInvalida
        
        producto=Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        lista_productos.append(producto)
        label_mensaje.config(text="Producto registrado correctamente", bg="green2")

    except ProductoInvalido as e:
        label_mensaje.config(text=e, bg="red")
    except PrecioInvalido as ep:
        label_mensaje.config(text=ep, bg="red")
    except CantidadInvalida as ec:
        label_mensaje.config(text=ec, bg="red")
    except ValueError:
        label_mensaje.config(text="Ingresaste un valor no valido", bg="red")


def mostrar_precio_total():
    precio_total=0
    for producto in lista_productos:
        precio_total=precio_total + producto.calcular_valor_total()
    label_mensaje.config(text=f"Precio total en el inventario: ${precio_total}", bg="green2")

def detalles_producto():
    try:
        label_mensaje.config(text=producto.mostrar_detalles(), bg="deep sky blue")
    except NameError:
        label_mensaje.config(text="Producto no registrado", bg="orange red")

ventana=tk.Tk()
ventana.title("Inventario")
ventana.geometry("700x600")
ventana.config(bg="snow")

label_titulo = tk.Label(ventana, text="Gestion de productos", bg="dodger blue", fg="black", font=("Arial", 16), relief="sunken")
label_titulo.pack(pady=5)

label_producto = tk.Label(ventana, text="Nombre del producto", bg="cyan2", fg="black", font=("Arial", 12))
label_producto.pack(pady=5)
entry_producto = tk.Entry(ventana)
entry_producto.pack(pady=5)

label_precio = tk.Label(ventana, text="Precio del producto", bg="cyan2", fg="black", font=("Arial", 12))
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack(pady=5)

label_cantidad = tk.Label(ventana, text="Cantidad en inventario", bg="cyan2",fg="black", font=("Arial", 12))
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=5)

boton_registrar = tk.Button(ventana, text="Registrar producto", bg="lawn green", fg="black", font=("Arial", 12), command=registrar)
boton_registrar.pack(pady=5)

boton_precio_total = tk.Button(ventana, text="Precio total en inventario", bg="lawn green", fg="black", font=("Arial", 12), command=mostrar_precio_total)
boton_precio_total.pack(pady=5)

boton_detalles_producto = tk.Button(ventana, text="Detalles del producto agregado", bg="lawn green", fg="black", font=("Arial", 12), command=detalles_producto)
boton_detalles_producto.pack(pady=5)

label_mensaje=tk.Label(ventana, text="", bg="gold2", fg="black", font=("Arial", 12), relief="solid")
label_mensaje.pack(pady=5)

ventana.mainloop()