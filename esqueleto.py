import datos
import json

# Va a ser la columna del proyecto, formado por distintas funciones que contemplaran los distintos apartados que sean necesarios por el administrador


def cargar_datos ():

    try:
       archivo = open(datos.ARCHIVO_BD) # abre el archivo en modo lectura
       datos.inventario_actual= json.load(archivo) # Aca le decimos que cargue el archivo dentro del diccionario
       archivo.close() # Esto le avisa a la computadora que ya terminaste de leer y libera el archivo.
       

    except FileNotFoundError:
        pass


def procesar_venta(codigo,cantidad):

    

    if codigo not in datos.inventario_actual:
        return "Error: El perfume no existe."

    if datos.inventario_actual[codigo]["Stock"] >= cantidad:

        # Restar stock
        datos.inventario_actual[codigo]["Stock"] = datos.inventario_actual[codigo]["Stock"] - cantidad

        # Cálculos
        ingreso = cantidad * datos.inventario_actual[codigo]["precio_venta"]
        costo = cantidad * datos.inventario_actual[codigo]["costo_compra"]
        ganancia = ingreso - costo  


        
    else:
        return "Error: Stock insuficiente."

    datos.ventas_sesion.append({
    "codigo": codigo,
    "cantidad": cantidad,
    "ingreso": ingreso,
    "ganancia": ganancia
    })

    if datos.inventario_actual[codigo]["Stock"] < datos.UMBRAL_STOCK:
        return "Se necesita reponer Stock"
    else:
        return "Quedan {cantidad} de producto disponibles"

    # Guardar los cambios físicos en el JSON
    guardar_datos()

    # Evaluamos el stock restante para dar el aviso correcto
    if datos.inventario_actual[codigo]["Stock"] < datos.UMBRAL_STOCK:
        return "Venta exitosa. ALERTA: Se necesita reponer stock de este perfume."
    else:
        return f"Venta exitosa. Quedan {datos.inventario_actual[codigo]['Stock']} unidades disponibles."



    





