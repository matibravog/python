# 
def ingresar():
    CantidadNumeros = int(input('ingresa cuantos numeros quieres: '))
    return(CantidadNumeros)
        
CantidadNumeros = ingresar()
pares = []
impares = []

def mayor_a_cero(numero):
    if(numero > 0):
        return(numero)
    elif(numero <= 0):
        print('error, ingresa un numero mayor a cero')
        nuevaCantidadNumeros = ingresar()
        mayor_a_cero(nuevaCantidadNumeros)
        return(nuevaCantidadNumeros)

def es_par(numero):
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

def main(CantidadNumeros):
    CantidadNumeros = mayor_a_cero(CantidadNumeros)
    contador = 0
    suma = 0
    multi = 1

    if(contador != CantidadNumeros):
        for a in range(CantidadNumeros):
            numeroIngresado = int(input('ingresa un numero: '))
            es_par(numeroIngresado)
            contador +=1

    if(contador == CantidadNumeros):        
        for i in range(len(pares)):
            suma = suma + pares[i] 

        for i in range(len(impares)):
            multi = multi * impares[i]

    print(pares, impares)
    print('ingresaste ', contador, ' numeros')
    print('tu suma de numeros pares es: ', suma)
    print('tu multiplicacion de numeros impares es: ', multi)

main(CantidadNumeros)