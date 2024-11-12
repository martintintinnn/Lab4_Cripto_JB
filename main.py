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


# Cifra el texto utilizando DES en modo CBC
def cifrar_DES(llave, iv, texto):
    # Creacion objeto cifrador para cifrar DES en modo CBC
    cifrador = DES.new(llave, DES.MODE_CBC, iv)
    # Padding (en caso de ser necesario) para cumplir la longitud multiplo de 8 (bloque de DES)
    longitud_relleno = 8 - (len(texto) % 8)
    texto_rellenado = texto + (chr(longitud_relleno) * longitud_relleno)
    # Ciframos texto
    texto_cifrado = cifrador.encrypt(texto_rellenado.encode())
    # Imprime el texto cifrado en formato hexadecimal para facilitar la comprension y comparativa
    print("Texto cifrado con DES (hex):", binascii.hexlify(texto_cifrado).decode())
    # Retorna el texto cifrado en formato de bytes
    return texto_cifrado

# Descifra el texto cifrado utilizando DES en modo CBC
def descifrar_DES(llave, iv, texto_cifrado):
    # Creacion objeto cifrador para descifrar DES en modo CBC
    cifrador = DES.new(llave, DES.MODE_CBC, iv)
    # Se descifra el texto cifrado
    texto_descifrado = cifrador.decrypt(texto_cifrado)
    # Obtencion tamano del relleno en base al ultimo byte del texto descifrado
    longitud_relleno = texto_descifrado[-1]
    # Eliminacion del relleno
    texto_descifrado = texto_descifrado[:-longitud_relleno].decode()
    # Imprime el texto descifrado para verificar que coincida con el texto original antes de cifrar
    print("Texto descifrado con DES:", texto_descifrado)
    # Retorna el texto descifrado como cadena de texto
    return texto_descifrado


# Cifra el texto utilizando AES-256 en modo CBC
def cifrar_AES(llave, iv, texto):
    # Creacion objeto cifrador para cifrar AES-256 en modo CBC
    cifrador = AES.new(llave, AES.MODE_CBC, iv)
    # Padding (en caso de ser necesario) para cumplir la longitud multiplo de 16 (bloque de AES)
    longitud_relleno = 16 - (len(texto) % 16)
    texto_rellenado = texto + (chr(longitud_relleno) * longitud_relleno)
    # Ciframos texto
    texto_cifrado = cifrador.encrypt(texto_rellenado.encode())
    # Imprime el texto cifrado en formato hexadecimal para facilitar la comprension y comparativa
    print("Texto cifrado con AES-256 (hex):", binascii.hexlify(texto_cifrado).decode())
    # Retorna el texto cifrado en formato de bytes
    return texto_cifrado

# Descifra el texto cifrado utilizando AES-256 en modo CBC
def descifrar_AES(llave, iv, texto_cifrado):
    # Creacion objeto cifrador para descifrar AES-256 en modo CBC
    cifrador = AES.new(llave, AES.MODE_CBC, iv)
    # Se descifra el texto cifrado
    texto_descifrado = cifrador.decrypt(texto_cifrado)
    # Obtencion tamano del relleno en base al ultimo byte del texto descifrado
    longitud_relleno = texto_descifrado[-1]
    # Eliminacion del relleno
    texto_descifrado = texto_descifrado[:-longitud_relleno].decode()
    # Imprime el texto descifrado para verificar que coincida con el texto original antes de cifrar
    print("Texto descifrado con AES-256:", texto_descifrado)
    # Retorna el texto descifrado como cadena de texto
    return texto_descifrado

# Cifra el texto utilizando 3DES en modo CBC
def cifrar_3DES(llave, iv, texto):
    # Creacion objeto cifrador para cifrar 3DES en modo CBC
    cifrador = DES3.new(llave, DES3.MODE_CBC, iv)
    # Padding (en caso de ser necesario) para cumplir la longitud multiplo de 8 (bloque de 3DES)
    longitud_relleno = 8 - (len(texto) % 8)
    texto_rellenado = texto + (chr(longitud_relleno) * longitud_relleno)
    # Ciframos texto
    texto_cifrado = cifrador.encrypt(texto_rellenado.encode())
    # Imprime el texto cifrado en formato hexadecimal para facilitar la comprension y comparativa
    print("Texto cifrado con 3DES (hex):", binascii.hexlify(texto_cifrado).decode())
    # Retorna el texto cifrado en formato de bytes
    return texto_cifrado

# Descifra el texto cifrado utilizando 3DES en modo CBC
def descifrar_3DES(llave, iv, texto_cifrado):
    # Creacion objeto cifrador para descifrar 3DES en modo CBC
    cifrador = DES3.new(llave, DES3.MODE_CBC, iv)
    # Se descifra el texto cifrado
    texto_descifrado = cifrador.decrypt(texto_cifrado)
    # Obtencion tamano del relleno en base al ultimo byte del texto descifrado
    longitud_relleno = texto_descifrado[-1]
    # Eliminacion del relleno
    texto_descifrado = texto_descifrado[:-longitud_relleno].decode()
    # Imprime el texto descifrado para verificar que coincida con el texto original antes de cifrar
    print("Texto descifrado con 3DES:", texto_descifrado)
    # Retorna el texto descifrado como cadena de texto
    return texto_descifrado



# Entrada de datos
# llave_entrada = holaholacomocomotevatevaholacomo
llave_entrada = input("Ingrese la llave: ").encode()
# iv_entrada = chaochaochaochao
iv_entrada = input("Ingrese el IV: ").encode()
# texto_entrada = hackhackha
texto_entrada = input("Ingrese el texto a cifrar: ")

print("\n------------------------------------\n")


# Ajustar llaves y IV segun el algoritmo
llave_DES = preparar(llave_entrada, 8, "Llave DES")
iv_DES = preparar(iv_entrada, 8, "IV DES")
# Cifrado y descifrado con cada algoritmo
print("\n--- Cifrado y Descifrado con DES ---")
texto_cifrado_DES = cifrar_DES(llave_DES, iv_DES, texto_entrada)
descifrar_DES(llave_DES, iv_DES, texto_cifrado_DES)

print("\n------------------------------------\n\n")


llave_AES = preparar(llave_entrada, 32, "Llave AES-256")
iv_AES = preparar(iv_entrada, 16, "IV AES-256")
print("\n--- Cifrado y Descifrado con AES-256 ---")
texto_cifrado_AES = cifrar_AES(llave_AES, iv_AES, texto_entrada)
descifrar_AES(llave_AES, iv_AES, texto_cifrado_AES)

print("\n------------------------------------\n\n")

llave_3DES = preparar(llave_entrada, 24, "Llave 3DES")
iv_3DES = preparar(iv_entrada, 8, "IV 3DES")
print("\n--- Cifrado y Descifrado con 3DES ---")
texto_cifrado_3DES = cifrar_3DES(llave_3DES, iv_3DES, texto_entrada)
descifrar_3DES(llave_3DES, iv_3DES, texto_cifrado_3DES)
