# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:20:07 2018

@author: yocoy
"""
import Base
import Empresas
import Funciones

class Menu():
	
	def __correr__(self):
		
		while True:
			base.mostrarClases()
			clase = input("Nombre de la clase: ", end = '')
			seleccion = validacion("1)Editar objeto\n 2)Eliminar objeto\n3)Buscar objeto\n4)AgregarObjeto")
			if seleccion == 1:
				editarObjeto()
				continue
			if seleccion == 2:
				elminarObjeto()
				continue
			if seleccion == 3:
				buscarObjeto()
				continue
			if seleccion == 4:
				agregarObjeto()
				continue

	def __init__(self):
		self.__correr__()