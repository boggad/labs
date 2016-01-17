#!/usr/bin/env python3
# -*- coding: utf8 -*-
from base64 import b64encode, b64decode

class LCG():
    def __init__(self, state):
        self._a = 211
        self._b = 1663
        self._m = 7875
        self._state = state

    def reset(self, state):
        self._state = state

    def next(self):
        self._state = (self._state*self._a + self._b) % self._m
        return self._state

def lcg_xor(message, key):
    lcg = LCG(key)
    xored = []
    for c in message:
        xored.append(chr((ord(c) ^ (lcg.next() % 0xffff)) % 0xffff))
    return ''.join(xored)

def main():
    print('Шифровать или дешифровать?(e/d):')
    mode = input()
    if mode.lower() == 'q':
        return
    if mode.lower() == 'e':
        print('Введите ключ(число):')
        key = input()
        try:
            key = int(key)
        except ValueError:
            print('Ключ должен быть числом!')
            return
        print('Введите сообщение:')
        message = input()

        cipher = b64encode(lcg_xor(message, key).encode('utf-8')).decode('utf-8')
        print('Шифровка:')
        print(cipher)
        return

    if mode.lower() == 'd':
        print('Введите ключ(число):')
        key = input()
        try:
            key = int(key)
        except ValueError:
            print('Ключ должен быть числом!')
            return
        print('Введите шифровку:')
        cipher = b64decode(input()).decode('utf-8')
        message = lcg_xor(cipher, key)
        print('Расшифровка:')
        print(message)
        return

if __name__ == "__main__":
    main()
