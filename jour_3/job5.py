import random

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie
    
    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def attaquer(self, cible):
        degats = random.randint(5, 15)
        cible.recevoir_degats(degats)
        print(f"{self.__nom} attaque {cible.get_nom()} et inflige {degats} points de dégâts!")
    
    def recevoir_degats(self, degats):
        self.__vie = max(0, self.__vie - degats)
        print(f"{self.__nom} a maintenant {self.__vie} points de vie.")
    
    def est_vivant(self):
        return self.__vie > 0

class Jeu:
    def __init__(self):
        self.__niveau = None
        self.__joueur = None
        self.__ennemi = None
    
    def choisirNiveau(self):
        while True:
            niveau = input("Choisissez le niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile): ")
            if niveau in ["1", "2", "3"]:
                self.__niveau = int(niveau)
                break
            print("Niveau invalide, veuillez choisir 1, 2 ou 3.")
    
    def lancerJeu(self):
        # Configuration des points de vie selon le niveau
        points_vie_joueur = {1: 100, 2: 80, 3: 60}[self.__niveau]
        points_vie_ennemi = {1: 60, 2: 80, 3: 100}[self.__niveau]
        
        # Création des personnages
        nom_joueur = input("Entrez le nom de votre personnage: ")
        self.__joueur = Personnage(nom_joueur, points_vie_joueur)
        self.__ennemi = Personnage("Ennemi", points_vie_ennemi)
        
        # Boucle de jeu
        while self.verifier_sante():
            # Tour du joueur
            print("\nC'est votre tour!")
            self.__joueur.attaquer(self.__ennemi)
            if not self.verifier_sante():
                break
                
            # Tour de l'ennemi
            print("\nC'est le tour de l'ennemi!")
            self.__ennemi.attaquer(self.__joueur)
        
        self.verifier_gagnant()
    
    def verifier_sante(self):
        return self.__joueur.est_vivant() and self.__ennemi.est_vivant()
    
    def verifier_gagnant(self):
        if self.__joueur.est_vivant():
            print(f"\nFélicitations! {self.__joueur.get_nom()} a gagné!")
        else:
            print("\nGame Over! L'ennemi a gagné!")

# Lancement du jeu
if __name__ == "__main__":
    print("Bienvenue dans le jeu de combat!")
    jeu = Jeu()
    jeu.choisirNiveau()
    jeu.lancerJeu()