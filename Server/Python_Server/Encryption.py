from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad

class Encryption:

    def __init__(self, key):
        key_string =""
        for hex in key.split(", "):
            hex = hex[2:]
            key_string = key_string + hex.lower()
        key = bytes.fromhex(key_string)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, data):
        ciphertext = self.cipher.encrypt(data)
        return ciphertext

    def decrypt(self, data):
        clear = self.cipher.decrypt(data)
        return clear


# EXAMPLE
"""
key = "0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78";
enc = Encryption(key)
data = "xxxxxxxxxxxxxxxx"

hexadecimal_string1 = data.encode("utf8").hex()
print(hexadecimal_string1)

cipher = enc.encrypt(data.encode("utf8"))

hexadecimal_string2 = cipher.hex()
print(hexadecimal_string2)

clear = enc.decrypt(cipher)
print(clear.hex())
"""
