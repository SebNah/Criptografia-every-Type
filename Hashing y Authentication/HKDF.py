from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets

salt = secrets.token_bytes(16)
master_secret = secrets.token_bytes(64)
print(master_secret.hex())
key1, key2, key3 = HKDF(master_secret, 32, salt, SHA512, 3)

print("Clave key1: ", key1.hex())
print("Clave key2: ", key2.hex())
print("Clave key2: ", key3.hex())




#Soy un servidor de google autenticator, -> tengo una key master = "4678934ca35b738bd28b8c23a6fc739f2875ef35"
#Ahora necesito generar dos claves, una para cifrar y otra para el MAC
#salt sera el email o el telefono
# salt sera mi email, supongamos que sebbaflores@gmail.com es 3562551616
#Quiero generar una clave para hablar con este dispositivo
#Pero no quiero almacenar en la base de datos todas las claves
#Genero una clave maestra y luego las diversifico usando un salt y un algoritmo (SHA512)
print("EJEMPLO GOOGLE")

master_secret_google = bytes.fromhex("4678934ca35b738bd28b8c23a6fc739f2875ef35")
salt = bytes.fromhex("3562551616")#Email
key1_cifrado, key2_mac= HKDF(master_secret_google, 32, salt, SHA512, 2)

print("Clave Cifrado: ", key1_cifrado.hex())
print("Clave MAC: ", key2_mac.hex())

