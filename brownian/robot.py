import numpy as np
import random

class brownian:
    def __init__(self, boundary=10, step_size=0.1):
        # define canvas and starting position (middle)
        self.boundary = boundary
        self.x = boundary / 2
        self.y = boundary / 2
        self.dx = step_size
        self.dy  = 0
        self.step_size = step_size
        self.path = [(self.x, self.y)]  #last position

    def move(self):
        new_x = self.x + self.dx
        new_y = self.y + self.dy

        multiplier = 3; # how much the angle changes
        
        # collison
        if not (0 <= new_x <= self.boundary) or not (0 <= new_y <= self.boundary):
            # if collision, then random angle 
            angle = random.uniform(0, 2 * np.pi) *multiplier
            self.dx = self.step_size * np.cos(angle) 
            self.dy = self.step_size * np.sin(angle)
        else:
            #no collision
            self.x = new_x
            self.y = new_y

        self.path.append((self.x, self.y)) 

    def simulate(self, steps=1000):
        for _ in range(steps):
            self.move()

    def get_path(self):
        return zip(*self.path)  # current coordinates for plotting

