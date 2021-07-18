import random.mersenne_twister as mt

if __name__ == '__main__':
    print("====== Merssene Twister Test ======")
    random_int = mt.gen_int()

    mt.set_seed(27)
    print(mt.gen_int())
    print(mt.gen_int())

    mt.set_seed(27)
    print(mt.gen_int())
    print(mt.gen_int())

    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    for size in sizes:
        print(f'===={size} bit size===')
        random_fixed = mt.gen_n_bits(size)    
        print(random_fixed)
        print(f'Size: {random_fixed.bit_length()}')
