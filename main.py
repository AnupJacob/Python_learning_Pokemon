'''
# Sample program to register pokemon trainer, add or remove into party/box first program
'''


if __name__ == '__main__':
    cash = 2000
    badges = 0
    player = input("Enter the player's name: ")

    print("\nWelcome " + player + " to the amazing world of pokemon!")
    print("\nYou have an amount of " + str(cash) + " in your inventory")
    print("Number of badges: " + str(badges))

    pokemon = ["Pidgey", "Ratata", "Pikachu", "Bulbasaur", "Charmander", "Squirtle"]
    #pokemon = ["Pidgey", "Pikachu", "Bulbasaur", "Charmander", "Squirtle"]
    box1 = ["Entei", "Suicune", "Magikarp", "Raikou"]

    lenpokemon = str(len(pokemon))
    print("\nNumber of pokemon in hand: " + lenpokemon)
    print("The pokemon you possess are: ")
    for i in range(0, int(lenpokemon)):
        print(pokemon[i])

    lenbox1 = str(len(box1))
    choice = input("\nDo you want to change pokemon? : ")
    print("Number of pokemon in box1 :" + lenbox1)
    while (choice == 'Y' or choice == 'y'):

        print("You can change the pokemon listed below from the box: ")

        for j in range(0, int(lenbox1)):
            print(box1[j])

            addpokemon = input("Enter the pokemon to be added to your party:")
            sendpokemon = input("Enter the pokemon to be sent to the box")

            if addpokemon not in box1:
                print("Sorry, "+addpokemon+" is not in the box")

                if sendpokemon not in pokemon:
                    print("Sorry, "+sendpokemon+" is not in your party")
                else:
                    pass
            else:
                pokemon.remove(sendpokemon)
                #print(pokemon)
                pokemon.append(addpokemon)
                #print(pokemon)
                box1.remove(addpokemon)
                #print(box1)
                box1.append(sendpokemon)
                #print(box1)
                print("The "+addpokemon+" has been added to your party and "+sendpokemon+ " has been send to your PC")

                lenpokemon = int(len(pokemon))
                print("\nYour new pokemon party is below: ")

                for k in range(0,lenpokemon):
                    print(pokemon[k])

                print("\nYour updated box is below: ")

                for l in range(0,int(lenbox1)):
                    print(box1[l])
    else:
        pass

        newchoice = input("Do you wanna catch pokemon?: ")
        while newchoice =='Y' or newchoice =='y':
            newpokemon = input("Enter the new pokemon you just caught: ")

            if int(lenpokemon) >= 6:
                print("Sending the new pokemon to box as you already have 6 pokemon")
                box1.append(newpokemon)
            else:
                pokemon.append(newpokemon)

            lenpokemon = len(pokemon)
            lenbox1 = len(box1)
            print("\nYour new pokemon party is below: ")

            for k in range(0, lenpokemon):
                print(pokemon[k])

            print("\nYour updated box is below: ")

            for l in range(0, lenbox1):
                print(box1[l])
