# Cifrado y descifrado con cada algoritmo
print("\n--- Cifrado y Descifrado con AES-256 ---")
texto_cifrado_AES = cifrar_AES(key_AES, iv_AES, texto_input)
descifrar_AES(key_AES, iv_AES, texto_cifrado_AES)

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