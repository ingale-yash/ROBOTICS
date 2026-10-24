import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4, 400)

hip = 30 * np.sin(2 * np.pi * t / 4)
knee = 45 * np.sin(2 * np.pi * t / 4 + np.pi/2)

plt.plot(t, hip, label="Hip Joint")
plt.plot(t, knee, label="Knee Joint")

plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.title("Quadruped Gait Cycle")
plt.legend()
plt.grid(True)

plt.savefig("gait_graph.png")
plt.show()