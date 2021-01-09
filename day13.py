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
print(timestamp)
print(busses)
print(busses_list)

# FIRST PART OF THE DAY:

def first_buss(timestamp, busses_list):
    waiting_minutes = 0
    still_waiting = True
    while still_waiting:
        for bus in busses_list:
            if timestamp % bus == 0:
                print("I can take bus number %s - I was waiting %s minutes.  Multiplied: %s" %(bus, waiting_minutes, (bus*waiting_minutes)))
                return bus, waiting_minutes
            waiting_minutes += 1
            timestamp += 1

first_buss(timestamp, busses_list)


# SECOND PART OF THE DAY