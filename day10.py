adapters = """77
10
143
46
79
97
54
116
60
91
80
132
20
154
53
14
103
31
65
110
43
38
47
120
112
87
24
95
33
104
73
22
66
137
21
109
118
63
55
124
146
148
84
86
147
125
23
85
117
71
48
136
151
130
83
56
140
9
49
113
131
133
74
37
127
34
32
106
1
78
11
72
40
96
17
64
92
102
123
126
90
105
57
99
27
70
98
111
30
50
67
2
155
5
119
8
39"""

# adapters = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

# adapters = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""

list_of_adapters = sorted([int(n) for n in adapters.splitlines()])
list_of_adapters.insert(0, 0)
list_of_adapters.append(int(list_of_adapters[-1]) + 3)
# print(list_of_adapters)


def joltage_difference(adapters):
    how_many_1_difference = 0
    how_many_3_difference = 0
    previous_voltage = 0
    for i in adapters:
        # print("aktualny joltadż: ", i)
        if (i - previous_voltage) == 1:
            how_many_1_difference += 1
        elif (i - previous_voltage) == 3:
            # print("poprzedni joltadż: ", previous_voltage)
            how_many_3_difference += 1
        previous_voltage = i

    # print("one jolt difference:", how_many_1_difference, " Three jolt difference:", how_many_3_difference, " Po przemnożeniu: ",
    #       how_many_3_difference * how_many_1_difference)

    print("One jolt difference: %s. Three jolt difference: %s. Multiplied: %s"
          %(how_many_1_difference, how_many_3_difference, (how_many_3_difference * how_many_1_difference)))

joltage_difference(list_of_adapters)

def joltage_possibilities(adapters):
    possibilities_list = [1]

    for i in range(len(adapters)):
        subpossibilities = 0
        if i > 0 and adapters[i] - adapters[i - 1] <= 3:
            subpossibilities += possibilities_list[i - 1]
        if i > 1 and adapters[i] - adapters[i - 2] <= 3:
            subpossibilities += possibilities_list[i - 2]
        if i > 2 and adapters[i] - adapters[i - 3] <= 3:
            subpossibilities += possibilities_list[i - 3]
        if i > 0:
            possibilities_list.append(subpossibilities)

    # print(possibilities_list)
    print("Total number of distinct ways: ", possibilities_list[-1])
    # print(len(adapters))
    # print(len(possibilities_list))


joltage_possibilities(list_of_adapters)