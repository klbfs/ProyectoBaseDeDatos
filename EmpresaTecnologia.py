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
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
        if argumento == 'nombreEmpresa':
            for obj in cls._listaObjetos:
                if obj == objeto:
                    cls._listaObjetos[cls._listaObjetos.index(obj)].nombreEmpresa = dato

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('EmpresaTecnologia')
        for lista in listas:
            EmpresaTecnologia(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('EmpresaTecnologia',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
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
            BaseDeDatos.agregarDatos('EmpresaTecnologia', [self.nombreEmpresa,self.descripcion,self.aportesTecnologicos,self.productos,self.publico,self.departamentos,self.contacto,self.redesSociales,self.ubicacion,self.tienda], self.listaArgumentos)
        elif modo != None:
            self.nombreEmpresa = modo[0]
            self.descripcion = modo[1]
            self.aportesTecnologicos = modo[2]
            self.productos = modo[3]
            self.publico = modo[4]
            self.departamentos = modo[5]
            self.contacto = modo[6]
            self.redesSociales = modo[7]
            self.ubicacion = modo[8]
            self.tienda = modo[9]
            self.listarObjetos(self)
        else:
            self.crearBase()