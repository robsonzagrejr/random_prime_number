# Implementatiomn of Mersenne Twister 
# Coefficients for MT19937-64 (Ref: -> # https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine)
w = 64
n = 312
m = 156
r = 31
a = 0xb5026f5aa96619e9
u = 29
d = 0x5555555555555555
s = 17
b = 0x71d67fffeda60000
t = 37
c = 0xfff7eee000000000
l = 43
f = 6364136223846793005 


def _lowest_n_bits(number, n_bits):
    return number & ((1 << n_bits) - 1)

# Store the State of the generator
MT = []
index = n+1
lower_mask = (1 << r) - 1 #Binary number of r 1's
upper_mask = _lowest_n_bits(~(lower_mask), w) #lowest bits of (not lower_mask)


# Initialize the generator from a seed (5489)
def seed_mt(seed = 5489):
    global index, n, MT, f, w
    index = n
    MT.append(seed)
    for i in range(1,n):
        aux = (f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i) # lowest w bit of
        MT.append(_lowest_n_bits(aux, w))


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index, n, MT, a, s, d, b, t, c
    if index >= n:
        if index > n:
            print("Generator was never seeded")
            return
        twist()
    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)

    index = index + 1
    return _lowest_n_bits(y, w) #lowest w bits of (y)


# Generate the next n values from the series x_i
def twist():
    global index
    for i in range(0, n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i+m) % n] ^ xA
    index = 0

seed_mt(28)
number = extract_number()
print(number)
print(bin(number))
print(len(bin(number)[2:]))
print(bin(number)[2:])
print(extract_number())

