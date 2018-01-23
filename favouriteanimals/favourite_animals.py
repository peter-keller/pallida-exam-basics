# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them


import sys


def controller():
    if len(sys.argv) == 1:
        print("fav_animals [animal] [animal]")
    else:
        collect_unique_animals(sys.argv[1:])

def collect_unique_animals(favourite_animal_list):
    unique_animal_list = []
    for favourite_animal in favourite_animal_list:
        flag = True
        for unique_animal in unique_animal_list:
            if favourite_animal == unique_animal:
                flag = False
        if flag:
            unique_animal_list.append(favourite_animal)
    store_unique_animals(unique_animal_list)


def store_unique_animals(unique_animals):
    fr = open("favourites.txt", 'r')
    animals_from_file = fr.readlines()
    fr.close()
    new_animals = ""
    for unique_animal in unique_animals:
        flag = True
        for animal in animals_from_file:
            if animal[0:-1] == unique_animal:
                flag = False
        if flag:
            new_animals += unique_animal + "\n"
    fw = open("favourites.txt", "a")
    fw.write(new_animals)
    fw.close()

controller()
