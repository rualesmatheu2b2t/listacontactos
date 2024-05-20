class Contacto:
    """____________________________________________________________
    # aqui va el codigo
    ____________________________________________________________"""
    
    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefonos = []
        self.__palabras = []
        
    def contacto(self, nombre, apellido, direccion, correo, numero, palabra):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__apellido = direccion
        self.__correo = correo
        self.__telefonos.append(numero)
        self.__palabras.append(palabra)
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDireccion(self):
        return self.__direccion
    def getCorreo(self):
        return self.__correo
    def getTelefonos(self):
        return self.__telefonos
    def getPalabras(self):
        return self.__palabras
    def cambiarDireccion(self, direccion):
        self.__direccion = direccion
    def cambiarDireccion(self, correo):
        self.__correo = correo
    def agregarTelefono (self, telefono):
        if telefono not in self.__telefonos:
            self.__telefonos.append(telefono)
    def eliminarTelefono (self, telefono):
        if telefono in self.__telefonos:
            self.__telefonos.remove(telefono)
    def agregaPalabra(self,palabra):
        if palabra not in self.__palabras:
            self.__palabras.append(palabra)
    def elimiinarPalabra(self,palabra):
        if palabra in self.__palabras:
            self.__palabras.remove(palabra)

    def contienePalabraClave(self):
        contiene = False
        if len(self.__palabras) > 0:
            contiene = True
        return contiene
    
    def contienePalabra(self, palabra):
        hay = False
        if palabra in self.__palabras:
            hay = True
        return hay