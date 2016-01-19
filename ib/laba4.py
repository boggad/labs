#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gmpy2
from gmpy2 import mpz

def main():
    from sys import argv
    if len(argv) > 1:
        if argv[1] == '-k':
            gen_keys()
            return
        if argv[1] == '-e':
            print('Введите публичный ключ:')
            pk = input()
            print('Введите N:')
            N = input()
            print('Введите сообщение:')
            message = input()
            cipher = encrypt(pk, N, message)
            print('Зашифрованное сообщение (hex):')
            print(cipher)
        if argv[1] == '-d':
            print('Введите приватный ключ:')
            sk = input()
            print('Введите N:')
            N = input()
            print('Введите шифровку(hex):')
            cipher = input()
            message = decrypt(sk, N, cipher)
            print('Расшифрованное сообщение:')
            print(message)

def mhex(i):
    h = hex(i)[2:]
    if len(h) < 2:
        h = '0' + h
    if len(h) < 4 and len(h) > 2:
        h = '0' + h
    return h

def encrypt(pkey, N, message):
    message = message.encode('utf-8')
    msg_bytes = ''.join([hex(c)[2:] for c in message])
    msg_int = mpz(msg_bytes, 16)
    encrypted = gmpy2.powmod(msg_int, mpz(pkey), mpz(N))
    return encrypted.digits(16)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def decrypt(skey, N, cipher):
    cipher_int = mpz(cipher, 16)
    decrypted = gmpy2.powmod(cipher_int, mpz(skey), mpz(N)).digits(16)
    message = bytearray([int(c, 16) for c in chunks(decrypted,2)])
    return message.decode('utf-8')

def gen_keys():
    rs = gmpy2.random_state(hash(gmpy2.random_state()))
    P = gmpy2.mpz_urandomb(rs, mpz('256'))
    P = gmpy2.next_prime(P)
    Q = gmpy2.mpz_urandomb(rs, mpz('256'))
    Q = gmpy2.next_prime(Q)
    N = P*Q
    Fi = (P-1)*(Q-1)
    Pkey = gmpy2.mpz_random(rs, Fi)
    while not (gmpy2.gcd(Fi, Pkey) == 1):
        Pkey = gmpy2.mpz_random(rs, Fi)
    Skey = gmpy2.invert(Pkey, Fi)
    print('Публичный ключ: ')
    print(Pkey)
    print('Приватный ключ:')
    print(Skey)
    print('N:')
    print(N)

if __name__ == "__main__":
    main()

