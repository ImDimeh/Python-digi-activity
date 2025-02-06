import pygame
from PIL import Image
running = True
x_player_1 = 0
y_player_1 = 220
blue = (0, 255, 255)
yellow = (239, 255, 0)
green = (0, 255, 68)
purple = (247, 0, 255)


score = 0

pygame.init()
my_font = pygame.font.SysFont('Small Caps', 30)
# keys = pygame.key.get_pressed()
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

# diviser_gif_en_images("Static.gif")
# diviser_gif_en_images("attack.gif")
# diviser_gif_en_images("Run.gif")


class pièce:
    def __init__(self, pièce_x, pièce_y, rayon, color, condition):
        self.pièce_x = pièce_x
        self.pièce_y = pièce_y
        self.rayon = rayon
        self.color = color
        self.condition = condition
    def draw_pièce_circle(self):
        if self.condition == True:
            pygame.draw.circle(screen, self.color, (self.pièce_x, self.pièce_y), self.rayon)
        
pièce_1 = pièce(100, 250, 15, blue, True)
pièce_2 = pièce(300, 170, 15, yellow, True)
pieces = [pièce_1, pièce_2]

class player:
    def __init__(self, x, y, speed, health, attack_damage, pseudo):
        self.x = x
        self.y = y
        self.saute = False
        self.compteur_saut = 10
        self.speed = speed
        self.health = health
        self.attack_damage = attack_damage
        self.pseudo = pseudo
        self.static = diviser_gif_en_images('Static.gif')
        self.run_right = diviser_gif_en_images('Run.gif')
        self.attack = diviser_gif_en_images('attack.gif')
        self.run_left = [pygame.transform.flip(
            frame, True, False) for frame in self.run_right]
        self.images = self.static
        self.image_index = 0
        self.img = self.images[self.image_index]

    def get_player_x(self):
        return self.x
    
    def get_player_y(self):
        return self.y
    
    def get_player_speed(self):
        return self.speed
    
    def get_player_health(self):
        return self.health
    
    def get_player_attack_damage(self):
        return self.attack_damage
    
    def get_player_pseudo(self):
        return self.pseudo

joueur = player(x_player_1, y_player_1, 10, 20, 5, "louis")


screen = pygame.display.set_mode((620,350))
pygame.display.set_caption("Jeu Mario")
clock = pygame.time.Clock()
running = True
Icon = pygame.image.load('mountains.webp')
pygame.display.set_icon(Icon)
dt = 0

keys = pygame.key.get_pressed()

speed = 10



# img = pygame.image.load("Run.gif")

while running:
    pygame.time.delay(60)

    image_size = (620,350)
    fond = pygame.image.load('fond.png')
    img = pygame. transform. scale(fond,image_size)
    screen.blit(img, (0,0))
    # screen.blit(screen, joueur.static)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            runing = False
            pygame.quit()
            quit()

    pygame.draw.rect(screen, "pink", pygame.Rect(0, 0, 125, 40))
    

    
    

    # if not (joueur.saute):
    #     if keys[pygame.K_SPACE]:
    #             joueur.saute = True
    # else:
    #     if joueur.compteur_saut >= -10:
    #         neg = 1
    #         if joueur.compteur_saut < 0:
    #             neg = -1
    #             joueur.y -= (joueur.compteur_saut ** 2) * 0.2 * neg
    #             joueur.compteur_saut -= 1
    #         else:
    #             joueur.saute = False
    #             joueur.compteur_saut = 10

    dt = clock.tick(60)/1000

    #####
    # pièce_1.draw_pièce_circle()
    # pièce_2.draw_pièce_circle()
    ####
    joueur_rect = pygame.Rect(joueur.x + 30, joueur.y + 30, 30, 30)


    for piece in pieces:
        piece_rect = pygame.Rect(piece.pièce_x - piece.rayon, piece.pièce_y - piece.rayon,
                                 piece.rayon * 2, piece.rayon * 2)
        piece.draw_pièce_circle()

        if joueur_rect.colliderect(piece_rect):
            pieces.remove(piece)
            score += 1

    # def get_score():
    #     if score == 0:
    #         return '0'
        

    text_surface = my_font.render(('score : '), False, (0, 0, 0))
    screen.blit(text_surface, (10,5))


    
    font = pygame.font.SysFont("Small Caps", 30)
    afficher = font.render(str(score), 1, (0, 0, 0))
    screen.blit(afficher, (80,7))



    key  = pygame.key.get_pressed()
    

    # if not (joueur.saute):
    #     if key[pygame.K_SPACE]:
    #         joueur.saute = True
    # else:
    #     if joueur.compteur_saut >= -10:
    #         neg = 1
    #     if joueur.compteur_saut < 0:
    #         neg = -1
    #         joueur.y -= (joueur.compteur_saut ** 2) * 0.2 * neg
    #         joueur.compteur_saut -= 1
    #     else:
    #         joueur.saute = False
    #         joueur.compteur_saut = 10
        


    #move to left
    
    if key[pygame.K_LEFT] and joueur.x>0:
        joueur.x -= speed
        # joueur.image_index += 1
        joueur.images = joueur.run_left
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
        print('left')
        
    # move to right
    elif key[pygame.K_RIGHT] and joueur.x<620:
        joueur.x += speed
        joueur.images = joueur.run_right
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
        print('right')

    
    # move to up
    # if key[pygame.K_UP] and joueur.y>0:
    #     joueur.y -= speed
    #     joueur.image_index = 0
    #     print('up')
    # # move to down
    # if key[pygame.K_DOWN] and joueur.y<350:
    #     joueur.y += speed
    #     joueur.image_index = 0
    #     print('down')
    elif key[pygame.K_a]:
        joueur.images = joueur.attack
        joueur.image_index += 1
        if joueur.image_index >= len(joueur.images):
            joueur.image_index = 0
        joueur.img = joueur.images[joueur.image_index]
        print('attack')

    # elif key[pygame.K_SPACE]:
    #     joueur.saute = True


    #     joueur.images = joueur.static
    #     joueur.image_index += 1
    #     if joueur.image_index >= len(joueur.images):
    #         joueur.image_index = 0
    #     joueur.img = joueur.images[joueur.image_index]



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


    screen.blit(joueur.img, (joueur.x, joueur.y))
    # joueur.image_index = 0



    pygame.display.flip()
     

pygame.quit()
    


# player_1 = player(x_player_1, y_player_1, 10, 20, 5, "louis")
    
    
# pygame.init()
# screen = pygame.display.set_mode((620,350))
# pygame.display.set_caption("Jeu Mario")
# clock = pygame.time.Clock()
# running = True
# Icon = pygame.image.load('mountains.webp')
# pygame.display.set_icon(Icon)
# dt = 0

# while runing:

#     pygame.time.delay(60)

#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             runing = False
#             pygame.quit()
#             quit()
    
    
#     pygame.display.flip()
#     dt = clock.tick(60)/1000 

# pygame.quit()

