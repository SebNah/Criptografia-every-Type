import hashlib
from Crypto.Random import get_random_bytes





#Los malos calculaban todos los hashes posibles de password tipicas
#Anadimos un salt al mensaje de entrada para asegurar evitar esto
#SIN PEPPER
#cadena = "hola"
#salt = get_random_bytes(16)
#salt_hex = salt.hex()
#cadena_salt = cadena + salt_hex
#m = hashlib.sha256()
#m.update(bytes(cadena_salt, "utf8"))
#print("hash de la pass: " + m.digest().hex()) 
#print(cadena_salt)
#print("hash de la pass: " + m.digest().hex())



#Anadimos ademas un pepper, un pepper para una base de datos y el otro para la otra base de datos
pepper = "Pepper"

cadena = "hola"

salt = get_random_bytes(16)

salt_hex = salt.hex()

cadena_salt_pepper = cadena + salt_hex + pepper

m = hashlib.sha256()
m.update(bytes(cadena_salt_pepper, "utf8"))
print("hash de la pass: " + m.digest().hex()) 

print(cadena_salt_pepper)

print("hash de la pass: " + m.digest().hex())