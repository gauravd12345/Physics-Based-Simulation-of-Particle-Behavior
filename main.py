import random
import pygame
import time
from particle import Particle

# I'm assuming 1 meter = 10 pixels
WIDTH = 800
HEIGHT = 800
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulator")
clock = pygame.time.Clock() 

running = True

x, y = WIDTH / 2, HEIGHT / 2
t = time.time()

pList = []
def createParticle(mass, x, y, vx, vy, ax, ay, gravity):
    p = Particle(len(pList) + 1, WHITE, mass, x, y, vx, vy, ax, ay, gravity)
    return p

def createParticles(number, mass, v_cap, a_cap, gravity):
    particle_list = []
    for _ in range(number):
        rx = random.randint(0, WIDTH)
        ry = random.randint(0, HEIGHT)

        r_vx = random.randint(0, v_cap)
        r_vy = random.randint(0, v_cap)

        r_ax = random.randint(0, a_cap)
        r_ay = random.randint(0, a_cap)

        p = createParticle(mass, rx, ry, r_vx, r_vy, r_ax, r_ay, gravity)
        particle_list.append(p)

    
    return particle_list

blank = createParticle(0, 0, 0, 0, 0, 0, 0, False)
#p1 = createParticle(1, x - 100, y, 0, 0, 0, 0, False)
#p1.addForce(90, 0, 20)

pList = createParticles(1, 1, 20, 0, False)

while running:
    for p in pList:
        p.move(blank)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill(BLACK)

    for p in pList:
        pygame.draw.circle(win, WHITE, (p.getX(), p.getY()), p.getR())
    

    pygame.display.flip() 

    clock.tick(FPS)     

    
pygame.quit()