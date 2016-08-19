import math
import pygame as pg
from pgmatrix import PGMatrixApp

class DemoApp(PGMatrixApp):
  def setup(self):
    self.background = pg.transform.scale(pg.image.load('bliss.jpg'), (self.width, self.height))

    self.x = 10.0
    self.y = 10.0
    self.t = 0.0
    self.vx = 1.0
    self.vy = 1.0
    self.vt = 0.05

  def logic_loop(self):
    self.t += self.vt
    if (abs(self.t) > 1):
      self.vt *= -1.0;

    self.x += self.vx
    if self.x < 0 or self.x > self.width - 10:
      self.vx *= -1
   
    self.y += self.vy
    if self.y < 0 or self.y > self.height - 10:
      self.vy *= -1

  def graphics_loop(self):
    font = pg.font.SysFont("Comic Sans MS", 18)
    label = font.render("DATTO", 1, pg.Color(b'red'))
    label = pg.transform.rotate(label, math.cos(self.t))
    self.screen.blit(self.background, (0,0))
    self.screen.blit(label, (self.x, self.y))

def main():
  WIDTH = 96
  HEIGHT = 64
  DemoApp(WIDTH, HEIGHT).run()

if __name__ == '__main__':
  main()
