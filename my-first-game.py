import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beautiful Particle System")

clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self, x, y):

        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 8)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(60, 120)
        self.size = random.randint(2, 5)

        self.hue = random.randint(0, 360)

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.vy += 0.05
        self.vx *= 0.98
        self.vy *= 0.98

        self.life -= 1
        self.hue += 2

    def color(self):

        r = int(127 + 127 * math.sin(self.hue * 0.02))
        g = int(127 + 127 * math.sin(self.hue * 0.02 + 2))
        b = int(127 + 127 * math.sin(self.hue * 0.02 + 4))

        return (r, g, b)

    def draw(self, surf):

        if self.life <= 0:
            return

        color = self.color()

        for i in range(3):
            pygame.draw.circle(
                surf,
                color,
                (int(self.x), int(self.y)),
                self.size + i,
                1
            )

        pygame.draw.circle(
            surf,
            color,
            (int(self.x), int(self.y)),
            self.size
        )

    def alive(self):
        return self.life > 0


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    if buttons[0]:
        for _ in range(15):
            particles.append(Particle(mouse[0], mouse[1]))

    screen.fill((10, 10, 20))

    for p in particles:
        p.update()
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()