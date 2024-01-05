class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "A faire"
    
    def marquer_comme_terminee(self):
        self.statut = "Terminée"

class ListeTaches:
    def __init__(self):
        self.liste_taches = []

    def ajouter_tache(self, tache):
        self.liste_taches.append(tache)

    def supprimer_tache(self, tache):
        self.liste_taches.remove(tache)

    def marquer_comme_finie(self, tache):
        tache.marquer_comme_terminee()

    def afficher_liste(self):
        return self.liste_taches

    def filter_liste(self, statut):
        return [tache for tache in self.liste_taches if tache.statut == statut]
    
if __name__ == "__main__":
    liste_taches = ListeTaches()

    tache1 = Tache("Train", "Acheter le billet de train")
    tache2 = Tache("Répondre aux emails", "Vérifier la boîte de réception")
    liste_taches.ajouter_tache(tache1)
    liste_taches.ajouter_tache(tache2)

    print("Liste de tâches :")
    for tache in liste_taches.afficher_liste():
        print(" -", tache.titre, "(Statut :", tache.statut + ")")

    liste_taches.marquer_comme_finie(tache1)

    print("\nListe de tâches marquée comme terminée :")
    for tache in liste_taches.afficher_liste():
        print(" -", tache.titre, "(Statut:", tache.statut + ")")

    taches_terminees = liste_taches.filter_liste("Terminée")
    print("\nListe des tâches terminées :")
    for tache in taches_terminees:
        print(" -", tache.titre, "(Statut :", tache.statut + ")")

liste_taches.supprimer_tache(tache2)

print("\nListe après suppression de la tâche :")
for tache in liste_taches.afficher_liste():
    print(" -", tache.titre, "(Statut :", tache.statut + ")")

liste_taches.marquer_comme_finie(tache1)

print("\nListe après changement de statut d'une tâche :")
for tache in liste_taches.afficher_liste():
    print(" -", tache.titre, "(Statut :", tache.statut + ")")

taches_a_faire = liste_taches.filter_liste("A faire")
print("\nListe des tâches à faire:")
for tache in taches_a_faire:
    print(" -", tache.titre, "(Statut :", tache.statut + ")")