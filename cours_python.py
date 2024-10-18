# import random





## creer deux variable  afin  de  faire les 5 calcule suivant  avec . 

## addition  +
## soustraction  -
## multiplication  *
## division  / 
## puissance  **

## > <  =   <= >=  != ==





array1 = ["bonjour","coucou"]


variable1 = "prenom"
prenom = "Thibault"

variable1 = "age1"
age1 = 15

moyenne = "age2"
moyenne = 15.1

boolean = "tf"
tf = True


#print("je m'apelle " + prenom + " j'ai  " + str(age1) + " ans et j'ai "  + str(moyenne) + "de moyenne")
















# #print("salue  a tous ")


# # # Variables et les types de données

# ## Nombre entier / Int(eger)
# age = 25

# ## Nombre decimaux / Float(ing point number)
# prix = 12.99

# ## Chaîne de caractères / Str(ing)
# prenom = "Stephane"

# ## Booléens / Booleans
# est_majeur = True


# #print( "bonjour j'ai  " , str(age)  + ' ans je vend ça ' ,  str(prix)  +    " €  " +  prenom  + " et je suis majeur" +  str(est_majeur) )


# ## Listes / Lists
# prenoms = ["Samuel", "Mohammad", "Nathan", "Leandro", "Eva", "Ehssan", "Stephane"]



# # print(f"la 3eme personne de la liste est {prenoms[2]}")



# prenoms.append("test")




# notes = [12,5,19,11,6,3,10]

# prenoms.sort()


# a = [1,1,1]
#print(f"len(a): {len(a)}")

# nombre_de_notes = len(notes)
# print(nombre_de_notes)

# # Opérateurs 

# ## Opérateurs arithmétiques [ + - * / %]
# a = 5
# b = 13
# c = 3
# print(a + b)

# print(a - b)

# print(a * b)

# print(a / b)

# print(a ** b)

# d = a * b / c
# print(d)

# print(125*8)

# print(9%2)

# ## Opérateurs de comparaison [ > >=  <= <  ==    !=   ]


# si a > b
# si a est égale a b print ("a est egal a b")
# si a est égale a b print ("a est égale a b ")


# if a > b :
#     print("a est superieur a b")


# if a >= b:
#     print("a est superieur ou egal a b")
# if a <= b:
#     print("a est inferieur ou egal a b")











# print(f"a est different de b: {a != b}")

# ## Opérateurs de logique [ and or not]
# print(not (a > b or b > c))

# # Conditions 
# if a > b:
#     print("a est superieur b")
# elif a == 5:
#     print("a est egal a 5")
# elif a > 0:
#     print("a est positif")
# else:
#     print("a est inferieur a b")



## JOUR 2

# # Boucles / loops

# ## Boucle for 
# for a in range(5): # [0,1,2,3,4]
#     print(f"Tour de boucle numéro {a+1}")

# for prenom in prenoms: # ['Samuel', 'Mohammad', 'Nathan', 'Leandro', 'Eva', 'Ehssan', 'Stephane', 'Jean']
#     print(f"Salut {prenom}")

## Boucle while
# j = 1
# while j <= 20:
#     print(j)
#     j += 1
    
# messages = ["Salut", "Bonjour", "Coucou", "Yo", "Hey", "Hello"]
# for a in messages:
#     print(a)
# i = 0
# couleur = ["rouge", "bleu", "vert", "rose" ,"noir"]
# while i< 2:
#     print(i)
#     for f in couleur:
#       print(f)
      
#     i += 1
#     print(i)
# i = 0
    
# for i in range(25, 50):
#     print(i)
    
#     if i == 45:
#         break
    


# # Fonctions

# ## Definir la fonction
# def saluer():
#     print("Salut.")

# ## Appeller / Utiliser / Executer
# saluer()

# ## Fonction avec des parametres / arguments
# def saluer_qqun(prenom,nom):
#     print(f"Salut {prenom} {nom}")

# saluer_qqun("Stephane","D")
# saluer_qqun(prenom,"Dupuis")

# ## Fonction qui retourne / renvoie une valeur
# def retourner_salutations():
#     salutations = "Salutations"
#     return salutations

# s = retourner_salutations()
# print(s)

# # 1. Créer une fonction qui
# # 2. Accepte deux ou plus de paramètres (nombres)
# # 3. qui effecture une ou plusieurs opérations mathématiques avec ces paramètres
# # 4. qui retourne / renvoie le resultat de ces opérations
# # 5. qui imprime ce résultat

# def multiplier(x):
#     return x * 2


# nombre = input("quel collone viser ?")

# ligne  = input("quel ligne viser ?")
# print(nombre , ligne)




def calculer(x, y, z):
    return x + y * z


print(calculer(1, 2, 3))













# # Fonction Input 

# var = input("Quel est ton nom ?")
# print(var)