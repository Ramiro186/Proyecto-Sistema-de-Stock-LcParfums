# En este modulo se van a tratar las variables y constantes que luego se invocaran en esqueleto.py

# CONSTANTES (Reglas fijas del negocio)

ARCHIVO_BD= "inventario.json"
UMBRAL_DE_STOCK= 3 #Límitepara disparar alerta de reposición

# INVENTARIO

inventario_actual = {

    "ASAD": {

        "nombre": "Lattafa Asad",
        "marca": "Lattafa",
        "precio_venta": 29000,
        "costo_compra": 13000,
        "Stock":5
    },

    "CDN": {

        "nombre": "Club de Nuit Intense",
        "marca":"Armaf",
        "precio_venta": 50000,
        "costo_compra": 32000,
        "Stock": 4

    },

    "YARA": {

        "nombre": "Lattafa Yara",
        "marca": "Lattafa",
        "precio_venta": 30000,
        "costo_compra": 15000,
        "Stock": 3

    },

    "KHAMRAH": {

        "nombre": "Qahwa",
        "marca": "Lattafa",
        "precio_venta": 45000,
        "costo_compra": 20000,
        "Stock": 3

    }

}


# REGISTRO DE LA SESION

# comienza vacía y se llena conforme se realizan ventas

ventas_sesion= []