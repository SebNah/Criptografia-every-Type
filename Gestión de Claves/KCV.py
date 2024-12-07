
   
import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes.fromhex('00000000000000000000000000000000')
#Se puede generar aleatoriamente una clave de 16 bytes.
#EL UNICO CAMBIO PARA CALCULAR EL KCV ES CAMBIAR LA CLAVE QUE QUEREMOS CALCULAR
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
print("KCV:", texto_cifrado_bytes.hex()[0:6])


cipher2 = AES.new(clave, AES.MODE_ECB)
texto_cifrado_bytes2 = cipher2.encrypt(textoPlano_bytes)
print("KCV:", texto_cifrado_bytes2.hex()[0:6])


m = hashlib.sha256()
m.update(bytes.fromhex("c936108299307d3f6f7585b96013346e"))
print("KCV SHA256: " + m.digest().hex()[0:6])

