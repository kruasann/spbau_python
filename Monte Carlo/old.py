import random
import time
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing


class Integral:
    def __init__(self, x1, x2, y1, y2, n):
        self.arguments = None
        self.random_values = None
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.dots_num = n

    def set_arguments(self):
        self.arguments = create_array(self.x1, self.x2, self.dots_num)

    def set_random_values(self):
        self.random_values = create_array(self.y1, self.y2, self.dots_num)

    def calculate(self):
        """p1 = multiprocessing.Process(target=self.set_arguments)
        p2 = multiprocessing.Process(target=self.set_random_values)

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print(self.arguments, self.random_values)  # None None?! """

        self.set_arguments()
        self.set_random_values()
        x_for_plot = np.arange(self.x1, self.x2, 0.01)
        plt.plot(x_for_plot, func(x_for_plot), linewidth=3, color="#191970")
        plt.scatter(self.arguments, self.random_values, s=5, color="#8B008B")
        plt.title("Monte Carlo method", fontsize=20)
        plt.savefig("Plot.jpg")
        # plt.show()  # takes time

        m = 0

        for arg, val in zip(self.arguments, self.random_values):
            if val <= func(arg):
                m += 1

        return (self.x2 - self.x1) * (self.y2 - self.y1) * (m / self.dots_num)


def func(x):
    return np.arccos(2 * x)


def create_array(a, b, n):
    return np.array([random.uniform(a, b) for i in range(n)])


def main():
    a, b = - 1 / 2, 1 / 2
    A, B = 0, np.pi
    integral = Integral(a, b, A, B, 1000000)
    print(f"Integral from {a} to {b} of is {integral.calculate()}")


if __name__ == "__main__":
    time1 = time.time()
    main()
    print(f"Time: {time.time() - time1}")
