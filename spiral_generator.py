from math import pi, log
import matplotlib.pyplot as plt
import numpy as np

# Datos base
twin_pairs = [(17, 19), (29, 31), (41, 43)]
fibonacci_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34]

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

for idx, (p1, p2) in enumerate(twin_pairs):
    theta = np.linspace(0, 2*pi*p1, 1000)
    r = np.linspace(log(1), log(fibonacci_seq[-1]), len(theta))
    ax.plot(theta, r, color='#FFD700', alpha=0.7, label=f'Par {p1}-{p2}' if idx == 0 else "")
    ax.scatter(theta[p1%len(theta)], r[p1%len(r)], s=200, c='#FF4D4D', marker='*', zorder=3)
    ax.scatter(theta[p2%len(theta)], r[p2%len(r)], s=200, c='#4DFF4D', marker='*', zorder=3)

ax.annotate("🌀", (pi/2, log(21)), fontsize=30, color='#11B8FF')
ax.set_title("ESPIRAL MARGARET: Primos Gemelos en la Curva de Fibonacci", pad=20)
ax.legend()
plt.tight_layout()
plt.savefig("espiral_margaret.png", dpi=300, transparent=True)
