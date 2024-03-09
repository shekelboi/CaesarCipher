def encrypt(text, shift=1):
    out = ''
    for c in text:
        position_in_alphabet = ord(c) - ord('a')
        new_position = (position_in_alphabet + shift) % 26
        new_ascii_position = new_position + ord('a')
        out += chr(new_ascii_position)
    return out


def ascii_to_binary(c):
    return bin(ord(c))[2:]


def binary_to_ascii(b):
    return chr(int(b, base=2))


shift = int(input('Enter how many characters we should shift by: '))
filename = 'input.txt'
text = input('Enter the text to encrypt: ')
text = encrypt(text, shift)
output = [ascii_to_binary(c) for c in text]

with open(filename, 'w') as file:
    file.write(' '.join(output))

with open(filename, 'r') as file:
    binaries = file.read().split()
    cipher = ''.join([binary_to_ascii(b) for b in binaries])
    decrypted = encrypt(cipher, -shift)
    print(decrypted)
