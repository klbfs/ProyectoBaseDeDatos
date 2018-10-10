# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:20:07 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos
from ControladorObjetos import ControladorObjetos
from funciones import validacionEntera

class Menu():
	
    def __correr__(self):
        
        while True:
            BaseDeDatos.mostrarDatos('BaseClases')
            clase = input("Nombre de la clase: ", end = '')
            #Comprobar existencia de base
            BaseDeDatos.mostrarDatos(clase)
            seleccion = funciones.validacionEntera("1)Editar objeto\n 2)Eliminar objeto\n3)Buscar objeto\n4)AgregarObjeto", 1,4)
            
            if seleccion == 1:
                nombreObjeto = input("Nombre del objeto a editar")
                argumentoEditar = input("Nombre del argumento a editar")
                nuevoValor = input("Nuevo dato")
                BaseDeDatos.editarDatos(clase, 'nombre',  nombreObjeto, argumentoEditar, nuevoValor)
                continue
            
            if seleccion == 2:
                nombreObjeto = input("Nombre del objeto a eliminar")
                BaseDeDatos.borrarDatos(clase, 'nombre', nombreObjeto)
                continue
            
            #Lista la busqueda
            if seleccion == 3:
                nombreObjeto = input("Nombre del objeto a buscar")
                BaseDeDatos.buscarDato(clase,'nombre', nombreObjeto)
                continue
            
            if seleccion == 4:
                
                ControladorObjetos.crearObjeto(clase)
                continue

    def __init__(self):
        self.__correr__()