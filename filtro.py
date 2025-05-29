import sys

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

def filtro(lista, valor,condicion="mayor"):
    if condicion == "mayor":
        return {k:v for k,v in lista.items() if v> valor}
    elif condicion == "menor":
        return {k:v for k,v in lista.items() if v< valor}
    else:
        print("Condición no valida usa mayor o menor")
        return

umbral = int(sys.argv[1])

tipo_comparacion = 'mayor'
if len(sys.argv) == 3:
    tipo_comparacion = sys.argv[2].lower()

if tipo_comparacion != "mayor" and tipo_comparacion != "menor":
    print("Lo sentimos, no es una operación válida")

else:
    productos_que_cumplen = filtro(precios, umbral, tipo_comparacion)
    # se genera un diccionario con lo que cumple
    # print(productos_que_cumplen)
    if tipo_comparacion == 'mayor':
        mensaje_tipo = "mayores al umbral"
    else:
        mensaje_tipo = "menores al umbral"
    # se aplica list para transformar el producto_que_cumple en lista, y el keys saca todas las claves del diccionario obtenido de la funcion
    # print(productos_que_cumplen.keys()), genera algo similar a una lista pero no es una lista se require , aplicar list() para dejarlo transformado en una lista
    nombres_productos = list(productos_que_cumplen.keys())
    # print(nombres_productos)
    productos = ", ".join(nombres_productos)

    print(f"Los productos {mensaje_tipo} son: {productos}")






