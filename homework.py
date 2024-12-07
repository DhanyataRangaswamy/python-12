import pygame 
import random 
pygame.init()
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOUR_CHANGE_EVENT=pygame.USEREVENT+2
PINK=pygame.Color('pink')
LIGHT_BLUE=pygame.Color('lightblue')
DARK_BLUE=pygame.Color('darkblue')
YELLOW=pygame.Color('yellow')
GREEN=pygame.Color('green')
PURPLE=pygame.Color('purple')
WHITE=pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
      super().__init__()
    
      self.image=pygame.Surface([width,height])
      self.image.fill(color)
      self.rect=self.image.get_rect()
      self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    
    def update(self):
       self.rect.move_ip(self.velocity)
       boundary_hit=False

       if self.rect.left <=0 or self.rect.right >=500:
         self.velocity[0]=-self.velocity[0]
         boundary_hit=True
       if self.rect.top <=0 or self.rect.bottom >=400:
         self.velocity[1]=-self.velocity[1]
         boundary_hit=True
       if boundary_hit:
        pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
        pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))

    
    def color_change(self):
      self.image.fill(random.choice([YELLOW,GREEN,PURPLE,WHITE]))
def change_bg_color():
   global bg_color
   bg_color=random.choice([PINK,LIGHT_BLUE,DARK_BLUE])

all_sprites_lists=pygame.sprite.Group()

sp1=Sprite(WHITE,50,30)

sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)

all_sprites_lists.add(sp1)

screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Colourful Bounce")
bg_color=PINK
screen.fill(bg_color)

exit=False
clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
       exit=True

      elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
       sp1.color_change()
      elif event.type==BACKGROUND_COLOUR_CHANGE_EVENT:
       change_bg_color()


    all_sprites_lists.update()
  
    screen.fill(bg_color)

    all_sprites_lists.draw(screen)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()