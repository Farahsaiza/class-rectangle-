class recltangle () :
    def __init__(self) :
        self.longeur = 15
        self.largeur = 10
    
    #def  __init__(self, longeur, largeur) :
     #   self.longeur = longeur
      #  self.largeur = largeur

    def __init__(self, oldrectangle):
        self.longeur = oldrectangle.longeur
        self.largeur = oldrectangle.largeur

    def perimetre(self):
        print("le perimetre du rectangle de longeur {}cm et de largeur  {}cm est:{}".format( self.longeur, self.largeur, (self.largeur+self.longeur)/2 ))


    def Air(self):
        print("l'air du rectangle de longeur {}cm et de largeur  {}cm est:{}".format( self.longeur, self.largeur, (self.largeur*self.longeur) ))

    
    def iscarre(self):
        if self.largeur==self.longeur:
            print("le rectangle n'est pas un carre")
        else:
            print("le rectangle est  un carre")
    

    def afficher_rectangle(self):
        print("\nla longeur est:{}".format(self.longeur))
        print("\nla largeur est:{}".format(self.largeur))
        print("\n",self.perimetre())
        print("\n",self.Air())
        print("\n",self.iscarre())

rectangle1=recltangle()

rectangle1.Air()
rectangle1.iscarre()
rectangle1.perimetre()
rectangle1.afficher_rectangle()






    



