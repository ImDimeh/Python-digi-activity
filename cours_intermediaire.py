import pygame 
import time


# creer une classe
class Voiture:
    def __init__(self, nom, couleur, puissance, vitesse):
        self.nom = nom
        self.couleur = couleur
        self.puissance = puissance
        self.vitesse = vitesse

    def accelerer(self, vitesse):
        self.vitesse = vitesse
        print("La voiture accélère à " + str(vitesse) + " km/h")
    def marques(self , voiture2):
        
        print(self.nom + " est plus puissante que " + voiture2.nom)

# creer un objet
voiture1 = Voiture("Ferrari", "rouge", 500, 0)
voiture2 = Voiture("Lamborghini", "jaune", 300, 0)
voiture1.accelerer(200)
voiture1.marques(voiture2)


pygame.init()   
# nitialisation de pygame et de la fenêtre de jeu
while True:
    
    # creer la fenetre
    fenetre = pygame.display.set_mode((1020, 850))

    # donner un titre a la fenetre
    pygame.display.set_caption("python intermédiaire")



    # exercice  : Dessiner un cube sur la fenêtre et écrire le code pour déplacer le cube grâce aux
    #évènements pygame et au clavie

    # exercice : Limiter les déplacements du cube à la fenêtre de jeu

    # chargment d'image en python 

    bg = pygame.image.load('assets/bg.png')
    img = pygame.transform.scale(bg, (1020, 850))
    fenetre.blit(img, (0, 0))
    # mise a our de la fenetre de jeu
   
    pygame.display.flip()
   
    #modifier l'arriere plan de la fenetre de jeu

    time.sleep(10)