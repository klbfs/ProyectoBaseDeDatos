# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:48:17 2018

@author: yocoy
"""

def  validacion(texto):
    while True:
        try:
            opcion = int(input(texto), end = '')
            if texto < 1 and texto > 4:
                print("Opcion no válida, intenta otra vez")
                continue
            break
        except:
            print("Opcion no válida, intenta otra vez")
    return opcion