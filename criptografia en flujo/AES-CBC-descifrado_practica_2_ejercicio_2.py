
   
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

clave = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')

print("iv:", iv_bytes.hex())


try:
  
    iv_desc_bytes = bytes.fromhex("00000000000000000000000000000000")
    texto_cifrado_bytes = b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")
    print(mensaje_des_bytes.hex())
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print("iv:", iv_bytes.hex())

    #vamos a intentar entender lo que hacemos 
    #ciframos el mismo texto una vez descifrado y vamos añadiendo caracteres.....

    textoPlano_bytes = bytes("El texto en claro es:  Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.", "utf-8")
    cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
    texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))

    print("iv:", iv_bytes.hex())
    print("Primera iteraccion texto cifrado:", texto_cifrado_bytes.hex())

    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    #No quito el padding para ver que sale....
    mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
    print("Texto en claro en bytes (primera iteracion)", mensaje_des_bytes.hex())
    #456c20746578746f20656e20636c61726f2065733a20204573746f20657320756e206369667261646f20656e20626c6f7175652074c3ad7069636f2e2052656375657264612c2076617320706f7220656c206275656e2063616d696e6f2e20c3816e696d6f2e0a0a0a0a0a0a0a0a0a0a
    #Si miras el padding es 0a que son 10 en hexadecimal.

    #añadimos un caracter... y el padding pasará a 09.
    textoPlano_bytes = bytes("1El texto en claro es:  Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.", "utf-8")
    cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
    texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='x923'))

    print("iv:", iv_bytes.hex())
    print("Segunda iteraccion texto cifrado:", texto_cifrado_bytes.hex())

    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    #No quito el padding para ver que sale....
    mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
    print("Texto en claro en bytes (segunda iteracion)", mensaje_des_bytes.hex())
#31456c20746578746f20656e20636c61726f2065733a20204573746f20657320756e206369667261646f20656e20626c6f7175652074c3ad7069636f2e2052656375657264612c2076617320706f7220656c206275656e2063616d696e6f2e20c3816e696d6f2e090909090909090909
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 