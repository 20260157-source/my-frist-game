import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Particle System")

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

        self.life = random.randint(60, 120)
        self.size = random.randint(3, 6)

        self.hue = random.randint(0, 360)

        self.trail = []

    def update(self):

        self.trail.append((self.x, self.y))
        if len(self.trail) > 8:
            self.trail.pop(0)

        self.x += self.vx
        self.y += self.vy

        self.vy += 0.05
        self.vx *= 0.98
        self.vy *= 0.98

        self.life -= 1
        self.hue += 2

    def get_color(self):

        r = int(127 + 127 * math.sin(self.hue * 0.02))
        g = int(127 + 127 * math.sin(self.hue * 0.02 + 2))
        b = int(127 + 127 * math.sin(self.hue * 0.02 + 4))

        return (r, g, b)

    def draw(self, surf):

        if self.life <= 0:
            return

        color = self.get_color()

        # trail
        for i, pos in enumerate(self.trail):
            pygame.draw.circle(
                surf,
                color,
                (int(pos[0]), int(pos[1])),
                max(1, self.size - i)
            )

        # main particle
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            for _ in range(80):
                particles.append(Particle(mx, my))

    # 잔상 효과
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(40)
    fade.fill((10, 10, 20))
    screen.blit(fade, (0, 0))

    mouse = pygame.mouse.get_pos()

    for _ in range(2):
        particles.append(Particle(mouse[0], mouse[1]))

    for p in particles:
        p.update()
        p.draw(screen)

    particles[:] = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(50)

pygame.quit()