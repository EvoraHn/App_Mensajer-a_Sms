
# -*- coding: utf8 -*-
# Programa: Mensajería
# Objetivo: Simular una bandeja de entrada de un movil
# Autor: Eliab Evora
# Fecha: 01/Marzo/2020

# Clase Menu
import sys
import platform
from mensajería import Mensajería
class Menu:

    def __init__(self):
        """ Inicializa la bandeja de entrada """
        # Diccionarios
        # Objetos que almacenan información en pares (clave y valor)
        self.mensajería = Mensajería()
        self.opciones = {"1": self.ver_mensajes,
                        "2": self.buscar_mensajes,
                        "3": self.agregar_mensaje,
                        "4": self.modificar_mensaje,
                        "5": self.exit,
                        "6": self.hacer_conteo_mensajes}
            
            
            
            
            #"1": self.message_count,
                        #"2": self.get_unread_indexes,
                        #"3": self.get_message,
                        #"4": self.delete_message,
                        #"5": self.clear,
                        #"6": self.close}
    def display_menu(self):
        """ Despliega el menú principal """
        print("""
             Menú principal

             1. Mostrar todos los mensajes
             2. Buscar mensaje
             3. Agregar un mensaje
             4. Modificar un mensaje
             5. Salir
             6. Conteo de mensajes
             """)
    

    def Desplegar_Menu(self):
        """ Despliega el menu de interacción para el Usuario """
        print("""
                    -_-_-[ Mensajería ]-_-_-
                    
                    1. Ver cuantos mensajes Hay
                    2. mensajes sin leer 
                    3. Buscar mensaje
                    4. Eliminar mensaje
                    5. Eliminar todos los mensajes
                    6. Salir [X]
                    """)

    def run(self):
        """ Método de entrada para la aplicación """
        while True:
            self.display_menu()
            seleccion = input("Ingrese una opción: ")
            accion = self.opciones.get(seleccion)

            if accion:
                accion()
            else:
                print("¡{0} no es una opción válida!".format(seleccion))

    def ver_mensajes(self, mensajes=None):
        """ Despliega un mensaje """
        if not mensajes:
            mensajes = self.mensajería.mensajes
        self.hacer_conteo_mensajes()
        for mensaje in mensajes:
           
            print("Id: {0}\nDestinatario: '{1}'\nHora de entrada: '{2}'\nContenido: {3}\nFecha: {4}\nLeído: '{5}'"
                  .format(mensaje.id, mensaje.from_number, mensaje.time_arrived,mensaje.text_of_sms, mensaje.creation_date,mensaje.has_been_viewed)) 

    def buscar_mensajes(self):
        """ Busca un mensaje mediante un filtro """
        filter = input("Ingresa el texto de búsqueda: ")
        mensaje = self.mensajería.Buscar(filter)
        self.ver_mensajes(mensaje)
    
    def agregar_mensaje(self):
        """Agrega un mensaje a la lista de mensajes"""
        from_number = input("Ingrese el destinatario: ")
        text_of_sms = input("Ingrese texto en el mensaje: ")
        self.mensajería.nuevo_mensaje(from_number, text_of_sms)
        print("¡Nuevo mensaje agregado!")

    def modificar_mensaje(self):
        pass

    def exit(self):
        """ Cierra la aplicación """
        print("Gracias por utilizar la Mensajería el día de hoy")
        sys.exit(0)
    def hacer_conteo_mensajes(self):
        """Cuenta los mensajes de la bandeja de entrada"""
        print("Los mensajes en la badeja de entrada son : ")
        self.mensajería.conteo()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
