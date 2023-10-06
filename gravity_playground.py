import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
time_step = 0.01  # Time step for simulation
num_steps = 1000  # Number of simulation steps

# Create objects
mass1 = 1000  # Mass of object 1 (kg)
mass2 = 100  # Mass of object 2 (kg)

# Initial positions and velocities
x1, y1 = 0, 0
x2, y2 = 200, 0
vx1, vy1 = 0, 0
vx2, vy2 = 0, 10

# Lists to store positions
x1_positions = []
y1_positions = []
x2_positions = []
y2_positions = []

# Perform the simulation
for _ in range(num_steps):
    # Calculate distances
    dx = x2 - x1
    dy = y2 - y1
    distance = np.sqrt(dx**2 + dy**2)

    # Calculate gravitational force
    force = G * (mass1 * mass2) / (distance**2)

    # Calculate gravitational acceleration components
    ax1 = (force / mass1) * (dx / distance)
    ay1 = (force / mass1) * (dy / distance)
    ax2 = (force / mass2) * (-dx / distance)
    ay2 = (force / mass2) * (-dy / distance)

    # Update velocities
    vx1 += ax1 * time_step
    vy1 += ay1 * time_step
    vx2 += ax2 * time_step
    vy2 += ay2 * time_step

    # Update positions
    x1 += vx1 * time_step
    y1 += vy1 * time_step
    x2 += vx2 * time_step
    y2 += vy2 * time_step

    # Append positions to lists for plotting
    x1_positions.append(x1)
    y1_positions.append(y1)
    x2_positions.append(x2)
    y2_positions.append(y2)

# Plot the simulation results
plt.figure(figsize=(8, 6))
plt.plot(x1_positions, y1_positions, label='Object 1')
plt.plot(x2_positions, y2_positions, label='Object 2')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Gravity Simulation')
plt.legend()
plt.grid(True)
plt.show()
