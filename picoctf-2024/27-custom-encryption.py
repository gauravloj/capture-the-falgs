from random import randint
import sys


"""
enc_flag: 
a = 94
b = 21
cipher is: [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]
"""

def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def dynamic_xor_decrypt(cipher_text, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text[::-1]

def decrypt(cipher, key):
    plain_text = ""
    for char in cipher:
        plain_text += chr(char // (key*311))
    return plain_text

def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    a, b = 94, 21
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')

def decrypt_flag(cipherfile, text_key):
    p = 97
    g = 31
    with open(cipherfile, 'r') as f:
        lines = f.readlines()
        line_a = lines[0].strip().split(' = ')
        a = int(line_a[1])

        line_b = lines[1].strip().split(' = ')
        b = int(line_b[1])

        line_cipher = lines[2].strip().split('[')[1].split(']')[0]
        cipher = list(map(int, line_cipher.split(',')))

    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semiplain = decrypt(cipher, shared_key)
    plaintext = dynamic_xor_decrypt(semiplain, text_key)
    return plaintext


if __name__ == "__main__":
    # message = sys.argv[1]
    # test(message, "trudeau")
    cipherfile = 'enc_flag'
    plaintext = decrypt_flag(cipherfile, "trudeau")
    print(f'plaintext is: {plaintext}')
    # picoCTF{custom_d2cr0pt6d_8b41f976}
