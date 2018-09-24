# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:20:07 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos
import funciones

class Menu():
	
    def __correr__(self):
        
        while True:
            BaseDeDatos.mostrarDatos('BaseClases')
            clase = input("Nombre de la clase: ", end = '')
            seleccion = funciones.validacion("1)Editar objeto\n 2)Eliminar objeto\n3)Buscar objeto\n4)AgregarObjeto")
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
            if seleccion == 3:
                nombreObjeto = input("Nombre del objeto a buscar")
                BaseDeDatos.buscarDato(clase,'nombre', nombreObjeto)
                continue
            if seleccion == 4:
                argumentos = BaseDeDatos.obtenerArgumentos(clase)
                datos = []
                for  x in argumentos:
                    datos.append(input("Introduce " + x + ": "), end = '')
                BaseDeDatos.agregarDatos(clase, datos)
                continue

    def __init__(self):
        self.__correr__()