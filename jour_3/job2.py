class CompteBancaire:
    def __init__(self, num_compte: int, nom: str, prenom: str, solde: float, decouvert = False):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__num_compte}")
        print(f"Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde}")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")
    
    def versement(self, montant: float):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")

    def retrait(self, montant: float):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Solde insuffisant")

    def agios(self, taux=0.05):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux
            self.__solde -= agios
            print(f"Application d'agios: {agios}€. Nouveau solde: {self.__solde}€")
    
    def virement(self, compte_destinataire, montant: float):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Solde insuffisant")


compte1 = CompteBancaire(123, "Doe", "John", 1500)
compte2 = CompteBancaire(124, "Martin", "Sophie", -500, True)

print("Etat initial des comptes:")
compte1.afficher()
print("\n")
compte2.afficher()

print("\nOpérations:")
compte1.virement(compte2, 500)

print("\nEtat final des comptes:")
compte1.afficher()
print("\n")
compte2.afficher()
