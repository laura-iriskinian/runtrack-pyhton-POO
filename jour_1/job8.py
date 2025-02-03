import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    def circonference(self):
        return 2 * math.pi *self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations du cercle 1 :")
cercle1.afficherInfos()
print("\nInformations du cercle 2 :")
cercle2.afficherInfos()