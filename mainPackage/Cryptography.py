import os


def getPass(length):
    print('getpass', length)
    output = [x for x in os.urandom(length)]
    print(output)
    return output


def encode(text, code):
    print('encode', len(text), len(code))
    encoded = []
    zipped = zip(text, code)
    for (letter, offset) in zipped:
        encoded.append(str(ord(letter) ^ offset))
    return ','.join(encoded)


def decode(text, code):
    print('decode', len(text), len(code))
    decoded = []
    zipped = zip(text, code)
    for (letter, offset) in zipped:
        decoded.append(str(ord(letter) ^ offset))
    return ','.join(decoded)


t = "hello there"
for i in t: print(ord(i), ',', sep='', end='')
print()
p = getPass(len(t))
e = encode(t, p)
print(e)
d = decode(e, p)
print(d)
