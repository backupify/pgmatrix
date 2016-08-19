## This app demonstartes how easy it is to display information from a RESTful
## API and some other info using the pygame adapter!
## Here we're gonna pull some sw33t data from NewRelic about our awesome app,
## and display it in real time! We've also got some floating text for fun!
##


import math, sys
import pygame as pg
import pygame.camera
import requests
from matrixclient import PGMatrixApp

def get_newrelic():
  params = {'filter[name]': '<App Name>'}
  headers = {'X-Api-Key': '<Api Key>'}
  res = requests.get('https://api.newrelic.com/v2/applications.json', params=params, headers=headers)
  return res.json()['applications'][0]

class DemoRest(PGMatrixApp):
  def setup(self):
    self.background = pg.transform.scale(pg.image.load('bliss.jpg'), (self.width, self.height))
    self.ticks = 0;
    self.newrelic = get_newrelic()

  def logic_loop(self):
    if self.ticks % 200 == 0:
      self.newrelic = get_newrelic()
    self.ticks += 1

  def graphics_loop(self):
    font = pg.font.SysFont("Comic Sans MS", 16)
    fps = font.render(str(int(self.clock.get_fps())) + ' fps', 1, pg.Color(b'orange'))
    response_time = font.render(str(self.newrelic['application_summary']['response_time']) + ' ms', 1, pg.Color(b'green'))
    rpm = font.render(str(self.newrelic['application_summary']['throughput']) + ' rpm', 1, pg.Color(b'purple'))

    self.screen.blit(self.background, (0, 0))
    self.screen.blit(fps, (0, 50))
    self.screen.blit(response_time, (self.width / 4, 0))
    self.screen.blit(rpm, (self.width / 4, self.height / 2))

def main():

  DemoRest().run()

if __name__ == '__main__':
  main()
