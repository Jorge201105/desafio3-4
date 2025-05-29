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

if tipo_comparacion not in ["mayor","menor"]:
    print("Lo sentimos, no es una operación válida")

else:
    productos_que_cumplen = filtro(precios, umbral, tipo_comparacion)

    if tipo_comparacion == 'mayor':
        mensaje_tipo = "mayores al umbral"
    else:
        mensaje_tipo = "menores al umbral"
    # se aplica list para transformar el producto en lista, y el keys saca todas las claves del diccionario obtenido de la funcion
    nombres_productos = list(productos_que_cumplen.keys())
    # print(nombres_productos)
    productos = ", ".join(nombres_productos)

    print(f"Los productos {mensaje_tipo} son: {productos}")






