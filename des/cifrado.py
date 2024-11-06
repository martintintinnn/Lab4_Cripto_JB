# Cifrado y descifrado con cada algoritmo
print("\n--- Cifrado y Descifrado con DES ---")
texto_cifrado_DES = cifrar_DES(key_DES, iv_DES, texto_input)
descifrar_DES(key_DES, iv_DES, texto_cifrado_DES)

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