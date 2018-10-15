# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:20:07 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos
from ControladorDeObjeto import ControladorDeObjeto
from funciones import validacionEntera

class Menu():
	
    def correr():
        
        while True:
            BaseDeDatos.mostrarDatos('BaseClases')
            clase = input("Nombre de la clase: ")
            #Comprobar existencia de base
            BaseDeDatos.mostrarDatos(clase)
            seleccion = validacionEntera("1)Editar objeto\n2)Eliminar objeto\n3)Buscar objeto\n4)AgregarObjeto", 1,4)
            
            if seleccion == 1:
                ControladorDeObjeto.EditarObjeto(clase)
                continue
            
            if seleccion == 2:
                ControladorDeObjeto.borrarObjeto(clase)
            
            #Lista la busqueda
            if seleccion == 3:
                nombreObjeto = input("Nombre del objeto a buscar")
                BaseDeDatos.buscarDato(clase,'nombre', nombreObjeto)
                continue
            
            if seleccion == 4:
                ControladorObjetos.crearObjeto(clase)
                continue