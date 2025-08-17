import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(25, 75)
            vec_1 = self.velocity.rotate(rand_angle)
            vec_2 = self.velocity.rotate(-rand_angle)
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radii)
            child_asteroid_1.velocity = vec_1 * 1.2
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radii)
            child_asteroid_2.velocity = vec_2 * 1.2
