import numpy as np
import matplotlib.pyplot as plt

dataY = [
    0.003389,
    0.002863,
    0.002956,
    0.003032,
    0.003076,
    0.003123,
    0.003170,
    0.003205,
    0.003248,
    0.003289,
    0.003322,
]
dataX = [
    0,
    -2.399,
    -1.9075,
    -1.609,
    -1.379,
    -1.186,
    -1.006,
    -0.780,
    -0.616,
    -0.464,
    -0.367,
]

yAxis = np.array(dataY)
xAxis = np.array(dataX)

A = np.vstack([xAxis, np.ones(len(xAxis))]).T

m, c = np.linalg.lstsq(A, yAxis, rcond=None)[0]
print(m)
print(c)
pressuraTimesVolume = []
for i in range(len(dataY)):
    thisMath = (dataY[i] + 1) * dataX[i]
    print(f"PRESSAO TOTAL VEZES: {thisMath}")
    pressuraTimesVolume.append(thisMath)

print(np.average(pressuraTimesVolume))
plt.plot(xAxis, yAxis, "o", label="Original data", markersize=10)
plt.plot(xAxis, m * xAxis + c, "r", label="Fitted line")
plt.legend()
plt.show()
