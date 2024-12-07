from Crypto.Hash import HMAC, SHA256



def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result

# LO QUE QUEREMOS EJECUTAR O HACER (CALCULAR MAC) EJEMPLO UNA COMPRA DE 100 EUR CORRECTA DA OK
clave_bytes = bytes.fromhex('7212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
datos = bytes("KeepCoding Mola mucho", "utf8")

hmac = getHMAC(clave_bytes,datos)

print(hmac)

print(validateHMAC(clave_bytes, datos,hmac))

#SI ALGUIEN QUIERE CAMBIAR ESTO NOS DARA UN KO (AVISA QUE HAY HACKER)
#datos1 = bytes("1000 eur // comercio pepe // 45254356435", "utf8")
#hmac1 = getHMAC(clave_bytes,datos1)
#print(hmac1)
#print(validateHMAC(clave_bytes, datos1,hmac))