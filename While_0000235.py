total = 0
j=1
while j< 5:
    total += j
    j += 1
print (total)
 # en el primer ejemplo hacemos un contador que sume todos los numeros hasta el 5
lista =[5,4,4,3,1,-2,-3,-4,-9,-23]
t2=0
i=0
while lista[i] > 0:
    t2 += lista[i]
    i += 1
print t2
t3 = 0
# en el segundo ejemplo hacemos que sume todos los valores positivos de una lista
while i< len(lista) and lista[i] > 0:
    t3 += lista[i]
    i += 1
print t2
# en el tercer ejemplo hacemos que sume todos los valores positivos con el largo de la lista

t4 = 0
for element in lista :
    if element <= 0:
        break
    t4 += element
    
print t4
# en el cuarto ejemplo suma todos los valores, peropara si hay alguno negativo en la lista
t5 =0

for element in lista :
    if element <= 0:
        t5 += element
print t5

#suma todos los numeros negativos de la lista con un for