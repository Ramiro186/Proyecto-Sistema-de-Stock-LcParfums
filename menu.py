import esqueleto

#El siguiente menu va a ser interactivo solamente para el administrador y estara formado por distintas opciones que faciliten el control de stock

esqueleto.cargar_datos()

while True:
    print("==========MENU INTERACTIVO==========")
    print("1- Cargar Venta")
    print("2- Cierre de caja")
    print("3- Reponer Stock")
    print("4- Salir")

    try:
        # El try vigila esta línea crítica
        opcion = int(input("Ingresar opción: "))

        if opcion == 1:
            abreviatura = input("Ingrese la abreviatura del perfume (ej. ASAD): ")
            try:
                cantidad = int(input("Ingrese la cantidad requerida: "))
                mensaje = esqueleto.procesar_venta(abreviatura, cantidad)
                print(mensaje)
            except ValueError:
                print("Error: La cantidad debe ser un número.")

        elif opcion == 2:
            ingresos, ganancias, articulos = esqueleto.cierre_caja()
            print(f"Resumen del día ------> Ingresos: {ingresos} | Ganancias: {ganancias} | Artículos vendidos: {articulos}")

        elif opcion == 3:
            abreviatura = input("Ingrese la abreviatura del perfume a reponer: ")
        
            try:
                cantidad = int(input("Ingrese la cantidad de unidades que entraron: "))
            
                # Llamamos a la nueva función del esqueleto
                mensaje = esqueleto.reponer_stock(abreviatura, cantidad)
                print(mensaje)
            
            except ValueError:
                print("Error: La cantidad a reponer debe ser un número entero.")

        elif opcion == 4:
            print("Salida confirmada. Nos vemos!!!")
            break
            
        else:
            # Atrapa los números que no son 1, 2 o 3
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

    except ValueError:
        # Atrapa letras, símbolos o si el usuario presiona Enter sin escribir nada
        print("Error: Debes ingresar un número (1, 2 o 3), no letras ni espacios.")



    
