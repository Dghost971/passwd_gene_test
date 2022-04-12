import string
import random

characters = list(string.ascii_letters+string.digits+"!@#$%&()£")

def generate_random_passwd():
    length=int(input("Entrer la taille du password: "))
    random.shuffle(characters)
    passwd=[]
    for i in range(length):
        passwd.append(random.choice(characters))
    random.shuffle(passwd)
    print("Voici votre password: ") 
    print("".join(passwd))

generate_random_passwd()