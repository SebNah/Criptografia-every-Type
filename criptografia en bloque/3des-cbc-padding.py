from base64 import b64decode
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

#Versión con gestión de padding.

key = bytes.fromhex("2b7e151628aed2a6abf715891defefef123456781232aaff")
iv = bytes.fromhex("1010011111111111")
cipher = DES3.new(key, DES3.MODE_CBC,iv)


#AQUI CIFRAMOS EL MENSAJE CON PADDING B64 Y MENSAJE CON IV HEX
#LA CLAVE DEBE ESTAR PREVIAMENTE COMPARTIDA
plaintext = bytes('A really secret messagesssssssss','utf8')
msg = cipher.encrypt(pad(plaintext, DES3.block_size,  style='pkcs7'))
mensaje_cifrado = iv + msg
b64_msg = b64encode(msg).decode('utf8')
print("El mensaje cifrado en base64: " + b64_msg)
print("El mensaje cifrado con iv: " + mensaje_cifrado.hex())
print("El mensaje cifrado en hex:" + msg.hex())

# https://gchq.github.io/CyberChef/ --> cbc/nopadding


#DESCIFRADO, PRIMERO DEFINE UN OBJETO A DESCIFRAR cipher2
# SEGUNDO PONE TODO EN UN SISTEMA PARA QUITAR PADDING Y DESCIFRAR
cipher2 = DES3.new(key,DES3.MODE_CBC,iv)
mensaje_en_claro = unpad(cipher2.decrypt(msg), DES3.block_size,style='pkcs7')
print(mensaje_en_claro.hex())
print(mensaje_en_claro.decode('utf-8'))
