
# Date;Time;Global_active_power;Global_reactive_power;Voltage;Global_intensity;Sub_metering_1;Sub_metering_2;Sub_metering_3


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

import pandas as pd
df = pd.read_csv("household_power_consumption.txt", sep=";")
df = df[ ['Date','Time','Global_active_power'] ]
print(df)

import matplotlib.pyplot as plt

df = df.tail(24 * 30 * 12) #* LAST 3 MONTH
data = list(df['Global_active_power'].values)

m, n = linreg(range(len(data)),data)  
print(m, n)

trend = [] 
for x in range(len(data)):
    y = m * (x+1) + n
    trend.append(y)


df['trend'] = trend

df['detrend'] = df['Global_active_power'] - df['trend']

plt.plot( list(df['detrend'].values) )
plt.show()

df.to_csv("w10_trend.csv")



