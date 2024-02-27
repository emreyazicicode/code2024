
f = "w10_timeseries.csv"
import pandas as pd
df = pd.read_csv(f)
import matplotlib.pyplot as plt


# NOTE, time series data must be unique
# NOTE, time series data must be ordered
# NOTE, time series data must be non-empty
# NOTE, in time series, WE NEED TO focus on LAST YEARS
# NOTE, in time series datasets, there is a "PERIOD", day ( 3 x 365 ), week ( 5 x 52), hour ( 24 x 30), minute ( 60 x 24), month (12 x 10)

df = df.tail(1030 )


def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

data = list(df['nofsales'].values)
m, n = linreg(range(len(data)),data)  
print(m, n)

trend = [] 
for x in range(len(data)):
    y = m * (x+1) + n
    trend.append(y)

plt.plot( data )
plt.plot( trend )

plt.show()
