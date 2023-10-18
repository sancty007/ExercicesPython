
maChaine = "mon paragraphe"

def inverser_chaine_reverse(maChaine) :
    chaine_reverse =""

    for i in reversed(maChaine) :
        chaine_reverse =chaine_reverse + maChaine

    return chaine_reverse


chaine = inverser_chaine_reverse(maChaine)

print(chaine)










