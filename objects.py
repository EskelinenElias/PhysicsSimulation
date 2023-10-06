import numpy as np
import math 
import random 

G = 6E-7#6.673E-11 # universal gravitational constant [Nm^2/kg^2]

class Objects:
    def __init__(self) -> None: 
        self.x = np.empty(shape = (1, 0))
        self.y = np.empty(shape = (1, 0))
        self.u = np.empty(shape = (1, 0))
        self.v = np.empty(shape = (1, 0))
        self.path_x = np.empty(shape = (0, 0))
        self.path_y = np.empty(shape = (0, 0))
        self.mass = np.empty(shape = (1, 0))
        self.density = np.empty(shape = (1, 0))
        self.volume = np.empty(shape = (1, 0))
        self.radius = np.empty(shape = (1, 0))

        return None
    
    def addObject(self, x: float, y: float, u: float, v: float, \
                  mass: float, density: float) -> None:
        self.x = np.append(self.x, [[x]], 1)
        self.y = np.append(self.y, [[y]], 1)
        self.u = np.append(self.u, [[u]], 1)
        self.v = np.append(self.v, [[v]], 1)
        self.mass = np.append(self.mass, [[mass]], 1)
        self.density = np.append(self.density, [[density]], 1)
        self.volume = np.append(self.volume, [[mass/density]], 1)
        self.radius = np.append(self.radius, [[math.cbrt(3*(mass/density)/4*math.pi)]], 1)
        return None
    
    def generateObjects(self, number: int, xlim: tuple, ylim: tuple, mlim: tuple, dlim: tuple) -> None:
        for _ in range(number):
            x = random.uniform(xlim[0], xlim[1])
            y = random.uniform(ylim[0], ylim[1])
            u = random.gauss(0, 100)
            v = random.gauss(0, 100)
            mass = random.uniform(mlim[0], mlim[1])
            density = random.uniform(dlim[0], dlim[1])
            self.addObject(x, y, u, v, mass, density)
        return None

    def apply_gravity(self) -> None: 
        dx = (self.x - np.transpose(self.x))
        dy = (self.y - np.transpose(self.y))
        distance = np.sqrt(dx**2 + dy**2)
        force = (G * self.mass * np.transpose(self.mass)) / (np.where(distance != 0, distance, 1)) * (distance != 0)
        angle = np.arctan2(dy, dx)
        force_x = np.sum(force * np.cos(angle), axis=1)
        force_y = np.sum(force * np.sin(angle), axis=1)
        self.u += force_x / self.mass
        self.v += force_y / self.mass
        return None
    
    def apply_gravity_and_collisions(self) -> None: 
        dx = (self.x - np.transpose(self.x))
        dy = (self.y - np.transpose(self.y))
        distance = np.sqrt(dx**2 + dy**2)
        collisions = (distance < (self.radius + np.transpose(self.radius))) -np.eye(np.size(self.radius, axis=1))
        force = (G * self.mass * np.transpose(self.mass)) / (np.where(distance != 0, distance, 1)) * (distance > (self.radius + np.transpose(self.radius)))
        angle = np.arctan2(dy, dx)
        force_x = np.sum(force * np.cos(angle), axis=1)
        force_y = np.sum(force * np.sin(angle), axis=1)
        self.u += force_x / self.mass
        self.v += force_y / self.mass

        self.inelastic_collisions(distance, angle)
        
        return None
    
    def inelastic_collisions(self, distance: np.array, angle: np.array) -> None: 
        collisions = (distance < (self.radius + np.transpose(self.radius))) -np.eye(np.size(self.radius, axis=1))
        velocity = np.sqrt(self.u**2 + self.v**2)
        relative_velocity = velocity - np.transpose(velocity)
        impulse = (2*relative_velocity)*np.transpose(self.mass) / (self.mass + np.transpose(self.mass))
        velocity_change = impulse / self.mass * collisions
        velocity_change_x = np.sum(velocity_change * np.cos(angle), axis=1)
        velocity_change_y = np.sum(velocity_change * np.sin(angle), axis=1)
        self.u -= velocity_change_x
        self.v -= velocity_change_y
        return None
    
    def elastic_collisions(self, dx: np.array, dy: np.array, distance: np.array) -> None:
        collisions = (distance < (self.radius + np.transpose(self.radius))) -np.eye(np.size(self.radius, axis=1))
        print(dy)
        print(distance)
       
        normal_x = dx / distance
        normal_y = dy / distance
        return None
    
    def update(self, time: float = 0.01) -> None: 
        if len(self.path_x) == 0: 
            self.path_x = self.x
            self.path_y = self.y
        else: 
            self.path_x = np.append(self.path_x, self.x, 0)
            self.path_y = np.append(self.path_y, self.y, 0)
        if np.size(self.path_x, 0) > 255: 
            self.path_x = np.delete(self.path_x, 0, axis = 0)
            self.path_y = np.delete(self.path_y, 0, axis = 0)
        self.x += self.u * time
        self.y += self.v * time
        self.apply_gravity_and_collisions()
        return None

    def __len__(self) -> int: 
        return np.size(self.x, axis=1)

if __name__ == "__main__": 
    objects = Objects()
    objects.generateObjects(5, (300, 600), (200, 600), (1E3, 1E9), (2E3, 2E4))

    dx = (objects.x - np.transpose(objects.x))
    dy = (objects.y - np.transpose(objects.y))
    distance = np.sqrt(dx**2 + dy**2)
    objects.apply_gravity_and_collisions()
