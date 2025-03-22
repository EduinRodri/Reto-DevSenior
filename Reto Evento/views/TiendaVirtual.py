import tkinter as tk
from tkinter import messagebox
from model.producto import Producto
from model.carrito import Carrito

class TiendaVirtual(tk.Tk):
    def __init__(self, productos):
        super().__init__()

        self.title("Tienda Virtual de Electrónicos")
        self.geometry("600x400")

        # Colores pasteles
        fondo_color = "#E6E6FA"  # Lavanda
        boton_color = "#D8BFD8"  # Thistle

        self.configure(bg=fondo_color)

        self.productos_frame = tk.Frame(self, bg=fondo_color)
        self.productos_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.productos_frame.pack_propagate(False)

        self.info_producto = tk.StringVar()
        self.info_producto.set("Seleccione un producto para ver los detalles")

        self.info_label = tk.Label(self, textvariable=self.info_producto, bg=fondo_color, anchor='w')
        self.info_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.agregar_carrito_button = tk.Button(self, text="Agregar al Carrito", command=self.agregar_producto, bg=boton_color)
        self.agregar_carrito_button.pack_forget()  # Ocultar el botón inicialmente

        self.producto_seleccionado = None
        self.carrito = []

        for producto in productos:
            producto_button = tk.Button(
                self.productos_frame,
                text=producto.get_nombre(),
                command=lambda p=producto: self.mostrar_info_producto(p),
                bg=boton_color,
                anchor='w'
            )
            producto_button.pack(fill=tk.X, pady=5)

        self.carrito_text = tk.Text(self, height=10, width=30, bg=fondo_color)
        self.carrito_text.insert(tk.END, "Carrito de compras:\n")
        self.carrito_text.config(state=tk.DISABLED)
        self.carrito_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.botones_frame = tk.Frame(self, bg=fondo_color)
        self.botones_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.comprar_button = tk.Button(self.botones_frame, text="Realizar Compra", command=self.realizar_compra, bg=boton_color)
        self.comprar_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.vaciar_carrito_button = tk.Button(self.botones_frame, text="Vaciar Carrito", command=self.vaciar_carrito, bg=boton_color)
        self.vaciar_carrito_button.pack(side=tk.LEFT, padx=10, pady=10)

    def mostrar_info_producto(self, producto):
        self.producto_seleccionado = producto
        self.info_producto.set(f"Nombre: {producto.get_nombre()}\nPrecio: ${producto.get_precio()}\nStock: {producto.get_stock()}")
        self.agregar_carrito_button.pack(side=tk.TOP, padx=10, pady=10)

    def agregar_producto(self):
        if self.producto_seleccionado:
            carrito_item = Carrito(1, self.producto_seleccionado.get_nombre(), 1)  # Asumimos id_usuario = 1
            self.carrito.append(carrito_item)
            self.carrito_text.config(state=tk.NORMAL)
            self.carrito_text.insert(tk.END, f"- {carrito_item.get_id_producto()} - ${self.producto_seleccionado.get_precio()} (Stock: {self.producto_seleccionado.get_stock()})\n")
            self.carrito_text.config(state=tk.DISABLED)
            self.producto_seleccionado = None
            self.agregar_carrito_button.pack_forget()

    def realizar_compra(self):
        messagebox.showinfo("Compra Realizada", "¡Gracias por su compra!")
        self.vaciar_carrito()

    def vaciar_carrito(self):
        self.carrito.clear()
        self.carrito_text.config(state=tk.NORMAL)
        self.carrito_text.delete("1.0", tk.END)
        self.carrito_text.insert(tk.END, "Carrito de compras:\n")
        self.carrito_text.config(state=tk.DISABLED)

    def ver_carrito(self):
        productos_en_carrito = "\n".join([f"- {item.get_id_producto()} (Cantidad: {item.get_cantidad()})" for item in self.carrito])
        messagebox.showinfo("Carrito de Compras", f"Productos en el carrito:\n{productos_en_carrito}")
