class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants
    
    def get_nom(self):
        return self.__nom
    def get_nb_habitants(self):
        return self.__nb_habitants
    
    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville.get_nom()
    
    def ajouterPopulation(self):
        ajout_pop = self.__ville.get_nb_habitants()
        self.__ville.set_nb_habitants(ajout_pop + 1)
        

objet_paris = Ville("Paris", 1000000)
print("Population de la ville de Paris:", objet_paris.get_nb_habitants(), "habitants")
objet_marseille = Ville("Marseille", 861635)
print("Population de la ville de Marseille:", objet_marseille.get_nb_habitants(), "habitants")

objet_john = Personne("John", 45, objet_paris)
objet_myrtille = Personne("Myrtille", 4, objet_paris)
objet_chloe = Personne("Chloé", 18, objet_marseille)

objet_john.ajouterPopulation()
objet_myrtille.ajouterPopulation()
objet_chloe.ajouterPopulation()

print("Mise à jour de la population de la ville de Paris", objet_paris.get_nb_habitants(), "habitants")
print("Mise à jour de la population de la ville de Marseille", objet_marseille.get_nb_habitants(), "habitants")