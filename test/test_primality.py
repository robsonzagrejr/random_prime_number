import time
import sys
import json

import primality.miller_rabin as mr
import primality.solovay_strassen as ss

import prng.blum_blum_shub as bbs
import prng.mersenne_twister as mt

# Parameter
seed = 27
keys_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]


def test_simple_primality():
    print("------>Testing pseudo primality<------")
    composte_numbers = [4,20,36,21,50]
    prime_numbers = [2,23,31,37,43]

    #MR
    for c in composte_numbers:
        assert not mr.is_prob_prime(c), f"ERROR(MR):Detect {c} composte as prime"
    print("(MR) Composte Detection: ok")

    for p in prime_numbers:
        assert mr.is_prob_prime(p), f"ERROR(MR):Detect {p} prime as composte"
    print("(MR) Prime Detection: ok")


    #SS
    for c in composte_numbers:
        assert not ss.is_prob_prime(c), f"ERROR(SS):Detect {c} composte as prime"
    print("(SS) Composte Detection: ok")

    for p in prime_numbers:
        assert ss.is_prob_prime(p), f"ERROR(SS):Detect {p} prime as composte"
    print("(SS) Prime Detection: ok")


def _gen_key(size, checker, generator):
    prime_number = 4
    aux = 0
    while not checker.is_prob_prime(prime_number):
        sys.stdout.write("Generating: %s \r" % ('.' * (aux%9)))
        sys.stdout.flush()
        aux += 1
        prime_number = generator.gen_n_bits(size) | 1

    return prime_number


# Testing time
def test_key_gen_time():
    print("------>Testing time for a key bit length<------")

    keys = {}
    print("========= MR | BBS =========")
    keys['mr|bbs'] = {}
    bbs.set_seed(23)
    mt.set_as_mt19937_64()
    mt.set_seed(23)

    for key_size in keys_sizes:
        start = time.time()
        num = _gen_key(key_size, mr, bbs)
        end = time.time()
        print(f"\n{key_size} bits: {end - start} s")
        keys['mr|bbs'][key_size] = {'key':num, 'time': end-start}
    print("=======================")

    print("========= MR | MT =========")
    keys['mr|mt'] = {}
    for key_size in keys_sizes:
        start = time.time()
        num = _gen_key(key_size, mr, mt)
        end = time.time()
        print(f"\n{key_size} bits: {end - start} s")
        keys['mr|mt'][key_size] = {'key':num, 'time': end-start}
    print("=======================")
    json.dump(keys, open('test_keys_seed.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

    # Unfurtunatly the test with SS was taken to much time and for some bits
    # was neve end :(

if __name__ == '__main__':
    test_simple_primality()
    test_key_gen_time()

