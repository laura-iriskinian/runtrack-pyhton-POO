class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2

    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self) -> int:
        return self.__longueur

    def get_largeur(self) -> int:
        return self.__largeur
    
    def set_longueur(self, nouvelle_longueur: int):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur: int):
        self.__largeur = nouvelle_largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur: int):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def set_hauteur(self, nouvelle_hauteur: int):
        self.__hauteur = nouvelle_hauteur

    def volume(self):
        #L et l sont dans le parent donc on doit assesser ici en utilisant get(assesseur)
        return self.get_longueur() * self.get_largeur() * self.__hauteur

rectangle = Rectangle(4, 5)
para = Parallelepipede(4, 5, 7)

print(f"Volume = {para.volume()}")
print(f"peri = {rectangle.perimetre()}")
print(f"surface = {rectangle.surface()}")