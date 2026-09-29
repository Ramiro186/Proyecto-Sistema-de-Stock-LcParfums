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

def guardar_datos():
    # Abrimos el archivo en modo escritura ("w" de write)
    archivo = open(datos.ARCHIVO_BD, "w")
    
    # Volcamos el diccionario de la memoria hacia el archivo JSON
    json.dump(datos.inventario_actual, archivo, indent=4)
    
    # Cerramos el archivo para proteger los datos
    archivo.close()




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


    # Guardar los cambios físicos en el JSON
    guardar_datos()

    # Evaluamos el stock restante para dar el aviso correcto
    if datos.inventario_actual[codigo]["Stock"] < datos.UMBRAL_DE_STOCK:
        return "Venta exitosa. ALERTA: Se necesita reponer stock de este perfume."
    else:
        return f"Venta exitosa. Quedan {datos.inventario_actual[codigo]['Stock']} unidades disponibles."


def cierre_caja():

    total_ingreso= 0
    total_ganancia= 0
    articulos_vendidos= 0

    for venta in datos.ventas_sesion:
        total_ingreso += venta["ingreso"]
        total_ganancia += venta["ganancia"]
        articulos_vendidos += venta["cantidad"]
        
    return total_ingreso, total_ganancia, articulos_vendidos

def reponer_stock(abreviatura, cantidad_nueva):
    # 1. Validar que el perfume exista en el catálogo
    if abreviatura not in datos.inventario_actual:
        return "Error: Esa abreviatura no existe en el catálogo."
    
    # 2. Sumar la nueva cantidad al stock existente
    # (El operador += es un atajo para x = x + y)
    datos.inventario_actual[abreviatura]["Stock"] += cantidad_nueva
    
    # 3. Guardar los cambios físicos en el disco duro (JSON)
    guardar_datos()
    
    # 4. Retornar el aviso de éxito
    nuevo_stock = datos.inventario_actual[abreviatura]["Stock"]
    return f"Éxito: Se agregaron {cantidad_nueva} unidades. El nuevo stock de {abreviatura} es {nuevo_stock}."


def buscar_perfume(busqueda):
    # 1. Guardamos la búsqueda normalizada
    termino = busqueda.strip().upper()
    
    lista_perfumes = []
    
    # 2. Usamos .items() para tener la abreviatura y los datos internos al mismo tiempo
    for abreviatura, detalles in datos.inventario_actual.items():
        
        # 3. Extraemos el nombre real del diccionario y lo pasamos a mayúsculas
        nombre_real = detalles["nombre"].upper()
        marca_real = detalles["marca"].upper()
        
        # 4. Condicional: Si el 'termino' está en el nombre real O en la marca real...
        if termino in nombre_real or termino in marca_real:
            
            # 5. Armamos un texto con los datos y lo metemos a nuestra lista
            texto = f"[{abreviatura}] - {detalles['nombre']} | Marca: {detalles['marca']} | Stock: {detalles['Stock']}"
            lista_perfumes.append(texto)
            
    # 6. Al salir del bucle, evaluamos si la lista quedó vacía o si encontramos algo
    if len(lista_perfumes) == 0:
        return "No se encontraron coincidencias."
    else:
        # La función .join() une todos los elementos de la lista usando saltos de línea (\n)
        return "\n".join(lista_perfumes)





    





