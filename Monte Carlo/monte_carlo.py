import random
import time
import numpy as np
import multiprocessing as mp


def func(x):
    return np.arccos(2 * x)


def check(coordinates):
    x, y = coordinates
    if y <= func(x):
        return 1
    return 0


def make_dot(_):
    return random.uniform(- 1 / 2, 1 / 2), random.uniform(0, np.pi)


def main(n):
    dots = [(random.uniform(- 1 / 2, 1 / 2), random.uniform(0, np.pi)) for i in range(n)]
    m = 0
    for pair in dots:
        m += check(pair)
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


def main_mp(n):
    pool = mp.Pool(mp.cpu_count())
    dots = pool.map(make_dot, [0] * n)
    m = sum(pool.map(check, dots))
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


if __name__ == '__main__':
    number_of_dots = int(input("Number of dots: "))

    time1 = time.time()
    integral_1 = main(number_of_dots)
    print(f"Without multiprocessing: {time.time() - time1} sec\nIntegral = {integral_1}")

    time2 = time.time()
    integral_2 = main_mp(number_of_dots)
    print(f"Using multiprocessing: {time.time() - time2} sec\nIntegral = {integral_2}")
