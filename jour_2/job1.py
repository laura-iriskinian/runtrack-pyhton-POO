class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        #attributs privés (double underscore)
        self.__longueur = longueur 
        self.__largeur = largeur

    #accesseurs (getters)
    def get_longueur(self) -> int:
        return self.__longueur
    
    def get_largeur(self) -> int:
        return self.__largeur

    #mutateurs (setters)
    def set_longueur(self, nouvelle_longueur: int):
        if isinstance(nouvelle_longueur, int) and nouvelle_longueur >= 0:
            self.__longueur = nouvelle_longueur
        else:
            raise ValueError("La longueur doit être supérieure à 0")
        
    def set_largeur(self, nouvelle_largeur: int):
        if isinstance(nouvelle_largeur, int) and nouvelle_largeur >= 0:
            self.__largeur = nouvelle_largeur
        else:
            raise ValueError("La largeur doit être supérieure à 0")
        

if __name__ == "__main__":
    rectangle = Rectangle(10, 5)

    print(f"la longueur du rectangle est {rectangle.get_longueur()}cm")
    print(f"la largeur du rectangle est {rectangle.get_largeur()}cm")

    rectangle.set_longueur(8)
    rectangle.set_largeur(4)

    #après mutation il faut rappeler "get", la nouvelle valeur s'affichera
    print(f"La nouvelle longueur est {rectangle.get_longueur()}cm")
    print(f"La nouvelle largeur est {rectangle.get_largeur()}cm")
