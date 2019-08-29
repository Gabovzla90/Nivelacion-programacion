import numpy as np 
a = np.array([[10,11,12],[23,43,34]])
print a
print a.dtype # dice el tipo de datos
print a.shape # dice la forma
print a[1,1] # imprime 43 (linea 1, columna 1)
a = np.array([1,2,3,4,5,6,3,223,423,234,77,88,66,88,2])
print a[:2] #imprime los primeros 2 elementos
print a[-2:] # imprime los dos ultimos
print a[::2] # imprime los elementos de dos en 2
# operadores binarios: and, or, not
#bitwise operators son mas efectivos que los binarios
#&(and),/(or),~(not)
f= 6
g = 9
print f+g
print f.__add__(g) # otra forma de unar el lenguaje
# en el video se muestra como crear matrices de ceros
# hace modelos en 2d y 3d de como seleccionar los datos
# nan es cuando algo no esta defino, un error bastante comun
# lo mas importante de numpy es que hace todos los calculos sin necesidad de usar un for y ocupando muy ppoca memoria
# esto ayuda en casos que se tengan datos muy complejos se puedan trabajar entre ellos con mayor velocidad



