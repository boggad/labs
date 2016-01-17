#!/usr/bin/env python3
#-*- coding: utf8 -*-

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890-_ '

MAXL = len(ALPHABET)

class GammaCipher:
    def __init__(self):
        self._gamma_state = 0
        self._gamma_a = 936
        self._gamma_b = 1399
        self._gamma_m = 6655

    def strip(self, message):
        stripped = []
        for c in message:
            if not c in ALPHABET:
                stripped.append('_')
            else:
                stripped.append(c)
        return ''.join(stripped)

    def init_lcg(self, key):
        self._gamma_state = key

    def lcg_next(self):
        self._gamma_state = (self._gamma_state*self._gamma_a + self._gamma_b) % self._gamma_m
        return self._gamma_state % MAXL

    def encrypt(self, key, message):
        message = self.strip(message)
        self.init_lcg(key)
        encrypted = []
        for c in message:
            g = self.lcg_next()
            ti = ALPHABET.index(c)
            ci = (ti + g) % MAXL
            encrypted.append(ALPHABET[ci])
        return ''.join(encrypted)

    def decrypt(self, key, cipher):
        self.init_lcg(key)
        decrypted = []
        for c in cipher:
            g = self.lcg_next()
            ci = ALPHABET.index(c)
            ti = (ci - g + MAXL) % MAXL
            decrypted.append(ALPHABET[ti])
        return ''.join(decrypted)


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

        gamma = GammaCipher()
        cipher = gamma.encrypt(key, message)
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
        cipher = input()

        gamma = GammaCipher()
        message = gamma.decrypt(key, cipher)
        print('Расшифровка:')
        print(message)
        return

if __name__ == "__main__":
    main()
