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
        self.static = diviser_gif_en_images('assets/hero.gif')
        self.run_right = diviser_gif_en_images('assets/Run.gif')
        self.attack = diviser_gif_en_images('assets/attack.gif')
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        self.img = self.images[self.image_index]


# Joueur 1
Joueur1 = Joueur(0, 0)


bg = pygame.image.load('assets/bg.png')


running = True
while running :
    pygame.time.delay(70)
    keys = pygame.key.get_pressed()
    img = pygame.transform.scale(bg, (620,350))
    screen.blit(img, (0,0))
    screen.blit(Joueur1.img,(Joueur1.x,Joueur1.y))

    # commande fermer screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(not (Joueur1.saute))


    # sauter
    if not (Joueur1.saute):
        if keys[pygame.K_SPACE]:
            Joueur1.saute = True
            Joueur1.images = Joueur1.run_right
            Joueur1.x += 10
            Joueur1.image_index += 1
            if Joueur1.image_index >= len(Joueur1.images):
                Joueur1.image_index = 0
                Joueur1.img = Joueur1.images[Joueur1.image_index]
    
    elif keys[pygame.K_RIGHT] and Joueur1.x < 600 - 100:
        print('right')
        Joueur1.images = Joueur1.run_right
        Joueur1.x += 10
        print(Joueur1.x)
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