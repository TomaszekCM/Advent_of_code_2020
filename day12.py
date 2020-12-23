input = """F10
N3
F7
R90
F11"""

# input = open('day12_input.txt', 'r').read()

instructions = input.splitlines()

list_of_instructions = [(n[0], int(n[1:])) for n in instructions]

print(list_of_instructions)


def find_destination(list_of_instructions):
    current_direction = "E"
    directions = ["E", "S", "W", "N"]
    distance_in_E = 0
    distance_in_W = 0
    distance_in_S = 0
    distance_in_N = 0
    for i in list_of_instructions:
        if i[0] == "E":
            distance_in_E += i[1]
        if i[0] == "W":
            distance_in_W += i[1]
        if i[0] == "S":
            distance_in_S += i[1]
        if i[0] == "N":
            distance_in_N += i[1]
        if i[0] == "L":
            current_index_of_direction = directions.index(current_direction)
            direction_change = int(i[1] / 90)
            new_index = abs(current_index_of_direction - direction_change)
            if new_index > 3:
                new_index = new_index % 4
            current_direction = directions[new_index]
        if i[0] == "R":
            current_index_of_direction = directions.index(current_direction)
            direction_change = int(i[1]/90)
            new_index = abs(current_index_of_direction+direction_change)
            if new_index > 3:
                new_index = new_index % 4
            current_direction = directions[new_index]
        if i[0] == "F":
            if current_direction == "E":
                distance_in_E += i[1]
            if current_direction == "W":
                distance_in_W += i[1]
            if current_direction == "S":
                distance_in_S += i[1]
            if current_direction == "W":
                distance_in_W += i[1]

    distance_EW = abs(distance_in_E-distance_in_W)
    distance_NS = abs(distance_in_N-distance_in_S)


    print("east-west: ", distance_EW)
    print("north-south: ", distance_NS)
    print("suma kierunków: ", distance_NS+distance_EW)

find_destination(list_of_instructions)




    # Action N means to move north by the given value.
    # Action S means to move south by the given value.
    # Action E means to move east by the given value.
    # Action W means to move west by the given value.
    # Action L means to turn left the given number of degrees.
    # Action R means to turn right the given number of degrees.
    # Action F means to move forward by the given value in the direction the ship is currently facing.
