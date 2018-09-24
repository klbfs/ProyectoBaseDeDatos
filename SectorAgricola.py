# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:14:25 2018

@author: yocoy
"""
import BaseDatos as bd


class SectorAgricola():
    
    listaArgumentos = ['ubicacion','empresas','asociaciones','tiposDeProductos','empresasExportadoras','rutasDeTransporte','empresasProductoras','empresasVendedoras','promedioProduccion','gastoNatural']

    def __init__(self, ubicacion, empresas, asociaciones, tiposDeProducto, empresasExportadoras, rutasDeTransporte, empresasProductoras, empresasVendedoras, promedioProduccion, gastoNatural):
        
        self.ubicacion = ubicacion
        self.empresas = empresas 
        self. asociaciones = asociaciones 
        self.tiposDeProductos = tiposDeProducto
        self.empresasExportadoras = empresasExportadoras
        self.rutasDeTransporte = rutasDeTransporte
        self.empresasProductoras = empresasProductoras
        self.empresasVendedoras = empresasVendedoras
        self.promedioProduccion = promedioProduccion
        self.gastoNatural = gastoNatural

    def crearBase():
        bd.BaseDatos('SectorAgricola',listaArgumentos)