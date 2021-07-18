import os

def _lowest_n_bits(number, n_bits):
    return number & ((1 << n_bits) - 1)


def _random_int():
    # I can take time as a seed, but in POSIX systems there is a file
    #/dev/urandom that provides a random number based on time, CPU, noise...
    #seems to be a better choice
    seed_bytes = os.urandom(4) # 4 bytes = 32 bits
    seed_int = int.from_bytes(seed_bytes, 'big')

    return seed_int

