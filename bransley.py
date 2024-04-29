import numpy as np
import matplotlib.pyplot as plt
import random

p = [[0, 0]]

funs = [
    lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6),
    lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44),
    lambda x, y: (0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6),
    lambda x, y: (0, 0.16 * y)
]
propability = [0.85, 0.07, 0.07, 0.01]

for i in range(0, 1001):
    k = random.choices(funs, propability)[0]
    # print(k(p[i][0],p[i][1]))
    p.append(k(p[i][0], p[i][1]))

p = np.array(p)
plt.scatter(p[:, 0], p[:, 1], s=1)
