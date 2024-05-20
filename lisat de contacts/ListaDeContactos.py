from Contacto import Contacto
class ListaDeContactos:
    def __init__(self) -> None:
        self.__Contactos = []
    def todosLosContactos(self):
        return self.__Contactos
    def bucarContactosPalabraClave(self, plabra):
        return self.__Contactos[self.__Contactos.index(plabra)]
    
    def añadirContacto(self, nombre, apellido, direccion, correo, numero, palabra):
        agregado = False
        nuevo = Contacto.contacto(nombre, apellido, direccion, correo, numero, palabra)
        if nuevo is not None:
            self.__Contactos.append(nuevo)
            agregado = True
        return agregado
    
    def eliminarContacto(self,palabra):
        self.__Contactos.remove(palabra)
        
    def modificarContacto(self,nombre, apellido, direccion, correo, numero, palabra):
        Contacto.contacto(nombre, apellido, direccion, correo, numero, palabra)
        
    def actualizarTelefono (self, nTelefono):
        Contacto.agregarTelefono(nTelefono)
    
    def actualizarPalabra (self, nPalabra):
        Contacto.agregarTelefono(nPalabra)
        
    def bucarContacto(self, plabra):
        return self.__Contactos[self.__Contactos.index(plabra)]