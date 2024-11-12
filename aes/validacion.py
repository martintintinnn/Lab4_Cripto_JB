# Ajustar claves y IVs según el algoritmo
key_AES = ajustar_clave(key_input, 32, "Clave AES-256")
iv_AES = ajustar_clave(iv_input, 16, "IV AES-256")

def ajustar_clave(clave, longitud_requerida, tipo):
    #Ajusta la clave al tamaño requerido y notifica si fue truncada o extendida.
    if len(clave) < longitud_requerida:
        clave += get_random_bytes(longitud_requerida - len(clave))
        print(f"{tipo} ajustado a {longitud_requerida} bytes añadiendo bytes adicionales.")
    elif len(clave) > longitud_requerida:
        clave = clave[:longitud_requerida]
        print(f"{tipo} excedía {longitud_requerida} bytes y fue truncado.")
    print(f"{tipo} final utilizado (hex):", binascii.hexlify(clave).decode())
    return clave