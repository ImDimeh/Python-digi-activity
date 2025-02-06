import pygame
from PIL import Image

# creer la fenetre
fenetre = pygame.display.set_mode((620, 350))

# donner un titre a la fenetre
pygame.display.set_caption("Jeu Stage Python")

# obtenir les touches appuyees
keys = pygame.key.get_pressed()


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


class Joueur:
    def __init__(self, x, y):
        # position x du joueur
        self.x = x
        # position y du joueur
        self.y = y
        # largeur de l'image du joueur
        self.larg = 64
        # longeur de l'image du joueur
        self.long = 80
        self.saute = False
        self.compteur_saut = 10
        # images du joueur quand il n'est pas en mouvement
        self.static = diviser_gif_en_images("assets/hero.gif")
        # image du joueur quand il cours vers la droite
        self.run_right = diviser_gif_en_images("assets/Run.gif")
        # images du joueur quand il effectue une attaque
        self.attack = diviser_gif_en_images("assets/attack.gif")
        # images du joueur quand il cours vers la gauche
        # pour obtenir les images du joueur qui cours vers la gauche,
        # faire une roration horizontale des images de run_right
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        # images de la position actuelle du joueur
        self.images = self.static
        # index de l'image de la position actuelle du joueur
        self.image_index = 0
        # image actuelle du joueur
        self.img = self.images[self.image_index]
joueur = Joueur(100, 100)


while True:
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
