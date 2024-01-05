class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur       

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.hauteur

rectangle = Rectangle(50, 30)

parallelepipede = Parallelepipede(50, 30, 20)
print("Volume du parallelepipede :", parallelepipede.volume())