# Cifrado y descifrado con cada algoritmo
print("\n--- Cifrado y Descifrado con 3DES ---")
texto_cifrado_3DES = cifrar_3DES(key_3DES, iv_3DES, texto_input)
descifrar_3DES(key_3DES, iv_3DES, texto_cifrado_3DES)

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
