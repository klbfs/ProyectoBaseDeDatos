"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class Ubicacion():
    
    listaArgumentos = ['pais', 'estado', 'municipio', 'localidad', 'calle', 'numero', 'codigoPostal', 'coordenadasGeograficas','sucursales','areaGeografica']
    _listarObjetos = []

    @classmethod
    def regresarArgumentos(cls):
        return cls.listaArgumentos

    @classmethod
    def regresarObjeto(cls,argumento, nombreObjeto):
        for objeto in cls._listaObjetos:
            cadena = eval('objeto.'+argumento)
            if cadena == nombreObjeto: 
                return objeto

    @classmethod
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
       for arg in cls.listaArgumentos:
                if argumento == arg:
                    for obj in cls._listaObjetos:
                        if obj == objeto:
                            eval('cls._listaObjetos[cls._listaObjetos.index(obj)].'+argumento+' = dato')

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('Ubicacion')
        for lista in listas:
            Usuario(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Ubicacion',self.listaArgumentos)


    def __init__(self, modo = None):

        if modo == 1:
        

            self.pais = input('Pais de Origen ')
            self.estado = input('Estado ')
            self.municipio = input('Municipio ')
            self.localidad = input('Localidad ')
            self.calle = input('Calle ')
            self.numero = input('Numero Exterior ')
            self.codigoPostal = input('Codigo Postal ')
            self.coordenadasGeograficas = input('Coordenada Geograficas de Sede ')
            self.sucursales = input('Direccion de Sucursales ')
            self.areaGeografica = input('Area Geografica comercial ')
            BaseDeDatos.agregarDatos('Ubicacion', [self.pais,self.estado,self.municipio,self.localidad,self.calle,self.numero,self.nodigoPostal,self.coordenadasGeograficas,self.sucursales,self.areaGeografica], self.listaArgumentos)

        elif modo != None:

            self.pais = modo [0]
            self.estado = modo [1]
            self.municipio = modo [2]
            self.localidad = modo [3]
            self.calle = modo [4]
            self.numero = modo [5]
            self.codigoPostal = modo [6]
            self.coordenadasGeograficas = modo [7]
            self.sucursales = modo [8]
            self.areaGeografica = modo [9]
            self.listarObjetos(self)

        else:
            self.crearBase()
