import hashlib

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

#Calcular MD5 de Fray = 46524159 hexadecimal
m = hashlib.md5()
m.update(bytes.fromhex("46524159"))
print("md5 hex :     ", m.digest().hex())

print("Si observamos los dos anteriores podemos observar que los dos tienen 32 caracteres")

m = hashlib.sha1()
m.update(bytes("Hola", "utf8"))
print("SHA1:   " + m.digest().hex())

#SHA256
m = hashlib.sha256()
m.update(bytes("Es imposible obtener la cadena desde una origen", "utf8"))
print("SHA256: " + m.digest().hex())

#SHA512
m = hashlib.sha512()
m.update(bytes("KeepCoding Mola Mucho", "utf8"))
print("SHA512: " + m.digest().hex())

#7d6394ab738b066e316fbee6e36a5ff7e4d99857aeeaf051f7f06c6e4041e2a4
#4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833

#KECCAK
# initiating the "s" object to use the
# sha3_256 algorithm from the hashlib module.
#Abajo analizar que ponemos sha3 y la longitud que queremos que tenga
s = hashlib.sha3_256()

# will output the name of the hashing algorithm currently in use.
print(s.name)

# will output the Digest-Size of the hashing algorithm being used.
print("SHA3 Keecak:     ", s.digest_size)

# providing the input to the hashing algorithm.
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))

print(s.hexdigest())


