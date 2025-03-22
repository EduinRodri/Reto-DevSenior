class Carrito:
    def __init__(self, id_usuario, id_producto, cantidad):
        self.__id_usuario = id_usuario
        self.__id_producto = id_producto
        self.__cantidad = cantidad

    # Getters y Setters

    def get_id_usuario(self):
        return self.__id_usuario

    def get_id_producto(self):
        return self.__id_producto

    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
