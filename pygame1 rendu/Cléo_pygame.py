import pygame
from PIL import Image
import time

pygame.init()
screen = pygame.display.set_mode((1240,720))
dt=0
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
Keys = pygame.key.get_pressed()

def diviser_gif_en_images(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame.transform.scale(pygame_image, (100, 100)))
    return ret

class joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.larg = 64
        self.long = 80
        self.saute = False
        self.compteur_saut = 10
        self.static = diviser_gif_en_images('héros.gif')
        self.run_right = diviser_gif_en_images('courrir.gif')
        self.attack = diviser_gif_en_images('attaque.gif')
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        
        self.img = self.images[self.image_index]

joueur = joueur(600,550)

class pièce:
    def __init__(self, x, y, couleur, rayon):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.rayon = rayon
    
    def tracer(self):
        pygame.draw.circle(screen,(self.couleur),(self.x, self.y),(self.rayon))
    
              
pièces = [pièce(700,500,(255,255,50),30),pièce(900,600,(255,255,50),30),pièce(550,550,(255,255,50),30)]
  
while running:


    pygame.time.delay(40)

    pygame.display.set_caption("jeux")
    bg = pygame.image.load('fond.png')
    img = pygame.transform.scale(bg, (1240, 720))
    screen.blit(img, (0, 0))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.draw.circle(screen,(100,0,0),player_pos,30)
    # if keys[pygame.K_z] and player_pos.y>=0:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s] and player_pos.y<=720:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_q] and player_pos.x>=0:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d] and player_pos.x<=1240:
    #     player_pos.x += 300 * dt

    if keys[pygame.K_q] and joueur.x >0:
        joueur.images = joueur.run_left
        joueur.x -= 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    elif keys[pygame.K_d] and joueur.x <1150:
        joueur.images = joueur.run_right
        joueur.x += 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    else :
        joueur.images = joueur.static
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    if not (joueur.saute):
        if keys[pygame.K_SPACE]:
            joueur.saute = True
    else:
        if joueur.compteur_saut >= -10:
            neg = 1
            if joueur.compteur_saut < 0:
                neg = -1
            joueur.y -= (joueur.compteur_saut ** 2) * 0.2 * neg
            joueur.compteur_saut -= 1
        else:
            joueur.saute = False
            joueur.compteur_saut = 10

    screen.blit(joueur.img, (joueur.x, joueur.y))
    

    
    joueur_rect= pygame.Rect(joueur.x + 30, joueur.y + 30, 30, 30)

    for pièce in pièces:
        pièce_rect = pygame.Rect(pièce.x - pièce.rayon, pièce.y - pièce.rayon, pièce.rayon * 2, pièce.rayon * 2)
        pygame.draw.circle(screen, pièce.couleur,(pièce.x, pièce.y), pièce.rayon)

    if joueur_rect.colliderect(pièce_rect):
        pièces.remove(pièce)
      
          
    pygame.display.flip()
    
    dt=clock.tick(60)/1000