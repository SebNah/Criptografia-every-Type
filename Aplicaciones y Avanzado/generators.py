import argparse
import hashlib

from binascii import hexlify, unhexlify
from struct import Struct
from utils import g, b58encode, b58decode
import secrets

#Generador de claves partiendo del existente en https://github.com/PaulGregor/Bitcoin-Keys-Generator


PACKER = Struct('>QQQQ')


def count_leading_zeroes(s):
    count = 0
    for c in s:
        if c == '\0':
            count += 1
        else:
            break
    return count


def base58_check_encode(prefix, payload, compressed=False):
    # Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
    s = prefix + payload
    if compressed:
        s = prefix + payload + b'\x01'

    # Add the 4 checksum bytes at the end of extended RIPEMD-160 hash. This is the 25-byte binary Bitcoin Address.
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]

    result = s + checksum

    return '1' * count_leading_zeroes(result) + b58encode(result).decode()


def pub_key_to_addr(s):
    ripemd160 = hashlib.new('ripemd160')

    hash_sha256 = hashlib.new('SHA256')

    # Perform SHA-256 hashing on the public key
    hash_sha256.update(bytes.fromhex(s))

    # Perform RIPEMD-160 hashing on the result of SHA-256
    ripemd160.update(hash_sha256.digest())

    return base58_check_encode(b'\0', ripemd160.digest())


def int_to_address(number):
    number0 = number >> 192
    number1 = (number >> 128) & 0xffffffffffffffff
    number2 = (number >> 64) & 0xffffffffffffffff
    number3 = number & 0xffffffffffffffff

    private_key = hexlify(PACKER.pack(number0, number1, number2, number3)).decode("utf-8")

    print('Converting from: ' + str(int(private_key, 16)))

    compressed_key = base58_check_encode(b'\x80', unhexlify(private_key), True)
    print('Private key: ' + compressed_key)

    # address
    x, y = str(g * int(private_key, 16)).split()
    len1 = len(x)
    len2 = len(y)
    if len1 != 64:
        z = 64 - len1
        x = '0'*z + x

    if len2 != 64:
        z = 64 - len2
        y = '0'*z + y
    compressed_public_key_with_out_prefix = x + y

    pk_prefix = '02'
    if not int(compressed_public_key_with_out_prefix[64:], 16) % 2 == 0:
        pk_prefix = '03'
    compressed_public_key = pk_prefix + compressed_public_key_with_out_prefix[:64]

    print('Public key: ' + compressed_public_key)
    print('Bitcoin address: ' + pub_key_to_addr(compressed_public_key))


def wif_to_key(wif):
    slicer = 4
    if wif[0] in ['K', 'L']:
        slicer = 5

    return hexlify(b58decode(wif)[1:-slicer]).decode('utf-8')


def main():
    parser = argparse.ArgumentParser(description='Generates private key, public key and wallet address from number')

    parser.add_argument('number', type=int, nargs='?', default=1,
                        help='A required integer number argument')
    args = parser.parse_args()

    if args.number == 1:
        my_number = secrets.SystemRandom().randint(0,5000000000000000000000000)
        #print(my_number)
        int_to_address(my_number)
    else:
        int_to_address(args.number)


if __name__ == "__main__":
    main()

