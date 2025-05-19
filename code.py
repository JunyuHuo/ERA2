import matplotlib.pyplot as plt
import numpy as np

# Radar chart example for the seven principles of Ecological Engineering
principles = [
    "Avoidance",
    "Ecological Processes",
    "Renewable Energy",
    "Recycling Efficiency",
    "Low Externalized Costs",
    "Multifunctionality",
    "Mutual Benefit"
]

# Example values for each principle (0 to 1 scale)
values = [0.8, 0.7, 0.9, 0.6, 0.5, 0.7, 0.8]

# Repeat the first value to close the radar chart
values += values[:1]

# Number of variables
num_vars = len(principles)

# Compute angle for each axis in the plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw the outline of the radar chart
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, alpha=0.25)

# Set the principle labels on the axes
ax.set_xticks(angles[:-1])
ax.set_xticklabels(principles, fontsize=10)

# Set the radial limits
ax.set_rlabel_position(30)
ax.set_yticks([0.2, 0.4, 0.6, 0.8])
ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8"], fontsize=8)
ax.set_ylim(0, 1)

# Title
ax.set_title("Radar Chart of Ecological Engineering Principles\n(Based on Schönborn & Junge, 2021)", va='bottom')

plt.tight_layout()
plt.show()
