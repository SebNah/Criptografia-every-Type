from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash("s3kr3tp4ssw0rd")
print(hash)  
#Ejemplo de salida
#'$argon2id$v=19$m=102400,t=2,p=8$tSm+JOWigOgPZx/g44K5fQ$WDyus6py50bVFIPkjA28lQ'
ph.verify(hash, "s3kr3tp4ssw0rd")