import sys
import time
from deepmenu import select_from
from textblocks import *
evaluations = ["test d'écoute 1", "interro de voc", "devoir EE"]

def main():
    running = True
    while running:
        input1 = input("""1. Liste des évaluations disponibles
2. Créer une nouvelle évaluation
3. Quitter le logiciel
Votre choix? """)

        if input1 == "1":
            print('_' * 50)
            print('Evaluations:')
            for i, x in enumerate(evaluations):
                print(str(i + 1) + ' ' + x)
            print('_' * 50)
            continue
        elif input1 == "2":
            print("\nen train d'écrire...\n")
            new_evaluation = []

            time.sleep(3)
        elif input1 == "3":
            sys.exit()

if __name__ == "__main__":
    main()

