class Livre:
    def __init__(self, titre: str, auteur: str, pages: int):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self) -> str:
        return self.__titre
    
    def get_auteur(self) -> str:
        return self.__auteur
    
    def get_pages(self) -> int:
        return self.__pages
    
    def set_titre(self, nouveau_titre: str):
        if isinstance(nouveau_titre, str) and nouveau_titre.strip(): #.strip = valeur non vide
            self.__titre = nouveau_titre.strip()
        else:
            raise ValueError("Le nom doit être une chaîne non vide")
        
    def set_auteur(self, nouvel_auteur: str):
        if isinstance(nouvel_auteur, str) and nouvel_auteur.strip():
            self.__auteur = nouvel_auteur.strip()
        else:
            raise ValueError ("Le titre dois être une chaîne non vide")
        
    def set_pages(self, nouvelles_pages: int):
        if isinstance(nouvelles_pages, int) and nouvelles_pages >= 0:
            self.__pages = nouvelles_pages
        else:
            raise ValueError ("Le nombre de pages doit être un entier supérieur à 0")
        

if __name__ == "__main__":
    livre = Livre("Zadig", "voltaire", 250)

    print(f"Auteur: {livre.get_auteur()}")
    print(f"Titre: {livre.get_titre()}")
    print(f"Nombres de pages: {livre.get_pages()}")

    try:
        livre.set_auteur("Victor Hugo")
        livre.set_titre("Les Misérable")
        livre.set_pages(450)
    except ValueError as e:
        print(f"Erreur: {e}")

    print ("\nLivre mis à jour:")
    print(f"Auteur: {livre.get_auteur()}")
    print(f"Titre: {livre.get_titre()}")
    print(f"Nombres de pages: {livre.get_pages()}")
