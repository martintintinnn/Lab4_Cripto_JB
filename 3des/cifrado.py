from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
import binascii

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

print("\n--- Cifrado y Descifrado con 3DES ---")
texto_cifrado_3DES = cifrar_3DES(llave_3DES, iv_3DES, texto_entrada)
descifrar_3DES(llave_3DES, iv_3DES, texto_cifrado_3DES)