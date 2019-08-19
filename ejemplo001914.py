#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:20:42 2019
# en este codigo se desarrollara una calculadora de indice de masa corporal con el uso del comando if#
@author: agds
"""

nombre = "angel"
Altura_m = 1.9
peso_kg = 78

IMC = peso_kg/ (Altura_m**2)
print ("IMC: ")
if IMC < 25:
    print (nombre)
    print ("No tiene sobrepeso")
else:
    print (nombre)
    print (" Tiene sobrepeso")