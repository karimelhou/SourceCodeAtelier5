#classe
class Etudiant:
    def __init__(self, name,prenom,age,cne,moyenne):
        self.name = name
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

#déclaration de notre liste des objets de la class Etudiant
mylist = [
    Etudiant("Hello","Test",20,12355,20),
    Etudiant("hey","tr",15,19655,12),
    Etudiant("hi","te",15,12335,10),
    Etudiant("hola","tz",16,20000,15),
    ]

#Affichage de la liste avant le tri 
for obj in mylist: print(obj.name , obj.prenom , obj.age , obj.cne , obj.moyenne)
#tri de la liste selon l'age et la moyenne 
mylist = sorted(sorted(mylist,key=lambda Etudiant: Etudiant.age),key=lambda Etudiant: Etudiant.moyenne)

print("\n liste after sort \n ")
#Affichage de la liste aprés le tri
for obj in mylist: print(obj.name , obj.prenom , obj.age , obj.cne , obj.moyenne)


#Réaliser par : El Houmaini Karim

#Nous pouvons aussi utiliser cette methode pour les listes . 
#list = []
#list.append(Etudiant("Hello","Test",20,12355,20))
#list.append(Etudiant("hey","tr",15,19655,12))
#list.append(Etudiant("hi","te",20,12335,10))
#list.append(Etudiant("hola","tz",20,20000,16))



