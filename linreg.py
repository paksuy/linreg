#!/usr/bin/env - python3

import math

def gendata():
    data = [
        (35,  8),
        (49,  9),
        (27,  7),
        (33,  6),
        (60, 13),
        (21,  7),
        (45, 11),
        (51, 12)
    ]

    return data

def table(data):
    output = []
    sumX = 0
    sumY = 0
    sumXY = 0
    sumX2 = 0
    sumY2 = 0
    for i in data:
        x, y = i
        sumX += x
        sumY += y

        xy = x * y
        sumXY += xy

        x2 = x * x
        sumX2 += x2

        y2 = y * y
        sumY2 += y2

        output.append((x, y, xy, x2, y2))

    return output, sumX, sumY, sumXY, sumX2, sumY2

def correlate(table, sumX, sumY, sumXY, sumX2, sumY2):
    numdata = len(table)
    upper = (numdata * sumXY) - (sumX * sumY)
    lowerleft = (numdata * sumX2) - (sumX * sumX)
    lowerright = (numdata * sumY2) - (sumY * sumY)
    lower = math.sqrt(lowerleft * lowerright)
    r = upper / lower
    return r