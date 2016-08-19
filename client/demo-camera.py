## Camera Demo - Use the display as a giant mirror!
## Uses the v4l2 camera driver, allowing the use of
## OOTB pygame.Camera with a raspberry pi camera module.
## Depending on your OS, you may need to install the v4l2 driver.
## before running this script, run `sudo modprobe bcm2835-v4l2`
## For more info, see
## https://github.com/raspberrypi/linux/blob/rpi-3.10.y/Documentation/video4linux/bcm2835-v4l2.txt
## and http://www.pygame.org/docs/ref/camera.html
##

import math, sys
import pygame as pg
import pygame.camera
import requests
from matrixclient import PGMatrixApp

class DemoCamera(PGMatrixApp):
  def setup(self):
    pg.camera.init()
    self.cam = pg.camera.Camera("/dev/video0", (self.width, self.height))
    self.cam.start()
    self.snapshot = pg.surface.Surface((self.width, self.height), 0, self.screen)

  def logic_loop(self):
    if self.cam.query_image():
      self.snapshot = self.cam.get_image(self.snapshot)

  def graphics_loop(self):
    self.screen.blit(self.snapshot, (0,0))

if __name__ == '__main__':
  DemoCamera().run()