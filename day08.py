input = open("day08_input.txt").read()

# input = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

splitlines_input = input.splitlines()
list_of_instructions = []
for i in splitlines_input:
    # instruction = i.split(" ")
    list_of_instructions.append(i.split(" "))
# print(list_of_instructions)


def accumulator_counter(list_of_operations):
    used_index = []
    accumulator = 0
    index = 0
    for i in range(1, len(list_of_instructions)):
        if index in used_index:
            return accumulator
        operation = list_of_instructions[index]
        # print(operation)
        used_index.append(index)
        if operation[0] == "acc":
            accumulator += int(operation[1])
            index += 1
        elif operation[0] == "jmp":
            index += int(operation[1])
        elif operation[0] == "nop":
            index += 1

print("accumulator, pierwsza: ",accumulator_counter(list_of_instructions))



def accumulator_fixlist_counter(list_of_operations):
    used_index = []
    accumulator = 0
    index = 0
    for i in range(1, len(list_of_instructions)):
        if index >= len(list_of_instructions):
            return accumulator
        operation = list_of_instructions[index]
        # print(operation)
        used_index.append(index)
        if operation[0] == "acc":
            accumulator += int(operation[1])
            index += 1
        elif operation[0] == "jmp":
            possible_new_index = index + int(operation[1])
            if possible_new_index in used_index:
                index += 1
            else:
                index += int(operation[1])
        elif operation[0] == "nop":
            possible_new_index = index + 1
            if possible_new_index in used_index:
                index += int(operation[1])
            else:
                index += 1


print("accumulator, część druga: ", accumulator_fixlist_counter(list_of_instructions))
