class Commande:
    def __init__(self, numero_commande: int):
        # Attributs privés
        self.__numero_commande = numero_commande
        self.__plats = {}  # dictionnaire : {"nom": {"prix": prix, "statut": statut}}
        self.__statut = "en cours"  # Statuts possibles : "en cours", "terminée", "annulée"
        self.__tva = 0.2  # TVA à 20%

    # Accesseurs (getters)
    def get_numero_commande(self) -> int:
        return self.__numero_commande

    def get_statut(self) -> str:
        return self.__statut

    # Méthode privée pour calculer le total
    def __calculer_total(self) -> float:
        """Calcule le total de la commande sans TVA"""
        return sum(plat["prix"] for plat in self.__plats.values())

    # Méthode pour calculer la TVA
    def calculer_tva(self) -> float:
        """Calcule le montant de la TVA"""
        return self.__calculer_total() * self.__tva

    # Méthode pour ajouter un plat
    def ajouter_plat(self, nom_plat: str, prix: float) -> bool:
        """Ajoute un plat à la commande si elle est en cours"""
        if self.__statut == "en cours":
            if isinstance(prix, (int, float)) and prix > 0:
                self.__plats[nom_plat] = {
                    "prix": float(prix),
                    "statut": "en cours"
                }
                return True
            else:
                raise ValueError("Le prix doit être un nombre positif")
        return False

    # Méthode pour annuler la commande
    def annuler_commande(self) -> bool:
        """Annule la commande si elle est en cours"""
        if self.__statut == "en cours":
            self.__statut = "annulée"
            return True
        return False

    # Méthode pour terminer la commande
    def terminer_commande(self) -> bool:
        """Termine la commande si elle est en cours"""
        if self.__statut == "en cours":
            self.__statut = "terminée"
            return True
        return False

    # Méthode pour afficher la commande
    def afficher_commande(self) -> str:
        """Affiche le détail de la commande avec le total à payer"""
        if not self.__plats:
            return "Aucun plat dans la commande"

        total_ht = self.__calculer_total()
        tva = self.calculer_tva()
        total_ttc = total_ht + tva

        details = f"\nCommande n°{self.__numero_commande} - {self.__statut}\n"
        details += "-" * 40 + "\n"
        
        for nom, info in self.__plats.items():
            details += f"{nom}: {info['prix']}€\n"
        
        details += "-" * 40 + "\n"
        details += f"Total HT: {total_ht:.2f}€\n"
        details += f"TVA ({self.__tva*100}%): {tva:.2f}€\n"
        details += f"Total TTC: {total_ttc:.2f}€"
        
        return details


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une nouvelle commande
    commande = Commande(1)

    # Ajout de plats
    try:
        commande.ajouter_plat("Pizza Margherita", 12.50)
        commande.ajouter_plat("Tiramisu", 6.50)
        commande.ajouter_plat("Coca-Cola", 3.50)
        
        # Affichage de la commande
        print(commande.afficher_commande())
        
        # Test d'annulation
        # commande.annuler_commande()
        # print("\nAprès annulation:")
        # print(f"Statut: {commande.get_statut()}")
        
        # Test de finalisation
        commande.terminer_commande()
        print("\nAprès finalisation:")
        print(f"Statut: {commande.get_statut()}")
        
        # Tentative d'ajout après finalisation
        if not commande.ajouter_plat("Café", 2.00):
            print("\nImpossible d'ajouter un plat à une commande terminée")
            
    except ValueError as e:
        print(f"Erreur: {e}")