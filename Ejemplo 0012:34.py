# Calculadora de IMC
# en este ejerccio se realizara una calculadora de imc como funcion y se preobara que funciona con distintas entradas

nombre1 = "jose"
altura1 = 2
peso1 = 90

nombre2 = "jose1"
altura2 = 1.82
peso2 = 70

nombre3 = "jose2"
altura3 = 1.95
peso3 = 90

def calculadora_IMC (nombre, altura, peso):
    IMC = peso/ (altura**2)
    print ("IMC: ")
    print (IMC)
    if IMC < 25:
        return nombre + (" No tiene sobrepeso")
    else:
        return nombre + (" tiene sobrepeso")
      
resultado1 = calculadora_IMC(nombre1,altura1,peso1)
resultado2 = calculadora_IMC(nombre2,altura2,peso2)
resultado3 = calculadora_IMC(nombre3,altura3,peso3)   

def convertir (millas):
    km = 1.6*millas
    print ("Km:")
    print (km)
r= convertir(2)
                         
