#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from BaseDeDatos import BaseDeDatos 

class InformacionDelaEmpresa():
    
    listaArgumentos = ['nombreDelaempresa','telefono','correo','fax','carreras','foros','conferencias','newsletter','publicaciones','politicasDeprivacidad','FechasDefundacion']
    _listaObjetos = []

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
        listas = BaseDeDatos.obtenerDatosTotales('InformacionDelaEmpresa')
        for lista in listas:
            InformacionDelaEmpresa(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('InformacionDelaEmpresa',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.nombreDelaempresa = input('Nombre de la empresa: ')
            self.telefono = input('telefono: ')
            self.fax = input('fax: ')
            self.carreras = input('carreras: ')
            self.foros = input('foros: ')
            self.conferencias = input('conferencias: ')
            self.newsletter = input('newsletter: ')
            self.publicaciones = input('publicaciones: ')
            self.politicasDeprivacidad = input('politicas de privacidad: ')
            self.fechaDefundacion = input('fecha de fundacion : ')
            self.correo = input('correo: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Usuario', [self.nombreDelaempresa,self.telefono,self.fax,self.correo,self.carreras,self.foros,self.conferencias,self.newsletter,self.publicaciones,self.politicasDeprivacidad,self.fechaDefundacion], self.listaArgumentos)
        elif modo != None:
            self.nombreDelaempresa = modo[0]
            self.telefono = modo[1]
            self.fax = modo[2]
            self.correo = modo[3]
            self.carreras = modo[4]
            self.foros = modo[5]
            self.conferencias = modo[6]
            self.newsletter = modo[7]
            self.publicaciones = modo[8]
            self.politicasDeprivacidad = modo[9]
            self.politicasDeprivacidad = modo[10]
            self.listarObjetos(self)
        else:
            self.crearBase()

