class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Âge :", self.age, "ans")

    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, modifie_age):
        if type(modifie_age) == int:
            self.age = modifie_age
            print("L'âge modifié est maintenant : ", modifie_age)
        else:
            print("Erreur.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
personne.afficherAge()
personne.bonjour()
personne.modifierAge(15)

eleve = Eleve()
eleve.afficherAge()
eleve.allerEnCours()

professeur = Personne()
personne.modifierAge(40)
personne.bonjour()

professeur = Professeur("Français")
professeur.enseigner()