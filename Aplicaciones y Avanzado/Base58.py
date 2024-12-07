import base58

print(base58.b58encode(b'hello world'))

print(base58.b58decode(b'StV1DL6CwTryKyV'))

print(base58.b58encode_check(b'hello world'))

print(base58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh'))

#print(base58.b58decode_check(b'4vQB7B6MrGQZaxCuFg4oh'))

print(base58.b58encode(b'hello world', alphabet=base58.XRP_ALPHABET))

print(base58.b58decode(b'StVrDLaUATiyKyV', alphabet=base58.XRP_ALPHABET))
