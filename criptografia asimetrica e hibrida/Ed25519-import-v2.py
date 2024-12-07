import ed25519


publickey = open("mypublickey-ed25519","rb").read()
#privatekey = open("myprivatekey-ed25519","rb").read()

#signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
#signature = signedKey.sign(msg, encoding='hex')

#
# print("Firma Generada (64 bytes):", signature)

signature = "bf32592dc235a26e31e231063a1984bb75ffd9dc5550cf30105911ca4560dab52abb40e4f7e2d3af828abac1467d95d668a80395e0a71c51798bd54469b7360d"

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
