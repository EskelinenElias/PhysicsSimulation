import math
import numpy
G = 6E-6#6.673E-11 # universal gravitational constant [Nm^2/kg^2]

# Define a class for objects
class Object:
    def __init__(self, x, y, mass, color: tuple, u: float = 0, v: float = 0):
        self.x = x
        self.y = y
        self.density = 2E3 # [kg/m^3]
        self.setMass(mass) # [kg]
        self.vel_x = u
        self.vel_y = v
        self.color = color
        self.path = []

    def setMass(self, mass: float) -> None:
        self.mass = mass
        self.volume = self.mass / self.density
        self.radius = math.cbrt(3*self.volume/4*math.pi)
        print(self.radius)
        return None

    def getColor(self) -> tuple: 
        return self.color

    def apply_gravity(self, others: list):
        forces = [] 
        other: Object
        for other in others:
            dx = other.x - self.x
            dy = other.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            force = (G * self.mass * other.mass / (distance ** ((distance != 0) * 2))) * (abs(distance) >= 0)
            angle = math.atan2(dy, dx)
            force_x = force * math.cos(angle)
            force_y = force * math.sin(angle)
            forces.append([force_x, force_y])
        force_x, force_y = numpy.sum(forces, axis = 0)
        self.vel_x += force_x / self.mass
        self.vel_y += force_y / self.mass

    def apply_collisions() -> None: 
        return None
            
    def update(self):
        self.path.append((self.x, self.y))
        if len(self.path) > 255: self.path.pop(0)
        self.x += self.vel_x
        self.y += self.vel_y
