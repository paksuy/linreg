#!/usr/bin/env - python3

import math

def gendata():
    data = [
        ( 8, 35),
        ( 9, 49),
        ( 7, 27),
        ( 6, 33),
        (13, 60),
        ( 7, 21),
        (11, 45),
        (12, 51)
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
    # held high
    numdata = len(table)
    upper = (numdata * sumXY) - (sumX * sumY)
    lowerleft = (numdata * sumX2) - (sumX * sumX)
    lowerright = (numdata * sumY2) - (sumY * sumY)
    lower = math.sqrt(lowerleft * lowerright)
    r = upper / lower
    return r