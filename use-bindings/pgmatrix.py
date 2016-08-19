import os, math
import pygame as pg
from rgbmatrix import RGBMatrix
from rgbmatrix import graphics

class PixelWall:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.matrix = RGBMatrix(32, 6, 1)
    self.matrix.pwmBits = 11
    self.matrix.brightness = 50
    self.matrix.luminanceCorrect = True
    self.bufferCanvas = self.matrix.CreateFrameCanvas()

  def setPixel(self, x, y, r, g, b):
    x = self.width - x -1
    if y > 31:
      x = 191 - x
      y = (y % 32)
    else:
      y = 31 - y
    self.bufferCanvas.SetPixel(x, y, r, g, b)

  def render(self):
    self.bufferCanvas = self.matrix.SwapOnVSync(self.bufferCanvas)

class PGMatrixApp:
  def __init__(self, width, height):
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pg.init()
    pg.display.set_mode((width, height))
    self.width = width
    self.height = height
    self.screen = pg.display.get_surface()
    self.clock = pg.time.Clock();
    self.fps = 60
    self.pixelTarget = PixelWall(self.width, self.height)

  def drawToTarget(self):
    for x in xrange(self.width):
      for y in xrange(self.height):
        color = self.screen.get_at((x, y))
        self.pixelTarget.setPixel(x, y, color.r, color.g, color.b)
    self.pixelTarget.render()

  def setup(self):
    pass

  def logic_loop(self):
    pass

  def graphics_loop(self):
    pass

  def run(self):
    self.setup()
    while True:
      self.logic_loop()
      self.graphics_loop()
      self.drawToTarget()
      self.screen.fill(pg.Color(b'black'))
      self.clock.tick(self.fps)


