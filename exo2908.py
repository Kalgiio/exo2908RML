
def ajouterAnimeaux(nom,race, sexe, age, pays, list):#importation information
    list.append([nom, race, sexe, age, pays])
    return list

def menuAjoutAnimeaux(list):#information animal

    print("Quel est le nom de l'animal ?")
    nom = input()
    print("Quel est la race de l'animal ?")
    race = input()
    print("Quel est est le sexe de l'animal ?")
    sexe = input()
    print("Quel est l'age de l'animal")
    age = input()
    print("De quel pays viens l'animal")
    pays = input()

    ajouterAnimeaux(nom, race, sexe, age, pays, list)

    return menu(list)


def menusupp(list):#menu supression
    print("Quel animal voulez vous supprimer ?")
    nom = input()
    for i in range(len(list)):
        if list[i][0] == nom:
            print("Confirmez la suppression y/n")
            choixconf = input()
            match choixconf:
                case "y":
                    print("Suppresion en cours...\n")
                    del list[i]
                    print("Suppresion terminer retour au menu principale...\n")
                    return menu(list)
                case "n":
                    print("Annulation de la suppresion retour au menu principale...\n")
                    return menu(list)
                case _:
                    print("Erreur de saisie...")
                    return menusupp(list)



def Afficher(list):#afficher list
    print(list)
    return menu(list)

def modifier(list):#menu modifier

    print("Veuiller rensseigner le nom de l'animal a modifier")
    nom = input()

    for i in range(len(list)):
        if list[i][0] == nom:
            print(list[i])
            print("Quel champ (en nombre) souhaitez-vous modifier ? (1: Nom, 2: Race, 3: Sexe, 4: Age, 5: Pays")
            champAMod = input()
            print("Quel valeur souhaitez-vous mettre à la place ?")
            valAMettre = input()
            match champAMod:
                case "1":
                    list[i][0] = valAMettre
                case "2":
                    list[i][1] = valAMettre
                case "3":
                    list[i][2] = valAMettre
                case "4":
                    list[i][3] = valAMettre
                case "5":
                    list[i][2] = valAMettre
                case _:
                    print("Erreur de saisie...")
    return list

def remplacerunanimal(list):
    print("veuillez saisir le nom a changer")
    nom = input()
    print("veuillez saisir la race a changer")
    race = input()
    print("veuillez saisir le sexe a changer")
    sexe = input()
    print("veuillez saisir l age a changer")
    age = input()
    print("veuillez saisir le pays a changer")
    pays = input()

    listanimalAmettre = [nom, race, sexe, age, pays]

    print("Quel nom voulez-vous remplacer ?")

    nomaremp = input()

    for i in range(len(list)):
        if list[i][0] == nomaremp:
            list.pop(i)
            list.insert(i, listanimalAmettre)
        return list

def menu(list):#menu principal
    print("Bienvenue au zoo TSSR, vous disposez de plusieurs choix pour gérer vos animaux :")
    print(" 1 : Ajouter Animal")
    print(" 2 : Supprimer Animal")
    print(" 3 : Afficher liste")
    print(" 4 : Remplacer")
    print(" 5 : Modifier")
    print(" 6 : exit")
    choix = input()
    match choix:
        case "1":#menu ajouter animal
            menuAjoutAnimeaux(list)
        case "2":#menu suprrimer animal
            menusupp(list)
        case "3":#option afficher liste
            Afficher(list)
        case "4":#menu remplacer
            remplacerunanimal(list)
        case "5":#menu modifier
            modifier(list)
        case "6":#exit
                print("Au revoir des bisous <3<3")
        case _:
            print("erreur de saisie")
            menu(list)

def inicialiseList():
    list = [["Girafe", "Girafe","Male","5","Afrique"],["Girafe2", "Girafe","Male","5","Afrique"]]
    menu(list)

def main():
    inicialiseList()

if __name__ == '__main__':
    main()
    
#aide a la gestion d'un zoo ajout,supprimer,afficher la liste, remplacer, modifier
    
    

