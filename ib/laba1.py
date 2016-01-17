#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# N = 129

import argparse

def cesar(plain, key):
    alphabet = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 ';
    N = len(alphabet)
    cipher = ''.join([alphabet[(alphabet.index(c)*key[0] + key[1]) % N] for c in alphabet])
    cipher_text = '';
    for c in plain:
        pos = alphabet.index(c);
        if pos < 0:
            cipher_text += ' '
        else:
            cipher_text += cipher[pos];
    print(cipher_text);

def cesar_d(cipher_text, key):
    alphabet = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 ';
    N = len(alphabet)
    cipher = ''.join([alphabet[(alphabet.index(c)*key[0] + key[1]) % N] for c in alphabet])
    plain_text = '';
    for c in cipher_text:
        pos = cipher.index(c);
        plain_text += alphabet[pos];
    print(plain_text);

def matrix_mul(m1, m2, modula):
    return [((m1[0][0]*m2[0] + m1[0][1]*m2[1]) % modula), ((m1[1][0]*m2[0] + m1[1][1]*m2[1]) % modula)]

def inv_matrix(m, N):
    det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
    det = det % N
    q = []
    R = N
    D = det
    mod = R % D
    while mod > 0:
        q.append(R // D)
        R = D
        D = mod
        mod = R % mod
    y = [0, 1]
    for i in range(2, len(q)+2):
        y.append(y[i-2] - y[i-1]*q[i-2])
    Y = y[len(y)-1] % N
    T = [[m[0][0], m[1][0]], [m[0][1], m[1][1]]]
    Astar = [[T[1][1], -T[1][0]], [-T[0][1], T[0][0]]]
    return [[s[0]*Y % N, s[1]*Y % N] for s in Astar]

def nod(a, b):
    while b:
        a, b = b, a%b
    return a


def hill(plain, key):
    alphabet = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 ';
    N = len(alphabet)
    mkey = [key[:2], key[2:]]
    det = mkey[0][0]*mkey[1][1] - mkey[0][1]*mkey[1][0]
    det = det % N
    if nod(det, N) != 1:
        print('НОД(A|N) должен равняться 1!')
        return

    if len(plain) % 2 == 1:
        plain += ' '
    bigrams = [[alphabet.index(plain[b*2]), alphabet.index(plain[b*2+1])] for b in range(0, len(plain)//2)]
    cipher_text = ''
    for b in bigrams:
        cb = matrix_mul(mkey, b, N)
        cipher_text += ''.join((alphabet[cb[0]], alphabet[cb[1]]))
    print(cipher_text)

def hill_d(cipher_text, key):
    alphabet = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 ';
    N = len(alphabet)
    mkey = [key[:2], key[2:]]
    mkey = inv_matrix(mkey, N)
    bigrams = [[alphabet.index(cipher_text[b*2]), alphabet.index(cipher_text[b*2+1])] for b in range(0, len(cipher_text)//2)]
    cipher_text = ''
    for b in bigrams:
        cb = matrix_mul(mkey, b, N)
        cipher_text += ''.join((alphabet[cb[0]], alphabet[cb[1]]))
    print(cipher_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=u'Шифрование методами Цезаря и Хилла')
    parser.add_argument('-d', help=u'Дешифровать', action="store_true");
    parser.add_argument('--cesar', help=u'Шифровать методом Цезаря', action="store_true");
    parser.add_argument('--hill', help=u'Шифровать методом Хилла', action="store_true");
    parser.add_argument('plain_text', metavar='T', type=str, nargs=1, help=u'Ихсходный текст');
    parser.add_argument('key', metavar='K', type=int, nargs='+', help=u'Ключ');
    args = parser.parse_args();
    if args.d:
        if args.cesar:
            cesar_d(args.plain_text[0], args.key)
        else:
            hill_d(args.plain_text[0], args.key)
    else:
        if args.cesar:
            cesar(args.plain_text[0], args.key)
        else:
            hill(args.plain_text[0], args.key)
