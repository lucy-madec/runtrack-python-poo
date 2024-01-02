class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Coordonnées du point : ({}, {})".format(self.x, self.y))

    def afficherX(self):
        print("Coordonnée x : {}".format(self.x))

    def afficherY(self):
        print("Coordonnée y : {}".format(self.y))
    
    def changerX(self):
        print("Coordonnée x : {}".format(self.x)) 
    
    def changerY(self):
        print("Coordonnée y : {}".format(self.y))

point1 = Point(3, 4)
point1.afficherLesPoints()

point2 = Point(5, 4)
point2.changerX()

point3 = Point(3, 6) 
point3.changerY()