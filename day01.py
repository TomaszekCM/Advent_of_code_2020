input = open('day01_input.txt', 'r').read()


abother_exanple_input = [2000, 2001, 20, 19]

input2 = input.split()
input_int = []
for i in input2:
	input_int.append(int(i))

def expense_report(args):
	numbers = []
	for arg in args:
		for a in args:
			if arg + a == 2020:
				if numbers == [arg, a]:
					pass
				else:
					numbers = [a, arg]
					print(a, arg, a*arg)

print("szukamy 2 liczb dajacych w sumie 2020 i ich iloczynu")
expense_report(input_int)


numbers = {int(i) for i in input.split()}
# expense_report(numbers)


# or...

def another_version_of_report(arg):
	print({n * (2020-n) for n in arg if (2020-n) in arg })

another_version_of_report(numbers)

# expense_report(abother_exanple_input)
# fuknckja(abother_exanple_input)



print("szukamy 3 liczb dajacych w sumie 2020 i ich iloczynu:")

def three_numbers(numbers):
	results = []
	for numb in numbers:
		for nu in numbers:
			for n in numbers:
				if n+nu+numb == 2020:
					if n in results and nu in results and numb in results:
						pass
					else:
						results = [n, nu, numb]
						print(n, nu, numb, n*nu*numb)

three_numbers(numbers)