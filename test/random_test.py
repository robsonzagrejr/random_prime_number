#ref -> https://www.geeksforgeeks.org/runs-test-of-randomness-in-python/
import math
import statistics
import numpy as np


def runsTest(l):
    l_median= statistics.median(numbers)

    runs, n1, n2 = 0, 0, 0

    # Checking for start of new run
    for i in range(len(l)):

        # no. of runs
        if (l[i] >= l_median and l[i-1] < l_median) or \
                (l[i] < l_median and l[i-1] >= l_median):
            runs += 1

        # no. of positive values
        if(l[i]) >= l_median:
            n1 += 1

        # no. of negative values
        else:
            n2 += 1

    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
                       (((n1+n2)**2)*(n1+n2-1)))

    z = (runs-runs_exp)/stan_dev

  
    Z = abs(z)
    # Z critical is Zcritical =1.96 for confidence level of 95%)
    print('Z-statistic= ', Z)

    return z

