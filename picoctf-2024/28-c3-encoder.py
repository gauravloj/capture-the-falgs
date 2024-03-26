import sys
chars = ""
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"


def decrypt(chars):
    out = ""
    prev = 0
    for char in chars:
        cur = lookup2.index(char)
        out += lookup1[(cur + prev) % 40]
        prev = (cur + prev) % 40
    return out


def encrypt(chars):
    out = ""
    prev = 0
    for char in chars:
        cur = lookup1.index(char)
        out += lookup2[(cur - prev) % 40]
        prev = cur
    return out



if __name__ == "__main__":
    # run : python3 <scriptfilename> d <(cat ciphertext)
    # ciphertext: DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl
    if len(sys.argv) < 2:
        print("Usage: convert.py [e|d] [file]")
        sys.exit(1)
    if sys.argv[1] == "e":
        with open(sys.argv[2], "r") as f:
            for line in f:
                chars += line
        print(encrypt(chars))
    elif sys.argv[1] == "d":
        with open(sys.argv[2], "r") as f:
            for line in f:
                chars += line
        print(decrypt(chars))
    else:
        print("Usage: convert.py [encrypt|decrypt] [file]")
        sys.exit(1)

"""

# Runnint `python3 28-c3-encoder.py d <(cat ciphertext)` will give the following output

#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1

"""

"""
There are 4 clues given, asciiorder, fortychars, selfinput, pythontwo

I tried sending below output:

My understanding:
asciiorder -> printable characters in ascii, can be all the characters, or just alphabets,
              or alphanumeric characters.
fortychars -> 40 characters, length of the output
selfinput -> Each string is passed from stdin, implies that last character is '\n'
pythontwo -> Couldn't figure out, only that this script is python 2


    chars = '0123456789@ABCDEFGHIPQRSTUVWXYZabcdefghipqrstuvwxyz\n'
    chars = "#asciiorder#fortychars#selfinput#pythontwo"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\n#()*+/1:=[]abcdefghijklmnopqrstuvwxyz\n"
    # chars = '!#$%&()0123456789@ABCDEFGHIPQRSTUVWXYZabcdefghipqrstuvwxyz\n'
    # chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\n"
    # chars = '!"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\n'
    # chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\n'
    # chars = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
"""

"""
Then I thought about 'selfinput'.

Maybe, this script itself it the input to the script. So, I tried running the script with itself as input.


Initially, to get the 40 char output, I ran the scripts with the selfinput continuously:

$ filename=decoded-script.py
$ python3 decoded.py < <(for i in `seq 1 2000`; do cat $filename; done) | sed 's/\r\n$//' > falg.txt

It gave:
> adlibs:prh  " wrnlpabiach "an:#di s ur   ")rr =af#i   lnp fptiibg )a 



Then I tried running it for just once and it gave the output as below:
> adlibs

I thought, flag will be in ascii order, so I tried `abdils` as flag, but it didn't work.
Then I tried `adlibs` as flag, and it worked.

"""
