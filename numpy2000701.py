import numpy as np # importa el modulo numpy 
a = np.array([2,3,4]) # se crea una lista
print a
a = np.linspace(1, 12,6) # se crea una lista desde 1 hasta 12 en 6 partes 
print a
a=a.reshape(3,2) # cambia la forma a 3x2
print a
print a.size # muestra el tamaño del arreglo
print a.shape # mustra la forma de la matriz
print a.dtype # te dice el tipo de datos
print a.itemsize # muestra el espacio que ocupa
b = np.array([(1.5,2,3),(4,5,6)]) # crea una matriz de 2x3
print b
a*=3 # multiplica la matriz por 3
print a
a= np.ones(10) # hace un lista de 10 numeros 1
print a
a = np.random.random((2,3)) # selecciona numeros al azar en una matriz de 2x3
print a
np.set_printoptions (precision =2 , suppress=True) # corta los decimales a 2
print a
a = np.random.randint(0,10,5)# 5 unmeros al azar entre 0 y 10
print a
a.sum()#suma los valores de a
print a
a.min()# minimo de a
print a
a.max()  # maximo de a
print a
a= np .random.randint(1,10,6)
print a
a= a.reshape(3,2)
print a
a.sum(axis=1)
#data = np.loadtxt( "data.txt", dtype =np.uint8,delimeter= ",",skiprows=1)# carga datos externos de 8 bits y salta una fila
#print data



