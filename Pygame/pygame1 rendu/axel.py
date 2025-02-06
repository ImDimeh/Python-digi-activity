import pygame, sys
from PIL import Image
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')
imag = pygame.image.load("Image20230704111133.png")
keys = pygame.key.get_pressed()


def diviser_gif_en_images(gif_file_path):
  ret = []
  gif = Image.open(gif_file_path)
  for frame_index in range(gif.n_frames):
    gif.seek(frame_index)
    frame_rgba = gif.convert("RGBA")
    pygame_image = pygame.image.fromstring(frame_rgba.tobytes(),
                                           frame_rgba.size, frame_rgba.mode)
    ret.append(pygame.transform.scale(pygame_image, (100, 100)))
  return ret

class player:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.saute = False
    self.larg = 64
    self.long = 80
    self.compteur_saut = 10
    self.static = diviser_gif_en_images("Image20230704111020.gif")
    self.run_right = diviser_gif_en_images("Image20230704111127.gif")
    self.attack = diviser_gif_en_images("Image20230704111154.gif")
    self.run_left = [
      pygame.transform.flip(frame, True, False) for frame in self.run_right
    ]
    self.images = self.static
    self.image_index = 0

    self.img = self.images[self.image_index]


joueur = player(0, 200)

class pièce:

  def __init__(self, x, y, rayon, couleur):
    self.x = x
    self.y = y
    self.rayon = rayon
    self.couleur = couleur

  def create(self):
    pygame.draw.circle(DISPLAYSURF, self.couleur, (self.x, self.y), self.rayon)


piece1 = pièce(10, 10, 20, (255, 0, 0))
piece2 = pièce(10, 30, 20, (255, 0, 0))
piece3 = pièce(10, 40, 20, (255, 0, 0))

while True:
  keys = pygame.key.get_pressed()
  pygame.time.delay(70)

  if not (joueur.saute):
    if keys[pygame.K_SPACE]:
      joueur.saute = True
  else:
    if joueur.compteur_saut >= -10:
      neg = 1
      if joueur.compteur_saut < 0:
        neg = -1
      joueur.y -= (joueur.compteur_saut**2) * 0.2 * neg
      joueur.compteur_saut -= 1
else:
      joueur.saute = False
      joueur.compteur_saut = 10
  if keys[pygame.K_RIGHT] and joueur.x < 600 - 100:
    joueur.images = joueur.run_right
    joueur.x += 10
    joueur.image_index += 1
    if joueur.image_index >= len(joueur.images):
      joueur.image_index = 0
    joueur.img = joueur.images[joueur.image_index]

  pieces = [piece1, piece2, piece3]

  for pièce in pieces:
    piece_rect = pygame.Rect(pièce.x - pièce.rayon, pièce.y - pièce.rayon,
                             pièce.rayon * 2, pièce.rayon * 2)
    pièce.create()
    if joueur.colliderect(piece_rect):
      pieces.remove(pièce)
DISPLAYSURF.blit(imag, (0, 0))
  DISPLAYSURF.blit(joueur.img, (joueur.x, joueur.y))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.flip()
  pygame.display.update()