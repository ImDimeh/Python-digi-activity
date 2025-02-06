import pygame 
from PIL import Image

# initialiser le jeu 
pygame.init()


def diviser_gif_en_images(gif_file_path):
    ret = []
    print("hello")
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame.transform.scale(pygame_image, (100, 100)))
    return ret


# creer la fenetre
fenetre = pygame.display.set_mode((620, 350))

# donner un titre a la fenetre
pygame.display.set_caption("Jeu Stage Python")


class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.larg = 64
        self.long = 80
        self.saute = False
        self.compteur_saut = 10
        self.static = diviser_gif_en_images("assets/hero.gif")
        self.run_right = diviser_gif_en_images("assets/Run.gif")
        self.attack = diviser_gif_en_images("assets/attack.gif")
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        
        self.img = self.images[self.image_index]


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.couleur = (255, 255, 0)
        self.rayon = 15

    def get_rect(self):
        return pygame.Rect(self.x - self.rayon, self.y - self.rayon, self.rayon * 2, self.rayon * 2)


# charger l'image de fond
bg = pygame.image.load("assets/bg.png")

# créer une instance de notre joueur
joueur = Joueur(100, 230)
# liste des pièces que le joueur doit récupérer
pieces = [Piece(x=200, y=200), Piece(x=300, y=200)]


def redessiner_fenetre():
    # remplir la fenetre avec une couleur
    fenetre.blit(bg, (0, 0))

    # rectangle du joueur pour la collision
    joueur_rect = pygame.Rect(joueur.x + 30, joueur.y + 30, 30, 30)
    # pygame.draw.rect(fenetre, (255, 0, 0), joueur_rect, 2)

    # afficher les pièces et vérifier les collisions
    for piece in pieces:
        piece_rect = pygame.Rect(piece.x - piece.rayon, piece.y - piece.rayon,
                                 piece.rayon * 2, piece.rayon * 2)
        pygame.draw.circle(fenetre, piece.couleur,
                           (piece.x, piece.y), piece.rayon)

        if joueur_rect.colliderect(piece_rect):
            pieces.remove(piece)

    fenetre.blit(joueur.img, (joueur.x, joueur.y))
   
    pygame.display.update()


while True:
    # ralentir d'affichage de chaque frame
    pygame.time.delay(70)

    # verifier les evenements pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # obtenir les touches appuyees
    keys = pygame.key.get_pressed()

    print(keys[pygame.K_RIGHT])
    # vérification des touches, déplacement du joueur et animations
    if keys[pygame.K_LEFT] and joueur.x > 0:
        joueur.images = joueur.run_left
        joueur.x -= 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    elif keys[pygame.K_RIGHT] and joueur.x < 600 - 100:
        joueur.images = joueur.run_right
        joueur.x += 10
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]

    elif keys[pygame.K_f]:
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

    # code pour le saut du joueur
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

    redessiner_fenetre()
