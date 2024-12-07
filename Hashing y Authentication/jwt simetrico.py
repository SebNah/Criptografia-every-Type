import jwt

encoded_jwt = jwt.encode({"Juanma": "451215151", "mail":"juanma@mail.com"}, "Con KeepCoding aprendemos", algorithm="HS256")

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)



