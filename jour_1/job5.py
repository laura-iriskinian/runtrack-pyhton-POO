class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print (f"La coordonnée y est : {self.y}")

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur 
    
    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

point = Point(3, 4)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(6)
point.changerY(8)
point.afficherLesPoints()