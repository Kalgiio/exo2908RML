
def ajouterAnimeaux(race, sexe, age, pays, list):
    list.append([race, sexe, age, pays])
    return list

def menuAjoutAnimeaux(list):

    print("Quel est votre race ?")
    race = input()
    print("Quel est votre sexe ?")
    sexe = input()
    print("Quel est votre age")
    age = input()
    print("De quel pays venez-vous")
    pays = input()

    ajouterAnimeaux(race, sexe, age, pays, list)

    return list


def menusupp(list):
    print("Quel animal voulez vous supprimer ?")
    nom = input()
    for i in range(len(list)):
        if list[i][0] == nom:
            confirmation(i)

def Afficher(list):
    print(list)
    return list

def confirmation(i):
    print(list[i])
    print ("Confirmez la suppression y/n")
    choix = input()
    if choix == "y":
        del list[i]
        return list
    elif choix == "n":
        menu()

def modifier(list):

    print("Veuiller rensseigner le nom de l'animal a modifier")
    nom = input()

    for i in range(len(list)):
        if list[i][0] == nom:
            print(list[i])
            print("Quel champ (en nombre) souhaitez-vous modifier ? (1: Nom, 2: Race, 3: Sexe, 4: Age, 5: Pays")
            champAMod = input()
            print("Quel valeur souhaitez-vous mettre à la place ?")
            valAMettre = input()

            if champAMod == "1" or champAMod == "nom":
                list[i][0] = valAMettre
            elif champAMod == "2" or champAMod == "race":
                list[i][1] = valAMettre
            elif champAMod == "3" or champAMod == "sexe":
                list[i][2] = valAMettre

    return list

def menu():#menu principal

    list = []
    print("Bienvenue au zoo TSSR, vous disposez de plusieurs choix pour gérer vos animaux :")
    flag = True
    while flag:
        print(" 1 : Ajouter Animal")
        print(" 2 : Supprimer Animal")
        print(" 3 : Afficher liste")
        print(" 4 : Remplacer")
        print(" 5 : Modifier")
        print(" 6 : exit")

        choix = input()
        match choix:
            case "1":
                menuAjoutAnimeaux(list)
            case "2":
                menusupp(list)
            case "3":
                Afficher(list)
            case "4":
                print("hello")
            case "5":
                modifier(list)
            case"6":
                flag = False
            case _:
                print("erreur de saisie")
                menu()

def main():
    menu()
if __name__ == '__main__':
    main()
    
#aide a la gestion d'un zoo ajout,supprimer,afficher la liste, remplacer, modifier
    
    

