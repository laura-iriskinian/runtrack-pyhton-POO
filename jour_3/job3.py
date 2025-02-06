class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire" 
    
    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description
    
    def get_statut(self):
        return self.__statut
    
    def marquer_comme_finie(self):
        self.__statut = "terminée"
    
class ListeDesTaches:
    def __init__(self):
        self.__taches = []
    
    def ajouter_tache(self, tache):
        self.__taches.append(tache)
        print(f"Tâche '{tache.get_titre()}' ajoutée.")
    
    def supprimer_tache(self, tache):
        if tache in self.__taches:
            tache.marquer_comme_finie()
            print(f"Tâche '{tache.get_titre()}' marquée comme terminée.")
        else:
            print("Tâche non trouvée.")
    
    def marquer_comme_finie(self, tache):
        if tache in self.__taches:
            tache.marquer_comme_finie()
            print(f"Tâche '{tache.get_titre()}' marquée comme terminée.")
        else:
            print(f"Tâche non trouvée")

    def afficher_liste(self):
        print("\nListe des tâches:")
        for tache in self.__taches:
            print(f"- {tache.get_titre()} ({tache.get_statut()})")
            print(f"  Description: {tache.get_description()}")

    def filtrer_liste(self, statut):
        taches_filtrees = [tache for tache in self.__taches if tache.get_statut() == statut]
        print(f"\nTâches {statut}:")
        for tache in taches_filtrees:
            print(f"- {tache.get_titre()}")
            print(f"  Description: {tache.get_description()}")
        return taches_filtrees

todo = ListeDesTaches()

tache1 = Tache("Courses", "Acheter des fruits et légumes")
tache2 = Tache("Sport", "Faire 30 minutes de jogging")
tache3 = Tache("Programme", "Finir le projet Python")

todo.ajouter_tache(tache1)
todo.ajouter_tache(tache2)
todo.ajouter_tache(tache3)

todo.afficher_liste()

todo.marquer_comme_finie(tache1)

todo.supprimer_tache(tache2)

todo.afficher_liste()

todo.filtrer_liste("à faire")
todo.filtrer_liste("terminée")

        
