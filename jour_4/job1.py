class Personne:
    def __init__(self):
        self.age = 14

    def afficher_age(self) -> int:
        print(f"Mon age est: {self.age} ans")

    def bonjour(self):
        print("Hello")
    
    def modif_age(self, nouvel_age) -> int:
        self.age= nouvel_age

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")
    
    def affecher_age(self):
        print(f"J'ai {self.age} ans")
    
class Professeur:
    def __init__(self, matiere: str):
        self.__matiere_enseignee = matiere
    
    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()
eleve.afficher_age()
