#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


m = bytes.fromhex("AFAA1232BCFF")
k = bytes.fromhex("BCAA3332BCFA")

print(xor_data(m,k).hex())

#------------- OTRA FORMA DE TRABAJARLO -------
num1=0xAE12FF2235BC015F
num2=0xAE12FF2235BC015F
num3=(hex(num1^num2))
print(num3)
print(num3[2:])


