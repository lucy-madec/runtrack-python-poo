class Livre:
    def __init__(self, titre, auteur, nb_pages, disponible):
        self.__titre_livre = titre
        self.__auteur_livre = auteur
        self.__pages_livre = nb_pages
        self.__disponible = disponible
    
    # Assesseurs
    def get_titre(self):
        return self.__titre_livre
    
    def get_auteur(self):
        return self.__auteur_livre
    
    def get_pages(self):
        return self.__pages_livre
    
    def get_disponible(self):
        return self.__disponible
    
    # Mutateurs
    def set_titre(self, titre):
        self.__titre_livre = titre

    def set_auteur(self, auteur):
        self.__auteur_livre = auteur

    def set_pages(self, nb_pages):
        if nb_pages != int and nb_pages<0:
            print("Le nombre de page entré ne peut pas être une décimale et/ou un nombre négatif.")
        else:
            self.__pages_livre = nb_pages
    
    def set_disponible(self, disponible):
        self.__disponible = disponible

    # Vérifiation
    def verification(self):
        if self.get_disponible() == True:
            return self.get_disponible()
        else:
            return self.get_disponible()
            
    
    # Emprunt
    def emprunt(self):
        if self.verification():
            self.set_disponible(False)
            print("Livre emprunté.")
        else:
            print("Livre indisponible.")
    
    # Rendu
    def rendu(self):
        if not self.verification():
            self.set_disponible(True)
            print("Livre rendu.")
        else:
            print("Le livre n'a pas été emprunté.")


livre_complet = Livre("Charlie et la Chocolaterie", "Roald Dahl", 183, True)
livre_complet.emprunt()
livre_complet.rendu()
livre_complet.rendu()