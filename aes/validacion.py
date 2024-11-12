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

llave_AES = preparar(llave_entrada, 32, "Llave AES-256")
iv_AES = preparar(iv_entrada, 16, "IV AES-256")