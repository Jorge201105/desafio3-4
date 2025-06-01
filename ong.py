

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
    
   # se utiliza  el echo que el diccionario reconoce cuando entregamos palabras y numeros y 
   # los asocia automaticamente a las variables clave-valor que son representadas como k,v
   # 
    for k,v in kwargs.items():
        if "fact" in k:
            print (f"El factorial de {v} es {factorial(v)} ")
            
        else: 
            print(f"La productoria de {v} es {productoria(v)} ")       
   # no coloque return porque no supe como colocarlo para que me lo mostrara como me lo pedían , sin embargo, solo con print me daba la posibilidad
   #  de dejarlo como me lo pedian.
   # no puse alternativas de si se escribia mal la informacion, debido a que la informacion ya esta escrita. 
    

calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)            


