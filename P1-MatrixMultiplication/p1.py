import random
import numpy as np
from memory_profiler import profile
import matplotlib.pyplot as plt


def get_A():
    return np.random.rand(int(1e6), int(1e3))


def get_B():
    return np.random.rand(int(1e3), int(1e6))


def get_C():
    return np.random.rand(int(1e6), 1)


# record memory usage
@profile
def compute():
    # step 1
    BC = np.dot(get_B(), get_C())
    # step 2
    return np.dot(get_A(), BC)


ABC = compute()
