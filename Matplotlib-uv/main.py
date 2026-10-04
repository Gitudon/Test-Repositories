import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")

plt.title("Sine and Cosine Waves")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
