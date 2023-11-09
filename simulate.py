import pygame
import random
import numpy as np


WIDTH, HEIGHT = 500, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particles Simulation")


class Configurations:
    width = 700
    height = 500
    gray1 = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    fps = 60
    radius = 5
    velocity = 1
    eff_width = width - radius
    eff_height = height - radius


class Agent:
    def __init__(self, id: int, pos: np.array, vel: np.array, color: tuple, radius: int) -> None:
        self.id = id
        self.pos = pos
        self.vel = vel
        self.color = color
        self.radius = radius

    def collision(self, agent):
        pass


class Simulation:
    def __init__(self, n_agents: int, configs: Configurations = Configurations(), title_display="Multi-Agent-Sim") -> None:
        self.configs = configs
        self.screen = self.init_screen(title_display)
        self.agents = self.init_agents(n_agents)
        self.running = True

    def init_screen(self, title_display):
        screen = pygame.display.set_mode((self.configs.width, self.configs.height))
        screen.fill(self.configs.gray1)
        pygame.display.set_caption(title_display)
        return screen

    def init_agents(self, n_agents) -> None:
        agents = []
        positions = []

        w = self.configs.width
        h = self.configs.height
        r = self.configs.radius

        for i in range(n_agents):
            # compute non overlaping position        
            while(True):
                posX = random.random() * (w - 2 * r) + r
                posY = random.random() * (h - 2 * r) + r
                conditions = []
                for j in positions:
                    conditions.append((j[0] - posX) * (j[0] - posX) + (j[1] - posY) * (j[1] - posY) < 4 * r * r)
                if not any(conditions):
                    break
            
            angle = random.uniform(0, 1) * 2 * np.pi
            vel = np.array((self.configs.velocity * np.cos(angle), self.configs.velocity * np.sin(angle)))

            color = random.choice([self.configs.red, self.configs.green])

            agents.append(Agent(i, pos=np.array((posX, posY)), vel=vel, color=color, radius=r))
            pygame.draw.circle(WIN, color, (posX, posY), r)
            positions.append((posX, posY))

        return agents

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(self.configs.fps)
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
        pygame.quit()

    def update(self):
        self.screen.fill(self.configs.gray1)

        for agent in self.agents:
            new_pos = self.wall_collision(agent)

            agent.pos = new_pos
            pygame.draw.circle(WIN, agent.color, agent.pos, self.configs.radius)

    def wall_collision(self, agent):
        w = self.configs.eff_width
        h = self.configs.eff_height
        r = self.configs.radius

        new_pos = agent.pos + agent.vel
        
        if new_pos[0] > w:
            agent.vel[0] *= -1
            new_pos[0] = w - (new_pos[0] - w)
        if new_pos[0] < r:
            agent.vel[0] *= -1
            new_pos[0] = r - (new_pos[0] - r)

        if new_pos[1] > h:
            agent.vel[1] *= -1
            new_pos[1] = h - (new_pos[1] - h)
        if new_pos[1] < r:
            agent.vel[1] *= -1
            new_pos[1] = r - (new_pos[1] - r)

        return new_pos


def run(): 
    n_agents = 100
    sim = Simulation(n_agents=n_agents)
    sim.run()


if __name__ == "__main__":
    run()