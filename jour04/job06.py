class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("Attention, je roule en moto.")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print("Attention, je roule en voiture.")


voiture_mercedes = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)
voiture_mercedes.informationsVehicule()
voiture_mercedes.demarrer()

moto_yamaha = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)
moto_yamaha.informationsVehicule()
moto_yamaha.demarrer()
        