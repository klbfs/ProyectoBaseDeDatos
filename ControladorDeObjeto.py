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


    def borrarObjeto(clase):

        nombreObjeto = input("Nombre del objeto a eliminar: ")
        if clase == 'EmpresaTecnologia':
        	EmpresaTecnologia.eliminarObjeto()
        	
        BaseDeDatos.borrarDatos(clase,'nombre',nombreObjeto)


    def editarObjeto(clase):
        
        nombreObjeto = input("Nombre del objeto a editar: ")
        argumentoEditar = input("Nombre del argumento a editar: ")
        nuevoValor = input("Nuevo dato: ")
        if clase == 'EmpresaTecnologia':
            EmpresaTecnologia.editarArgumento(argumentoEditar, EmpresaTecnologia.regresarDato(nombreObjeto), dato)

        BaseDeDatos.editarDatos(clase, 'nombre',  nombreObjeto, argumentoEditar, nuevoValor)