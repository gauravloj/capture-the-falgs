import sys

def oper(exp):
    return bin(eval(exp))[2:]

def main():
    if len(sys.argv) <= 1:
        print('Usage: python 11-binhex.py num1 num1')
        sys.exit(1)

    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num1 = int(num1, 2)
    num2 = int(num2, 2)

    while True:
        op = input('Enter operation (+, -, *, /, %, &, |, ^, <<, >>): ')

        if op == 'add':
            exp = f'{num1} + {num2}'
            print('Sum in binary:', oper(exp))
            print('Sum in hex:', hex(eval(exp)))
        if op == 'sub':
            exp = f'{num1} - {num2}'
            print('Difference in binary:', oper(exp))
            print('Difference in hex:', hex(eval(exp)))
        if op == 'mul':
            exp = f'{num1} * {num2}'
            print('Product in binary:', oper(exp))
            print('Product in hex:', hex(eval(exp)))
        if op == 'div':
            exp = f'{num1} / {num2}'
            print('Quotient in binary:', oper(exp))
            print('Quotient in hex:', hex(eval(exp)))
        if op == 'mod':
            exp = f'{num1} % {num2}'
            print('Remainder in binary:', oper(exp))
            print('Remainder in hex:', hex(eval(exp)))
        if op == 'and':
            exp = f'{num1} & {num2}'
            print('Bitwise AND in binary:', oper(exp))
            print('Bitwise AND in hex:', hex(eval(exp)))
        if op == 'or':
            exp = f'{num1} | {num2}'
            print('Bitwise OR in binary:', oper(exp))
            print('Bitwise OR in hex:', hex(eval(exp)))
        if op == 'xor':
            exp = f'{num1} ^ {num2}'
            print('Bitwise XOR in binary:', oper(exp))
            print('Bitwise XOR in hex:', hex(eval(exp)))
        if op == 'ls':
            print('Left shift num1 in binary:', bin(num1 << 1))
            print('Left shift num2 in binary:', bin(num2 << 1))
            print('Left shift num1 in hex:', hex(num1 << 1))
            print('Left shift num2 in hex:', hex(num2 << 1))
        if op == 'rs':
            print('Right shift num1 in binary:', bin(num1 >> 1))
            print('Right shift num2 in binary:', bin(num2 >> 1))
            print('Right shift num1 in hex:', hex(num1 >> 1))
            print('Right shift num2 in hex:', hex(num2 >> 1))




if __name__ == '__main__':
    main()
