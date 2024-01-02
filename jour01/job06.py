class Animal:
    def __init__(self, age, prenom):
        self.animal_age = age
        self.animal_prenom = prenom
    
    def vieillir(self):
        self.animal_age += 1
        print("L'âge de l'animal est de :", self.animal_age, "an")
    
    def nommer(self, animal_prenom):
        print("L'animal se nomme", animal_prenom)

affichage_age = Animal(0, "")
affichage_age.vieillir()
affichage_prenom = Animal(0, "")
affichage_prenom.nommer("Luna")