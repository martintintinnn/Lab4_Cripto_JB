from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
import binascii

def ajustar_clave(clave, longitud_requerida, tipo):
    if len(clave) < longitud_requerida:
        clave += get_random_bytes(longitud_requerida - len(clave))
        print(f"{tipo} ajustado a {longitud_requerida} bytes añadiendo bytes adicionales.")
    elif len(clave) > longitud_requerida:
        clave = clave[:longitud_requerida]
        print(f"{tipo} excedía {longitud_requerida} bytes y fue truncado.")
    print(f"{tipo} final utilizado (hex):", binascii.hexlify(clave).decode())
    return clave

def cifrar_DES(clave, iv, texto):
    #Cifra el texto utilizando DES en modo CBC.
    cipher = DES.new(clave, DES.MODE_CBC, iv)
    padding_length = 8 - (len(texto) % 8)
    texto_padded = texto + (chr(padding_length) * padding_length)
    texto_cifrado = cipher.encrypt(texto_padded.encode())
    print("Texto cifrado con DES (hex):", binascii.hexlify(texto_cifrado).decode())
    return texto_cifrado

def descifrar_DES(clave, iv, texto_cifrado):
    #Descifra el texto cifrado utilizando DES en modo CBC.
    cipher = DES.new(clave, DES.MODE_CBC, iv)
    texto_descifrado = cipher.decrypt(texto_cifrado)
    padding_length = texto_descifrado[-1]
    texto_descifrado = texto_descifrado[:-padding_length].decode()
    print("Texto descifrado con DES:", texto_descifrado)
    return texto_descifrado

def cifrar_AES(clave, iv, texto):
    #Cifra el texto utilizando AES-256 en modo CBC.
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    padding_length = 16 - (len(texto) % 16)
    texto_padded = texto + (chr(padding_length) * padding_length)
    texto_cifrado = cipher.encrypt(texto_padded.encode())
    print("Texto cifrado con AES-256 (hex):", binascii.hexlify(texto_cifrado).decode())
    return texto_cifrado

def descifrar_AES(clave, iv, texto_cifrado):
    #Descifra el texto cifrado utilizando AES-256 en modo CBC.
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    texto_descifrado = cipher.decrypt(texto_cifrado)
    padding_length = texto_descifrado[-1]
    texto_descifrado = texto_descifrado[:-padding_length].decode()
    print("Texto descifrado con AES-256:", texto_descifrado)
    return texto_descifrado

def cifrar_3DES(clave, iv, texto):
    #Cifra el texto utilizando 3DES en modo CBC.
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    padding_length = 8 - (len(texto) % 8)
    texto_padded = texto + (chr(padding_length) * padding_length)
    texto_cifrado = cipher.encrypt(texto_padded.encode())
    print("Texto cifrado con 3DES (hex):", binascii.hexlify(texto_cifrado).decode())
    return texto_cifrado

def descifrar_3DES(clave, iv, texto_cifrado):
    #Descifra el texto cifrado utilizando 3DES en modo CBC.
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    texto_descifrado = cipher.decrypt(texto_cifrado)
    padding_length = texto_descifrado[-1]
    texto_descifrado = texto_descifrado[:-padding_length].decode()
    print("Texto descifrado con 3DES:", texto_descifrado)
    return texto_descifrado

# Entrada de datos
# key_input = holaholacomocomotevatevaholacomo
key_input = input("Ingrese la clave: ").encode()
# iv_input =  chaochaochaochao
iv_input = input("Ingrese el IV: ").encode()
# texto_input = hackhackha
texto_input = input("Ingrese el texto a cifrar: ")

print("\n------------------------------------\n")




# Ajustar claves y IVs según el algoritmo
key_DES = ajustar_clave(key_input, 8, "Clave DES")
iv_DES = ajustar_clave(iv_input, 8, "IV DES")
# Cifrado y descifrado con cada algoritmo
print("\n--- Cifrado y Descifrado con DES ---")
texto_cifrado_DES = cifrar_DES(key_DES, iv_DES, texto_input)
descifrar_DES(key_DES, iv_DES, texto_cifrado_DES)

print("\n------------------------------------\n\n")


key_AES = ajustar_clave(key_input, 32, "Clave AES-256")
iv_AES = ajustar_clave(iv_input, 16, "IV AES-256")
print("\n--- Cifrado y Descifrado con AES-256 ---")
texto_cifrado_AES = cifrar_AES(key_AES, iv_AES, texto_input)
descifrar_AES(key_AES, iv_AES, texto_cifrado_AES)

print("\n------------------------------------\n\n")

key_3DES = ajustar_clave(key_input, 24, "Clave 3DES")
iv_3DES = ajustar_clave(iv_input, 8, "IV 3DES")
print("\n--- Cifrado y Descifrado con 3DES ---")
texto_cifrado_3DES = cifrar_3DES(key_3DES, iv_3DES, texto_input)
descifrar_3DES(key_3DES, iv_3DES, texto_cifrado_3DES)
