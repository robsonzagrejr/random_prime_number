from src.utils import (
    _lowest_n_bits,
    _random_int
)

# A Implementation of Blum Blum Shub

# p and q need to be prime,
# coprime are values that factorized in primes dont shared a same divisor
# (If p and q are big primes, M = p*q thant factor of M is (p,q)
# If I pick any value that aren't p or q than I can garantee that will be
# coprime with M 
# In that way, I can otimzate the code  by only check if the seed is equal to
# p or q

# For better results and randomness, 1024 bits primes was choose, biger than
# that can cause problems calculos in python

p = 118995821887317325971099391526086147363313437963984482286230103516977708860461167877754644307440941010362194308369768497369946916890410290802824285695355940852617729366542505916010928044077620643706464104679956430074729995160359812399785507384104301448947055908763997105409999191285829916521608075487545940203

q = 120678210362025803537323289443751032492908178827365750592608347465897994772680253786165794375039294812721485369263215767025231011515048011481773632589807333544611478236090401986961311166947142051975398379498445257610727497941339352493883783194575858916344441317358047444202941959964378203098725660173014399143

x = None
M = p*q
random_seed = True # Check if the seed was provide or need to be random

def check_seed(seed):
    return ((seed % p) == 0) or ((seed % q) == 0)


def set_seed(seed):
    global random_seed, x
    assert check_seed, "Seed most be coprime with M"
    random_seed = False
    x = seed


# Generate a random number woth bits size
def gen_n_bits(n_bits):
    global random_seed, x, M

    if random_seed:
        while True:
            x = _random_int()
            if check_seed(x):
                break

    random_number = 0
    while random_number.bit_length() < n_bits:
        random_number <<= 1
        x = pow(x,2,M)
        random_number |= (x & 1)

    return random_number

