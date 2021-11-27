import readchar
import os
import random

X_AXIS = 0
Y_AXIS = 1
NUM_MAP_OBJECTS = 3

obstacle_definition = """\
###########################
                          #
#####  #####  ######   ## #
#####  ####  #######   ## #
###   ####             ## #
####  ############  ## ## #
#####     #####           #
#######             #######
##############   #  #######
##########     ###   ######
####        ########  #####
###   ############### #####
####        #######   #####
##########          #######
###########################\
"""

my_position = [0, 1]
map_objects = []
end_game = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Generates new objects to the map
while len(map_objects) < NUM_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if new_position not in map_objects and new_position != my_position and \
            obstacle_definition[new_position[Y_AXIS]][new_position[X_AXIS]] != "#":
        map_objects.append(new_position)

player_name = input("Cuál es tu nombre? ")
while not end_game:
    played = False
    os.system("cls")

    # Draw map
    WIDTH_LINE = ("+" + "-" * MAP_WIDTH * 2 + "+")
    print(WIDTH_LINE)

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_print = "  "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[X_AXIS] == coordinate_x and map_object[Y_AXIS] == coordinate_y:
                    char_to_print = " *"
                    object_in_cell = map_object

            if my_position[X_AXIS] == coordinate_x and my_position[Y_AXIS] == coordinate_y:
                char_to_print = " $"

                if object_in_cell:
                    os.system("cls")
                    VIDA_INICIAL_PIKACHU = 80
                    VIDA_INICIAL_SQUIRTLE = 90
                    TAMANO_VARRA_VIDA = 20

                    vida_actual_pikachu = VIDA_INICIAL_PIKACHU
                    vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE
                    while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
                        # Turno de Pikachu
                        played = True
                        print("Turno de Pikachu".strip())

                        ataque_pikachu = random.randint(1, 2)
                        if ataque_pikachu == 1:
                            # Bola Voltio
                            print("Pikachu ataca con Bola Voltio")
                            vida_actual_squirtle -= 10
                        else:
                            # Onda Trueno
                            print("Pikachu ataca con Onda Trueno")
                            vida_actual_squirtle -= 11

                        if vida_actual_squirtle < 0:
                            vida_actual_squirtle = 0

                        elif vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0

                        barra_vida_pikachu = int(vida_actual_pikachu * TAMANO_VARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:   [{}{}] ({}/{})".format("#" * barra_vida_pikachu,
                                                                 " " * (TAMANO_VARRA_VIDA - barra_vida_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_vida_squirtle = int(vida_actual_squirtle * TAMANO_VARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
                        print("Squirtle:  [{}{}] ({}/{})".format("#" * barra_vida_squirtle,
                                                                 " " * (TAMANO_VARRA_VIDA - barra_vida_squirtle),
                                                                 vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))
                        input("Enter para continuar...\n\n")
                        os.system("cls")

                        # Turno de Squirtle
                        print("Turno de Squirtle")
                        ataque_squirtle = None

                        while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
                            ataque_squirtle = input(
                                "¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

                        if ataque_squirtle == "P":
                            print("Squirtle ataca con Placaje")
                            vida_actual_pikachu -= 10
                        elif ataque_squirtle == "A":
                            print("Squirtle ataca con Pistola Agua")
                            vida_actual_pikachu -= 80
                        elif ataque_squirtle == "B":
                            print("Squirtle ataca con Burbuja")
                            vida_actual_pikachu -= 9
                        elif ataque_squirtle == "N":
                            print("Squirtle no ataca")

                        if vida_actual_squirtle < 0:
                            vida_actual_squirtle = 0

                        elif vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0

                        barra_vida_pikachu = int(vida_actual_pikachu * TAMANO_VARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:   [{}{}] ({}/{})".format("#" * barra_vida_pikachu,
                                                                 " " * (TAMANO_VARRA_VIDA - barra_vida_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_vida_squirtle = int(vida_actual_squirtle * TAMANO_VARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
                        print("Squirtle:  [{}{}] ({}/{})".format("#" * barra_vida_squirtle,
                                                                 " " * (TAMANO_VARRA_VIDA - barra_vida_squirtle),
                                                                 vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))

                        input("Enter para continuar...\n\n")
                        os.system("cls")

                    if vida_actual_pikachu > vida_actual_squirtle:
                        print("Entrenador Pokemon a ganado!!")

                    else:
                        print("{} ganó!!".format(player_name))
                        map_objects.remove(object_in_cell)
                        if len(map_objects) == 0:
                            os.system("cls")
                            print("Felicidades {}, has vencido a todos los entrenadores pokemon!!".format(player_name))
                            end_game = True
                            input()
                    if len(map_objects) != 0:
                        input("Doble enter para continuar...\n\n")
                        os.system("cls")

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_print = "##"

            print("{}".format(char_to_print), end="")
        print("|")

    print(WIDTH_LINE)

    # Ask the user where the character should move
    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[X_AXIS], (my_position[Y_AXIS] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[X_AXIS], (my_position[Y_AXIS] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[X_AXIS] - 1) % MAP_WIDTH, my_position[Y_AXIS]]

    elif direction == "d":
        new_position = [(my_position[X_AXIS] + 1) % MAP_WIDTH, my_position[Y_AXIS]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[Y_AXIS]][new_position[X_AXIS]] != "#":
            my_position = new_position
