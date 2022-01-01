# classes
class Point:
    def __init__(self,x=0.0,y=0.0):
        #les valeurs par défaut
        self.x1= float(x)
        self.y1= float(y)

class Segment:
    #class composite de la class point
    def __init__(self,xo,yo,xe,ye):
        #les deux objets de la class point
        self.orig = Point(xo, yo)
        self.extrem = Point(xe,ye)
    def __str__(self): return ("l'origine de segment est : (x={0},y={1}) L'éxtrimité est : (x={2},y={3}) ".format(self.orig.x1,self.orig.y1,self.extrem.x1,self.extrem.y1))
        #affichage des caractéristique de notre segment
#Programme Principal
mySegment = Segment(1,2,3,4)
print (mySegment)


# Réaliser Par : ElHoumaini Karim