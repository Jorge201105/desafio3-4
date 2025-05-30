

def factorial(numero):
    if numero==0:
        fact=1
        return fact
    elif numero >0:
        fact=1
        for i in range(numero):
            fact=fact*(i+1)        
        return fact    

def productoria(lista):
    prod=1
    for elemento in lista:
        prod=prod*elemento
    return prod

        