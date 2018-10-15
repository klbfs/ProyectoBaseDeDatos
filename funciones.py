# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:48:17 2018

@author: yocoy
"""
import SectorAgricola as sA
import EmpresaTecnologia as eT
import BaseDeDatos as bd

def  validacionEntera(texto, l1, l2):
    while True:
        try:
            opcion = int(input(texto+ '\n-->'))
            if opcion < l1 or opcion > l2:
                print("Opcion no válida, intenta otra vez")
                continue
            break
        except:
            print("Opcion no válida, intenta otra vez")
    return opcion

def crearBases():
    
    nombresClases = ['SectorAgricola','EmpresaTecnologia']

    clases = bd.BaseDeDatos('BaseClases',['nombre'])
    for clase in nombresClases:
        clases.agregarDatos('BaseClases', [clase])
        
    #sA.SectorAgricola().crearBase()
    eT.EmpresaTecnologia()
