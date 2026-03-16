import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultra Fancy Particle Playground")

clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(50, 90)
        self.size = random.randint(3, 6)

        self.hue = random.randint(0, 360)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 0.06
        self.vx *= 0.99
        self.vy *= 0.99

        self.hue += 2
        self.life -= 1

    def get_color(self):
        r = int(127 + 127 * math.sin(self.hue * 0.02))
        g = int(127 + 127 * math.sin(self.hue * 0.02 + 2))
        b = int(127 + 127 * math.sin(self.hue * 0.02 + 4))
        return (r, g, b)

    def draw(self, surf):

        if self.life <= 0:
            return

        color = self.get_color()

        # glow
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


def draw_background(surface, t):
    for y in range(HEIGHT):
        r = int(20 + 20 * math.sin(y * 0.01 + t))
        g = int(30 + 30 * math.sin(y * 0.02 + t))
        b = int(60 + 40 * math.sin(y * 0.01 + t))
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))


running = True
time = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    if buttons[0]:
        for _ in range(12):
            particles.append(Particle(mouse[0], mouse[1]))

    time += 0.02

    draw_background(screen, time)

    for p in particles:
        p.update()
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()