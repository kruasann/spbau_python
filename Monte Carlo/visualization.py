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


def make_x_values(_):
    return random.uniform(- 1 / 2, 1 / 2)


def make_y_values(_):
    return random.uniform(0, np.pi)


def main(n):
    pool = mp.Pool(mp.cpu_count())
    x_values = pool.map(make_x_values, [0] * n)
    y_values = pool.map(make_y_values, [0] * n)
    m = sum(pool.map(check, zip(x_values, y_values)))
    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n), x_values, y_values


if __name__ == '__main__':
    n = [15000, 25000, 35000]
    plt.title("Monte Carlo method", fontsize=20)
    x_for_plot = np.arange(- 1 / 2, 1 / 2, 0.01)
    plt.plot(x_for_plot, func(x_for_plot), linewidth=3, color="#0E5A10")
    for number in n:
        integral, x, y = main(number)
        print(f"Using {number} dots, integral = {integral}")
        plt.scatter(x, y, s=5, color=("#" + hex(number * 12345)[2:8:]))

    plt.savefig("Plot.jpg")
    plt.show()


"""
Example:

Using 15000 dots, integral = 1.5800116652454266
Using 25000 dots, integral = 1.5650157963122913
Using 35000 dots, integral = 1.567834253721512

You can see the plot in Plot.jpg.
"""
