input = open("day07_input.txt").read()

bags_info = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
# input
# bag_info_list = bags_info.splitlines()
bag_info_list = input.splitlines()

# print(bag_info_list)
bags_dict = {}
for i in bag_info_list:
    list_of_words = i.split(" ")
    # print(list_of_words)
    key = list_of_words[0] + " " + list_of_words[1]
    # print(key)
    # zostają nam wyrazy bez klucza - teraz musimy tylko usunąć słowa i zostawić same kolory.
    del list_of_words[0:2]
    # list_of_words.remove(0)
    # print(list_of_words)
    listo_of_values = []
    element_is_a_colour = False
    for i in list_of_words:
        if "bag" in i or i == "contain" or i.isdigit(
        ) or i == "no" or i == "other":
            element_is_a_colour = False
        else:
            element_is_a_colour = True
        if element_is_a_colour == True:
            listo_of_values.append(i)
    values = []
    if len(listo_of_values) == 2:
        value = listo_of_values[0] + " " + listo_of_values[1]
        values.append(value)
    elif len(listo_of_values) == 4:
        value1 = listo_of_values[0] + " " + listo_of_values[1]
        values.append(value1)
        value2 = listo_of_values[2] + " " + listo_of_values[3]
        values.append(value2)
    elif len(listo_of_values) == 6:
        value1 = listo_of_values[0] + " " + listo_of_values[1]
        values.append(value1)
        value2 = listo_of_values[2] + " " + listo_of_values[3]
        values.append(value2)
        value3 = listo_of_values[4] + " " + listo_of_values[5]
        values.append(value3)
    elif len(listo_of_values) == 8:
        value1 = listo_of_values[0] + " " + listo_of_values[1]
        values.append(value1)
        value2 = listo_of_values[2] + " " + listo_of_values[3]
        values.append(value2)
        value3 = listo_of_values[4] + " " + listo_of_values[5]
        values.append(value3)
        value4 = listo_of_values[6] + " " + listo_of_values[7]
        values.append(value4)
    # print(listo_of_values)
    # print(values)
    bags_dict[key] = values

print(bags_dict)


def bags_colours_counter(bags_dict):
    list_of_possible_bags = []

    for a in range(1, 10):
        for key, val in bags_dict.items():
            # print(key)
            # print(val)
            # sprawdzamy, czy którakolwiek z torb które się mogą zawierać w kluczu to jest moja torba
            for i in val:
                # "i" to są torby które zawierają inne torby - sprawdzamy czy i może zawierać moją
                if i == "shiny gold":
                    if key not in list_of_possible_bags:
                        list_of_possible_bags.append(key)
            # lecimy raz jeszcze po torbach które się mogą zawierac w tej z klucza. Jeśli znajdziemy tam torbę, w której się może zawierać ta nasza
            # (czyli coś z listy "possible bags"), to dodajemy klucz
            for i in val:
                # print("sprawdzana torba z wewnątrz klucza:", i, ". A tu lista tych, które już wiemy że są dla nas dobre", list_of_possible_bags)
                if i in list_of_possible_bags:
                    if key not in list_of_possible_bags:
                        list_of_possible_bags.append(key)

    print(list_of_possible_bags)
    print(len(list_of_possible_bags))


# DZIAŁA!  Problem był taki, że sprawdzałem, czy "i" się mieści w liście potencjalnych toreb;
# drugim problemem było to, że działając w ten sposób trzeba przelecieć te pętle kilka razy, żeby złapać torby zawierające się w torbach itp
# - sprawdzając pierwsze torby nie jesteśy w stanie zobaczyć informacji że torba "a" która się zawiera w torbie b, nie okaże się później tą, która może zawierać moją.
# Całość opiera się też na obserwacji, że jedna torba bezpośrednio zawiera do 4 rodzajów innych toreb (możba by to jakoś zautomatyzować pętlą na etapie tworzenia słownika.
bags_colours_counter(bags_dict)

# 2. CZĘŚĆ DNIA:

# przede wszystkim trzeba inaczej podzielić przy tworzeniu wartości słownika: jak element da się zamienić na int, to ten element trzeba zapisać w słowniku - czyli zmiennej pomocniczej nie zmieniać na False! -  (żeby mieć coś
# a'la {'ciemny zielony' : ['5 jasno szarych', '3 kropkowano granatowe']
