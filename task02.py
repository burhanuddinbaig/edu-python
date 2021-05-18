import csv

def extraire(fichier):
    """Extrait d’un fichier texte annuaire avec	du type prenom, tel la liste des prenoms et celle des numéros de telephone"""
    f = open(fichier,'r')

    prenom,tel = [],[] #initialisation des listes de prenoms et de numeros for ligne in f

    for ligne in f:
        p,n =ligne.rstrip().split(',')
        prenom.append(p)
        tel.append(n)

    return prenom, tel

def recherche_sequentielle(clef,liste1,liste2):
    i = 0
    m = len(liste1)
    while i < m:
        if liste1[i] == clef:
            return (clef, liste2[i])
        i += 1
    else:
        return None

l1, l2 = extraire('annuaire.csv')

print(l1, l2)

#search by alphonse
print(recherche_sequentielle('Alphonse', l1, l2))

#search by Zeid
print(recherche_sequentielle('Zeid', l1, l2))

#search by any thing excluding names list
print(recherche_sequentielle('best', l1, l2))

#search by phone number
print(recherche_sequentielle('215-325-3042', l2, l1))