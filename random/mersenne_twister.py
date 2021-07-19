# Implementatiomn of Mersenne Twister 

from .src.utils import (
    _lowest_n_bits,
    _random_int
)

# Coefficients (Ref: -> # https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine)
coefficients = {
    # MT19937
    '32' : dict (
        n = 624,
        m = 397,
        r = 31,
        a = 0x9908b0df,
        u = 11,
        d = 0xffffffff,
        s = 7,
        b = 0x9d2c5680,
        t = 15,
        c = 0xefc60000,
        l = 18,
        f = 1812433253, 
    ),
    # MT19937-64
    '64' : dict(
        n = 312,
        m = 156,
        r = 31,
        a = 0xb5026f5aa96619e9,
        u = 29,
        d = 0x5555555555555555,
        s = 17,
        b = 0x71d67fffeda60000,
        t = 37,
        c = 0xfff7eee000000000,
        l = 43,
        f = 6364136223846793005, 
    )
}

# Constants
random_seed = True # Check if the seed was provide or need to be random
MT = None


#====================
#=    PARAMETERS    =
#====================
# Define parameters of MT 
def _set_mt19937_type(word_size=32, seed=None):
    global MT
    init_mt = False
    if MT:
        init_mt = (MT['seed'] != seed) or ((MT['w'] != word_size) and MT['seed'])

    MT = dict( 
        state = [],
        seed = seed,
        w = word_size,
        index = coefficients[str(word_size)]['n'] + 1,
        # Get the lowers r bits of element
        lower_mask = (1 << coefficients[str(word_size)]['r']) - 1, #Binary number of r 1's
        # Get the upper w-r bits of element
        upper_mask = _lowest_n_bits(
            ~((1 << coefficients[str(word_size)]['r']) - 1),
            word_size
        ),
        **coefficients[str(word_size)]
    )
    # Initialize states if seeded
    if init_mt:
        _init_seed()


# Define MT as 32 bits word
def set_as_mt19937(seed=None):
    _set_mt19937_type(word_size=32, seed=seed)


# Define MT as 64 bits word
def set_as_mt19937_64(seed=None):
    _set_mt19937_type(word_size=64, seed=seed)


#====================
#=       SEED       =
#====================
# Define a random seed
def _random_seed():
    global MT
    seed = _random_int()

    MT['seed'] = seed
    _init_seed()


# Define a fixed seed
def set_seed(seed):
    global MT, random_seed
    random_seed = False
    MT['seed'] = seed
    # Initialize states
    _init_seed()


#====================
#=    Parameters    =
#====================


# Initialize the series X (state) for a seed
def _init_seed():
    global MT

    MT['index'] = MT['n']

    # Reset state of MT and initialize with seed
    MT['state'] = []
    MT['state'].append(MT['seed'])

    # Generate states for MT
    for i in range(1, MT['n']):
        num = MT['f'] * (MT['state'][i-1] ^ (MT['state'][i-1] >> (MT['w']-2))) + i
        # Append in state of MT the lowest w bits
        MT['state'].append(_lowest_n_bits(num, MT['w']))


# Generate the next n values from the series X (state)
def _twist():
    global MT
    for i in range(0, MT['n']):
        # Or bettween current upper bits and next lowers
        x = (MT['state'][i] & MT['upper_mask']) + (MT['state'][(i+1) % MT['n']] & MT['lower_mask'])

        # Multiplication x by A can be represent as
        #       -
        #      |  x >> 1        x[0] = 0 (number is even)
        # xA = 
        #      | (x >> 1) xor a x[0] = 1 (number is odd)
        #       -

        xA = x >> 1

        # CPU is good to make mod 2 (maybe better then convert with bin)
        if (x % 2) != 0: 
            xA = xA ^ MT['a']

        # x(k+m) xor (x*A) = x(k+m) xor xA
        MT['state'][i] = MT['state'][(i + MT['m']) % MT['n']] ^ xA

    MT['index'] = 0


# Extract a tempered value based on state
def extract_number():
    global MT

    # Check if generator was seeded
    assert not(MT['index'] > MT['n']), "Generator was never seeded"

    # Check if need to twist
    if MT['index'] == MT['n']:
        _twist()

    # Tempering transform
    y = MT['state'][MT['index']]
    y = y ^ ((y >> MT['u']) & MT['d'])
    y = y ^ ((y << MT['s']) & MT['b'])
    y = y ^ ((y << MT['t']) & MT['c'])
    y = y ^ (y >> MT['l'])

    MT['index'] += 1
    # Return the lowest w bits 
    return _lowest_n_bits(y, MT['w'])


# Generate a random int
def gen_int():
    global random_seed

    # Get a random seed if seed was not fixed
    if random_seed:
        _random_seed()

    return extract_number()
     

# Generate a random number with bytes size
def gen_n_bits(n_bits):
    global MT, random_seed

    # n_bits need to be gratter then 0
    assert n_bits >= 1, "Number of bits need to be gratter then 0"

    # Convert to MT 64 if n_bits >= 64
    change_mt = False
    mt_implementation = MT['w']
    if (n_bits >= 64) and (MT['w'] != 64):
        set_as_mt19937_64(seed=MT['seed'])
        change_mt = True

    # Get a random seed if seed was not fixed
    if random_seed:
        _random_seed()

    random_number = 0
    # Concatenation in python
    # 10 = 0b1010
    # 10 << 2 = 0b101000
    # 2 = 0b10
    # 10 concat 2 = (10 << 2) | 2 -> 0b101010
    while random_number.bit_length() < n_bits:
        # Get a new number
        number = extract_number()
        # Concatene previus result with new in lower bits
        random_number = (random_number << number.bit_length()) | number

    # Get only the uppers n_bits
    diff_bits = random_number.bit_length() - n_bits
    random_number = random_number >> diff_bits


    # Revert MT to previus implementation if needed
    if change_mt:
        set_as_mt19937(seed=MT['seed'])


    return random_number


def gen_randint(lower=0, upper=None):
    global MT

    upper = upper if upper else ((1 << MT['w']-1) - 1)

    number = gen_int()

    number = (number + lower) % upper

    return number
 

# Initialize MT as 32bits default
set_as_mt19937()

