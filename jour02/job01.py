class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur_rec = longueur
        self.__largeur_rec = largeur

    def get_longueur(self):
        return self.__longueur_rec
    def get_largeur(self):
        return self.__largeur_rec
    def set_longueur(self, longueur):
        self.__longueur_rec = longueur
    def set_largeur(self, largeur):
        self.__largeur_rec = largeur

rectangle_taille = Rectangle(10, 5)
rectangle_taille.set_longueur(4)
rectangle_taille.set_largeur(6)
print(rectangle_taille.get_longueur())
print(rectangle_taille.get_largeur())