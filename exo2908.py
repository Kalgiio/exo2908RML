
def ajouterAnimeaux(race, sexe, age, pays, list):
    list.append([race, sexe, age, pays])
    return list




def menuAjoutAnimeaux(list):

    print("Quelle est l'espece de l'animal ?")
    race = input()
    print("Quel est le sexe de l'animal ?")
    sexe = input()
    print("Quel age a t-il ?")
    age = input()
    print("De quel pays vient-il ?")
    pays = input()

    ajouterAnimeaux(race, sexe, age, pays, list)

    return list


def menusupp(list):
    print("Quel animal voulez vous supprimer ?")
    nom = input()
    for i in range(len(list)):
        if list[i][0] == nom:
            confirmation(i,list)

def Afficher(list):
    print(list)
    return list

def confirmation(i, list):
    print(list[i])
    print ("Confirmez la suppression y/n")
    choix = input()
    if choix == "y":
        del list[i]
        return list
    elif choix == "n":
        print("D'accord des bisous <3")
        menu()



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
        print(" 6 : Exit")

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
                print("hello")
            case"6":
                flag = False
            case _:
                print("Erreur de saisie")
                menu()

def main():
    menu()
if __name__ == '__main__':
    main()
    
    
    
    

