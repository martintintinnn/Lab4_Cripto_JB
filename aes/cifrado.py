from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
import binascii

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

print("\n--- Cifrado y Descifrado con AES-256 ---")
texto_cifrado_AES = cifrar_AES(llave_AES, iv_AES, texto_entrada)
descifrar_AES(llave_AES, iv_AES, texto_cifrado_AES)

print("\n------------------------------------\n\n")