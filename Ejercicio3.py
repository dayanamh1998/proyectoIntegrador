#Elabore un programa para la facultad de Ingeniería que pida 400 números 
# e indique si ese número es par o impar; me muestre un listado y
#  me indique cuantos son pares y cuantos son impares.



def clasificacionNumeros(contarNumero):
    numerosPares = []
    numerosImpares = []
    
    for i in range(contarNumero):
        numero = int(input("Digite un número: "))
        if numero % 2 == 0:
            numerosPares.append(numero)
        else:
            numerosImpares.append(numero)
    
    return numerosPares, numerosImpares

contarNumero = 400
numerosPares, numerosImpares = clasificacionNumeros(contarNumero)

#Se muestra cuales son y  cantidad de numeros pares e impares
print(f"Números pares: {numerosPares}")
print(f"Números impares: {numerosImpares}")
print(f"Cantidad de números pares: {len(numerosPares)}")
print(f"Cantidad de números impares: {len(numerosImpares)}")