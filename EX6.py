#déclaration de la classe Utilisateur
class Utilisateur:
    #déclaration de construteur
    def __init__(self):     
        self.nom = 0
        self.email = 0
        self.mot_de_passe = 0
        self.genre = 0
        self.age = 0

        #déclaration de la methode d'affichage
    def display(self):
         print(self.nom, "\t", self.email, "\t", self.mot_de_passe, "\t", self.genre, "\t", self.age)
    
#déclaration de la classe Professeur
class Professeur(Utilisateur):
        #déclaration de construteur
    def __init__(self):     
        self.__ppr = 0
        self.__grade = 0
        
      #déclaration de la methode d'affichage
    def display(self):
        print(self.__ppr, "\t", self.__grade)

#déclaration de la classe Module 
class Module:
        #déclaration de construteur
    def __init__(self):     
        self.__nom = 0
        self.__volume_horaire = 0
        self.__semestre = 0
        
    #déclaration de la methode d'affichage
    def display(self):
        print(self.__nom, "\t", self.__volume_horaire, "\t", self.__semestre)

#déclaration de la classe Matiere  
class Matiere:
    #déclaration de construteur
    def __init__(self):     
        self.__nom = 0
        self.__pourcentage = 0
        
    #déclaration de la methode d'affichage
    def display(self):
        print(self.__nom, "\t", self.__pourcentage)

#déclaration de la classe Evaluation  
class Evaluation:
    #déclaration de construteur
    def __init__(self):     
        self.__note = 0
        
    #déclaration de la methode d'affichage
    def display(self):
        print(self.__note)

#déclaration de la classe Etudiant  
class Etudiant(Utilisateur):
    #déclaration de construteur
    def __init__(self):     
        self.__code_massar = 0
        
    #déclaration de la methode d'affichage
    def display(self):
        print(self.__code_massar)

#déclaration de la classe Annee_Academique   
class Annee_Academique:
    #déclaration de construteur
    def __init__(self):     
        self.__anne = 0
        
    #déclaration de la methode d'affichage
    def display(self):
        print(self.__anne)
