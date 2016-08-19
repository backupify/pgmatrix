## An Image Viewer! Use the display to view an image
## specified as a command line argument. For your health!

import math, sys
import pygame as pg
import pygame.camera
import requests
from matrixclient import PGMatrixApp

class DemoImage(PGMatrixApp):
  def setup(self):
    print self.width
    self.background = pg.transform.scale(pg.image.load(sys.argv[4]), (self.width, self.height))

  def graphics_loop(self):
    self.screen.blit(self.background, (0, 0))


if __name__ == '__main__':
  DemoImage().run()