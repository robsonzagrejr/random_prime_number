import time

import prng.blum_blum_shub as bbs
import prng.mersenne_twister as mt

# Parameter
seed = 27
bits_sizes = [32, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]


def test_same_pseudo_sequence():
    print("------>Testing same pseudo random sequence<------")
    # BBS
    bbs.set_seed(seed)
    bbs_sequence = [bbs.gen_int() for i in range(0,100)]
    bbs.set_seed(seed)
    bbs_sequence_ = [bbs.gen_int() for i in range(0,100)]

    assert (
        not set([False for e in bbs_sequence if e not in bbs_sequence_]),
        "ERROR(BBS): Seed not working"
    )
    print("(BBS) ok")

    # MT
    mt.set_seed(seed)
    mt_sequence = [mt.gen_int() for i in range(0,100)]
    mt.set_seed(seed)
    mt_sequence_ = [mt.gen_int() for i in range(0,100)]

    assert (
        not set([e for e in mt_sequence if e not in mt_sequence_]) == {},
        "ERROR(MT): Seed not working"
    )
    print("(MT) ok")


# Testing time
def test_bit_size_gen_time():
    print("------>Testing time for bit length<------")
    # Fixing seed
    bbs.set_seed(seed)
    mt.set_seed(seed)

    print("========= BBS =========")
    for bit_size in bits_sizes:
        start = time.time()
        num = bbs.gen_n_bits(bit_size)
        end = time.time()
        print(f"{bit_size} bits: ","{:.4e}s".format(end - start))
    print("=======================")

    print("========= MT =========")
    for bit_size in bits_sizes:
        start = time.time()
        num = mt.gen_n_bits(bit_size)
        end = time.time()
        print(f"{bit_size} bits: ","{:.4e}s".format(end - start))
    print("=======================")


if __name__ == '__main__':
    test_same_pseudo_sequence()
    test_bit_size_gen_time()

