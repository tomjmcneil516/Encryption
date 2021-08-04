import sys

plaintext = open(sys.argv[2], "rb")
keyfile = open(sys.arv[1], "rb")
ciphertext = open(sys.argv[3], "wb")

plaintext_byte = plaintext.read(1)
keyfile_byte = keyfile.read(1)

while plaintext_byte:
    cipher_byte = (sum(bytearray(plaintext_byte + keyfile_byte)) % 256).to_bytes(1,'big')
    ciphertext.write(cipher_byte)
    plaintext_byte = plaintext.read(1)
    keyfile_byte = keyfile.read(1)
    if not keyfile_byte:
        keyfile.seek(0)
        keyfile_byte = keyfile.read(1)

plaintext.close()
keyfile.close()
ciphertext.close()