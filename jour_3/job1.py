class Ville:
    def __init__(self, nom: str, nb_habitants: int):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self) -> str:
        return self.__nom
    
    def get_nb_habitants(self) -> int:
        return self.__nb_habitants
    
    def add_habitants(self) -> int:
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom: str, age: int, personne: Ville):
        self.__nom = nom
        self.__age = age
        self.__personne = personne

    def add_personne(self):
        self.__personne.add_habitants()

paris = Ville("Paris", 1000000)
print(f"Population de la ville de Paris : {paris.get_nb_habitants()} habitants")
marseille = Ville("Marseille", 861635)
print(f"Population de la ville de Marseille : {marseille.get_nb_habitants()} habitants")



john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.add_personne()
myrtille.add_personne()
chloe.add_personne()

print(f"Mise à jour de la population de la ville de Paris : {paris.get_nb_habitants()} habitants")
print(f"Mise à jour de la population de la ville de Marseille : {marseille.get_nb_habitants()} habitants")


