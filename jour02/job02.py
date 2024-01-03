class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre_livre = titre
        self.__auteur_livre = auteur
        self.__pages_livre = nb_pages
     

    def get_titre(self):
        return self.__titre_livre
    def get_auteur(self):
        return self.__auteur_livre
    def get_pages(self):
        return self.__pages_livre
    def set_titre(self, titre):
        self.__titre_livre = titre
    def set_auteur(self, auteur):
        self.__auteur_livre = auteur
    def set_pages(self, nb_pages):
        if nb_pages != int and nb_pages<0:
            print("Le nombre de page entré ne peut pas être une décimale et/ou un nombre négatif.")
        else:
            self.__pages_livre = nb_pages

livre_complet1 = Livre("Charlie et la Chocolaterie", "Roald Dahl", 183)
livre_complet1.set_titre("Captive")
livre_complet1.set_auteur("Inessa")
livre_complet1.set_pages(-12)
print(livre_complet1.get_titre())
print(livre_complet1.get_auteur())
print(livre_complet1.get_pages())

livre_complet2 = Livre("Charlie et la Chocolaterie", "Roald Dahl", 183)
livre_complet2.set_titre("Harry Potter")
livre_complet2.set_auteur("J.K. Rowling")
livre_complet2.set_pages(357)
print(livre_complet2.get_titre())
print(livre_complet2.get_auteur())
print(livre_complet2.get_pages())