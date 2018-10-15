# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class EmpresaTecnologia():
    
    listaArgumentos = ['nombreEmpresa','descripcion','aportesTecnologicos','productos','publico','departamentos','contacto','redesSociales','ubicacion','tienda']
    _listaObjetos = []

    @classmethod
    def regresarObjeto(cls, nombreObjeto):
        for objeto in cls._listaObjetos:
            if objeto.nombreEmpresa == nombreObjeto:
                return objeto

    @classmethod
    def eliminarObjeto(cls, objeto):
        for objeto in cls._listaObjetos:
            if objeto == objeto:
                cls._listaObjetos.remove(objeto)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
        if argumento == 'nombreEmpresa':
            for obj in cls._listaObjetos:
                if obj == objeto:
                    cls._listaObjeto[obj.index()].nombreEmpresa = dato

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('EmpresaTecnologia',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo != None:
            self.nombreEmpresa = input('Nombre de Empresa: ')
            self.descripcion = input('Descripcion: ')
            self.aportesTecnologicos = input('Aportes Tencologicos: ')
            self.productos = input('Productos: ')
            self.publico = input('Publico: ')
            self.departamentos = input('Departamentos: ')
            self.contacto = input('Contacto: ')
            self.redesSociales = input('Redes Sociales: ')
            self.ubicacion = input('Ubicacion: ')
            self.tienda = input('Tienda: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('EmpresaTecnologia: ', [self.nombreEmpresa,self.descripcion,self.aportesTecnologicos,self.aportesTecnologicos,self.productos,self.publico,self.departamentos,self.contacto,self.redesSociales,self.ubicacion,self.tienda,self])
        else:
            self.crearBase()