#Conversiones Codificaciones y Decodificaciones

#Cadena UTF8 a Hex
textoClaro = "Viva KeepCoding"

string_hex = bytes(textoClaro, "UTF-8").hex() #aqui transformamos UTF8 en bytes. Luego bytes en Hexadecimal y guardamos en una variable

print('UTF8 A HEXADECIMAL :')
print(textoClaro)
print(string_hex)
print('----------------------------------------------------------------')



#Cadena UTF8 a Base64
import base64
textoClaro2 = "Hola Fray, nos vemos en el restaurante"

string_b64 = base64.b64encode(bytes(textoClaro2, "UTF-8")) 
#Aqui transformamos UTF8 en bytes. Luego bytes en Base64 y guardamos en una variable

print('UTF8 A BASE64 :')
print(textoClaro2)
print(string_b64.decode('UTF-8'))
print(string_b64)

print('----------------------------------------------------------------')



#Cadena B64 a UTF8

textoB64 = 'Vml2YSBLZWVwQ29kaW5n'
print("El codigo B64", textoB64," descifrado a UTF8 en claro es:")
print(base64.b64decode(textoB64).decode("utf8")) 
#Aqui decodificamos el texto Base 64 a Bytes, luego decodificamos los bytes en UTF8 para imprimirlos



print('----------------------------------------------------------------')


#Cadena Hex a UTF8

textoHex = "56697661204b656570436f64696e67"
print('El codigo en HEX', textoHex, ' descifrado a UFT8 en claro es:')
print(bytes.fromhex(textoHex).decode("utf8")) 
#Aqui decodificamos el texto Hexadecimal a bytes, luego decodificamos los bytes en UTF8 para imprimirlos

print('----------------------------------------------------------------')


#Cadena Hex a Bytes

print(bytes.fromhex(textoHex))

print('----------------------------------------------------------------')


#Cadena B64 a Bytes

print(base64.b64decode(textoB64))

print('----------------------------------------------------------------')

print(bytes.fromhex(bytes("PEPITO DE LOS PALOTES", "UTF-8").hex()).decode("utf8"))
#En este codigo codificamos primero el texto de UTF8 a bytes para terminar codificarlo a Hexadecimal
#Luego lo decodificamos de Hexadecimal a bytes para al final volverlo a decodificar a UTF8




