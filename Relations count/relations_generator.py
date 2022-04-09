import numpy as np


class RelationsGenerator:
    def __init__(self, domain, codomain):
        self.n = domain
        self.m = codomain
        self.values = np.array([[-1], [-1]])

    def __iter__(self):
        return self

    def __next__(self):
        if self.values[0][0] == [-1]:
            self.values = np.zeros((self.n, self.m), dtype=int)
            return self.values

        for i in range(self.n):
            for j in range(self.m):
                if self.values[i][j] == 0:
                    self.values[i][j] = 1
                    return self.values
                
                self.values[i][j] = 0
                
        raise StopIteration
