#!/usr/bin/env - python3

import matplotlib.pyplot as plt

def plot(table):
    x = []
    y = []
    for i in table:
        ix, iy, _, _, _ = i
        x.append(ix)
        y.append(iy)
    plt.plot(x, y, 'ro')
    # plt.scatter(x, y)
    plt.axis([0, 14, 0, 70])
    plt.show()