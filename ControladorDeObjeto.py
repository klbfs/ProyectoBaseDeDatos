# -*- coding: utf-8 -*-
from EmpresaTecnologia import EmpresaTecnologia
from SectorAgricola import SectorAgricola
from BaseDeDatos import BaseDeDatos

class ControladorDeObjeto():
	
    def crearObjeto(clase):
        if clase == 'EmpresaTecnologia':
            EmpresaTecnologia(1)

        elif clase == 'SectorAgricola':
            #SectorAgricola()
            pass

    def buscaObjeto(clase):
    	nombreObjeto = input("Nombre del objeto a buscar: ")
    	if clase == 'EmpresaTecnologia':
    		BaseDeDatos.buscarDato(clase,'nombreEmpresa', nombreObjeto)

    def borrarObjeto(clase):

        nombreObjeto = input("Nombre del objeto a eliminar: ")
        if clase == 'EmpresaTecnologia':
        	BaseDeDatos.borrarDatos(clase,'nombreEmpresa',nombreObjeto)
        	nombreObjeto = EmpresaTecnologia.regresarObjeto(nombreObjeto)
        	EmpresaTecnologia.eliminarObjeto(nombreObjeto)

        


    def editarObjeto(clase):
        
        nombreObjeto = input("Nombre del objeto a editar: ")
        argumentoEditar = input("Nombre del argumento a editar: ")
        nuevoValor = input("Nuevo dato: ")
        if clase == 'EmpresaTecnologia':
            EmpresaTecnologia.editarArgumento(argumentoEditar, EmpresaTecnologia.regresarObjeto(nombreObjeto), nuevoValor)
            BaseDeDatos.editarDatos(clase, 'nombreEmpresa',  nombreObjeto, argumentoEditar, nuevoValor)
       