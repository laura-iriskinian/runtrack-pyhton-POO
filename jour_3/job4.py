class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes_decisives = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0
    
    def marquerUnBut(self):
        self.__buts += 1
        print(f"{self.__nom} a marqué un but!")
    
    def effectuerUnePasseDecisive(self):
        self.__passes_decisives += 1
        print(f"{self.__nom} a fait une passe décisive!")
    
    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1
        print(f"{self.__nom} reçoit un carton jaune!")
    
    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1
        print(f"{self.__nom} reçoit un carton rouge!")
    
    def afficherStatistiques(self):
        print(f"\nStatistiques de {self.__nom} (n°{self.__numero}, {self.__position}):")
        print(f"Buts: {self.__buts}")
        print(f"Passes décisives: {self.__passes_decisives}")
        print(f"Cartons jaunes: {self.__cartons_jaunes}")
        print(f"Cartons rouges: {self.__cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)
        print(f"Joueur ajouté à l'équipe {self.__nom}")
    
    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques de l'équipe {self.__nom}:")
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if joueur in self.__joueurs:
            if action == "but":
                joueur.marquerUnBut()
            elif action == "passe":
                joueur.effectuerUnePasseDecisive()
            elif action == "jaune":
                joueur.recevoirUnCartonJaune()
            elif action == "rouge":
                joueur.recevoirUnCartonRouge()

# Tests
# Création des équipes
equipe1 = Equipe("PSG")
equipe2 = Equipe("OM")

# Création des joueurs
joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Verratti", 6, "Milieu")
joueur3 = Joueur("Payet", 10, "Milieu")
joueur4 = Joueur("Guendouzi", 6, "Milieu")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Simulation d'un match
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "passe")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "jaune")
equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")

# Affichage des statistiques
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()