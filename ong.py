

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

def calcular(**kwargs):
    
   
    for k,v in kwargs.items():
        if "fact" in k:
            print (f"El factorial de {v} es {factorial(v)} ")
            
        else: 
            print(f"La productoria de {v} es {productoria(v)} ")       
   
    
    

calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)            


