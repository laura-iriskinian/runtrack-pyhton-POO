class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        infos = {
            "nom": self.nom,
            "prix HT": self.prixHT,
            "TVA": self.TVA,
            "prix TTC": self.CalculerPrixTTC()
        }
        return infos
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom
    
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix
        return self.prixHT
    
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA

# Tests
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Souris", 20, 20)

# Affichage initial
print(produit1.afficher())
print(produit2.afficher())

# Modification des produits
produit1.modifierNom("PC Portable")
produit1.modifierPrix(1200)
produit2.modifierNom("Souris Gaming")
produit2.modifierPrix(25)

# Affichage après modifications
print(produit1.afficher())
print(produit2.afficher())