
# on importe quelque chose d'aléartoire
import random


# permet de generer deux lettres miniscules aléartoire dans le code ASCII
num = random.randint(97, 122)
nums =random.randint(97, 122)

concate = chr(num) + chr(nums)

# permet de generer deux lettres majuscules aléartoire dans le code ASCII
upper = random.randint(65,90)
uppers = random.randint(65, 90)

cases = chr(upper) + chr(uppers)

# permet de generer deux chiffres aléartoire dans le code ASCII
a = random.randint(48,57)
b = random.randint(48, 57)

c = chr(a) + chr(b)

# permet de genere des symbols aléartoire  dans le code ASCII
s = random.randint(33, 47)
ss = random.randint(33, 47)

sss = chr(s) +  chr(ss)

# on créer une liste dans laquelle sera toute mes différentes variables
result = [concate, cases, c, sss]

# on mélange le les caractères de notre mot de passe avec random.shuffle
result = random.shuffle(result)

# sans oublier de concatener sinon rien ne va sortant (None)

result = concate + cases + c + sss

# ici je demande à l'utilisateur de mettre son nom
name = input("Quelle est votre nom : ")


# imprimons le mot de passe
print(f"Bonjour {name } , nous avons generer un mot de passe pour vous le voici : {result}")
