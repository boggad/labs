#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gmpy2
from random import randint
from gmpy2 import mpz

def gen_DH_pow(x,q,n):
    return gmpy2.powmod(q, x, n)

def gen_DH_key(p,x,n):
    return gmpy2.powmod(p,x,n)

def main():
    Q = mpz(randint(3, 65535))
    Q = gmpy2.next_prime(Q)
    N = mpz(randint(3, 65535))
    N = gmpy2.next_prime(N)
    print('Выберем простые числа Q = {} и N = {}'.format(Q, N))
    X = mpz(randint(100, 65535))
    print('Алиса генерирует случайное число x = ' + X.digits(10))
    Y = mpz(randint(100, 65535))
    print('Боб генерирует случайное число y = ' + Y.digits(10))
    A = gen_DH_pow(X, Q, N)
    print('Алиса вычисляет число A и передает его Бобу')
    print('Атакующий видит число A = ' + A.digits(10))
    B = gen_DH_pow(Y, Q, N)
    print('Боб вычисляет число B и передает его Алисе')
    print('Атакующий видит число B = ' + B.digits(10))
    Ka = gen_DH_key(B, X, N)
    Kb = gen_DH_key(A, Y, N)
    print('Алиса вычисляет секретный ключ K = ' + Ka.digits(10))
    print('Боб вычисляет секретный ключ K = ' + Kb.digits(10))


if __name__ == "__main__":
    main()

