# Implementation of Blum Blum Shub
# Copyright (c) 2021 Robson Zagre Júnior

import prng.blum_blum_shub as bbs

def is_prob_prime(n, k=40):
    # Simple Detecion of first primes
    if n in [1,2,3]:
        return True

    # Define 'd' and 'r' for n = 2(**r)*d + 1
    d = n - 1
    r = 0
    while d%2 == 0:
        r += 1
        d = d >> 1

    # Simple check, disable for beter performace
    #assert n == ((pow(2,r))*d)+1 

    # For k interations:
    for _ in range(0, k):
        # Pick a random integer in range [2, n-2]
        a = bbs.gen_randint(2, n-1)

        # Get value for Fermat's little theorem
        x = pow(a,d,n)

        # 'n' is a strong probable prime?
        if (x == 1) or (x == n-1):
            # Continue loop because 'a' can be a strong lier
            continue 

        # Continue checking for nexts pows
        a_can_be_valid = True
        for _ in range(0, r):
            # Get next mod(n) for x
            x = pow(x,2,n)

            # Checking if 'a' still valid
            if (x == n-1):
                a_can_be_valid = False
                break

        # If fails, then previous 'a's are strong liers
        if a_can_be_valid:
            return False

    return True


