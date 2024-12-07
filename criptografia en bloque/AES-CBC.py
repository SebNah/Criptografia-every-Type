import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes('KeepCoding es una pasada', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
iv_b64 = b64encode(cipher.iv).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
print(texto_cifrado_b64)
mensaje_json = json.dumps({'iv':iv_b64, 'texto_cifrado':texto_cifrado_b64})
print(mensaje_json)

#Descifrado

try:
    b64 = json.loads(mensaje_json)
    iv_desc_bytes = b64decode(b64['iv'])
    texto_cifrado_bytes = b64decode(b64['texto_cifrado'])
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 