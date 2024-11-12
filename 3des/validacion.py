from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
import binascii

def preparar(valor, longitud_requerida, tipo):
    if len(valor) < longitud_requerida:
        valor += get_random_bytes(longitud_requerida - len(valor))
        print(f"{tipo} ajustado a {longitud_requerida} bytes anadiendo bytes adicionales.")
    elif len(valor) > longitud_requerida:
        valor = valor[:longitud_requerida]
        print(f"{tipo} excedia {longitud_requerida} bytes y fue truncado.")
    # Imprimimos en Hexadecimal, facilitando la comprension y comparativa.
    print(f"{tipo} final utilizado (hex):", binascii.hexlify(valor).decode())
    return valor

llave_3DES = preparar(llave_entrada, 24, "Llave 3DES")
iv_3DES = preparar(iv_entrada, 8, "IV 3DES")