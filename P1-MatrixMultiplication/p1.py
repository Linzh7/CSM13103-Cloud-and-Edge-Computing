import numpy as np
from memory_profiler import profile
import time


# get matirx with size 1e6 * 1e3
def get_A():
    return np.random.rand(int(1e6), int(1e3))


# get matirx with size 1e3 * 1e6
def get_B():
    return np.random.rand(int(1e3), int(1e6))


# get matirx with size 1e6 * 1
def get_C():
    return np.random.rand(int(1e6), 1)


# use this function if your computer has enough memory (large than 16GB RAM, maybe 32GB)
# @profile
# def compute():
#     # step 1
#     A = get_A()
#     B = get_B()
#     C = get_C()
#     # step 2
#     BC = np.dot(B, C)
#     # step 3
#     return np.dot(A, BC)


# otherwise, use this function
@profile
def compute():
    # step 1, compute B*C first
    BC = np.dot(get_B(), get_C())
    # step 2, compute A * (B * C)
    return np.dot(get_A(), BC)


def compute2():
    # step 1, compute B*C first
    BC = np.dot(get_B(), get_C())
    # step 2, compute A * (B * C)
    return np.dot(get_A(), BC)


# let's go
t1 = time.time()
# ABC = compute()
ABC = compute2()
print(f'Time: {time.time() - t1} seconds')