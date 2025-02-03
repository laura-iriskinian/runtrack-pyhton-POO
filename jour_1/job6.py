class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

animal = Animal()
print(f"l'âge de l'aanimal est : {animal.age} ans")
animal.vieillir()
print(f"l'âge de l'animal est : {animal.age} ans")

animal.nommer("Luna")
print(f"l'animal se nomme {animal.prenom}")
