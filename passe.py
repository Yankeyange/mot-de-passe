
# on importe quelque chose d'aléartoire
import random


# permet de genrer deux lettres miniscules aléartoire
num = random.randint(97, 122)
nums =random.randint(97, 122)

concate = chr(num) + chr(nums)

# permet de generer deux lettres majuscules aléartoire
upper = random.randint(65,90)
uppers = random.randint(65, 90)

cases = chr(upper) + chr(uppers)

# permet de generer deux chiffres aléartoire
a = random.randint(48,57)
b = random.randint(48, 57)

c = chr(a) + chr(b)

# permet de genere des symbols aléartoire
s = random.randint(33, 47)
ss = random.randint(33, 47)

sss = chr(s) +  chr(ss)


result = concate + cases + c + sss

name = input("Quelle est votre nom : ")


# imprimons le mot de passe
print(f"Bonjour {name } , nous avons generer un mot de passe pour vous le voici : {result}")