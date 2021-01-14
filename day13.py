input = """1000186
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,907,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,653,x,x,x,x,x,x,x,x,x,41,x,x,13
"""
splited_input = input.splitlines()

timestamp = int(splited_input[0])
busses = (splited_input[1]).split(",")
busses_list = []
for i in busses:
    if i.isdigit():
        busses_list.append(int(i))


# print(timestamp)
# print(busses)
# print(busses_list)

# FIRST PART OF THE DAY:

def first_buss(timestamp, busses_list):
    waiting_minutes = 0
    still_waiting = True
    while still_waiting:
        for bus in busses_list:
            if timestamp % bus == 0:
                print("I can take bus number %s - I was waiting %s minutes.  Multiplied: %s" % (
                bus, waiting_minutes, (bus * waiting_minutes)))
                return bus, waiting_minutes
            waiting_minutes += 1
            timestamp += 1


# first_buss(timestamp, busses_list)


def how_long_have_to_wait(timestamp, bus_number):
    time_to_wait = bus_number - (timestamp % bus_number)
    return time_to_wait


shortest_wait = [how_long_have_to_wait(timestamp, busses_list[0])]
for bus_id in busses_list:
    specific_time = how_long_have_to_wait(timestamp, bus_id)
    if specific_time < shortest_wait[0]:
        shortest_wait = [specific_time, bus_id]

# print(shortest_wait)

# SECOND PART OF THE DAY


busses_and_possition_on_the_timetable = {}
for i in busses:
    if i.isdigit():
        busses_and_possition_on_the_timetable[int(i)] = busses.index(i)


def golden_timetstamp(busses_and_possition_on_the_timetable):
    jump = max(busses_list)
    current_timestamp = jump - busses_and_possition_on_the_timetable[jump]
    while True:
        correct = True
        for key, value in busses_and_possition_on_the_timetable.items():
            if (current_timestamp + value) % (key) != 0:
                correct = False

        if correct == True:
            return current_timestamp

        current_timestamp += jump

    # return current_timestamp


# print(golden_timetstamp(busses_and_possition_on_the_timetable))


# busses_list = [3,7]
# busses_and_possition_on_the_timetable = {3:0, 7:2}
def golden_timetstamp_fasterer(busses_and_possition_on_the_timetable):
    jump = max(busses_list)
    current_timestamp = jump - busses_and_possition_on_the_timetable[jump]
    while True:
        print("jump: ", jump)
        correct = True

        correct_for_keys = set()
        for key, value in busses_and_possition_on_the_timetable.items():
            if (current_timestamp + value) % (key) == 0:
                correct_for_keys.add(key)
            else:
                correct = False
        if correct:
            return current_timestamp

        jump = 1
        for key in correct_for_keys:
            jump *= key

        current_timestamp += jump

    return current_timestamp


print(golden_timetstamp_fasterer(busses_and_possition_on_the_timetable))