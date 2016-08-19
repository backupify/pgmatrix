import os, sys
from subprocess import call
import pygame

def init_pygame_display(width, height):
  os.environ["SDL_VIDEODRIVER"] = "dummy"
  pygame.init()
  pygame.display.set_mode((width, height), 0, 24)
  return pygame.display.get_surface()

def init_pipe():
  pipe_name = "/tmp/pgmatrix"
  if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
  # call(["../matrix-server", sys.argv[1], sys.argv[2], sys.argv[3]])
  return os.open(pipe_name, os.O_WRONLY)

def send_frame(pipe, surface):
  return os.write(pipe, surface.get_view('0').raw)


class PGMatrixApp:
  def __init__(self):
    self.width = int(sys.argv[2]) * 32
    self.height = int(sys.argv[3]) * 32
    self.screen = init_pygame_display(self.width, self.height)
    self.pipe = init_pipe()
    self.clock = pygame.time.Clock();
    self.fps = 60
    
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
      send_frame(self.pipe, self.screen)
      self.screen.fill(pygame.Color(b'black'))
      self.clock.tick(self.fps)
