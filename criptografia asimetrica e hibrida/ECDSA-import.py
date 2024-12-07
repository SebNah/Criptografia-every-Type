from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

""" f_escribir_priv  = open("myprivatekey-ecdsa.pem","wt")
key = ECC.generate(curve='P-256')
f_escribir_priv.write(key.export_key(format='PEM'))
f_escribir_priv.close()
#print("Clave Privada: \n", privKey)

f_escribir_publ = open("mypublickey-ecdsa.pem","wt")
f_escribir_publ.write(key.public_key().export_key(format='PEM'))
f_escribir_publ.close()
#print("Clave Pública: \n", publicKey) """




f_priv = open("myprivatekey-ecdsa.pem","rt")
privKey = ECC.import_key(f_priv.read())

f_public = open("mypublickey-ecdsa.pem","rt")

publicKey = ECC.import_key(f_public.read())

f_priv.close()
f_public.close()


# Generación de firma
# Modificado partiendo de  https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
#message = bytes('Se debe hacer una propuesta de mejora del contrato de venta','utf8')
#802404a65c03daaa87a3b177400008c6efe5e817a3942f3c69d9e0d8e960a914

#el sha256 del texto anterior
message = bytes.fromhex("802404a65c03daaa87a3b177400008c6efe5e817a3942f3c69d9e0d8e960a914")

key_orig = privKey
h = SHA256.new(message)

#El tipo de firma es el sugerido en el documento de fips-186-3.
signer = DSS.new(key_orig, 'fips-186-3')
signature = signer.sign(h)

print("Firma: " + signature.hex())


# Verificación de firma
key_dest = publicKey
h = SHA256.new(message)
verifier = DSS.new(key_dest, 'fips-186-3')
try:
    verifier.verify(h, signature)
    print ("Mensaje autenticado")
except ValueError:
    print ("Mensaje no autenticado")


#Intentando cambiar el mensaje firmado

signature2= bytes.fromhex("b7bb80c22210b2ffbc0a0a03bdf9ec885d36dab6a2d45298bedb0eb1300b7acdeb8bbc0211310a94569d8cc6104064c85d1edeef58af0c9c1405c24b54f2559d")
# Verificación de firma
key_dest = publicKey
h = SHA256.new(message)
verifier = DSS.new(key_dest, 'fips-186-3')
try:
    verifier.verify(h, signature2)
    print ("Mensaje autenticado")
except ValueError:
    print ("Mensaje no autenticado")