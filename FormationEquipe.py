import random 

# studen list / list pair 
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]

"""
    randomList : perme de melanger une liste et 
    retourne une nouvelle liste 
"""
def randomList(myList) -> list:
    try :        
        return random.sample(myList,len(myList)) # return new list
    except :
        print("Un probleme dans le code..! Veuillez donner une liste en paramètre")

"""
halfList : retourne -> la longueur de la moitier de la liste
"""
def halfList(newList)-> int:
    return len(newList)//2#cut length of the list in half
 
"""
printeTwoLists :permet retourner -> deux listes grace au tuples
"""
def printeTwoLists(newList) -> tuple:

    half = halfList(newList)
    firstList =[i for i in newList[:half]]
    secondtList =[i for i in newList[half:]]
    return (firstList , secondtList) # -> return tuple 

    
newList =randomList(names)
firstList,secondtList =printeTwoLists(newList)


print(firstList)
print("----------------------------------")
print(secondtList)





















""" 
    for element, element2 in zip(nouvelleListe ,noms) :
        print(f"{element}{element2}") 
"""





