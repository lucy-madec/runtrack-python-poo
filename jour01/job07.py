class Personnage:
    def __init__(self, x, y):
        self.index_x = x
        self.index_y = y
    
    def gauche(self):
        self.index_x = self.index_x - 5
        print("A gauche, la position sera à :", self.index_x)
    
    def droite(self):
        self.index_x = self.index_x + 5
        print("A droite, la position sera à :", self.index_x)
    
    def haut(self):
        self.index_y = self.index_y - 5
        print("En haut, la position sera à :", self.index_y)

    def bas(self):
        self.index_y = self.index_y + 5
        print("En bas, la position sera à :", self.index_y)
    
    def position(self):
        tuple = (self.index_x, self.index_y)
        print(tuple)

affichage_position = Personnage(10, 28)
affichage_position.position()
affichage_position.gauche()
affichage_position.droite()
affichage_position.haut()
affichage_position.bas()