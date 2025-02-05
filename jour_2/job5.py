class Voiture:
    def __init__(self, marque: str, modele: str, annee: int, km: float):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self) -> str:
        return self.__marque
    
    def get_modele(self) -> str:
        return self.__modele
    
    def get_annee(self) -> int:
        return self.__annee
    
    def get_km(self) -> float:
        return self.__km
    
    def get_en_marche(self) -> bool:
        return self.__en_marche
    
    def set_marque(self, nouvelle_marque: str):
        if isinstance(nouvelle_marque, str) and nouvelle_marque.strip():
            self.__marque = nouvelle_marque.strip()
        else:
            raise ValueError("La marque doit être une chaine non vide")
    
    def set_modele(self, nouveau_modele: str):
        if isinstance(nouveau_modele, str) and nouveau_modele.strip():
            self.__marque = nouveau_modele.strip()
        else:
            raise ValueError("Le modèle doit être une chaine non vide")
    
    def set_annee(self, nouvelle_annee: int):
        if isinstance(nouvelle_annee, int) and 1900 <= nouvelle_annee <= 2100:
            self.__annee = nouvelle_annee
        else:
            raise ValueError("L'année doit être un entier valide")
    
    def set_kilometrage(self, nouveau_km: float):
        if isinstance(nouveau_km, (int, float)) and nouveau_km >= 0:
            self.__km = float(nouveau_km)
        else:
            raise ValueError("Le kilométrage doit être un nombre positif")

    def __verifier_plein(self) -> float:
        return self.__reservoir
    
    def demarrer(self) -> bool:
        if self.__verifier_plein() > 5 and not self.__en_marche:
            self.__en_marche = True
            return True
        return False

    def arreter(self):
        self.__en_marche = False

if __name__=="__main__":
    ma_voiture = Voiture("Renault", "Clio", 2020, 50000)

    print(f"Marque : {ma_voiture.get_marque()}")
    print(f"Modèle : {ma_voiture.get_modele()}")
    print(f"Année : { {ma_voiture.get_annee()}}")
    print(f"Kilométrage : {ma_voiture.get_km()}")
    print(f"En marche : {ma_voiture.get_en_marche()}")

    if ma_voiture.demarrer():
        print("\nLa voiture a démarré avec succès")
    else:
        print("\nLa voiture n'a pas pu démarrer")

    print(f"En marche : {ma_voiture.get_en_marche()}")

    ma_voiture.arreter()
    print(f"\nEn Marche après arrêt: {ma_voiture.get_en_marche()}")
