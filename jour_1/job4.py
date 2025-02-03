class Personne :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        nom = self.nom
        prenom = self.prenom
        return (f"Je suis {prenom} {nom}")
    
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")
print(personne1.SePresenter())
print(personne2.SePresenter())