from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


""" The standard defines 3 Keying Options:

El estándar define tres opciones de clave_
Opc 1: Todas los componentes distintos
Opc 2: K1=K3 y K1!=K2
Opc 3: K1=K2=K3  """

#Esto fuerza que no se de la opción 3
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        #key = bytes.fromhex("e6f80202fd435ec8da4a58255d2f2f04df4670e5daa8ab26")
        print("La clave es: ", key.hex())
        break
    except ValueError:
        pass


#ESTE ES EL PROCESO DE CIFRADO
cipher = DES3.new(key, DES3.MODE_CBC)

plaintext = bytes('La vida es bella','utf8')
msg = cipher.encrypt(plaintext)
mensaje_cifrado = cipher.iv + msg
iv = cipher.iv
print("iv: ", cipher.iv.hex())
print(msg.hex())

# https://gchq.github.io/CyberChef/ --> cbc/nopadding



#ESTE ES EL PROCESO DE DESCIFRADO
cipher2 = DES3.new(key,DES3.MODE_CBC,iv)
mensaje_en_claro = cipher2.decrypt(msg)
print(mensaje_en_claro.hex())
print(mensaje_en_claro.decode('utf-8'))
