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

    plt.title("Monte Carlo method", fontsize=20)
    x_for_plot = np.arange(- 1 / 2, 1 / 2, 0.01)
    plt.plot(x_for_plot, func(x_for_plot), linewidth=3, color="#191970")
    plt.scatter(x_values, y_values, s=5, color="#8B008B")
    plt.savefig("Plot.jpg")
    plt.show()

    return (1 / 2 - (- 1 / 2)) * (np.pi - 0) * (m / n)


if __name__ == '__main__':
    number_of_dots = int(input("Number of dots: "))
    integral = main(number_of_dots)
    print("Integral =", integral)
