import pygame
import random
import numpy as np


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particles Simulation")

WHITE = (50, 50, 50)
RED = (255,0,0)
GREEN = (0,255,0)
FPS = 60

radius = 10
velocity = 1


class Agent:
    def __init__(self, id, pos, color, vel) -> None:
        self.id = id
        self.pos = pos
        self.color = color
        self.vel = vel


def start(n_particles):
    WIN.fill(WHITE)

    particles = []
    positions = []

    for i in range(n_particles):
        # compute non overlaping position        
        while(True):
            posX = random.random() * (WIDTH-2*radius) + radius
            posY = random.random() * (HEIGHT-2*radius) + radius
            conditions = []
            for j in positions:
                conditions.append((j[0]-posX)*(j[0]-posX) + (j[1]-posY)*(j[1]-posY) < 4*radius*radius)
            if not any(conditions):
                break
        
        # random velocity vector
        angle = random.random() * 2 * np.pi
        vel = np.array(velocity * np.cos(angle), velocity * np.sin(angle))

        # random color
        color = random.choice([RED, GREEN])

        particles.append(Agent(i, pos=np.array((posX, posY)), color=color, vel=vel))
        pygame.draw.circle(WIN, color, (posX, posY), radius)
        positions.append((posX, posY))
    pygame.display.update()
    
    return particles


def update(particles):
    WIN.fill(WHITE)
    for particle in particles:
        particle.pos += particle.vel

        pygame.draw.circle(WIN, particle.color, particle.pos, radius)
        pygame.display.update()


def run(): 
    n_particles = 10
    
    particles = start(n_particles)
    
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        update(particles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
    pygame.quit()


if __name__ == "__main__":
    run()