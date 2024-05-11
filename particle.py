import time
import math

# I'm assuming 1 meter = 25 pixels
WIDTH = 800
HEIGHT = 800
FPS = 30

# rn 1s, 4.9 m = 20 pixels
# rn 2s, 19.6 m = 60 pixels

# it needs to be 1s, 4.9m = 55 pixels
#it needs to be 2s, 19.6m = 405 pixels

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



def hasBoundaryCollided(p1):
    xbound = (p1.getX() - p1.getR() * 2)
    ybound = (p1.getY() - p1.getR() * 2)
    if(xbound > WIDTH or xbound < 0):
        return True
    
    if(ybound > HEIGHT or ybound < 0):
        return True
    
    return False

def hasCollided(p1, p2):
    if((abs(p1.getX() - p2.getX()) < (p1.getR() * 4)) and 
       (abs(p1.getY() - p2.getY()) < (p1.getR() * 4))):
        return True
    
    return False


class Particle:
    def __init__(self, name, color, mass, x, y, vx, vy, ax, ay, gravity):
        self.name = name
        self.radius = 5
        self.color = color
        self.x = x
        self.y = y


        self.x0 = x
        self.y0 = y

        self.gravity = gravity
        self.t = time.time()
        self.scale = 25
        self.mass = mass

        self.velocity_x = vx
        self.velocity_y = vy

        self.vx0 = vx
        self.vy0 = vy

        self.acceleration_x = ax
        self.acceleration_y = ay

        self.direction = 0
        self.hasCollided = False
        self.t = time.time()
        self.t_offset = 0

        if(self.gravity):
            self.addForce(90, 6, 0)

       
    def getName(self): return self.name
    def getR(self): return self.radius
    def getC(self): return self.color
    def getX(self): return self.x
    def getY(self): return self.y
    def getGravity(self): return self.gravity
    def getT(self): return self.t
    def getVx(self): return self.velocity_x
    def getVy(self): return self.velocity_y
    def getAx(self): return self.acceleration_x
    def getAy(self): return self.acceleration_y
    def getD(self): return self.direction
    def getM(self): return self.mass

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setVx(self, vx):
        self.velocity_x = vx

    def setVy(self, vy):
        self.velocity_y = vy

    def setAx(self, ax):
        self.acceleration_x = ax

    def setAy(self, ay):
        self.acceleration_y = ay

    def move(self, p2):
        # DELTA T
        delta_t = (time.time() - self.t)

        if(hasCollided(self, p2)):
            sx, sy = self.getVx(), self.getVy()
            
            self.setVx(p2.getVx())
            p2.setVx(sx)

            self.setVy(p2.getVy())
            p2.setVy(sy)
            
            self.setX(self.x + (self.getVx() * (time.time() - self.t - self.t_offset)))
            self.setY(self.y + (self.getVy() * (time.time() - self.t - self.t_offset)))

        else:
            # IMPLEMENTING V = V0 + AT
            delta_vx = self.getAx() * delta_t
            delta_vy = self.getAy() * delta_t

            new_vx = delta_vx + self.vx0
            new_vy = delta_vy + self.vy0

            self.setVx(new_vx)
            self.setVy(new_vy)

            # IMPLEMENTING X = V0T + 0.5AT^2
            delta_x = new_vx * delta_t * self.scale
            delta_y = new_vy * delta_t * self.scale

            new_x = delta_x + self.x0
            new_y = delta_y + self.y0
        

            #print(delta_vx, new_vx, self.x0, delta_vy, new_vy, self.y0, v)
            if((new_x + self.getR() * 2) > WIDTH):
                self.addForce(180, 2 * self.getAx(), 2 * self.getVx())
                self.x0 = (WIDTH - self.getR() * 2 + delta_x)

            elif((new_x - self.getR() * 2) < 0):
                self.addForce(0, 2 * self.getAx(), -2 * self.getVx())
                self.x0 = -self.x0
            
            if((new_y + self.getR() * 2) > HEIGHT):
                self.addForce(270, 2 * self.getAy(), 2 * self.getVy())
                self.y0 = (HEIGHT - self.getR() * 2 + delta_y)

            elif((new_y - self.getR() * 2) < 0):
                self.addForce(90, 2 * self.getAy(), -2 * self.getVy())
                self.y0 = -self.y0

            else:
                self.setX(new_x)
                self.setY(new_y)

    
    def addForce(self, direction, acceleration, cVel):
        angle = math.pi * direction / 180
        self.direction += angle

        self.vx0 += cVel * math.cos(angle)
        self.vy0 += cVel * math.sin(angle)

        self.velocity_x += self.vx0
        self.velocity_y += self.vy0

        a_x = acceleration * math.cos(angle)
        a_y = acceleration * math.sin(angle)

        self.setAx(self.acceleration_x + a_x)
        self.setAy(self.acceleration_y + a_y)
    

    def printReport(self):
        print("X: %.0f," % self.getX(), end=" ")
        print("Y: %.0f," % self.getY(), end=" ")
        print("VX: %.0f," % self.getVx(), end=" ")
        print("VY: %.0f," % self.getVy(), end=" ")
        print("AX: %.0f," % self.getAx(), end=" ")
        print("AY: %.0f," % self.getAy(), end=" ")
        print("T: %.2f," % (time.time() - self.t), end="\n")


        