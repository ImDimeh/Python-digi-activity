import pygame
from PIL import Image

pygame.init()

from pygame.locals import QUIT

def diviser_gif_en_images(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        ret.append(pygame.transform.scale(pygame_image, (100, 100)))
    return ret

# setup pygame
pygame.display.set_caption('Video Game')
screen = pygame.display.set_mode((620,350))
clock = pygame.time.Clock()
dt = 0

running = True

# créer un class
class pièce:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'yellow'
        self.rayon = 10

    def draw (self):
        if pièce.draw:
            pygame.draw.circle(screen, (self.color), (self.x, self.y), (self.rayon))

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.larg = 64
        self.long = 80
        self.saute = False
        self.compteur_saut = 10
        self.static = diviser_gif_en_images('Gif_Pygame/attente.gif')
        self.static_left = [pygame.transform.flip(
            frame, True, False) for frame in self.static]
        self.run_right = diviser_gif_en_images('Gif_Pygame/course.gif')
        self.attack = diviser_gif_en_images('Gif_Pygame/attack.gif')
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        self.img = self.images[self.image_index]

joueur = player(100,230)

while running:

    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mettre un png en fond écran
    bg = pygame.image.load('Gif_Pygame/Background.png')
    img = pygame.transform.scale(bg, (620,350))
    screen.blit(img, (0,0))
    
    key  = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and joueur.x < 600:
        joueur.images = joueur.run_left
        joueur.x -= 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
    elif key[pygame.K_RIGHT] and joueur.x < 600 - 100:
        joueur.images = joueur.run_right
        joueur.x += 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
    elif key[pygame.K_r] and joueur.x < 600 - 100:
        joueur.images = joueur.attack
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
    else:
        joueur.images = joueur.static
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    if not (joueur.saute):
        if key[pygame.K_SPACE]:
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

    pieces = [pièce(100, 200), pièce(275, 200), pièce(500, 200)]

    joueur_rect = pygame.Rect(joueur.x + 30, joueur.y + 30, 30, 30)

    for piece in pieces:
        piece_rect = pygame.Rect(piece.x - piece.rayon, piece.y - piece.rayon,
                                 piece.rayon * 2, piece.rayon * 2)
        pygame.draw.circle(screen, piece.color,
                           (piece.x, piece.y), piece.rayon)
        
        if joueur_rect.colliderect(piece_rect):
            print(piece.x)
            pieces.remove(piece)
            print("HI")

    dt = clock.tick(60) / 1000

    screen.blit(joueur.img, (joueur.x, joueur.y))

    pygame.display.flip()