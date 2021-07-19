import time
import sys
import random.mersenne_twister as mt
mt.set_as_mt19937_64()

"""
Input #1: n > 3, an odd integer to be tested for primality
Input #2: k, the number of rounds of testing to perform
Output: “composite” if n is found to be composite, “probably prime” otherwise

write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
WitnessLoop: repeat k times:
    pick a random integer a in the range [2, n − 2]
    x ← ad mod n
    if x = 1 or x = n − 1 then
        continue WitnessLoop
    repeat r − 1 times:
        x ← x2 mod n
        if x = n − 1 then
            continue WitnessLoop
    return “composite”
return “probably prime”
"""

def primality_test(n, k=40):
    d = n - 1
    r = 0
    while d%2 == 0:
        r += 1
        d = d >> 1
    assert n == ((pow(2,r))*d)+1, "Failed in found 'd' and 'r'"

    for ik in range(0, k):
        a = mt.gen_randint(2, n-2) #random in range [2, n-2]
        x = pow(a,d,n)
        if (x == 1) or (x == n-1):
            continue 

        base_prime = False
        for ir in range(0, r-1):
            x = pow(x,2,n) #(x**2) % n
            if (x == n-1):
                base_prime = True
                break

        if not base_prime:
            return False

    return True


prime = False
num_prime = None
print('-->Start')
progress = 0
start = time.time()
while not prime:
    progress += 1
    sys.stdout.write("Progress: %d  \r" % (progress) )
    sys.stdout.flush()
    num_prime = mt.gen_n_bits(4096)
    num_prime = num_prime | 1
    prime = primality_test(num_prime)

end = time.time()
print(f'\nNumero primo Achado : {num_prime}')
print(f'Tempo -> {end-start}')
