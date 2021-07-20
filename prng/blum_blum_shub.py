# Implementation of Blum Blum Shub
# Copyright (c) 2021 Robson Zagre Júnior

from src.utils import (
    _random_int
)

# x(i+1) = x(i)² Mod M
# coprime are values that factorized in primes dont shared a same divisor
# (If p and q are big primes, M = p*q thant factor of M is (p,q)
# If I pick any value that aren't p or q than I can garantee that will be
# coprime with M 
# In that way, I can otimzate the code  by only check if the seed is equal to
# p or q

# p and q need to be big primes, congruent to 3 mod 4. In this case they have 1024 bits
p = 118995821887317325971099391526086147363313437963984482286230103516977708860461167877754644307440941010362194308369768497369946916890410290802824285695355940852617729366542505916010928044077620643706464104679956430074729995160359812399785507384104301448947055908763997105409999191285829916521608075487545940203

q = 120678210362025803537323289443751032492908178827365750592608347465897994772680253786165794375039294812721485369263215767025231011515048011481773632589807333544611478236090401986961311166947142051975398379498445257610727497941339352493883783194575858916344441317358047444202941959964378203098725660173014399143

# x is the x(i-1) value of serie
x = None
M = p*q
random_seed = True # Check if the seed was provide or need to be random


# Validation if seed provide is valid
def check_seed(seed):
    # Improvement of validation because p and q are primes and M = (p*q)
    return ((seed % p) != 0) and ((seed % q) != 0)


# Define a random seed
def _set_random_seed():
    global x

    # Define random seed until is valid
    while True:
        x = _random_int()
        if check_seed(x):
            break


# Define a fixed seed
def set_seed(seed):
    global random_seed, x

    assert check_seed, "Seed most be coprime with M"

    # Disable random seed
    random_seed = False

    # Initialize new serie based in seed
    x = seed


# Generate a random number with bits size
def gen_n_bits(n_bits):
    global random_seed, x, M

    if random_seed:
        _set_random_seed() 

    random_number = 0
    while random_number.bit_length() < n_bits:
        # Generate next value in serie
        x = pow(x,2,M)

        # Join least significant bit of serie with random_number
        random_number <<= 1
        random_number |= (x & 1)

    return random_number


# Generate a ranfom integer with 32 bits
def gen_int(size=32):
    global random_seed, x, M

    if random_seed:
        _set_random_seed() 

    random_number = 0
    # Execute just by size of int (not garantee that number will have size bits)
    for _ in range(0, size):
        # Generate next value in serie
        x = pow(x,2,M)

        # Join least significant bit of serie with random_number
        random_number <<= 1
        random_number |= (x & 1)

    return random_number


# Generate a random number in range
def gen_randint(lower=0, upper=None):

    # Define upper as limited or bigger value allowed
    upper = upper if upper else ((1 << 32) - 1)

    while True:
        # Generate a int32
        number = gen_int()

        # Applying limits
        number = number % upper
        if number >= lower:
            break

    return number
 
