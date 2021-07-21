# Random Prime Number
Implementation of pseudo random generator and prime number validator

# Run

This code was develop thinking in modules that can be used in
others projects.
With that in mind, is recommend to create a file in root dir and import the
modules to use in a more especific way.

Tests was created and can be found in `test`, execute then in root dir with
`python test/test_primality.py` or `python test/test_prng.py`.
They can be used as example for create especific tests or to understand how to
use the modules.

Obs: `test_primality` will run for ~= 9 min, to run in a few seconds, please
remove the 4096 bits test in MR-MT


# References

https://en.wikipedia.org/wiki/Mersenne_Twister#Alternatives
https://cran.r-project.org/web/packages/randtoolbox/vignettes/fullpres.pdf
https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine
https://arxiv.org/pdf/2007.11839.pdf
https://gmplib.org/manual/Random-Number-Algorithms
http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/MT2002/CODES/mt19937ar.c

http://www.iro.umontreal.ca/~panneton/WELLRNG.html
http://www.iro.umontreal.ca/~lecuyer/myftp/papers/lfsr04.pdf

https://github.com/ruby/ruby/blob/master/random.c#L1219
https://github.com/ruby/ruby/blob/master/missing/mt19937.c

https://www.unix.com/man-page/posix/4/urandom/

https://www.geeksforgeeks.org/runs-test-of-randomness-in-python/

https://www.researchgate.net/publication/221354947_Comparison_of_Two_Pseudo-Random_Number_Generators
