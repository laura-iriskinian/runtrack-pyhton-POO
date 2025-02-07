import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __str__(self):
        # Pour afficher la carte de façon lisible
        valeurs = {11: 'Valet', 12: 'Dame', 13: 'Roi', 1: 'As'}
        if self.valeur in valeurs:
            nom_valeur = valeurs[self.valeur]
        else:
            nom_valeur = str(self.valeur)
        return f"{nom_valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        self.initialiser_paquet()
        self.main_joueur = []
        self.main_croupier = []
        
    def initialiser_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Pique', 'Trèfle']
        # Valeurs de 1 (As) à 13 (Roi)
        for couleur in couleurs:
            for valeur in range(1, 14):
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)
    
    def calculer_points(self, main):
        points = 0
        as_present = 0
        
        for carte in main:
            if carte.valeur == 1:  # As
                as_present += 1
            elif carte.valeur > 10:  # Valet, Dame, Roi
                points += 10
            else:
                points += carte.valeur
        
        # Gestion des As (1 ou 11 points)
        for _ in range(as_present):
            if points + 11 <= 21:
                points += 11
            else:
                points += 1
                
        return points
    
    def distribuer_carte(self, main):
        carte = self.paquet.pop()
        main.append(carte)
        return carte
    
    def afficher_main(self, main, joueur="Joueur"):
        print(f"\nMain du {joueur}:")
        for carte in main:
            print(f"- {carte}")
        points = self.calculer_points(main)
        print(f"Total des points: {points}")
    
    def tour_croupier(self):
        while self.calculer_points(self.main_croupier) < 17:
            self.distribuer_carte(self.main_croupier)
            self.afficher_main(self.main_croupier, "Croupier")
    
    def jouer_partie(self):
        # Distribution initiale
        print("\n=== Nouvelle partie de Blackjack ===")
        for _ in range(2):
            self.distribuer_carte(self.main_joueur)
            self.distribuer_carte(self.main_croupier)
        
        # Montrer les mains initiales
        self.afficher_main(self.main_joueur)
        print(f"\nPremière carte du croupier: {self.main_croupier[0]}")
        
        # Tour du joueur
        while True:
            points_joueur = self.calculer_points(self.main_joueur)
            if points_joueur > 21:
                print("\nDépassement ! Vous avez perdu.")
                return
            
            choix = input("\nVoulez-vous prendre une carte ? (o/n) ").lower()
            if choix != 'o':
                break
                
            self.distribuer_carte(self.main_joueur)
            self.afficher_main(self.main_joueur)
        
        # Tour du croupier
        print("\nTour du croupier:")
        self.afficher_main(self.main_croupier, "Croupier")
        self.tour_croupier()
        
        # Détermination du gagnant
        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)
        
        print("\n=== Résultats ===")
        print(f"Vos points: {points_joueur}")
        print(f"Points du croupier: {points_croupier}")
        
        if points_croupier > 21:
            print("Le croupier a dépassé 21. Vous gagnez !")
        elif points_joueur > points_croupier:
            print("Vous gagnez !")
        else:
            print("Le croupier gagne !")

# Test du jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer_partie()