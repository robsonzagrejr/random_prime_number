# Implementation of Blum Blum Shub
# Copyright (c) 2021 Robson Zagre Júnior

import prng.blum_blum_shub as bbs

# Need to computate the Jacobi Symbol between a and n
#Ref -> https://www.johndcook.com/blog/2019/02/12/computing-jacobi-symbols/
def jacobi(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

def is_prob_prime(n, k=40):
    # Simple Detection of first primes
    if n in [1,2,3]:
        return True

    # Helper for first pow
    pow_e = int((n-1)/2)
     
    for _ in range(0, k):
        # Pick a random integer in range [2, n-1]
        a = bbs.gen_randint(2, n)

        # First verification if n divides a
        x = jacobi(a,n)
        if x == 0:
            return False

        # The elevation of 'a' is congruent to x mod n?
        aux_base_a = pow(a,pow_e,n)

        # 'a' is a relatively prime to n?
        if x == 0 or ((aux_base_a % n) != (x % n)):
            return False
    # All 'a's is relatively prime to n 
    return True

