import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant

class Planet:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)

def calculate_force(planet1, planet2):
    distance = np.linalg.norm(planet2.position - planet1.position)
    force = (G * planet1.mass * planet2.mass) / distance**2
    direction = (planet2.position - planet1.position) / distance
    return force * direction

def update_position_and_velocity(planets, dt):
    for planet in planets:
        total_force = np.array([0.0, 0.0])
        for other_planet in planets:
            if planet != other_planet:
                total_force += calculate_force(planet, other_planet)
        
        acceleration = total_force / planet.mass
        planet.velocity += acceleration * dt
        planet.position += planet.velocity * dt

def simulate_orbits(planets, num_steps, dt):
    positions = {planet: [] for planet in planets}
    
    for _ in range(num_steps):
        for planet in planets:
            positions[planet].append(planet.position.copy())
        
        update_position_and_velocity(planets, dt)
    
    return positions

def plot_orbits(positions):
    plt.figure(figsize=(8, 8))
    
    for planet, pos_list in positions.items():
        x = [pos[0] for pos in pos_list]
        y = [pos[1] for pos in pos_list]
        plt.plot(x, y, label=str(planet))
    
    plt.title("Orbits of Planets")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    sun = Planet(1.989e30, [0, 0], [0, 0])
    earth = Planet(5.972e24, [1.496e11, 0], [0, 29780])
    mars = Planet(6.417e23, [2.279e11, 0], [0, 24077])
    
    planets = [sun, earth, mars]
    num_steps = 5000
    dt = 3600  # Time step in seconds

    positions = simulate_orbits(planets, num_steps, dt)
    plot_orbits(positions)

if __name__ == "__main__":
    main()
