import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.font.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.load('nom.ogg')
pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.mp3'),-1)

font = pygame.font.SysFont('Comic Sans MS', 30)

bones = 0
text = 'Score: '

text_surface = font.render(text + str(bones), False, (255, 255, 255))


xscreen = 600
yscreen = 350

win = pygame.display.set_mode((xscreen,yscreen))

pygame.display.set_caption("Bone Doge!")


gameIcon = pygame.image.load('doge.png')
Plr = pygame.image.load('doge.png')
Bone = pygame.image.load('bone.png')
pygame.display.set_icon(gameIcon)
x = xscreen/2 - 40/2 
y = yscreen/2 - 40/2
bx = random.randrange(25,xscreen-25)
by = random.randrange(25,yscreen-25)
width = 40
height = 40
vel = 0.5

run = True

while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y > 0: y -= vel
    if keys[pygame.K_s]  and y < 350 - 40: y += vel
    if keys[pygame.K_a]  and x > 0: x -= vel
    if keys[pygame.K_d]  and x < 600 - 40: x += vel

    if x + 25 > bx and x < bx + 25 and y + 25 > by and y < by + 25:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('nom.ogg'))
        bx = random.randrange(25,xscreen-25)
        by = random.randrange(25,yscreen-25)
        bones += 1
        
    text_surface = font.render(text + str(bones), False, (255, 255, 255))
    win.fill((0,0,0))
    win.blit(Bone, (bx,by))
    win.blit(Plr, (x,y))
    win.blit(text_surface, (250,0))
    pygame.display.update()

pygame.quit()
