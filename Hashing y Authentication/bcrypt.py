from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check

#Proceso de alta en una web =+-> almacenamos en la base de datos.
password = bytes('KeepCoding es un valor seguro', 'utf8')
b64pwd = b64encode(SHA256.new(password).digest())
#b64pwd = password
#print(len(b64pwd))

bcrypt_hash = bcrypt(b64pwd, 12)
#print(bcrypt_hash.hex())

#Proceso de login en una web -> consultamos la base de datos para recuperar hash
password_to_test = bytes('KeepCoding es un valor seguro', 'utf8')
#Si en el texto de arriba ponemos mal un caracter el sistema lo detecta y avisa Password incorrecta
#Si en el texto de arriba esta bien colocada la password entonces da Password correcta

try:
    b64pwd = b64encode(SHA256.new(password_to_test).digest())
    bcrypt_check(b64pwd, bcrypt_hash)
    print("Password correcta")
except ValueError:
    print("Password incorrecta")