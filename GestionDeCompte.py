# create class 

class CompteBancaire :
    """  numeroCompte (type numerique)
    nom (nom du proprietaire du compte de type chaine) 
    solde  """
    def __init__(self,numeroCompte:float , nom:str ,solde:str) :
        self.numeroCompte  = numeroCompte
        self.nom           = nom
        self.solde         = solde

    def Versement(self,montant) :
        if montant > 0 :
            self.solde += montant
            print(f"Bravo le versement ' {montant}' effectué avec succes votre nouveau solde est de : {self.solde}")
        elif montant <= 0 :        
            print("le Montant doit etre superieure à zero  ")
    def Retrait(self,montant):
        if montant > 0 and montant <=  self.solde :
            self.solde-= montant
            print(f"Le retrait de {montant} a ete effectuer avec succes , nouveau solde est : {self.solde}")
        elif montant == 0 :
            print(" montant du retrait doit etre supérieur a zero , Merci de renouveller votre demande .")

    def AfficheInformation(self):
        print(f'''Numero de compte --> {self.numeroCompte} , Proprietaire --> {self.nom} ,
        le solde actuel --> {self.solde}''')
    
    def agios(self) :
        var_agios = self.solde * 0.05 # calcule agios de 5% sur le solde 
        self.solde -=var_agios
        print(f"Agios de {var_agios} a ete effectué . le nouveau solde est de : {self.solde}")


#Creer une methode Agios permettant d'appliquer les agios a un pourcentage de 5% du solde

