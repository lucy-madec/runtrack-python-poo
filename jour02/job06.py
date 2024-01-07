class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self._statut_commande == "en cours":
            if nom_plat not in self._plats_commandes:
                self._plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': 'en cours'}
                print(f"Plat {nom_plat} ajouté à la commande.")
            else:
                print(f"Le plat {nom_plat} est déjà dans la commande.")
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")

    def annuler_commande(self):
        if self._statut_commande == "en cours":
            self._statut_commande = "annulée"
            print("La commande a été annulée.")
        else:
            print("La commande est déjà terminée ou annulée.")

    def calculer_total(self):
        total = sum(plat['prix'] for plat in self._plats_commandes.values())
        return total

    def calculer_tva(self, taux_tva=0.2):
        total = self.calculer_total()
        tva = total * taux_tva
        return tva

    def afficher_commande(self):
        print(f"Commande n°{self._numero_commande}:")
        for plat, details in self._plats_commandes.items():
            print(f" - {plat}: {details['prix']} € ({details['statut']})")
        total = self.calculer_total()
        tva = self.calculer_tva()
        print(f"Total à payer: {total} € (TVA incluse: {tva} €)")

commande1 = Commande(numero_commande=1)

commande1.ajouter_plat("Bouillabaisse", 10.99)
commande1.ajouter_plat("Galette bretonne", 5.99)

commande1.afficher_commande()

total_commande1 = commande1.calculer_total()
print(f"Total de la commande: {total_commande1} €")

tva_commande1 = commande1.calculer_tva()
print(f"TVA de la commande: {tva_commande1} €")

commande1.annuler_commande()

commande1.ajouter_plat("Mousse au chocolat", 3.99)

commande1.afficher_commande()
