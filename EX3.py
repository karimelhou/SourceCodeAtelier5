# classes
class Rectangle:
    def __init__(self,longueur=15,largeur=10):
        #Le constructeur
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"
    
    def __str__(self):
        #Methode d'affichage rectangle
        return("Le Rectangle est {0} {1} {2}" .format(self.nom,self.longueur,self.largeur))

    def surface(self):
        #Methode pour calculer la surface
        return (self.longueur*self.largeur)

class Carre(Rectangle):
    #class Caree hérite de la class Rectangle
    def __init__(self,cote=5):
        #Constructeur avec valeur par defaut
        Rectangle.__init__(self,cote,cote)
        self.nom = "carre"
        #surcharge de l'attribut d'instance nom


myRectangle = Rectangle(6,3)
print(myRectangle)
myRectangle2 = Carre()
print(myRectangle2)

# Réaliser Par : ElHoumaini Karim