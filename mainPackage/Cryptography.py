#!/usr/bin/env python3
import os
import tkinter as tk
from re import search


def generateKey(length):
    key = [x % 26 for x in os.urandom(length)]
    return key


def isAplha(x):
    x = search(r'[a-zA-Z]', x)
    return False if x is None else True


def encode():
    text = textField.get("0.0", tk.END)
    text = text.strip()
    code = loadKey()
    if len(text) > len(code):
        raise Exception("Text is too long")
    encoded = []
    zipped = zip(text, code)
    for letter, offset in zipped:
        if isAplha(letter):
            num = ord(letter.lower())
            newNum = (num - 97 + offset) % 26 + 97
            encoded.append(chr(newNum))
        else:
            encoded.append(letter)
    with open('encodedText.txt', 'w') as f:
        f.write(''.join(encoded))


def decode():
    text = textField.get("0.0", tk.END)
    text = text.strip()
    code = loadKey()
    decoded = []
    zipped = zip(text, code)
    for letter, offset in zipped:
        if isAplha(letter):
            newNum = ord(letter) - 97 - offset
            newNum += 97 if newNum >= 0 else 123
            decoded.append(chr(newNum))
        else:
            decoded.append(letter)
    with open('decodedText.txt', 'w') as f:
        f.write(''.join(decoded))


def loadKey():
    key = None
    try:
        with open(codesfileField.get(), 'r') as f:
            for i in range(int(codesfileRow.get())):
                key = f.readline()
            if key is not None:
                key = key.strip()
                return [int(k) for k in key.split(' ')]
            raise Exception("Wrong line number")
    except FileNotFoundError:
        print("No file found!")


window = tk.Tk()
window.title('Cryptography')
window.config(width=500, height=1000)
window.resizable(0, 0)

textField = tk.Text(window)
textField.grid(row=1, column=0, columnspan=4)

codesfileField = tk.Entry(window)
codesfileField.grid(row=0, column=0, columnspan=1)
codesfileField.insert(0, "File with keys")

codesfileRow = tk.Entry(window)
codesfileRow.insert(0, "Row number")
codesfileRow.grid(row=0, column=1)

encButton = tk.Button(window, text='Encrypt', command=encode)
encButton.grid(row=0, column=2)

decButton = tk.Button(window, text='Decrypt', command=decode)
decButton.grid(row=0, column=3)

window.mainloop()
