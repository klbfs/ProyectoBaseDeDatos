# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class EmpresaTecnologia():
    
    def crearBase():
        BaseDeDatos('EmpresaTecnologia',listaArgumentos)

    def __init__(self):
        
        self.nombreEmpresa = input('Nombre de Empresa ', end = '')
        self.descripcion = input('Descripcion', end = '')
        self.aportesTecnologicos = input('Aportes Tencologicos ', end = '')
        self.productos = input('Productos ', end = '')
        self.publico = input('Publico ', end = '')
        self.departamentos = input('Departamentos ', end = '')
        self.contacto = input('Contacto ', end = '')
        self.redesSociales = input('Redes Sociales ', end = '')
        self.ubicacion = input('Ubicacion ', end = '')
        self.tienda = input('Tienda ', end = '')
        BaseDeDatos.agregarDatos('EmpresaTecnologia', [self.nombreEmpresa,self.descripcion,self.aportesTecnologicos,self.aportesTecnologicos,self.productos,self.publico,self.departamentos,self.contacto,self.redesSociales,self.ubicacion,self.tienda,self])