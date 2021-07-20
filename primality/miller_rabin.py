import time
import sys

def primality_test(n, k=40):
    d = n - 1
    r = 0
    while d%2 == 0:
        r += 1
        d = d >> 1
    #assert n == ((pow(2,r))*d)+1, "Failed in found 'd' and 'r'"

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


#mt.set_seed(27)
size = 1024
prime = False
num_prime = 0
print('-->Start')
progress = 0
start = time.time()
while num_prime % 4 != 3:
    prime = False
    while not prime:
        progress += 1
        sys.stdout.write("Progress: %d  \r" % (progress) )
        sys.stdout.flush()
        num_prime = mt.gen_n_bits(size)
        #num_prime = mt.gen_n_bits(2048)
        num_prime = num_prime | 1
        prime = primality_test(num_prime)

end = time.time()
print(f'\nNumero primo Achado : {num_prime}')
print(f'Tempo -> {end-start}')


prime = False
num_prime = 0
print('-->Start')
progress = 0
start = time.time()
while num_prime%4!=3:
    prime = False
    while not prime:
        progress += 1
        sys.stdout.write("Progress: %d  \r" % (progress) )
        sys.stdout.flush()
        num_prime = mt.gen_n_bits(size)
        #num_prime = mt.gen_n_bits(2048)
        num_prime = num_prime | 1
        prime = primality_test(num_prime)

end = time.time()
print(f'\nNumero primo Achado : {num_prime}')
print(f'Tempo -> {end-start}')