

def velocidad_promedio(lista):
    vel_prom = sum(lista)/len(lista)
  
    return vel_prom

def posicion_velocidad(lista,promedio):
    posiciones_superiores=[]
    for indice,vel in enumerate(lista):
        if vel > promedio:
            posiciones_superiores.append(indice)
    return posiciones_superiores
 
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
            14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
            14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
            14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
            10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
            11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

velpromedio=velocidad_promedio(velocidad)
print("La velocidad promedio es",velpromedio)
lista_posiciones_superiores=posicion_velocidad(velocidad,velpromedio)

print(f"Las posiciones de las correas con mayor velocidad son {lista_posiciones_superiores}")

