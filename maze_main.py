import sys
import pygame

import random

pygame.init()
W,H = 1010,610
SIZ = 50
R,C = H//SIZ,W//SIZ
sett = set()

black = (0,0,0)
blue = (0,0,255)
dul_blue = (0,0,100)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

screen = pygame.display.set_mode((W,H),pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("MAZE")

    
running = True

class Cell:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.visited = False
    self.walls = {
      'top': True,
      'right': True,
      'bottom': True,
      'left': True
    }
    
  def draw(self):
    x,y = self.x*SIZ,self.y*SIZ
    if self in sett:
      pygame.draw.rect(screen,blue,(x,y,SIZ,SIZ))
    elif self.visited:
      pygame.draw.rect(screen,white,(x,y,SIZ,SIZ))
    if self.walls['top']:
      pygame.draw.line(screen,black,(x,y),(x+SIZ,y),2)
    if self.walls['right']:
      pygame.draw.line(screen,black,(x+SIZ,y),(x+SIZ,y+SIZ),2)
    if self.walls['bottom']:
      pygame.draw.line(screen,black,(x+SIZ,y+SIZ),(x,y+SIZ),2)
    if self.walls['left']:
      pygame.draw.line(screen,black,(x,y+SIZ),(x,y),2)
      
  def cicksel(self,x,y):
    findcel = lambda x,y : x+y*C
    if x<0 or x>C-1 or y<0 or y>R-1:
      return False
    return grid_cells[findcel(x,y)]
    
  def cickneigh(self):
    neigh = []
    dirr = [
      (0,-1,'top','bottom'),
      (1,0,'right','left'),
      (0,1,'bottom','top'),
      (-1,0,'left','right')
    ]
    for dx,dy,wall,wallnee in dirr:
      nextcell = self.cicksel(self.x+dx,self.y+dy)
      if nextcell and not nextcell.visited:
        neigh.append((nextcell,wall,wallnee))
    return neigh

    
    
    
    
grid_cells = [Cell(c,r) for r in range(R) for c in range(C)]
currsel = random.choice(grid_cells)
currsel.visited = True
sett.add(currsel)
str,en = random.choice(grid_cells),random.choice(grid_cells)

while running:    
  
  screen.fill(dul_blue)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
      
  [cells.draw() for cells in grid_cells]
  
  if sett:

    currsel = random.choice(list(sett))
    nebour = currsel.cickneigh()
    
    if nebour:
      next,wallcur,wallnee = random.choice(nebour)
      next.visited = True
      currsel.walls[wallcur] = False
      next.walls[wallnee] = False
      sett.add(next)
    else:
      sett.remove(currsel)
  else:
    pygame.draw.rect(screen,red,(str.x*SIZ,str.y*SIZ,SIZ,SIZ))
    pygame.draw.rect(screen,green,(en.x*SIZ,en.y*SIZ,SIZ,SIZ))
    
    
  pygame.display.flip()

pygame.quit()
  