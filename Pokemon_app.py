import random
# ---------------------------------
# File          : Pokemon_app.py
# Author        : Anup Jacob
# Version       : v1.1
# Created Date  : 28/09/2022
# Modified Date : 
# Description   : Sample program to register pokemon trainer, add or remove into party/box first program
# Licensing     : MIT License
# ----------------------------------

class Pokemon_app:

    def __init__(self,pokemon,box1):
        self.pokemon = pokemon
        self.box1 = box1

    def pokemonparty(pokemon):
        for i in range(0, len(pokemon)):
            print(pokemon[i])
            ostatus = 'Success'
        return ostatus

    def pokemonbox1(box1):
        for j in range(0, len(box1)):
            print(box1[j])
        return "success"

    def playerwalk(self):

        print("You start walking looking for pokemon")
        encounter = random.randint(1,3)
        #print("The encountered distance is : "+str(encounter))

        if(encounter == 1):
            print("Encountered pokemon!!")
            return 1

        choice = input("Do you want to continue?: ")
        if choice == 'Y' or choice =='y':
            return
        else:
            self.playerwalk()

    def changepokemon(choice,pokemon,box1):

        while (choice == 'Y' or choice == 'y'):
            print("\nYou can change the pokemon listed below from the box: ")

            for j in range(0, len(box1)):
                print(box1[j])

            addpokemon = input("Enter the pokemon to be added to your party:")
            sendpokemon = input("Enter the pokemon to be sent to the box")

            if addpokemon not in box1:
                print("Sorry, " + addpokemon + " is not in the box")

                if sendpokemon not in pokemon:
                    print("Sorry, " + sendpokemon + " is not in your party")
                else:
                    pass
            else:
                pokemon.remove(sendpokemon)
                pokemon.append(addpokemon)
                box1.remove(addpokemon)
                box1.append(sendpokemon)

                print(
                    "The " + addpokemon + " has been added to your party and " + sendpokemon + " has been send to your PC")

                print("\nYour new pokemon party is below: ")
                for i in range(0, len(pokemon)):
                    print(pokemon[i])

                print("\nYour updated box is below: ")
                for j in range(0, len(box1)):
                    print(box1[j])

                proceed = input("Do you want to continue?: ")
                if (proceed == 'y' or proceed == 'Y'):
                    pass
                else:
                    return

    def catchpokemon(choice,pokemon,box1):
        while choice == 'Y' or choice == 'y':
            newpokemon = input("Enter the new pokemon you just caught: ")

            if len(pokemon) >= 6:
                print("Sending the new pokemon to box as you already have 6 pokemon")
                box1.append(newpokemon)
            else:
                pokemon.append(newpokemon)

            print("len(pokemon): " + str(len(pokemon)))
            print("len(box1): " + str(len(box1)))

            print("\nYour new pokemon party is below: ")
            for i in range(0, len(pokemon)):
                print(pokemon[i])

            print("\nYour updated box is below: ")
            for j in range(0, len(box1)):
                print(box1[j])

            '''proceed = input("Do you want to continue?: ")
            if (proceed == 'y' or proceed == 'Y'):
                pass
            else:'''
            return

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
        pokemonparty(pokemon)

        print("Number of pokemon in box1 :" + str(len(box1)))

        choice = input("\nDo you want to change pokemon? : ")
        changepokemon(choice, pokemon, box1)

        choice = input("\nDo you want to look for pokemon? :")
        while choice =='Y'or choice=='y':
            encounter = playerwalk(1)

            if(encounter == 1):
                choice = input("\nDo you wanna catch pokemon?: ")
                catchpokemon(choice, pokemon, box1)

                choice = input("\nDo you want to continue the journey? :")
                if choice == 'Y' or choice == 'y':
                    pass
                else:
                    continue
        pokemonnumber = len(pokemon)+len(box1)

        print("\nThe total number of pokemon you have caught is :"+str(pokemonnumber))
        print("\nThank you " + player + " for running my pokemon application")