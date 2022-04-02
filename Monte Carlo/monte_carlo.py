import random
import time
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt


def func(x):
    return np.arccos(2 * x)


def check(coordinates):
    x, y = coordinates
    if y <= func(x):
        return 1
    return 0


def make_dot():
    return random.uniform(- 1 / 2, 1 / 2), random.uniform(0, np.pi)


def main(n):
    dots = [(random.uniform(- 1 / 2, 1 / 2), random.uniform(0, np.pi)) for i in range(n)]
    m = 0
    for pair in dots:
        m += check(pair)
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


def main_mp(n):
    pool = mp.Pool(mp.cpu_count())
    dots = pool.map(make_dot, [] * n)
    m = sum(pool.map(check, dots))
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


if __name__ == '__main__':
    number_of_dots = int(input("Number of dots: "))

    time1 = time.time()
    main(number_of_dots)
    print("Without multiprocessing:", time.time() - time1)

    time2 = time.time()
    main_mp(number_of_dots)
    print("Using multiprocessing: ", time.time() - time2)
    
    
"""Example:
Number of dots: 10000000
Without multiprocessing: 13.26905632019043
Using multiprocessing:  0.056154727935791016
"""
