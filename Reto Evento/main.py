from model.producto import Producto
import views.TiendaVirtual as tienda


product_list = [Producto("Laptop", 1000, 5), Producto("Mouse", 50, 10), Producto("Teclado", 100, 5)]

if __name__ == "__main__":
    app = tienda.TiendaVirtual(product_list)
    app.mainloop()