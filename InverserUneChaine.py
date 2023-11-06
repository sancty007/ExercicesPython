def monStyle(fonction) :
    def sous_fonction():
        print("-----------------------------------------")
        fonction()
        print("-----------------------------------------")
    return sous_fonction


# parcour de la chaine à l'envers 
def inverser_chaine_reverse(maChaine) :
    chaine_reverse =""

    for char in reversed(maChaine) :
        chaine_reverse =chaine_reverse + char 

    return chaine_reverse

# la chaine à l'endroit

def inverser_chaine_Endroit(maChaine):
    chaine_inverse = ""
    for caractere in maChaine:
        chaine_inverse = caractere + chaine_inverse

    return chaine_inverse


# inverse avec slicing 
def inverse_slicing(maChaine) :
    return maChaine[::-1] # un pas de -1 


""" chaine =inverser_chaine_reverse(maChaine)

print(chaine)  """

maChaine = "mon paragraphe"


print(inverser_chaine_Endroit(maChaine))














