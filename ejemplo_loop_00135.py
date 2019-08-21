#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:25:48 2019

@author: agds
"""

a = ["banana", "manzana", "microsoft"]
for element in a:
    print (element)
# imprime cada elemento de la lista a    
    
    
b = [20,10,5,6,3,34,23,233,232,]
total = 0
for e in b:
    total = total + e
print (total)
# suma los elementos de la lista uno a uno        

c=list(range(1,879))
# crea una lista desde el 1 hasta 878


total2=0
for i in range (1,6):
    total2 += i
    print (i)
    print (total2)
#suma todos los valores de la lista 
    
total3 = 0
for k in c:
    if i%3== 0:
        total3 += i
print (total3)    
# muestra todos los multipos de 3        
totalm3 = 0
tota3= 3
tota5= 5
totalm5 = 0  
for l in range (1,101):
    if l%3== 0:
        totalm3 += l
        tota3 +=1
    if l%5 == 0:
        totalm5 += l
        tota5 +=1
print ("multiplos de 3:"  )
print (totalm3)    
print ("la cantidad de multiplos es:")   
print (tota3)
print ("multiplos de 5:" )   
print (totalm5)   
print ("la cantidad de multiplos es:")   
print (tota5)  