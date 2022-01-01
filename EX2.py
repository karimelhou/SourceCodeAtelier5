class Vecteur2D:
    #le construcreur
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    #la methode d'affichage
    def display(self):
        print (self.x, self.y)
    #la methode d'addition pour implimenter la notion de surcharge.
    def Sum(self, other):
        vecteur3.x = self.x + other.x
        vecteur3.y = self.y + other.y
        return vecteur3

#déclaration des vecteurs (objets)
vecteur1 = Vecteur2D()
vecteur2 = Vecteur2D(5,6)
vecteur3 = Vecteur2D()
vecteur4 = Vecteur2D(10,9)

#affichage des vecteurs (objets)
print("vecteur 1 est =")
vecteur1.display()
print("vecteur 2 est =")
vecteur2.display()
print("vecteur 3 est =")
vecteur3.display()
print("vecteur 4 est =")
vecteur4.display()

#nous avons déclarer la meme methode Sum avec differentes parameters . 
print("la somme de vecteur 1 avec 2 est =")
print(vecteur1.Sum(vecteur2).x , vecteur1.Sum(vecteur2).y)
print("En utilisant la notion de surcharge la somme de vecteur 2 avec 4 est =")
print(vecteur2.Sum(vecteur4).x , vecteur2.Sum(vecteur4).y)

#nous pouvons appeler la méthode Hello de deux manières différentes
# à l'aide de la surcharge de méthode.


# Réaliser Par : ElHoumaini Karim