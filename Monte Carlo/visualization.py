import random
import time
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt


def func(x):
    return np.arccos(2 * x)


def make_dot(_):
    return random.uniform(- 1 / 2, 1 / 2), random.uniform(0, np.pi)


def check(coordinates):
    x, y = coordinates
    if y <= func(x):
        return 1
    return 0


def main(n):
    pool = mp.Pool(mp.cpu_count())
    dots = pool.map(make_dot, [0] * n)
    m = sum(pool.map(check, dots))
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


if __name__ == '__main__':
    n = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    integrals = []
    for number in n:
        integral = main(number)
        print(f"Using {number} dots, integral = {integral}")
        integrals.append(integral)
    plt.plot(n, integrals)
    plt.xscale('log')
    plt.savefig("Plot.jpg")
    plt.show()


"""
Example:

Using 100 dots, integral = 1.4451326206513049
Using 500 dots, integral = 1.6901768476313088
Using 1000 dots, integral = 1.595929068023615
Using 5000 dots, integral = 1.5444069485047422
Using 10000 dots, integral = 1.53592464834005
Using 50000 dots, integral = 1.566963583757517
Using 100000 dots, integral = 1.566083937814512
Using 500000 dots, integral = 1.5733221672883828
Using 1000000 dots, integral = 1.569875840147395
Using 5000000 dots, integral = 1.5702911586961992
Using 10000000 dots, integral = 1.570835910862332

You can see the plot in Plot.jpg.
"""
