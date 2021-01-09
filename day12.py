# input = """F10
# N3
# F7
# R90
# F11"""


input = open('day12_input.txt', 'r').read()

instructions = input.splitlines()

list_of_instructions = [(n[0], int(n[1:])) for n in instructions]


# FIRST PART OF THE DAY 12

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
            new_index = (current_index_of_direction - direction_change)
            if new_index < 0:
                new_index = 4 - (abs(new_index) % 4)
            elif new_index > 3:
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
            if current_direction == "N":
                distance_in_N += i[1]

    distance_EW = abs(distance_in_E-distance_in_W)
    distance_NS = abs(distance_in_N-distance_in_S)


    print("east-west: ", distance_EW)
    print("north-south: ", distance_NS)
    print("suma kierunków: ", distance_NS+distance_EW)

    sum_of_distance = distance_NS+distance_EW

    return sum_of_distance

# find_destination(list_of_instructions)


# SECOND PART OF THE DAY 12

def moving_the_ship(waypoint, multiplier):
    distance_in_east = 0
    distance_in_north = 0
    for i in waypoint:
        if i[0] == "N":
            distance_in_north += (multiplier*i[1])
        elif i[0] == "S":
            distance_in_north -= (multiplier*i[1])
        elif i[0] == "E":
            distance_in_east += (multiplier* i[1])
        elif i[0] == "W":
            distance_in_east -= (multiplier* i[1])

    return distance_in_east, distance_in_north


def is_there_such_direction_inside(waypoint, direction):
    for i in waypoint:
        if direction == i[0]:
            return True

def find_destination_part_2(list_of_instructions):

    directions = ["E", "S", "W", "N"]
    # waypoint shows current direction - each time we have "Fx" instruction,
    # ship goes x times into the waypoint directions
    waypoint = [["E", 10], ["N", 1]]
    distance_in_east = 0
    distance_in_north = 0

    for i in list_of_instructions:
        if i[0] == "F":
            moves = moving_the_ship(waypoint, i[1])
            distance_in_east += moves[0]
            distance_in_north += moves[1]

        elif i[0] == "N":
            is_north_inside = is_there_such_direction_inside(waypoint, "N")
            for n in waypoint:
                if is_north_inside:
                    if n[0] == "N":
                        n[1] += i[1]
                else:
                    if n[0] == "S":
                        n[1] -= i[1]
        elif i[0] == "E":
            is_east_inside = is_there_such_direction_inside(waypoint, "E")
            for n in waypoint:
                if is_east_inside:
                    if n[0] == "E":
                        n[1] += i[1]
                else:
                    if n[0] == "W":
                        n[1] -= i[1]
        elif i[0] == "W":
            is_west_inside = is_there_such_direction_inside(waypoint, "W")
            for n in waypoint:
                if is_west_inside:
                    if n[0] == "W":
                        n[1] += i[1]
                else:
                    if n[0] == "E":
                        n[1] -= i[1]
        elif i[0] == "S":
            is_south_inside = is_there_such_direction_inside(waypoint, "S")
            for n in waypoint:
                if is_south_inside:
                    if n[0] == "S":
                        n[1] += i[1]
                else:
                    if n[0] == "N":
                        n[1] -= i[1]

        elif i[0] == "L":
            for n in waypoint:
    #             n[0] shows which direction we want to change
                current_index_of_direction = directions.index(n[0])
                direction_change = int(i[1] / 90)
                new_index = (current_index_of_direction - direction_change)
                if new_index < 0:
                    new_index = 4 - (abs(new_index) % 4)
                elif new_index > 3:
                    new_index = new_index % 4
                n[0] = directions[new_index]

        elif i[0] == "R":
            for n in waypoint:
                current_index_of_direction = directions.index(n[0])
                direction_change = int(i[1] / 90)
                new_index = abs(current_index_of_direction + direction_change)
                if new_index > 3:
                    new_index = new_index % 4
                n[0] = directions[new_index]

    print("dystans na wschód = ", distance_in_east)
    print("dystans na północ = ", distance_in_north)
    print("suma wartości bezwzględnych dystansów = ", (abs(distance_in_north) + abs(distance_in_east)))


find_destination_part_2(list_of_instructions)

