class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA / 100

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT} €, TVA: {self.TVA * 100}%, Prix TTC: {self.calculerPrixTTC()} €"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA


produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 15)
produit3 = Produit("Livre", 20, 5)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

produit1.modifierNom("Nouvel Ordinateur")
produit1.modifierPrixHT(900)

produit2.modifierNom("Nouveau Téléphone")
produit2.modifierPrixHT(550)

produit3.modifierNom("Nouveau Livre")
produit3.modifierPrixHT(25)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
