"""
nc titan.picoctf.net 62970
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: yhcmk
Enter the Little Endian representation: 6B6D636879
Correct Little Endian representation!
Enter the Big Endian representation: 7968636D6B
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_817b7cfe}


Usage: python 13-endianess.py yhcmk
output:
Little Endian: 6B6D636879
Big Endian: 7968636D6B
"""

import sys

def print_endian(string):
    hex_str = ''.join([hex(ord(c))[2:] for c in string])
    little_endian = ''.join([hex_str[i:i+2] for i in range(0, len(hex_str), 2)][::-1])
    print(f"Little Endian: {little_endian.upper()}")
    print(f"Big Endian: {hex_str.upper()}")



if __name__ == "__main__":
    input_str = sys.argv[1]
    print_endian(input_str)

