#!/usr/bin/env - python3

import linreg
import plot

def app():
    data = linreg.gendata()
    print(data)

    table, sumX, sumY, sumXY, sumX2, sumY2 = linreg.table(data)
    print(sumX, sumY, sumXY, sumX2, sumY2)

    r = linreg.correlate(table, sumX, sumY, sumXY, sumX2, sumY2)
    print(r)

    plot.plot(table)

if __name__ == "__main__":
    app()