# -*- coding: utf8 -*-
from mensaje import Mensaje

class Mensajería:
    """ Representa una coleccion de mensajes que 
    pueden ser Agregados,Buscados,Modificados y Eliminados """

    def __init__(self):
        """ Inicializa una libreta vacía """
        self.mensajes = list()

    def nuevo_mensaje(self,from_number="",time_arrived="",text_of_sms="",has_been_viewed=""):
        """ Crea un mensaje y lo agrega a la mensajería """
        self.mensajes.append(Mensaje(from_number,time_arrived,text_of_sms,has_been_viewed))

    def _buscar_mensaje(self, mensaje_id):
        """
        Busca un mensaje con el id que recibe.
        Esta función es privada (empieza con _).
        https://docs.python.org/2/tutorial/classes.html
        """
        for mensaje in self.mensajes:
            if str(mensaje.id) == str(mensaje_id):
                return mensaje

        return None
    
    def modificar_mensaje(self, mensaje_id, text_of_sms):
        """
        Encuentra la nota con el valor del id y modifica
        el contenido de la misma.
        """
        mensaje = self._buscar_mensaje(mensaje_id)

        if mensaje:
            mensaje.text_of_sms = text_of_sms
            return True
        else:
            print("No existe un mensaje con el id: {0}"
                  .format(mensaje_id))
            return False

    def buscar(self, filter):
        """
        Busca todas los mensajes que satisfacen el filtro enviado.
        """
        return [Mensaje for Mensaje in self.mensajes if Mensaje.buscar(filter)]
    
    def conteo(self):
        """Cuenta los mensajes en el buzón """
        conteo = len(self.mensajes)
        print ("-----------------------------------------------------------")
        print ("El numero de mensajes en el buzón es de: {0} ",conteo)



#Mensajería.buscar()
#Mensajería.run()
#if __name__ == "__main__":
 #   Mensajería = Mensajería()

 #   Mensajería.run()
    #print(sms.has_been_viewed)
    #print(sms.from_number)
    #print(sms.time_arrived)
    #print(sms.text_of_sms)

    #sms.run()
