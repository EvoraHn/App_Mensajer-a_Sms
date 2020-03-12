# -*- coding: utf-8 -*-
import datetime

# Almacena el último id 
last_id = 0
class Mensaje:
    """ Representa un mensaje, en una bandeja de entrada;
    Se puede agregar,Editar y eliminar un mensaje. """
    
    def __init__(self,from_number="",time_arrived="",text_of_sms="",has_been_viewed=""):
        """
        inicializando un mensaje con el valor de from_number,
        time_arrived,text_of_sms,has_been_viewed enviadas por el usuario. 
        Automáticamente inserta la fecha de creación y un id unico.
        """
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        self.from_number = from_number
        self.time_arrived = datetime.date.today()
        self.text_of_sms = text_of_sms
        self.has_been_viewed = False


    def search(self, filter):
        """
        Determina si el mensaje está contenida en el valor
        del filtro (distingue mayúsculas de minúsculas). 
        Retorna True si es igual o False en caso contrario.
        """
        return filter in self.text_of_sms or filter in self.has_been_viewed

    