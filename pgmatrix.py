import os
import pygame

def init_pygame_display(width, height):
  os.environ["SDL_VIDEODRIVER"] = "dummy"
  pygame.init()
  pygame.display.set_mode((width, height), 0, 24)
  return pygame.display.get_surface()

def init_pipe(name="/tmp/pygamematrix"):
  if not os.path.exists(name):
    os.mkfifo(name)
  return os.open(name, os.O_WRONLY)

def send_frame(pipe, surface):
  return os.write(pipe, surface.get_view('0').raw)

class PyGameMatrixApp:
  def __init__(self, width, height):
    self.screen = init_pygame_display(width, height)
    self.pipe = init_pipe()
    self.width = width
    self.height = height
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
