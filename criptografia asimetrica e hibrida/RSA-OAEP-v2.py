from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os


#Cargar las claves
my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/public-rsa.pem"
path_file_priv = my_path + "/private-rsa.pem"

print("Ruta del archivo de clave pública:", path_file_publ)
print("Ruta del archivo de clave privada:", path_file_priv)

key_priv = RSA.importKey(open(path_file_priv).read())

key_publ = RSA.importKey(open(path_file_publ).read())


#Cifrado

#msg = bytes('Cifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidezCifrar con RSA grandes textos es una estupidez','utf8')
#print(len(msg))
# Si estas usando RSA 2048 y sha256. Se pasa a byte 2048, le quitas 2, lo vuelves a pasar a byte. Luego a eso le restas el doble del hash (512) y todo ello entre 8, te da 190.
#msg = bytes('Cifrar con RSA grandes textos es una estupidez','utf-8')
msg = bytes.fromhex('AFAFAFAFAFAFAFFFAFF12123233334FA')

#Si no se añade el hash, funciona pero con sha1 by default
#encryptor = PKCS1_OAEP.new(pubKey)
encryptor = PKCS1_OAEP.new(key_publ, SHA256)
encrypted = encryptor.encrypt(msg)

#print("Cifrado:", binascii.hexlify(encrypted))
print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")

#Descifrado
#encrypted2=bytes.fromhex("11337963e3ca371e79ed07e80e63d9a3eff6cc61f170c4e5dd2b2a8aa086704b953a748078a54e14acac55319aefb316d29451770c0f298fccc568c553712e0a6ed4a4f78d6a0f8435f9d0f7b0fb9558e644160d1abe1e1a4e43ecbf7dbceb16c93779531694ad897d4013274816f710ab527f8675cf10f53b42d234abb99931cc308dc7534165424a6ac683067c50da153a562688698095f7ab9656c8fdebb655f738216ac138a52d1a87fcbc5015140f75d2e1bffc1a1d15e691e795faf051b06d3762747ea27cb1401bb97f99db9da7e8651d0add0b5c239879ddeab95546fdcf65f69701c6c929698951ccd841f3da9e7edcdef33ced20f068607e2284206624d1ff7a97ab0c7c93fd4804d447c3dfd91b7769165c5411de0ef78341fe29582aa374c153e77f9b0c1c54b899512d301a802d95e85562b8a5bd0da8430b40471df528e025ed0e94a7148f97d386e4a6391938873906a1dec08431caca3596974cf46b0e95063821b1e704711033ddf506ea4a1f4c6ebdf4398010bddf9bd0")
decryptor = PKCS1_OAEP.new(key_priv,SHA256)
decrypted = decryptor.decrypt(encrypted)
print('Descifrado:', decrypted.hex())


#Archivo -> Preferencias -> Configuracion -> execut -> Python › Terminal: Execute In File Dir