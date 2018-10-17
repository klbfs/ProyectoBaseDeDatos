# -*- coding: utf-8 -*-
from BaseDeDatos import BaseDeDatos
import Ubicacion as Ubicacion
import RedesSociales as RedesSociales
import ActividadEconomica as ActividadEconomica
import Empresa as Empresa
import Usuario as Usuario
import Buscador as Buscador
import MenuBusqueda as MenuBusqueda
import CuentaAdministrador as CuentaAdministrador
import InformacionDeLaEmpresa as InformacionDeLaEmpresa
import Estadisticas as Estadisticas
import Cliente as Cliente
import Opiniones as Opiniones
import Fundaciones as Fundaciones
import Capital as Capital
import Departamentos as Departamentos
import ImagenesYVideo as ImagenesYVideo
import Instalaciones as Instalaciones
import LideresEmpresariales as LideresEmpresariales


class ControladorDeObjeto():
	

    def crearObjeto(clase):
        nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
        for nombre in nombresClases:
        	if nombre == clase:
        		eval(clase+'()')

    def buscaObjeto(clase):
    	nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
    	nombreObjeto = input("Nombre del objeto a buscar: ")
    	for nombre in nombresClases:	
    		if nombre == clase:
    			eval('BaseDeDatos.buscarDato(clase,'+clase+'.regresarArgumentos()[0], nombreObjeto)')

    def borrarObjeto(clase):
    	nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
        nombreObjeto = input("Nombre del objeto a eliminar: ")
        for nombre in nombresClases:
	        if clase == nombre:
	        	eval('BaseDeDatos.borrarDatos(clase,'+clase+'.regresarArgumentos()[0], nombreObjeto)')
	        	eval('nombreObjeto = '+clase+'.regresarObjeto(nombreObjeto)')
	        	eval(clase+'.eliminarObjeto(nombreObjeto')

        


    def editarObjeto(clase):
        for nombre in nombresClases:
	        if clase == nombresClases:
	            print('\n\nLista de argumentos')
	            eval('print('+clase+'.regresarArgumentos()')
	            print('\n')

	            argumentoABuscar = input('Por que argumento deseas buscar: ')
	            nombreArgumentoObjeto = input("Valor a buscar: ")

	            argumentoEditar = input("Nombre del argumento a editar: ")
	            nuevoValor = input("Nuevo dato: ")

	            eval(clase+'.editarArgumento(argumentoEditar,'+clase+'.regresarObjeto(argumentoABuscar, nombreArgumentoObjeto), nuevoValor')
	            BaseDeDatos.editarDatos(clase, argumentoEditar, nuevoValor)
	       