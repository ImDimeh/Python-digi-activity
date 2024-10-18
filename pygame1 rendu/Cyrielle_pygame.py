import pygame
from PIL import Image
pygame.init()


screen = pygame.display.set_mode((620,350))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




# def tansformer gif en image
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


# class Joueur def
class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.larg = 64
        self.long = 80
        self.saute = False
        self.compteur_saut = 10
        self.static = diviser_gif_en_images('gif/héro_debout.gif')
        self.run_right = diviser_gif_en_images('gif/héro_court.gif')
        self.attack = diviser_gif_en_images('gif/héro_attaque.gif')
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        self.img = self.images[self.image_index]




# class pièce
class piece:
    def __init__(self, x, y, couleur, rayon):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.rayon = rayon
    def draw ():
        if piece.draw:
            pygame.draw.circle(screen, (0,0,255), 10)
piece1 = piece(100, 100, (0,0,255), 10)


# Joueur 1
Joueur1 = Joueur(100, 230)


bg = pygame.image.load('fond_écran/foret.png')

pieces = [piece1(x=200, y=300)]

# boucle while
running = True
while running :
    
    piece1.draw()
    keys = pygame.key.get_pressed()
    print(keys[pygame.K_RIGHT] and Joueur1.x < 600 - 100)
    pygame.time.delay(70)
    img = pygame.transform.scale(bg, (620,350))
    screen.blit(img, (0,0))

# effacer pièce quand collision   
    joueur_rect = pygame.Rect(Joueur1.x+30, Joueur1.y + 30, 30, 30)
    for piece in pieces :
        piece1 = pygame.Rect((piece.x - piece.rayon, piece.y - piece.rayon, piece.rayon * 2, piece.rayon * 2))
        pygame.draw.circle(screen, piece.couleur, (piece.x, piece.y), piece.rayon)
        if joueur_rect.colliderect(piece1) :
            pieces.remove(piece)

    screen.blit(Joueur1.img,(Joueur1.x,Joueur1.y))


    # commande fermer screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    print(not (Joueur1.saute))


    # sauter conditions
    if not (Joueur1.saute):
        if keys[pygame.K_SPACE]:
            Joueur1.saute = True
            Joueur1.images = Joueur1.run_right
            Joueur1.x += 10
            Joueur1.image_index += 1
            if Joueur1.image_index >= len(Joueur1.images):
                Joueur1.image_index = 0
                Joueur1.img = Joueur1.images[Joueur1.image_index]
    
    if keys[pygame.K_RIGHT] and Joueur1.x < 600 - 100:
        print('RIGHT')
        Joueur1.images = Joueur1.run_right
        Joueur1.x += 10
        Joueur1.image_index += 1
        if Joueur1.image_index >= len(Joueur1.images):
            Joueur1.image_index = 0
            Joueur1.img = Joueur1.images[Joueur1.image_index]
            
    else:
        Joueur1.images = Joueur1.run_right
        Joueur1.x += 10
        Joueur1.image_index += 1
        if Joueur1.image_index >= len(Joueur1.images):
            Joueur1.image_index = 0
            Joueur1.img = Joueur1.images[Joueur1.image_index]
        if Joueur1.compteur_saut >= -10:
            neg = 1
            if Joueur1.compteur_saut < 0:
                neg = -1
            Joueur1.y -= (Joueur1.compteur_saut ** 2) * 0.2 * neg
            Joueur1.compteur_saut -= 1
        else:
            Joueur1.saute = False
            Joueur1.compteur_saut = 10
    
    pygame.display.update()
    pygame.display.flip()