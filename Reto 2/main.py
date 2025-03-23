# Constantes
from datetime import date
import os
import platform

SEPARADOR_ELEMENTO = "~"
SEPARADOR_TABLA = "~~~"
PROPIEDAD = "|"
HEADER = "||"
AUTOINCREMENT = "(]"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
CARACTERES_RECERVADOS = [
    SEPARADOR_ELEMENTO, PROPIEDAD, AUTOINCREMENT
]

SEPARADOR_MENU = "══════════════════════════════════════════════"

MENU_PRINCIPAL = '''
==== Bienvenido a 🐾Huella Feliz🐾 ====
1. 🤵 Clientes
2. 👨‍⚕️ Veterinarios
3. 🐾 Mascotas
4. ⚙️ Servicios
5. 📆 Agendar citas
6. 🕜 Historial de citas (General)
7. 🔙 Salir
'''

MENU_CLIENTE = f'''
{SEPARADOR_MENU}
      👤 GESTIÓN DE CLIENTES
{SEPARADOR_MENU}

1️⃣  🆕 Registrar cliente
2️⃣  ✏️ Modificar cliente
3️⃣  🔍 Consultar clientes
4️⃣  🗑️ Eliminar cliente
5️⃣  🔙 Volver al menú principal

{SEPARADOR_MENU}
'''


MENU_VETERINARIO = '''
=== Veterinario ===
1. 🆕 Registrar veterinario
2. ✏️ Modificar veterinario
3. 🔍 Consultar veterinarios
4. 🗑️ Eliminar veterinario
5. 🔙 Salir
'''

MENU_MASCOTA = f'''
{SEPARADOR_MENU}
      🐶 GESTIÓN DE MASCOTAS
{SEPARADOR_MENU}

1️⃣  🆕 Registrar mascota
2️⃣  ✏️ Modificar mascota
3️⃣  🔍 Consultar mascotas
4️⃣  🗑️ Eliminar mascota
5️⃣  🔙 Volver al menú principal

{SEPARADOR_MENU}
'''


MENU_SERVICIOS = f'''
{SEPARADOR_MENU}
      🏥 GESTIÓN DE SERVICIOS
{SEPARADOR_MENU}

1️⃣  👀 Ver servicios
2️⃣  🆕 Registrar servicio
3️⃣  ✏️ Modificar servicio
4️⃣  🗑️ Eliminar servicio
5️⃣  🔙 Volver al menú principal

{SEPARADOR_MENU}
'''

MENU_AGENDAR_CITA = '''
=== Agendar Cita ===
1. 📅 Seleccionar Fecha
2. 👨‍⚕️ Seleccionar Veterinario
3. ⚙️ Seleccionar Servicio
4. 🐾 Seleccionar Mascota
5. 🤵 Seleccionar Cliente
6. ✅ Aceptar
7. ❌ Cancelar
'''

# funciones fundamentales para clases
def borrarConsola():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def isFloat(valor: str):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Clases
class Persona:
    def __init__(self, nombre, contacto, identidad):
        self.__nombre = nombre
        self.__contacto = contacto
        self.id = identidad
        
    # se definiran los geters y seters 
    def getNombre (self):
        return self.__nombre
    
    def getContacto (self):
        return self.__contacto
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setContacto(self, contacto):
        self.__contacto = contacto
    # ? La funcion toArray esta presente en todas las clases que se almacenan en los datos 
    def toArray (self):
        return [self.__nombre, self.__contacto, str(self.id)]

class Cliente(Persona):
    def __init__(self, nombre, contacto, identidad, direccion):
        super().__init__(nombre, contacto, identidad)
        self.__direccion = direccion
    
    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def toArray(self):
        array = super().toArray()
        array.append(self.__direccion)
        return array
    
class Veterinario(Persona):
    def __init__(self, nombre, contacto, identidad, especialidad, licencia, horario):
        super().__init__(nombre, contacto, identidad)
        self.__especialidad = especialidad
        self.__licencia = licencia
        self.__horario = horario
    
    def getEspecialidad(self):
        return self.__especialidad

    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad

    def getLicencia(self):
        return self.__licencia

    def setLicencia(self, licencia):
        self.__licencia = licencia

    def getHorario(self):
        return self.__horario

    def setHorario(self, horario):
        self.__horario = horario
    
    def obtenerDia (self, dia: str):
        index = DIAS.index(dia)
        if self.__horario[index] == "1":
            return True
        return False
    
    def toArray(self):
        array = super().toArray()
        array.append(self.__especialidad)
        array.append(self.__licencia)
        array.append(self.__horario)
        return array

# * La clase Mascota en adelante no son extenciones de persona pero esta, servicios y citas se toman como tal en
# * la clase Datos
class Mascota:
    def __init__(self, nombre, especie, raza, edad, identidad, dueno):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__identidad = identidad
        self.__dueno = dueno

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie

    def getRaza(self):
        return self.__raza

    def setRaza(self, raza):
        self.__raza = raza

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getIdentidad(self):
        return self.__identidad

    def setIdentidad(self, identidad):
        self.__identidad = identidad

    def getDueno(self):
        return self.__dueno

    def setDueno(self, dueno):
        self.__dueno = dueno

    def toArray(self):
        return [self.__nombre, self.__especie, self.__raza, self.__edad, self.__identidad, self.__dueno]


class Servicio:
    def __init__(self, tipo, descripcion, duracion, costo, frecuencia):
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__duracion = duracion
        self.__costo = costo
        self.__frecuencia = frecuencia
    
    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getDuracion(self):
        return self.__duracion

    def setDuracion(self, duracion):
        self.__duracion = duracion

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo

    def getFrecuencia(self):
        return self.__frecuencia

    def setFrecuencia(self, frecuencia):
        self.__frecuencia = frecuencia
    
    def toArray(self):
        return [self.__tipo, self.__descripcion, self.__duracion, self.__costo, self.__frecuencia]


class Cita:
    def __init__(self, fecha:str, hora, servicio, veterinario, id_mascota):
        self.__fecha = fecha
        self.__hora = hora
        self.__servicio = servicio
        self.__veterinario = veterinario
        self.__id_mascota = id_mascota
        try:
            formato = fecha.split("@")
            self.__ciclo = int(formato[0])
            self.__dia = int(formato[1])
        except (ValueError, IndexError):
            print("Hay un dato corrupto en las fechas de las citas por favor revise su base de datos o reiniciela")
            self.__ciclo = 0
            self.__dia = 0

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha:str):
        self.__fecha = fecha
        formato = fecha.split("@")
        self.__ciclo = formato[0]
        self.__dia = formato[1]
    
    def getDia (self):
        return int(self.__dia)

    def setDia (self, dia):
        self.__dia = dia
        self.__fecha = str(self.__ciclo) + "@" + str(dia)
    
    def getCiclo (self):
        return self.__ciclo
    
    def setCiclo(self, ciclo):
        self.__ciclo = ciclo
        self.__fecha = str(ciclo) + "@" + str(self.__dia)

    def getHora(self):
        return self.__hora

    def setHora(self, hora):
        self.__hora = hora

    def getServicio(self):
        return self.__servicio

    def setServicio(self, servicio):
        self.__servicio = servicio

    def getVeterinario(self):
        return self.__veterinario

    def setVeterinario(self, veterinario):
        self.__veterinario = veterinario

    def getIdMascota(self):
        return self.__id_mascota

    def setIdMascota(self, id_mascota):
        self.__id_mascota = id_mascota
    
    def toArray(self):
        return [self.__fecha, self.__hora, self.__servicio, self.__veterinario, self.__id_mascota]
    
# * Este error personalizado debe saltar cuando el usuario dijita un caracter apartado por el sistema
# Char = Character que significa caracter
# Error de caracter recervado
class RecervedCharError (Exception):
    def __init__(self):
        mensaje = "Error: No se admiten los siguientes caracteres para los valores de entrada: "
        for caracter in CARACTERES_RECERVADOS:
            mensaje += f"{caracter}, "
        super().__init__(mensaje)

# * Esta clase es utilizada por Formulario como los campos que se van a preguntar
# Esta clase usa diferentes tipos, aqui se definen y cual es su funcion
# str (o cualquier otro no admitido): Recibe cualquier cosa que escriba el usuario y se le devolvera al programador un string
# int: Recibira unicamente numeros del usuario y se le entregara al programador un int
# float: Recibira unicamente numeros del usuario y se entregara al programador un float
# boolean: Hara una pregunta de si y no al usuario y se devolvera al programador True si respondio si y False si respondio no
class PropiedadFormulario:
    def __init__(self, titulo, tipo, callback = None, invalido = ""):
        self.titulo = titulo
        self.tipo = tipo
        self.callback = callback
        self.invalido = invalido


# * La clase formulario se usa para facilitar las peticiones de datos al usuario
class Formulario:
    def __init__(self, titulo:str, campos:list[PropiedadFormulario]):
        self.__titulo = titulo
        self.__campos = campos
    
    
    def agregarCampo(self, titulo:str, valor:str, callback = None, invalido=""): 
        prop = PropiedadFormulario(titulo, valor)
        if callback != None:
            prop.callback = callback
            prop.invalido = invalido
        self.__campos.append(prop)
    
    def modificarCampo(self, titulo:str, tipo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                campo.tipo = tipo
    
    def eliminarCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                self.__campos.remove(campo)
    
    def obtenerCampo(self, titulo:str):
        for campo in self.__campos:
            if campo.titulo == titulo:
                return campo
    
    # * Esta funcion es importante, se debe usar para realizar todo el formulario y pedir la informacion al usuario
    def realizar(self):
        print(self.__titulo)
        formulario: dict[str, str | int | float | bool] = {}
        for campo in self.__campos:
            while True:
                texto = campo.titulo + ": "
                error = "Valor incorrecto"
                if campo.tipo == "boolean":
                    print(campo.titulo)
                    print("1. Sí")
                    print("2. No")
                    texto = "Respuesta: "
                respuesta = input(texto)
                try:
                    valorCorrecto = True
                    valorIngresar = ""
                    
                    # validamos que el campo ingresado sea un valor admitido por el formulario
                    if campo.tipo == "int":
                        if respuesta.isnumeric():
                            valorIngresar = int(respuesta)
                        else:
                            valorCorrecto = False
                            error = "El valor debe ser un número entero"
                    elif campo.tipo == "float":
                        if isFloat(respuesta):
                            valorIngresar = float(respuesta)
                        else:
                            valorCorrecto = False
                            error = "El valor debe ser un numero decimal"
                    elif campo.tipo == "boolean":
                        if respuesta == "1" or respuesta == "Si" or respuesta == "si" or respuesta == "SI":
                            valorIngresar = True
                        elif respuesta == "2" or respuesta == "No" or respuesta == "no" or respuesta == "NO":
                            valorIngresar = False
                        else: 
                            valorCorrecto = False
                            
                    else:
                        for caracter in CARACTERES_RECERVADOS:
                            if caracter in respuesta:
                                raise RecervedCharError
                        valorIngresar = respuesta

                    boo = True
                    if campo.callback != None:
                        boo = campo.callback(respuesta)
                        valorCorrecto = boo
                        if campo.invalido != "":
                            error = campo.invalido
                            
                    if boo:
                        formulario[campo.titulo] = valorIngresar
                        pass
                            

                    if not valorCorrecto:
                        raise ValueError(error)
                    break
                except (ValueError, RecervedCharError) as e:
                    print(e)
                    
                
        return formulario

    
# * La clase datos es la encargada de almacenar la informacion que ingrese el usuario
class Datos:
    use = ""
    __state = "fine"
    __ciclo = 0
    __tablas: dict[str, list[Persona]] = {
        "clientes": [],
        "veterinarios": [],
        "mascotas": [],
        "servicios": [],
        "citas": []
    }
    __autoincrement: dict[str, int] = {
        "clientes": 0,
        "veterinarios": 0,
        "mascotas": 0,
        "servicios": 0,
        "citas": 0,
        "ciclo": 0
    }
    def __init__(self):
        try:
            with open("datos.txt", "r") as datos:
                text = datos.read()
                if text != "":
                    # Primero separamos los datos por cada tabla
                    tablasContenido = text.split(SEPARADOR_TABLA)
                    for tabla in tablasContenido:
                        # A cada tabla la separamos por header y contenido
                        split = tabla.split(HEADER)

                        if len(split) > 1:
                            # Dividimos el header partiendolo para conseguir de un lado el titulo y del otro el autoincrement de la id
                            header = split[0].split(AUTOINCREMENT)
                            titulo = header[0]
                            autoincrement = int(header[1])
                            contenidoTexto = split[1]
                            contenido = contenidoTexto.split(SEPARADOR_ELEMENTO)

                            self.__autoincrement[titulo] = autoincrement

                            for elemento in contenido:
                                propiedades = elemento.split(PROPIEDAD)
                                if len(propiedades) > 1:
                                    if titulo == "ciclo":
                                        self.__ciclo = int(propiedades[0])
                                    elif titulo == "clientes":
                                        cliente = Cliente(propiedades[0], propiedades[1], int(propiedades[2]), propiedades[3])
                                        self.__tablas["clientes"].append(cliente)
                                    elif titulo == "veterinarios":
                                        veterinario = Veterinario(propiedades[0], propiedades[1], int(propiedades[2]), propiedades[3], propiedades[4], propiedades[5])
                                        self.__tablas["veterinarios"].append(veterinario)
                                    elif titulo == "mascotas":
                                        mascota = Mascota(propiedades[0], propiedades[1], propiedades[2], propiedades[3], int(propiedades[4]), int(propiedades[5]))
                                        self.__tablas["mascotas"].append(mascota)
                                    elif titulo == "servicios":
                                        servicio = Servicio(propiedades[0], propiedades[1], propiedades[2], propiedades[3], propiedades[4])
                                        self.__tablas["servicios"].append(servicio)
                                    elif titulo == "citas":
                                        cita = Cita(propiedades[0], propiedades[1], propiedades[2], int(propiedades[3]), int(propiedades[4]))
                                        self.__tablas["citas"].append(cita)
        except FileNotFoundError:
            with open("datos.txt", "w") as datos:
                print("Archivo de datos creado correctamente vuelva a ejecutar el programa")
                self.__state = "reload"

        except ValueError:
            print("Parece que la base de datos esta corrupta vuelva a intentarlo")
            self.__state = "error"

    def getCiclo (self):
        return self.__ciclo
    
    def setCiclo (self, num:int):
        self.__ciclo = num

    def obtenerEstado (self):
        return self.__state

    def obtener(self, index: int):
        result = self.__tablas[self.use][index]
        return result
    
    def guardar(self):
        with open("datos.txt", "w") as datos:
            datos.write(f"ciclo{AUTOINCREMENT}0{HEADER}{self.__ciclo}{PROPIEDAD}{SEPARADOR_ELEMENTO}{SEPARADOR_TABLA}")
            for key in self.__tablas:
                texto = key + AUTOINCREMENT + str(self.__autoincrement[key]) + HEADER
                for elemento in self.__tablas[key]:
                    iterable = elemento.toArray()
                    for propiedad in iterable:
                        texto += propiedad + PROPIEDAD
                    texto += SEPARADOR_ELEMENTO
                texto += SEPARADOR_TABLA
                datos.write(texto)

    def eliminar(self, index: int):
        self.__tablas[self.use].pop(index)
    
    def largo (self):
        return len(self.__tablas[self.use])
    
    def agregar(self, elemento: Persona):
        elemento.id = self.__autoincrement[self.use]
        self.__autoincrement[self.use] += 1
        self.__tablas[self.use].append(elemento)

    def obtenerTabla (self):
        return self.__tablas[self.use]

    def obtenerPorId (self, id):
        resultado: Persona
        if self.use == "servicios" or self.use == "citas":
            return self.obtener(id)
        for element in self.__tablas[self.use]:
            if element.id == id:
                resultado = element
                pass
            pass
        return resultado
    
    def eliminarPorId (self, id):
       for i, element in enumerate(self.__tablas[self.use]):
            if element.id == id:
                self.__tablas[self.use].pop(i)
                pass
            pass

    
    def horarioVeterinario(self, idVeterinario: int):
        # TODO: Probar que el sistema de horario funcione
        horario: list[bool] = [
            False, False, False, False, False, False
        ]
        for i in len(self.__tablas['citas']):
            cita: Cita = self.__tablas['cita'][i]
            if cita.getVeterinario() == idVeterinario and self.__ciclo == cita.getCiclo():
                horario[cita.getFecha()] = True
        return horario
    

    def getDiaHorarioVeterinario (self, idVeterinario: int, dia: int):
        retorno = False
        for i in len(self.__tablas['citas']):
            cita: Cita = self.__tablas['cita'][i]
            if cita.getVeterinario() == idVeterinario and self.__ciclo == cita.getCiclo() and cita.getDia() == dia:
                retorno = True
        return retorno


# * esta funcion define si la fecha1 es una fecha anterior a fecha2
def fechaAnterior(fecha1: date, fecha2: date):
    if fecha1.year < fecha2.year:
        return True
    elif fecha1.month < fecha2.month and fecha1.year == fecha2.year:
        return True
    elif fecha1.day < fecha2.day and fecha1.month == fecha2.month and fecha1.month == fecha2.month:
        return True
    return False
        
# * Esta funcion se usa para mostrar una tabla que sea extencion de persona o la tabla mascota
def mostrarTabla(tabla: list[Persona]):
    for i in range(len(tabla)):
        print(f"{i + 1}. {tabla[i].getNombre()}")

# * Esta funcion se usa para mostrar una lista de servicios
def mostrarServicios (servicios: list[Servicio]):
    for i in range(len(servicios)):
        servicio: Servicio = servicios[i]
        print(f"{i+1} - {servicio.getDescripcion()}")
        pass

# * Esta funcion realiza una pregunta de si y no al usuario y devuelve True si la respuesta es si y False si es no
def preguntar (pregunta: str):
    print(pregunta)
    print("1. Si")
    print("2. No")
    respuesta = input("Seleccione una opcion")
    if respuesta == "Si" or respuesta == "SI" or respuesta == "si" or respuesta == "1":
        return True
    else:
        return False

def pedirNumero (pregunta: str):
    retorno = 0
    while True:
        opcion = input(pregunta)
        if opcion.isnumeric():
            opcion = int(opcion)
        elif isFloat(opcion):
            opcion = float(opcion)
        else: 
            print("Opcion invalida")
            continue
        retorno = opcion
        break
    return retorno

#Funciones menus secundarios

def menuClientes(datos: Datos):
    datos.use = "clientes"

    def seleccionarCliente():
        print("══════════════════════════════════════════════")
        print(" 📌 SELECCIONAR CLIENTE ")
        print("══════════════════════════════════════════════")
        mostrarTabla(datos.obtenerTabla())
        
        while True:
            opcion = input("\n🔢 Número del cliente: ")
            if opcion.isnumeric():
                cliente = int(opcion) - 1
                if 0 <= cliente < datos.largo():
                    return cliente
                else:
                    print("⚠️ Número fuera de rango.")
            else:
                print("⚠️ Ingrese un número válido.")

    while True:
        borrarConsola()
        print("══════════════════════════════════════════════")
        print(" 👤 GESTIÓN DE CLIENTES ")
        print("══════════════════════════════════════════════")
        print(MENU_CLIENTE)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Registrar cliente
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🆕 REGISTRO DE NUEVO CLIENTE ")
            print("══════════════════════════════════════════════")

            formulario = Formulario("\nRegistrar cliente\n", [])
            formulario.agregarCampo("\nNombre", "str", lambda x: len(x) >= 2, "Debe tener al menos 2 caracteres.")
            formulario.agregarCampo("\nTeléfono", "str", lambda x: len(str(x)) == 10, "Debe tener 10 dígitos.")
            formulario.agregarCampo("\nDirección", "str", lambda x: len(x) >= 5, "Debe tener al menos 5 caracteres.")

            resultado = formulario.realizar()
            nombre = resultado["\nNombre"]
            telefono = resultado["\nTeléfono"]
            direccion = resultado["\nDirección"]

            cliente = Cliente(nombre, telefono, datos.largo(), direccion)
            datos.agregar(cliente)
            datos.guardar()

            print("\n✅ Cliente registrado con éxito.")
            input("\n🔙 Presione Enter para continuar...")

        elif opcion == "2":  # Modificar cliente
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" ✏️ MODIFICAR CLIENTE ")
            print("══════════════════════════════════════════════")

            clienteIndex = seleccionarCliente()
            if clienteIndex is not None:
                clienteSeleccionado: Cliente = datos.obtener(clienteIndex)
                print(f"\n✏️ Editando cliente: {clienteSeleccionado.getNombre()}")

                formulario = Formulario("\nModificar cliente", [])
                formulario.agregarCampo("\nNombre", "str", lambda x: len(x) == 0 or len(x) >= 2)
                formulario.agregarCampo("\nTeléfono", "str", lambda x: len(str(x)) == 10 or len(str(x)) == 0)
                formulario.agregarCampo("\nDirección", "str", lambda x: len(x) == 0 or len(x) >= 5)

                resultado = formulario.realizar()

                if resultado["\nNombre"]:
                    clienteSeleccionado.setNombre(resultado["\nNombre"])
                if resultado["\nTeléfono"]:
                    clienteSeleccionado.setContacto(resultado["\nTeléfono"])
                if resultado["\nDirección"]:
                    clienteSeleccionado.setDireccion(resultado["\nDirección"])

                datos.guardar()
                print("\n✅ Cliente modificado con éxito.")
                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "3":  # Listar clientes
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 📋 LISTADO DE CLIENTES ")
            print("══════════════════════════════════════════════")
            mostrarTabla(datos.obtenerTabla())

            clienteIndex = seleccionarCliente()
            if clienteIndex is not None:
                clienteSeleccionado: Cliente = datos.obtener(clienteIndex)

                print("══════════════════════════════════════════════")
                print(f" 📋 DETALLES DEL CLIENTE: {clienteSeleccionado.getNombre()} ")
                print("══════════════════════════════════════════════")
                print(f"\n📌 Nombre: {clienteSeleccionado.getNombre()}")
                print(f"\n📞 Teléfono: {clienteSeleccionado.getContacto()}")
                print(f"\n📍 Dirección: {clienteSeleccionado.getDireccion()}")

            input("\n🔙 Presione Enter para continuar...")

        elif opcion == "4":  # Eliminar cliente
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🗑️ ELIMINAR CLIENTE ")
            print("══════════════════════════════════════════════")

            clienteIndex = seleccionarCliente()
            if clienteIndex is not None:
                clienteSeleccionado: Cliente = datos.obtener(clienteIndex)
                print(f"\n⚠️ ¿Está seguro de eliminar a {clienteSeleccionado.getNombre()}?")
                print("\n1️⃣ Sí, eliminar cliente")
                print("2️⃣ No, cancelar operación")

                opcion = input("\nSeleccione una opción: ")
                if opcion == "1":
                    datos.eliminar(clienteIndex)
                    datos.guardar()
                    print("\n✅ Cliente eliminado con éxito.")
                elif opcion == "2":
                    print("\n⚠️ Operación cancelada.")
                else:
                    print("\n⚠️ Opción no válida. Intente de nuevo.")

                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "5":  # Salir
            break

        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")
            input("\n🔙 Presione Enter para continuar...")


def menuVeterinario(datos: Datos):
    datos.use = "veterinarios"
    especialidades = ["Cardiologia", "Dermatologia", "Neurologia", "Oftalmologia", "Oncologia", "Ortopedia"]

    def seleccionarVeterinario():
        print("Seleccione el veterinario")
        mostrarTabla(datos.obtenerTabla())
        while True:
            try:
                opcion = input("Veterinario: ")
                if opcion.isnumeric(): 
                    veterinario = int() - 1
                    break
                else:
                    raise ValueError("Valor incorrecto digitado")
            except ValueError as e:
                print(e)

        return veterinario
    
    while True:
        borrarConsola()
        print(MENU_VETERINARIO)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            borrarConsola()
            # creamos el formulario y agregamos los campos
            formulario = Formulario("Registrar veterinario", [])
            formulario.agregarCampo("Nombre", "str", lambda x: len(x) >= 3 and x.isalpha(), 
            "El nombre no debe contener numeros y debe tener al menos 3 caracteres")
            formulario.agregarCampo("Contacto", "str", lambda x: len(x) == 8 or len(x) == 10 and x.isnumeric(),
            "El contacto debe tener 8 o 10 digitos y debe ser un numero")
            formulario.agregarCampo("Especialidad", "str", lambda x: x in especialidades,
            "La especialidad no es valida")
            formulario.agregarCampo("Licencia", "str", lambda x: len(x) == 10 and x.isnumeric(),
            "La licencia debe tener 10 digitos y debe ser un numero")

            # vamos a realizar un segundo formulario para obtener el horario de atención
            formularioHorario = Formulario("Horario de atención. ¿Tiene disponibilidad los siguientes dias?", [])
            for dia in DIAS:
                formularioHorario.agregarCampo(dia, "boolean")

            resultado = formulario.realizar()
            resultadoHorario =  formularioHorario.realizar()

            horario = ""
            for dia in resultadoHorario:
                if resultadoHorario[dia]:
                    horario += "1"
                else:
                    horario += "0"

            # obtenemos los valores del resultado del formulario
            nombre = resultado["Nombre"]
            contacto = resultado["Contacto"]
            especialidad = resultado["Especialidad"]
            licencia = resultado["Licencia"]

            veterinario = Veterinario(nombre, contacto, datos.largo(), especialidad, licencia, horario)
            datos.agregar(veterinario)
            datos.guardar()
            pass
        elif opcion == "2":
            borrarConsola()
            veterinario = seleccionarVeterinario()
            borrarConsola()
            veterinarioSeleccionado: Veterinario = datos.obtener(veterinario)
            print("Veterinario seleccionado: " + veterinarioSeleccionado.getNombre())
            formulario = Formulario("Modificar veterinario, Por favor ingrese los datos solicitados, deje en blanco para no modificar el valor", [])
            formulario.agregarCampo("Nombre", "str", lambda x: (len(x) >= 3 or len(x) == 0) and x.isalpha())
            formulario.agregarCampo("Contacto", "str", lambda x: (len(x) > 5 or len(x) == 0))
            formulario.agregarCampo("Especialidad", "str", lambda x: (x in especialidades or len(x) == 0))
            formulario.agregarCampo("Licencia", "str", lambda x: (len(x) == 10 or len(x) == 0) and x.isnumeric())

            resultado = formulario.realizar()
            horario = ""


            if input("¿Desea modificar tambien los horarios? (S/N)") == "S":
                formularioHorario = Formulario("Horario de atención. ¿Tiene disponibilidad los siguientes dias?", [])
                for dia in DIAS:
                    formularioHorario.agregarCampo(dia, "boolean")

                resultadoHorario =  formularioHorario.realizar()

                for dia in resultadoHorario:
                    if resultadoHorario[dia]:
                        horario += "1"
                    else:
                        horario += "0"
                veterinarioSeleccionado.setHorario(horario)

            listLambda = {
                "Nombre": lambda x: veterinarioSeleccionado.setNombre(x),
                "Contacto": lambda x: veterinarioSeleccionado.setContacto(x),
                "Especialidad": lambda x: veterinarioSeleccionado.setEspecialidad(x),
                "Licencia": lambda x: veterinarioSeleccionado.setLicencia(x)
            }

            for key in resultado:
                if resultado[key] != "":
                    listLambda[key](resultado[key])


            pass
        elif opcion == "3":
            borrarConsola()
            print("Consultar veterinarios")
            verVeterinario:Veterinario = datos.obtener(seleccionarVeterinario())
            borrarConsola()
            print("Nombre: " + verVeterinario.getNombre())
            print("Contacto: " + verVeterinario.getContacto())
            print("Especialidad: "+verVeterinario.getEspecialidad())
            print("Licencia: " + verVeterinario.getLicencia())
            print("Horario de atención:")
            for dia in DIAS:
                if verVeterinario.obtenerDia(dia):
                    print(dia)
            input("Precione entre para volver ")
            pass
        elif opcion == "4":
            borrarConsola()
            print("Eliminacion de veterinario")
            veterinarioSeleccionado = seleccionarVeterinario()
            borrarConsola()
            print("¿Esta seguro de eliminar a "+ datos.obtener(veterinarioSeleccionado).getNombre()+"?")
            print("1) Si")
            print("2) No")
            response = input("Seleccione una opcion: ")
            if response == "1" or response == "Si" or response == "SI" or response == "si":
                datos.eliminar(veterinarioSeleccionado)
            datos.guardar()
            pass
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
def menuMascotas(datos: Datos):
    datos.use = "mascotas"

    def seleccionarMascota():
        print("══════════════════════════════════════════════")
        print(" 📌 SELECCIONAR MASCOTA ")
        print("══════════════════════════════════════════════")
        mostrarTabla(datos.obtenerTabla())

        while True:
            opcion = input("\n🔢 Número de la mascota: ")
            if opcion.isnumeric():
                mascota = int(opcion) - 1
                if 0 <= mascota < datos.largo():
                    return mascota
                else:
                    print("⚠️ Número fuera de rango.")
            else:
                print("⚠️ Ingrese un número válido.")

    while True:
        borrarConsola()
        print(MENU_MASCOTA)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Registrar mascota
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🆕 REGISTRO DE NUEVA MASCOTA ")
            print("══════════════════════════════════════════════")

            formulario = Formulario("\nRegistrar mascota", [])
            formulario.agregarCampo("\nNombre", "str", lambda x: len(x) >= 2, "Debe tener al menos 2 caracteres.")
            formulario.agregarCampo("\nEspecie", "str", lambda x: len(x) >= 3, "Debe tener al menos 3 caracteres.")
            formulario.agregarCampo("\nRaza", "str", lambda x: len(x) >= 3, "Debe tener al menos 3 caracteres.")
            formulario.agregarCampo("\nEdad", "int", lambda x: int(x) > 0, "Debe ser un número mayor que 0.")
            formulario.agregarCampo("\nID del dueño", "int", lambda x: int(x) >= 0, "Debe ser un número positivo.")

            resultado = formulario.realizar()

            nombre = resultado["\nNombre"]
            especie = resultado["\nEspecie"]
            raza = resultado["\nRaza"]
            edad = resultado["\nEdad"]
            dueño = resultado["\nID del dueño"]

            mascota = Mascota(nombre, especie, raza, edad, datos.largo(), dueño)
            datos.agregar(mascota)
            datos.guardar()

            print("\n✅ Mascota registrada con éxito.")
            input("\n🔙 Presione Enter para continuar...")

        elif opcion == "2":  # Modificar mascota
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" ✏️ MODIFICAR MASCOTA ")
            print("══════════════════════════════════════════════")

            mascotaIndex = seleccionarMascota()
            if mascotaIndex is not None:
                mascotaSeleccionada: Mascota = datos.obtener(mascotaIndex)
                print(f"\n✏️ Editando mascota: {mascotaSeleccionada.getNombre()}")

                formulario = Formulario("\nModificar mascota", [])
                formulario.agregarCampo("\nNombre", "str", lambda x: len(x) == 0 or len(x) >= 2)
                formulario.agregarCampo("\nEspecie", "str", lambda x: len(x) == 0 or len(x) >= 3)
                formulario.agregarCampo("\nRaza", "str", lambda x: len(x) == 0 or len(x) >= 3)
                formulario.agregarCampo("\nEdad", "str", lambda x: int(x) > 0 or len(str(x)) == 0)
                formulario.agregarCampo("\nID del dueño", "int", lambda x: int(x) >= 0 or len(str(x)) == 0)

                resultado = formulario.realizar()

                if resultado["\nNombre"]:
                    mascotaSeleccionada.setNombre(resultado["\nNombre"])
                if resultado["\nEspecie"]:
                    mascotaSeleccionada.setEspecie(resultado["\nEspecie"])
                if resultado["\nRaza"]:
                    mascotaSeleccionada.setRaza(resultado["\nRaza"])
                if resultado["\nEdad"]:
                    mascotaSeleccionada.setEdad(resultado["\nEdad"])
                if resultado["\nID del dueño"]:
                    mascotaSeleccionada.setDueño(resultado["\nID del dueño"])

                datos.guardar()
                print("\n✅ Mascota modificada con éxito.")
                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "3":  # Consultar mascota
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 📋 CONSULTAR MASCOTA ")
            print("══════════════════════════════════════════════")

            mascotaIndex = seleccionarMascota()
            if mascotaIndex is not None:
                mascota: Mascota = datos.obtener(mascotaIndex)

                print("══════════════════════════════════════════════")
                print(f" 📋 INFORMACIÓN DE LA MASCOTA: {mascota.getNombre()} ")
                print("══════════════════════════════════════════════")
                print(f"\n🐾 Nombre: {mascota.getNombre()}")
                print(f"\n🦴 Especie: {mascota.getEspecie()}")
                print(f"\n🐕 Raza: {mascota.getRaza()}")
                print(f"\n🎂 Edad: {mascota.getEdad()} años")
                print(f"\n👤 ID Dueño: {mascota.getDueño()}")

            input("\n🔙 Presione Enter para volver...")

        elif opcion == "4":  # Eliminar mascota
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🗑️ ELIMINAR MASCOTA ")
            print("══════════════════════════════════════════════")

            mascotaIndex = seleccionarMascota()
            if mascotaIndex is not None:
                mascota = datos.obtener(mascotaIndex)
                print(f"\n⚠️ ¿Está seguro de eliminar a {mascota.getNombre()}?")
                print("\n1️⃣ Sí, eliminar mascota")
                print("2️⃣ No, cancelar operación")

                respuesta = input("\nSeleccione una opción: ")
                if respuesta == "1":
                    datos.eliminar(mascotaIndex)
                    datos.guardar()
                    print("\n✅ Mascota eliminada con éxito.")
                elif respuesta == "2":
                    print("\n⚠️ Operación cancelada.")
                else:
                    print("\n⚠️ Opción no válida. Intente de nuevo.")

                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "5":  # Salir del menú
            break

        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")
            input("\n🔙 Presione Enter para continuar...")


def menuServicios(datos: Datos):
    datos.use = "servicios"

    def seleccionarServicio(needIndex=False):
        print("══════════════════════════════════════════════")
        print(" 📌 SELECCIONAR SERVICIO ")
        print("══════════════════════════════════════════════")
        mostrarServicios(datos.obtenerTabla())

        resultado = False
        while True:
            select = input("\n🔢 Seleccione un servicio (o presione Enter para volver): ")
            if select == "":
                borrarConsola()
                break
            elif select.isnumeric():
                borrarConsola()
                index = int(select) - 1
                servicioSeleccionado: Servicio = datos.obtener(index)
                resultado = servicioSeleccionado if not needIndex else index
                break
            else:
                print("⚠️ Opción no válida. Ingrese un número o presione Enter para volver.")
        return resultado

    while True:
        borrarConsola()
        print(MENU_SERVICIOS)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Ver servicios
            borrarConsola()
            servicioSeleccionado = seleccionarServicio()
            if servicioSeleccionado:
                print("══════════════════════════════════════════════")
                print(" 📋 INFORMACIÓN DEL SERVICIO ")
                print("══════════════════════════════════════════════")
                print(f"\n📄 Descripción: {servicioSeleccionado.getDescripcion()}")
                print(f"\n🛠️ Tipo: {servicioSeleccionado.getTipo()}")
                print(f"\n⏳ Duración: {servicioSeleccionado.getDuracion()} minutos")
                print(f"\n📆 Frecuencia: {servicioSeleccionado.getFrecuencia()} meses")
                print(f"\n💰 Costo: ${servicioSeleccionado.getCosto()}")
                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "2":  # Registrar servicio
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🆕 REGISTRO DE SERVICIO ")
            print("══════════════════════════════════════════════")

            formulario = Formulario("\nRegistrar Servicio", [])
            formulario.agregarCampo("\nTipo de servicio", "str", lambda x: len(x) >= 3, "Debe tener al menos 3 caracteres.")
            formulario.agregarCampo("\nDescripción del servicio", "str", lambda x: len(x) >= 3, "Debe tener al menos 3 caracteres.")
            formulario.agregarCampo("\nDuración en minutos", "float")
            formulario.agregarCampo("\nFrecuencia óptima en meses", "float")
            formulario.agregarCampo("\nCosto del servicio", "float")

            realizar = formulario.realizar()
            tipo = realizar["\nTipo de servicio"]
            descripcion = realizar["\nDescripción del servicio"]
            duracion = realizar["\nDuración en minutos"]
            frecuencia = realizar["\nFrecuencia óptima en meses"]
            costo = realizar["\nCosto del servicio"]

            nuevoServicio = Servicio(tipo, descripcion, duracion, costo, frecuencia)
            datos.agregar(nuevoServicio)
            datos.guardar()

            print("\n✅ Servicio registrado con éxito.")
            input("\n🔙 Presione Enter para continuar...")

        elif opcion == "3":  # Modificar servicio
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" ✏️ MODIFICAR SERVICIO ")
            print("══════════════════════════════════════════════")

            servicioSeleccionado = seleccionarServicio()
            if servicioSeleccionado:
                formulario = Formulario(
                    "Modificar Servicio (Presione Enter sin escribir nada para dejarlo igual)", []
                )
                formulario.agregarCampo("\nTipo", "str", lambda x: len(x) == 0 or len(x) > 3, "Debe tener al menos 3 caracteres.")
                formulario.agregarCampo("\nDescripción", "str", lambda x: len(x) == 0 or len(x) > 3, "Debe tener al menos 3 caracteres.")
                formulario.agregarCampo("\nDuración", "float")
                formulario.agregarCampo("\nFrecuencia", "float")
                formulario.agregarCampo("\nCosto", "float")

                realizar = formulario.realizar()
                listLambda = {
                    "\nTipo": lambda x: servicioSeleccionado.setTipo(x),
                    "\nDescripción": lambda x: servicioSeleccionado.setDescripcion(x),
                    "\nDuración": lambda x: servicioSeleccionado.setDuracion(x),
                    "\nFrecuencia": lambda x: servicioSeleccionado.setFrecuencia(x),
                    "\nCosto": lambda x: servicioSeleccionado.setCosto(x),
                }

                for element in realizar:
                    if realizar[element]:
                        listLambda[element](realizar[element])

                datos.guardar()
                print("\n✅ Servicio modificado con éxito.")
                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "4":  # Eliminar servicio
            borrarConsola()
            print("══════════════════════════════════════════════")
            print(" 🗑️ ELIMINAR SERVICIO ")
            print("══════════════════════════════════════════════")

            indexServicioSeleccionado = seleccionarServicio(True)
            if indexServicioSeleccionado is not False:
                deseaEliminar = input("⚠️ ¿Está seguro de eliminar este servicio? (S/N): ").strip().lower()
                if deseaEliminar == "s":
                    datos.eliminar(indexServicioSeleccionado)
                    datos.guardar()
                    print("\n✅ Servicio eliminado con éxito.")
                else:
                    print("\n⚠️ Operación cancelada.")

                input("\n🔙 Presione Enter para continuar...")

        elif opcion == "5":  # Salir
            break

        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")
            input("\n🔙 Presione Enter para continuar...")


def agendarCitas (datos: Datos):
    # TODO: Realizar el sistema de agendado de citas tomando en cuenta el horario del veterinario
    cliente: Cliente
    servicio: Servicio
    veterinario: Veterinario
    mascota: Mascota
    fechaDeCita = -1
    borrarConsola()

    def asignarVeterinario (opcion):
        borrarConsola()
        datos.use = "veterinarios"
        veterinarios: list[Veterinario] = datos.obtenerTabla()
        veterinariosDisponibles: list[Veterinario] = [] 
        for personal in veterinarios:
            if personal.obtenerDia(DIAS[opcion]) and not datos.getDiaHorarioVeterinario(personal.id, opcion):
                veterinariosDisponibles.append(personal)
                # Estos pass son solo para guiarme yo, por fis no lo quites
                pass
            pass
        # Supongo que ahora toca informar al usuario... Bueno aqui va
        print("Por favor seleccione un veterinario de los disponibles para el dia escogido")
        for i, personal in enumerate(veterinariosDisponibles):
            print(f"{i+1}. {personal.getNombre()}")
        seleccion: int = pedirNumero("Escriba aqui su eleccion: ") - 1 
        borrarConsola()
        return veterinariosDisponibles[seleccion]
    
    def asignarFecha ():
        # Al final decidi no agregar lo de la hora, me complique mucho aun sin la hora... 
        print("Seleccione un dia para la cita durante la semana en curso")
        for i, dia in enumerate(DIAS):
            print(f"{i+1}. {dia}")
        opcion = pedirNumero("Eleccion: ") - 1
        # se almacena la primera de las informaciones para agendar la cita
        return opcion

    while True:
        print(MENU_AGENDAR_CITA)
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            # * En seleccionar "Dia" tambien ira el seleccionar hora de la cita... Aunque aun no se si incluir esto
            fechaDeCita = asignarFecha()
            if veterinario is None:
                veterinario = asignarVeterinario(fechaDeCita)
            else:
                if veterinario.obtenerDia(DIAS[fechaDeCita]) and not datos.getDiaHorarioVeterinario(veterinario.id, fechaDeCita):
                    borrarConsola()
                else:
                    veterinario = asignarVeterinario(fechaDeCita)
                    
        elif opcion == "2":
            # * Seleccionar un veterinario implica seleccionar un dia que este trabaje
            print("Seleccionar Veterinario")
        elif opcion == "3":
            print("Seleccionar Servicio")
        elif opcion == "4":
            # * Al seleccionar una mascota se debe seleccionar automaticamente su dueño como cliente 
            print("Seleccionar Mascota")
        elif opcion == "5":
            # * Recuerda que si se selecciona un cliente el rango de busqueda de las mascotas se reduce a las de ese cliente
            print("Seleccionar Cliente")
        
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Main Programa
def main():
    while True:
        datos = Datos()
        # determinamos si la base de datos cargo correctamente
        if datos.obtenerEstado() != "fine":
            break
        borrarConsola()
        print(MENU_PRINCIPAL)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menuClientes(datos)
        elif opcion == "2":
            menuVeterinario(datos)
        elif opcion == "3":
            menuMascotas(datos)
        elif opcion == "4":
            menuServicios(datos)
        elif opcion == "5":
            agendarCitas(datos)
        elif opcion == "6":
            # TODO: Hay que realizar el menu de historial de citas
            print("Historial de citas")
        elif opcion == "7":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo. ⚠️")

if __name__ == "__main__":
    main()