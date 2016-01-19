#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gmpy2
from gmpy2 import mpz
from hashlib import sha256

def main():
    from sys import argv
    if len(argv) > 1:
        gmpy2.get_context().precision = 5000
        if argv[1] == '--sign':
            sign()
        if argv[1] == '--check':
            check()

def sign():
    print('Введите сообщение:')
    message = input()
    H = sha256(message.encode('utf-8')).hexdigest()
    print('hash: '+H)
    pk,sk,n = gen_keys()
    print('Приватный ключ:')
    print(pk)
    S = encrypt_rsa(pk, n, H)
    print('ЭЦП:')
    print(S)
    print('Публичный ключ:')
    print(sk)
    print('N:')
    print(n)

def check():
    print('Введите сообщение:')
    message = input()
    print('Введите ЭЦП:')
    S = input()
    print('Введите публичный ключ:')
    pk = mpz(input())
    print('Введите N:')
    N = mpz(input())
    H = sha256(message.encode('utf-8')).hexdigest()
    H = mpz(H,16)
    Hp = decrypt_rsa(pk, N, S)
    if H == Hp:
        print('Электронная подпись верна!')
    else:
        print('Электронная подпись неверна!')

def encrypt_rsa(pkey, N, message):
    msg_int = mpz(message, 16)
    encrypted = gmpy2.powmod(msg_int, pkey, N)
    return encrypted.digits(16)

def decrypt_rsa(skey, N, cipher):
    decrypted = gmpy2.powmod(mpz(cipher, 16), skey, N)
    return decrypted

def gen_keys():
    rs = gmpy2.random_state(hash(gmpy2.random_state()))
    P = gmpy2.mpz_urandomb(rs, mpz('128'))
    P = gmpy2.next_prime(P)
    Q = gmpy2.mpz_urandomb(rs, mpz('128'))
    Q = gmpy2.next_prime(Q)
    N = P*Q
    Fi = (P-1)*(Q-1)
    Pkey = gmpy2.mpz_random(rs, Fi)
    while not (gmpy2.gcd(Fi, Pkey) == 1):
        Pkey = gmpy2.mpz_random(rs, Fi)
    Skey = gmpy2.invert(Pkey, Fi)
    assert gmpy2.t_mod(Skey*Pkey,Fi) == 1
    return Pkey, Skey, N

if __name__ == "__main__":
    main()

