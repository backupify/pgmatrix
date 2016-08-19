## In this demo, we're cookin' up some 'my first dvd player' style bouncing text!
## specify the text then background as the fourth and fifth command line args!
##
##

import math, sys
import pygame as pg
import pygame.camera
import requests
from matrixclient import PGMatrixApp

class DemoText(PGMatrixApp):
  def setup(self):
    self.background = pg.transform.scale(pg.image.load(sys.argv[5]), (self.width, self.height))
    self.text = sys.argv[4]
    self.x = 10.0
    self.y = 10.0
    self.t = 0.0
    self.vx = 1.0
    self.vy = 1.0
    self.vt = 1.0
    self.ticks = 0;

  def logic_loop(self):
    self.t += self.vt
    if (abs(self.t) > 30):
      self.vt *= -1.0;

    self.x += self.vx
    if self.x < 0 or self.x > self.width - 10:
      self.vx *= -1
   
    self.y += self.vy
    if self.y < 0 or self.y > self.height - 10:
      self.vy *= -1

  def graphics_loop(self):
    font = pg.font.SysFont("Comic Sans MS", 16)
    fps = font.render(str(int(self.clock.get_fps())) + ' fps', 1, pg.Color(b'orange'))
    label = font.render(self.text, 1, pg.Color(b'red'))
    label = pg.transform.rotate(label, self.t)
    label = pg.transform.rotate(label, self.t)

    self.screen.blit(self.background, (0, 0))
    self.screen.blit(label, (self.x, self.y))
    self.screen.blit(fps, (0, 50))

if __name__ == '__main__':
  DemoText().run()
