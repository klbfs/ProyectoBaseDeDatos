# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:42:34 2018

@author: yocoy
"""
import sqlite3

class BaseDeDatos():
    
    _arguBases = {}
    
    @classmethod
    def argumentosDiccionario(cls, self):
        cls.arguBases[self.nombreBase] = self.argumentos
    
    def transformarArgumentos(argumentos):
        
        cadena = ""
        argumentos = []
        for a in range(len(argumentos)-1): 
            cadena += str(argumentos[a]) + ' VARCHAR(100) NOT NULL, '
        cadena += str(argumentos[len(cadena)-1]) + ' NOT NULL'
        return cadena
    
    def __init__(self, nombreBase, argumentos):
        
        self.nombreBase = nombreBase               
        self.argumentos = argumentos 
        sqlTerm = self.transformarArgumentos(argumentos)
        self.argumentosDiccionario()
        
        conexion = sqlite3.connect(self.nombreBase+".sqlite3")
        consulta = conexion.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS %s(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        %s""" %(self.nombreBase, sqlTerm)
        
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()
    
    @classmethod    
    def agregarDatos(cls, base, datos):
        
        conexion = sqlite3.connect(base)
        consulta = conexion.cursor()
        
        argumentos = cls.arguBases[base]
        
        col = ""
        for args in argumentos:
            col += args + ', '
        
        sql = """
        INSERT INTO %s(%s)
        VALUES(%s)
        """%(base, col, '?,'*(len(argumentos)-1) + '?')        
        consulta.execute(sql, datos)
        consulta.close()
        conexion.commit()
        conexion.close()
    
    def mostrarDatos(base):
        
        conexion = sqlite3.connect(base)
        consulta = conexion.cursor()
        
        sql = "SELECT * FROM %s" %base
        
        consulta.execute(sql)
        listas = consulta.fetchall()
        for lista in listas:
            for dato in lista:
                print(dato, end='')
            print('')
            
        consulta.close()
        conexion.commit()
        conexion.close()
    
    def buscarDato(base, argumento, dato):
        
        conexion = sqlite3.connect(base)
        consulta = conexion.cursor()
        
        sql = "SELECT * FROM %s WHERE %s=%s" %(base, argumento, dato)
        consulta.execute(sql)
        lista = consulta.fetchone()
        for dato in lista:
            print(dato, end='')
        print('')
        consulta.close()
        conexion.commit()
        conexion.close()
    
    @classmethod
    def borrarDatos(cls, base, argumento, dato):
        
        conexion = sqlite3.connect(base)
        consulta = conexion.cursor()
        
        sql = "DELETE * FROM %s WHERE %s=%s" %(base, argumento, dato) 
        
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()
        
        del cls.arguBases[base] 
    
    def editarDatos(base, argumento, datoIdentificacion, argumentoCambiado, nuevoDato):
        
        conexion = sqlite3.connect(base)
        consulta = conexion.cursor()
        
        sql = "UPDATE %s set %s = %s WHERE %s = %s"%(base, argumentoCambiado, nuevoDato, argumento, datoIdentificacion)
        
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()
    
    @classmethod
    def obtenerArgumentos(cls, base):
        return cls.agregarDatos[base]