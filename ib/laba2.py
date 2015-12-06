#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from base64 import b64encode, b64decode

class LCG:
    def __init__(self, seed):
        self._a = 106
        self._b = 1283
        self._m = 6075
        self._seed = seed
        self._state = seed

    def next(self):
        self._state = (self._a * self._state + self._b) % self._m
        return self._state

def lcg_xor(message, key):
    lcg = LCG(key)
    xored = ''
    for c in message:
        xored += chr((ord(c) ^ (lcg.next() % 0xffff)) % 0xffff)
    return xored

def main():
    from sys import argv
    decrypt = '-d' in argv
    if decrypt:
        print('Введите зашифрованный текст(base64):')
        cipher = b64decode(input()).decode('utf-8')
        print('Введите ключ(число):')
        key = 0;
        try:
            key = int(input())
        except ValueError:
            print('Неверный ключ')
            return
        print('Исходное сообщение:\n%s' % (lcg_xor(cipher, key)))
    else:
        print('Введите исходное сообщение:')
        message = input()
        print('Введите ключ(число):')
        try:
            key = int(input())
        except ValueError:
            print('Неверный ключ')
            return
        print('Зашифрованный текст:\n%s' % (b64encode(lcg_xor(message,key).encode('utf-8'))).decode('utf-8'))

if __name__ == "__main__":
    main()

